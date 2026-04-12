#!/usr/bin/env python3
"""Verarbeitet hochgeladene Bewertungsdaten und startet die Bewertungsimplementierung."""

from __future__ import annotations

import argparse
from pathlib import Path

from assessment_assistant.aggregation import (
    export_html_reports_to_downloads,
    generate_batch_reports,
)
from assessment_assistant.bootstrap import bootstrap_workspace
from assessment_assistant.config import AssessmentWorkspaceConfig, default_workspace_root
from assessment_assistant.evaluation import (
    evaluate_project,
    evaluate_project_with_profile,
    parse_rubric_to_criteria,
    write_report_html,
    write_report_json,
    write_report_markdown,
)
from assessment_assistant.ingestion import (
    copy_upload_file,
    detect_criterion_candidates,
    extract_project_archive,
    load_rubric_lines,
    select_latest_uploads,
    write_kickoff_report,
    write_rubric_markdown,
)
from assessment_assistant.live_test_setup import ensure_live_test_extensions
from assessment_assistant.profile_loader import find_profile, load_profile
from assessment_assistant.project_detector import detect_project_type


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Nimmt Uploads aus material/uploads entgegen, legt sie im owner-only "
            "Workspace ab und erstellt erste Rohartefakte fuer die Bewertung."
        )
    )
    parser.add_argument(
        "--uploads-dir",
        type=Path,
        default=Path("material") / "uploads",
        help="Pfad zum Upload-Ordner mit ZIP und Bewertungsbogen",
    )
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=default_workspace_root(),
        help="Owner-only Workspace ausserhalb des Repositories",
    )
    parser.add_argument(
        "--profile-name",
        default="default",
        help="Profilname fuer spaetere Mehrfach-Konfigurationen",
    )
    parser.add_argument(
        "--project-name",
        default="",
        help="Optionaler Name fuer den Startbericht, sonst aus ZIP-Dateiname",
    )
    parser.add_argument(
        "--profile-id",
        default="",
        help="ID eines Bewertungsprofils aus scripts/config/grading_profiles/",
    )
    parser.add_argument(
        "--download-html-dir",
        type=Path,
        default=Path.home() / "Downloads",
        help="Zielverzeichnis fuer den Export aller HTML-Bewertungsdateien",
    )
    parser.add_argument(
        "--skip-live-test-setup",
        action="store_true",
        help="Ueberspringt die automatische Installation der Live-Test-Extensions vor dem Bewertungslauf.",
    )
    parser.add_argument(
        "--skip-html-export",
        action="store_true",
        help="Kein HTML-Export ins Download-Verzeichnis ausfuehren",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.skip_live_test_setup:
        profile_name, ext_count = ensure_live_test_extensions("live-test")
        print(f"- live_test_setup: Profil '{profile_name}' aktiv, {ext_count} Extensions sichergestellt")

    config = AssessmentWorkspaceConfig(
        workspace_root=args.workspace_root,
        profile_name=args.profile_name,
    )

    bootstrap_workspace(config)

    profile_id = args.profile_id.strip() or "webprojekte"
    profiles_dir = Path(__file__).resolve().parent / "config" / "grading_profiles"
    profile_path = find_profile(profiles_dir, profile_id)

    uploads_dir = args.uploads_dir.resolve()
    if profile_path is None:
        print(
            f"[Hinweis] Kein Profil mit ID '{profile_id}' gefunden. "
            "Es wird auf Rubrik-Parsing zurueckgefallen; dafuer ist eine Rubrikdatei im Upload-Ordner noetig."
        )

    try:
        selected = select_latest_uploads(
            uploads_dir,
            config,
            allow_missing_rubric=profile_path is not None,
        )
    except FileNotFoundError as exc:
        if profile_path is None:
            raise FileNotFoundError(
                f"{exc} Profil '{profile_id}' wurde nicht gefunden; ohne Profil ist eine Rubrikdatei erforderlich."
            ) from exc
        raise

    incoming_dir = config.workspace_root / config.directory_map["eingang"]
    rubric_dir = config.workspace_root / config.directory_map["boegen"]
    extracted_dir = config.workspace_root / config.directory_map["entpackt"]

    archived_zip = copy_upload_file(selected.archive_path, incoming_dir)
    archived_rubric = (
        copy_upload_file(selected.rubric_path, rubric_dir)
        if selected.rubric_path is not None
        else None
    )

    extraction_target = extracted_dir / archived_zip.stem
    extracted_project_path = extract_project_archive(archived_zip, extraction_target)

    rubric_lines = load_rubric_lines(archived_rubric) if archived_rubric is not None else []
    criterion_candidates = detect_criterion_candidates(rubric_lines) if rubric_lines else []

    rubric_markdown_path = None
    if archived_rubric is not None:
        rubric_markdown_path = config.reports_dir / f"{archived_rubric.stem}_rohtext.md"
        write_rubric_markdown(rubric_markdown_path, archived_rubric, rubric_lines)

    project_name = args.project_name.strip() or archived_zip.stem
    kickoff_report_path = config.reports_dir / f"{project_name}_korrekturhilfe_start.md"
    write_kickoff_report(
        target_path=kickoff_report_path,
        project_name=project_name,
        extracted_project_path=extracted_project_path,
        rubric_source_path=archived_rubric,
        criterion_candidates=criterion_candidates,
    )

    # --- Projekttyp erkennen ---
    detected_type = detect_project_type(extracted_project_path)
    print(f"- erkannter_projekttyp: {detected_type}")

    # --- Profilbasierte Bewertung (bevorzugt) ---
    if profile_path is not None:
        profile = load_profile(profile_path)
        print(f"- profil_geladen: {profile_path.name} ({profile.profile_name})")
        if archived_rubric is None:
            print("- rubrik: keine separate Rubrikdatei gefunden, Profilbewertung wird direkt verwendet")
        evaluation_report = evaluate_project_with_profile(
            project_name=project_name,
            project_root=extracted_project_path,
            profile=profile,
        )
    else:
        print(f"[Hinweis] Kein Profil mit ID '{profile_id}' gefunden - Fallback auf Heuristik.")
        structured_criteria = parse_rubric_to_criteria(rubric_lines)
        if not structured_criteria:
            structured_criteria = parse_rubric_to_criteria(criterion_candidates)
        evaluation_report = evaluate_project(
            project_name=project_name,
            project_root=extracted_project_path,
            rubric_id=archived_rubric.stem,
            criteria=structured_criteria,
        )

    evaluation_json_path = config.reports_dir / f"{project_name}_korrekturhilfe_draft.json"
    evaluation_md_path = config.reports_dir / f"{project_name}_korrekturhilfe_draft.md"
    evaluation_html_path = config.reports_dir / f"{project_name}_korrekturhilfe_draft.html"
    write_report_json(evaluation_json_path, evaluation_report)
    write_report_markdown(evaluation_md_path, evaluation_report)
    write_report_html(evaluation_html_path, evaluation_report)
    batch_reports = generate_batch_reports(config.reports_dir)

    exported_html: list[Path] = []
    if not args.skip_html_export:
        exported_html = export_html_reports_to_downloads(
            reports_dir=config.reports_dir,
            download_dir=args.download_html_dir,
        )

    print("Assessment-Ingestion abgeschlossen:")
    print(f"- zip_incoming: {archived_zip}")
    print(f"- rubric_incoming: {archived_rubric if archived_rubric is not None else 'keine separate Rubrikdatei'}")
    print(f"- extracted_project: {extracted_project_path}")
    print(f"- rubric_markdown: {rubric_markdown_path if rubric_markdown_path is not None else 'nicht erzeugt'}")
    print(f"- kickoff_report: {kickoff_report_path}")
    print(f"- evaluation_json: {evaluation_json_path}")
    print(f"- evaluation_markdown: {evaluation_md_path}")
    print(f"- evaluation_html: {evaluation_html_path}")
    print(f"- overview_markdown: {batch_reports['overview_markdown']}")
    print(f"- overview_html: {batch_reports['overview_html']}")
    print(f"- ranking_markdown: {batch_reports['ranking_markdown']}")
    print(f"- ranking_html: {batch_reports['ranking_html']}")
    if args.skip_html_export:
        print("- html_export: uebersprungen (--skip-html-export)")
    else:
        print(f"- html_export_dir: {args.download_html_dir / 'edu-assessment-html'}")
        print(f"- html_export_count: {len(exported_html)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
