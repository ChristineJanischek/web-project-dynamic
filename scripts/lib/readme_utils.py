from __future__ import annotations

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
README_FILE = PROJECT_ROOT / "README.md"
DOCS_DIR = PROJECT_ROOT / "docs"

_WHATS_NEW_HEADING_PATTERN = re.compile(
    r"^##\s+🆕\s+Was ist neu\?\s*(?:\(Stand:\s*\d{2}\.\d{2}\.\d{4}\))?\s*$",
    flags=re.MULTILINE,
)


def read_readme() -> str:
    if not README_FILE.exists():
        raise FileNotFoundError(f"README.md nicht gefunden: {README_FILE}")
    return README_FILE.read_text(encoding="utf-8")


def write_readme(content: str) -> None:
    README_FILE.write_text(content, encoding="utf-8")


def replace_markdown_section(content: str, section_heading: str, replacement: str) -> str:
    pattern = rf"(^{re.escape(section_heading)}.*?)(\n##\s|\Z)"

    match = re.search(pattern, content, flags=re.DOTALL | re.MULTILINE)
    if not match:
        raise ValueError(f"Abschnitt nicht gefunden: {section_heading}")

    updated = content[: match.start()] + replacement + "\n\n" + match.group(2) + content[match.end() :]
    return updated


def get_markdown_section(content: str, section_heading: str) -> str:
    pattern = rf"(^{re.escape(section_heading)}.*?)(\n##\s|\Z)"
    match = re.search(pattern, content, flags=re.DOTALL | re.MULTILINE)
    if not match:
        raise ValueError(f"Abschnitt nicht gefunden: {section_heading}")
    return match.group(1)


def update_whats_new_heading(content: str, formatted_date: str) -> tuple[str, bool]:
    new_heading = f"## 🆕 Was ist neu? (Stand: {formatted_date})"
    match = _WHATS_NEW_HEADING_PATTERN.search(content)
    if not match:
        raise ValueError("Überschrift '## 🆕 Was ist neu?' nicht gefunden.")

    updated_content = content[: match.start()] + new_heading + content[match.end() :]
    return updated_content, updated_content != content
