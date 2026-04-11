#!/usr/bin/env python3
"""Bündelt alle Korrekturhilfe-Artefakte in ein ZIP-Archiv im Workspace.

Das ZIP wird unter exports/ abgelegt – dort kann es im VS Code Explorer
per Rechtsklick -> 'Download...' direkt auf den lokalen Rechner geladen werden.

Nutzung:
    python3 scripts/export_assessments.py
    python3 scripts/export_assessments.py --assessment-dir ~/Downloads/edu-assessment-owner
    python3 scripts/export_assessments.py --formats html md json
    python3 scripts/export_assessments.py --list
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from datetime import datetime
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSESSMENT_DIR = Path.home() / "Downloads" / "edu-assessment-owner"
EXPORTS_DIR = WORKSPACE_ROOT / "exports"

DOWNLOAD_HINT = """
Fertig! Naechste Schritte um das ZIP auf deinen lokalen Rechner zu laden:

  1. VS Code Explorer oeffnen  (Strg+Shift+E / Cmd+Shift+E)
  2. Den Ordner  exports/  aufklappen
  3. Die Datei  {filename}  rechts-anklicken
  4. 'Download...'  waehlen

Das ZIP enthaelt:
    - Einzelberichte (je Schueler)
    - Korrekturhilfeuebersicht
  - Rangliste
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Exportiert Korrekturhilfe-Dateien als ZIP in den Workspace-Ordner exports/"
    )
    parser.add_argument(
        "--assessment-dir",
        type=Path,
        default=DEFAULT_ASSESSMENT_DIR,
        help=f"Owner-only Assessment-Verzeichnis (Standard: {DEFAULT_ASSESSMENT_DIR})",
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=["html", "md", "json"],
        default=["html", "md"],
        help="Dateiformate die ins ZIP aufgenommen werden (Standard: html md)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Zeigt alle verfuegbaren Bewertungsdateien ohne ZIP zu erstellen",
    )
    parser.add_argument(
        "--output-name",
        default="",
        help="Optionaler Dateiname (ohne .zip) fuer das Archiv",
    )
    return parser.parse_args()


def collect_files(reports_dir: Path, formats: list[str]) -> list[Path]:
    """Sammelt alle relevanten Korrekturhilfe-Dateien sortiert nach Name."""
    found: list[Path] = []
    suffixes = {f".{fmt}" for fmt in formats}

    for path in sorted(reports_dir.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() not in suffixes:
            continue
        # Rohtexte und Startberichte nicht exportieren
        if "_rohtext" in path.name or "_start" in path.name:
            continue
        found.append(path)

    return found


def build_zip(files: list[Path], zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=f"korrekturhilfen/{f.name}")


def print_listing(files: list[Path]) -> None:
    if not files:
        print("Keine Korrekturhilfe-Dateien gefunden.")
        return
    print(f"Verfuegbare Korrekturhilfe-Dateien ({len(files)}):")
    for f in files:
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name:60s} {size_kb:>7.1f} KB")


def main() -> int:
    args = parse_args()
    reports_dir = args.assessment_dir / "ausgang"

    if not reports_dir.exists():
        print(
            f"Fehler: Assessment-Ausgangsordner nicht gefunden: {reports_dir}\n"
            "Stelle sicher dass mindestens ein Korrekturlauf abgeschlossen wurde:\n"
            "  python3 scripts/process_assessment_uploads.py",
            file=sys.stderr,
        )
        return 1

    files = collect_files(reports_dir, args.formats)

    if args.list:
        print_listing(files)
        return 0

    if not files:
        print(
            f"Keine Korrekturhilfe-Dateien mit den Formaten {args.formats} gefunden.",
            file=sys.stderr,
        )
        return 1

    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = args.output_name.strip() or f"korrekturhilfen_export_{timestamp}"
    zip_path = EXPORTS_DIR / f"{archive_name}.zip"

    build_zip(files, zip_path)

    size_kb = zip_path.stat().st_size / 1024
    print(f"ZIP erstellt: {zip_path.relative_to(WORKSPACE_ROOT)}")
    print(f"Groesse:      {size_kb:.1f} KB")
    print(f"Dateien:      {len(files)}")
    for f in files:
        print(f"  + {f.name}")

    print(DOWNLOAD_HINT.format(filename=zip_path.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
