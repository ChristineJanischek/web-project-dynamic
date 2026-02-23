#!/usr/bin/env python3
"""
Aktualisiert den Datumsstand in der README-Überschrift:
"## 🆕 Was ist neu? (Stand: TT.MM.JJJJ)"

Verwendung:
    python3 scripts/update_whats_new_date.py
    python3 scripts/update_whats_new_date.py --check
"""

from __future__ import annotations

import argparse
from datetime import date
from lib.readme_utils import read_readme, update_whats_new_heading, write_readme


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aktualisiert den Datumsstand in der README-Überschrift 'Was ist neu?'."
    )
    parser.add_argument(
        "--date",
        dest="manual_date",
        help="Optionales Datum im Format TT.MM.JJJJ (sonst heutiges Datum).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Nur prüfen, ob README.md geändert werden müsste (Exit-Code 2 bei Abweichung).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    content = read_readme()
    today = args.manual_date or date.today().strftime("%d.%m.%Y")

    try:
        updated_content, changed = update_whats_new_heading(content, today)
    except ValueError as error:
        print(f"❌ {error}")
        return 1

    if not changed:
        print("ℹ️ Datumsstand ist bereits aktuell. Keine Änderung nötig.")
        return 0

    if args.check:
        print("⚠️ README.md ist nicht aktuell (Was-ist-neu-Datumsstand weicht ab).")
        return 2

    write_readme(updated_content)
    print(f"✅ README aktualisiert: Stand {today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
