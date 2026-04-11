from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import shutil
import zipfile
import xml.etree.ElementTree as ET

from .config import AssessmentWorkspaceConfig
from .security import ensure_directory


MAX_RUBRIC_LINES = 500


@dataclass(slots=True)
class UploadSelection:
    archive_path: Path
    rubric_path: Path | None


def select_latest_uploads(
    uploads_dir: Path,
    config: AssessmentWorkspaceConfig,
    allow_missing_rubric: bool = False,
) -> UploadSelection:
    if not uploads_dir.exists():
        raise FileNotFoundError(f"Uploads-Verzeichnis nicht gefunden: {uploads_dir}")

    archive_files = _collect_by_suffix(uploads_dir, config.allowed_archive_suffixes)
    rubric_files = _collect_by_suffix(uploads_dir, config.allowed_rubric_suffixes)

    if not archive_files:
        allowed = ", ".join(config.allowed_archive_suffixes)
        raise FileNotFoundError(
            f"Keine Projektarchive im Upload-Ordner gefunden (erlaubt: {allowed})."
        )
    if not rubric_files and not allow_missing_rubric:
        allowed = ", ".join(config.allowed_rubric_suffixes)
        raise FileNotFoundError(
            f"Kein Bewertungsbogen im Upload-Ordner gefunden (erlaubt: {allowed})."
        )

    return UploadSelection(
        archive_path=archive_files[0],
        rubric_path=rubric_files[0] if rubric_files else None,
    )


def copy_upload_file(source_path: Path, target_dir: Path) -> Path:
    ensure_directory(target_dir)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = target_dir / f"{source_path.stem}_{timestamp}{source_path.suffix}"
    shutil.copy2(source_path, candidate)
    return candidate


def extract_project_archive(archive_path: Path, extraction_dir: Path) -> Path:
    ensure_directory(extraction_dir)

    with zipfile.ZipFile(archive_path, "r") as archive:
        _safe_extract_all(archive, extraction_dir)

    child_entries = sorted(extraction_dir.iterdir(), key=lambda item: item.name.lower())
    if len(child_entries) == 1 and child_entries[0].is_dir():
        return child_entries[0]
    return extraction_dir


def load_rubric_lines(rubric_path: Path) -> list[str]:
    suffix = rubric_path.suffix.lower()
    if suffix == ".docx":
        return _extract_docx_lines(rubric_path)
    if suffix == ".md":
        text = rubric_path.read_text(encoding="utf-8", errors="ignore")
        return _normalize_lines(text.splitlines())
    raise ValueError(f"Rubrik-Format wird noch nicht unterstuetzt: {rubric_path.suffix}")


def write_rubric_markdown(
    target_path: Path,
    source_path: Path,
    rubric_lines: list[str],
) -> Path:
    ensure_directory(target_path.parent)
    limited_lines = rubric_lines[:MAX_RUBRIC_LINES]

    content_lines = [
        "# Bewertungsbogen Rohtext",
        "",
        f"Quelle: {source_path}",
        "",
        "## Extrahierte Zeilen",
        "",
    ]

    for line in limited_lines:
        content_lines.append(f"- {line}")

    if len(rubric_lines) > MAX_RUBRIC_LINES:
        content_lines.extend(
            [
                "",
                (
                    f"Hinweis: Ausgabe auf {MAX_RUBRIC_LINES} Zeilen begrenzt. "
                    f"Original hat {len(rubric_lines)} Zeilen."
                ),
            ]
        )

    target_path.write_text("\n".join(content_lines) + "\n", encoding="utf-8")
    return target_path


def write_kickoff_report(
    target_path: Path,
    project_name: str,
    extracted_project_path: Path,
    rubric_source_path: Path | None,
    criterion_candidates: list[str],
) -> Path:
    ensure_directory(target_path.parent)

    if not criterion_candidates:
        criterion_candidates = [
            "Projektstruktur und Vollstaendigkeit manuell pruefen",
            "Funktionale Kernlogik gegen Erwartungshorizont pruefen",
            "Codequalitaet und Wartbarkeit bewerten",
        ]

    lines = [
        "# Bewertungs-Startbericht",
        "",
        f"Projekt: {project_name}",
        f"Extrahierter Quellpfad: {extracted_project_path}",
        (
            f"Rubrikquelle: {rubric_source_path}"
            if rubric_source_path is not None
            else "Rubrikquelle: Keine separate Rubrikdatei vorhanden; Profilbewertung wird verwendet."
        ),
        "",
        "## Naechster Bearbeitungsschritt",
        "",
        (
            "- Rubrik-Rohtext in konkrete Kriterien ueberfuehren."
            if rubric_source_path is not None
            else "- Profilkriterien gegen Aufgabenstellung und Abgabekontext abgleichen."
        ),
        "- Kriterien mit max_points und Status initialisieren.",
        "- Evidenz direkt aus dem Projektpfad belegen.",
        "",
        "## Vorerkannte Kriterienkandidaten",
        "",
    ]

    for candidate in criterion_candidates:
        lines.append(f"- [ ] {candidate}")

    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target_path


def detect_criterion_candidates(rubric_lines: list[str], limit: int = 20) -> list[str]:
    candidates: list[str] = []

    for line in rubric_lines:
        lowered = line.lower()
        if (
            "punkt" in lowered
            or "kriter" in lowered
            or "bewert" in lowered
            or "anforder" in lowered
        ):
            candidates.append(line)
        if len(candidates) >= limit:
            break

    return candidates


def _collect_by_suffix(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    """Sammelt Dateien nach Suffix-Reihenfolge (Priorität) dann mtime."""
    normalized = tuple(item.lower() for item in suffixes)
    entries = [
        path
        for path in root.iterdir()
        if path.is_file() and path.suffix.lower() in normalized
    ]
    suffix_rank = {s: i for i, s in enumerate(normalized)}
    return sorted(
        entries,
        key=lambda path: (suffix_rank.get(path.suffix.lower(), 99), -path.stat().st_mtime),
    )


def _safe_extract_all(archive: zipfile.ZipFile, destination: Path) -> None:
    destination_resolved = destination.resolve()

    for member in archive.infolist():
        member_target = (destination / member.filename).resolve()
        if not _is_within_directory(member_target, destination_resolved):
            raise ValueError(
                "Unsicherer ZIP-Inhalt erkannt (Pfad traversal). "
                f"Datei: {member.filename}"
            )
        archive.extract(member, destination)


def _is_within_directory(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _extract_docx_lines(docx_path: Path) -> list[str]:
    with zipfile.ZipFile(docx_path, "r") as archive:
        document_xml = archive.read("word/document.xml")

    root = ET.fromstring(document_xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    lines: list[str] = []
    for paragraph in root.findall(".//w:p", ns):
        text_parts = [node.text or "" for node in paragraph.findall(".//w:t", ns)]
        paragraph_text = "".join(text_parts)
        if paragraph_text.strip():
            lines.append(paragraph_text.strip())

    return _normalize_lines(lines)


def _normalize_lines(lines: list[str]) -> list[str]:
    normalized: list[str] = []
    for line in lines:
        compact = " ".join(line.split())
        if compact:
            normalized.append(compact)
    return normalized