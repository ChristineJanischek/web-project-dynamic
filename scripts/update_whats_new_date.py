#!/usr/bin/env python3
"""
Aktualisiert den Datumsstand in der README-Überschrift:
"## 🆕 Was ist neu? (Stand: TT.MM.JJJJ)"

Verwendung:
    python3 scripts/update_whats_new_date.py
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
README_FILE = PROJECT_ROOT / "README.md"

HEADING_PATTERN = re.compile(
    r"^##\s+🆕\s+Was ist neu\?\s*(?:\(Stand:\s*\d{2}\.\d{2}\.\d{4}\))?\s*$",
    flags=re.MULTILINE,
)


def update_whats_new_heading(content: str, today: str) -> tuple[str, bool]:
    new_heading = f"## 🆕 Was ist neu? (Stand: {today})"

    match = HEADING_PATTERN.search(content)
    if not match:
        raise ValueError("Überschrift '## 🆕 Was ist neu?' nicht gefunden.")

    updated_content = content[: match.start()] + new_heading + content[match.end() :]
    return updated_content, updated_content != content


def main() -> int:
    if not README_FILE.exists():
        print(f"❌ README nicht gefunden: {README_FILE}")
        return 1

    content = README_FILE.read_text(encoding="utf-8")
    today = date.today().strftime("%d.%m.%Y")

    try:
        updated_content, changed = update_whats_new_heading(content, today)
    except ValueError as error:
        print(f"❌ {error}")
        return 1

    if not changed:
        print("ℹ️ Datumsstand ist bereits aktuell. Keine Änderung nötig.")
        return 0

    README_FILE.write_text(updated_content, encoding="utf-8")
    print(f"✅ README aktualisiert: Stand {today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
