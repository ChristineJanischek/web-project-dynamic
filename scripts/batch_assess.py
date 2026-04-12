#!/usr/bin/env python3
"""Verarbeitet alle Projektarchive in material/uploads/ als Batch-Bewertungslauf.

Fuer jede ZIP-Datei wird ein vollstaendiger Bewertungszyklus durchgefuehrt:
- Profil-basierte Bewertung (webprojekte oder --profile-id)
- Einzelberichte JSON, Markdown, HTML je Schueler
- Danach: aktualisierte Uebersicht + Rangliste

Nutzung:
    python3 scripts/batch_assess.py
    python3 scripts/batch_assess.py --profile-id webprojekte
    python3 scripts/batch_assess.py --uploads-dir material/uploads
    npm run assessment:batch
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from assessment_assistant.aggregation import export_html_reports_to_downloads, generate_batch_reports
from assessment_assistant.bootstrap import bootstrap_workspace
from assessment_assistant.config import AssessmentWorkspaceConfig, default_workspace_root
from assessment_assistant.evaluation import (
    evaluate_project_with_profile,
    write_report_html,
    write_report_json,
    write_report_markdown,
)
from assessment_assistant.ingestion import (
    copy_upload_file,
    extract_project_archive,
    write_kickoff_report,
)
from assessment_assistant.live_test_setup import ensure_live_test_extensions
from assessment_assistant.profile_loader import find_profile, load_profile
from assessment_assistant.project_detector import detect_project_type


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bewertet alle ZIPs in material/uploads/ mit dem angegebenen Profil."
    )
    parser.add_argument(
        "--uploads-dir",
        type=Path,
        default=Path("material") / "uploads",
    )
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=default_workspace_root(),
    )
    parser.add_argument(
        "--profile-name",
        default="default",
    )
    parser.add_argument(
        "--profile-id",
        default="webprojekte",
    )
    parser.add_argument(
        "--download-html-dir",
        type=Path,
        default=Path.home() / "Downloads",
    )
    parser.add_argument(
        "--skip-live-test-setup",
        action="store_true",
        help="Ueberspringt die automatische Installation der Live-Test-Extensions vor dem Batch-Lauf.",
    )
    parser.add_argument(
        "--skip-html-export",
        action="store_true",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.skip_live_test_setup:
        profile_name, ext_count = ensure_live_test_extensions("live-test")
        print(f"Live-Test-Setup: Profil '{profile_name}' aktiv, {ext_count} Extensions sichergestellt")

    config = AssessmentWorkspaceConfig(
        workspace_root=args.workspace_root,
        profile_name=args.profile_name,
    )
    bootstrap_workspace(config)

    profiles_dir = Path(__file__).resolve().parent / "config" / "grading_profiles"
    profile_path = find_profile(profiles_dir, args.profile_id)
    if profile_path is None:
        print(
            f"Fehler: Profil '{args.profile_id}' nicht gefunden in {profiles_dir}",
            file=sys.stderr,
        )
        return 1

    profile = load_profile(profile_path)
    print(f"Profil: {profile_path.name} – {profile.profile_name} (max {profile.max_points} Pkt)")

    uploads_dir = args.uploads_dir.resolve()
    if not uploads_dir.exists():
        print(f"Fehler: Upload-Ordner nicht gefunden: {uploads_dir}", file=sys.stderr)
        return 1

    zip_files = sorted(uploads_dir.glob("*.zip"))
    if not zip_files:
        print(f"Keine ZIP-Dateien in {uploads_dir} gefunden.", file=sys.stderr)
        return 1

    print(f"\n{len(zip_files)} ZIP(s) gefunden – starte Batch-Bewertung:\n")

    incoming_dir = config.workspace_root / config.directory_map["eingang"]
    extracted_dir = config.workspace_root / config.directory_map["entpackt"]
    ok_count = 0
    fail_count = 0

    for zip_file in zip_files:
        # Projektnamen aus ZIP-Dateinamen ableiten (ohne Timestamp-Suffix)
        project_name = zip_file.stem

        print(f"  Bewerte: {zip_file.name}")
        try:
            archived_zip = copy_upload_file(zip_file, incoming_dir)
            extraction_target = extracted_dir / archived_zip.stem
            extracted_project_path = extract_project_archive(archived_zip, extraction_target)

            detected_type = detect_project_type(extracted_project_path)

            kickoff_path = config.reports_dir / f"{project_name}_korrekturhilfe_start.md"
            write_kickoff_report(
                target_path=kickoff_path,
                project_name=project_name,
                extracted_project_path=extracted_project_path,
                rubric_source_path=None,
                criterion_candidates=[],
            )

            evaluation_report = evaluate_project_with_profile(
                project_name=project_name,
                project_root=extracted_project_path,
                profile=profile,
            )

            write_report_json(
                config.reports_dir / f"{project_name}_korrekturhilfe_draft.json",
                evaluation_report,
            )
            write_report_markdown(
                config.reports_dir / f"{project_name}_korrekturhilfe_draft.md",
                evaluation_report,
            )
            write_report_html(
                config.reports_dir / f"{project_name}_korrekturhilfe_draft.html",
                evaluation_report,
            )

            print(
                f"    OK: Note {evaluation_report.grade:.2f} | "
                f"{evaluation_report.awarded_points:.0f}/{evaluation_report.max_points:.0f} Pkt | "
                f"Typ: {detected_type}"
            )
            ok_count += 1

        except Exception as exc:  # noqa: BLE001
            print(f"    FEHLER bei {zip_file.name}: {exc}", file=sys.stderr)
            fail_count += 1

    print(f"\nBatch abgeschlossen: {ok_count} OK, {fail_count} Fehler")

    print("\nErzeuge Uebersicht und Rangliste ...")
    batch_reports = generate_batch_reports(config.reports_dir)
    print(f"  - {batch_reports['overview_markdown'].name}")
    print(f"  - {batch_reports['ranking_markdown'].name}")

    if not args.skip_html_export:
        exported = export_html_reports_to_downloads(
            reports_dir=config.reports_dir,
            download_dir=args.download_html_dir,
        )
        export_dir = args.download_html_dir / "edu-assessment-html"
        print(f"\nHTML-Export: {len(exported)} Dateien nach {export_dir}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
