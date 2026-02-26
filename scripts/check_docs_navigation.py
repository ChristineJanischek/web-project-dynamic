#!/usr/bin/env python3
"""Prüft Navigationskonsistenz in docs/programmierung/grundlagen.

Regeln (Single Source of Truth):
- Kapitelreihenfolge pro Sprache aus scripts/config/docs_navigation_rules.json
- Rücklink in jedem Kapitel zur Sprach-Übersicht
- Weiter-Link in jedem Kapitel zum nächsten Kapitel
- Letztes Kapitel verlinkt auf den Sprachvergleich
- Sprach-README enthält Link zur Grundlagen-Übersicht und zum Sprachvergleich
- Sprach-README führt Kapitel in definierter Reihenfolge
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "scripts" / "config" / "docs_navigation_rules.json"


@dataclass
class LanguageRule:
    key: str
    display: str
    base_path: Path
    overview: str
    chapters: List[str]


@dataclass
class Rules:
    cross_language_file: Path
    languages: List[LanguageRule]


def load_rules() -> Rules:
    data: Dict[str, Any] = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    cross_language_file = PROJECT_ROOT / data["crossLanguageFile"]
    languages: List[LanguageRule] = []

    for item in data["languages"]:
        languages.append(
            LanguageRule(
                key=item["key"],
                display=item["display"],
                base_path=PROJECT_ROOT / item["basePath"],
                overview=item["overview"],
                chapters=item["chapters"],
            )
        )

    return Rules(cross_language_file=cross_language_file, languages=languages)


def require_file(path: Path, issues: List[str]) -> bool:
    if not path.exists():
        issues.append(f"Datei fehlt: {path.relative_to(PROJECT_ROOT)}")
        return False
    return True


def check_contains(text: str, needle: str, issue: str, issues: List[str]) -> None:
    if needle not in text:
        issues.append(issue)


def check_readme(language: LanguageRule, cross_rel: str, issues: List[str]) -> None:
    readme = language.base_path / language.overview
    if not require_file(readme, issues):
        return

    text = readme.read_text(encoding="utf-8")

    check_contains(
        text,
        "../README.md",
        f"{readme.relative_to(PROJECT_ROOT)}: Link zur Grundlagen-Übersicht fehlt (../README.md)",
        issues,
    )
    check_contains(
        text,
        cross_rel,
        f"{readme.relative_to(PROJECT_ROOT)}: Link zum Sprachvergleich fehlt ({cross_rel})",
        issues,
    )

    positions: List[int] = []
    for chapter in language.chapters:
        marker = f"]({chapter})"
        pos = text.find(marker)
        if pos == -1:
            issues.append(
                f"{readme.relative_to(PROJECT_ROOT)}: Kapitel-Link fehlt ({chapter})"
            )
        else:
            positions.append(pos)

    if positions and positions != sorted(positions):
        issues.append(
            f"{readme.relative_to(PROJECT_ROOT)}: Kapitel-Reihenfolge weicht von Konfiguration ab"
        )


def check_chapters(language: LanguageRule, cross_rel_from_chapter: str, issues: List[str]) -> None:
    for index, chapter in enumerate(language.chapters):
        file_path = language.base_path / chapter
        if not require_file(file_path, issues):
            continue

        text = file_path.read_text(encoding="utf-8")

        back_phrase = f"Zurück zur {language.display}-Übersicht"
        check_contains(
            text,
            back_phrase,
            f"{file_path.relative_to(PROJECT_ROOT)}: Rücklink-Text fehlt ({back_phrase})",
            issues,
        )
        check_contains(
            text,
            "](README.md)",
            f"{file_path.relative_to(PROJECT_ROOT)}: Rücklink-Ziel fehlt (README.md)",
            issues,
        )

        check_contains(
            text,
            "Weiter:",
            f"{file_path.relative_to(PROJECT_ROOT)}: Weiter-Link fehlt",
            issues,
        )

        if index < len(language.chapters) - 1:
            expected_target = language.chapters[index + 1]
        else:
            expected_target = cross_rel_from_chapter

        check_contains(
            text,
            f"]({expected_target})",
            f"{file_path.relative_to(PROJECT_ROOT)}: Weiter-Link zeigt nicht auf {expected_target}",
            issues,
        )


def main() -> int:
    if not CONFIG_PATH.exists():
        print(f"❌ Konfiguration nicht gefunden: {CONFIG_PATH}")
        return 1

    rules = load_rules()
    issues: List[str] = []

    if not require_file(rules.cross_language_file, issues):
        print("❌ Sprachvergleichsdatei fehlt.")
        return 1

    cross_rel_from_language_readme = "../" + rules.cross_language_file.name
    cross_rel_from_chapter = "../" + rules.cross_language_file.name

    for language in rules.languages:
        check_readme(language, cross_rel_from_language_readme, issues)
        check_chapters(language, cross_rel_from_chapter, issues)

    cross_text = rules.cross_language_file.read_text(encoding="utf-8")
    check_contains(
        cross_text,
        "](README.md)",
        f"{rules.cross_language_file.relative_to(PROJECT_ROOT)}: Rücklink zur Grundlagen-Übersicht fehlt (README.md)",
        issues,
    )

    if issues:
        print("❌ Navigations-Check fehlgeschlagen:\n")
        for issue in issues:
            print(f"- {issue}")
        print(f"\nGefundene Probleme: {len(issues)}")
        return 2

    print("✅ Navigations-Check erfolgreich: Alle Regeln erfüllt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
