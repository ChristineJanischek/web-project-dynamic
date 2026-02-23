#!/usr/bin/env python3
"""
Automatisches Update der Dokumentations-Tabelle in README.md
Scannt docs/ Ordner und aktualisiert die Lernpfad-Tabelle

Verwendung:
    python3 scripts/update_readme_docs.py
    python3 scripts/update_readme_docs.py --check
"""

import argparse
from typing import List, Tuple

from lib.readme_utils import (
    DOCS_DIR,
    get_markdown_section,
    replace_markdown_section,
    read_readme,
    write_readme,
)

# Dokumentations-Metadaten (Reihenfolge = Lernpfad)
DOC_METADATA: List[Tuple[str, str, str]] = [
    ("README.md", "Docs-Startseite", "Navigation über statisch, dynamisch, konzeption, programmierung und handbook"),
    ("STRUKTUR.md", "Doku-Struktur", "Ablageregeln, Link-Regeln und Wartungsroutine für langfristige Pflege"),
    ("handbook/BACKUP_STRATEGY.md", "Backup-Strategie", "Best-Practice für lokale und automatisierte Repository-Snapshots"),
    ("statisch/intro.md", "Einstieg & Überblick", "Was ist das Web? Rollen von Client/Server"),
    (
        "statisch/html-grundgeruest.md",
        "HTML Grundgerüst",
        "Aufbau von `<!DOCTYPE html>`, Grundtags, Validierung",
    ),
    (
        "statisch/seitenstrukturelemente.md",
        "Seitenstrukturelemente",
        "Semantische Tags (`header`,`nav`,`main`,`section`,...)",
    ),
    ("statisch/css-einbinden.md", "CSS einbinden", "Externe, interne & inline CSS, Best Practices"),
    ("statisch/css-basis.md", "CSS Basis", "Selektoren, Eigenschaften, erste Styles"),
    (
        "statisch/css-formatierung.md",
        "CSS Formatierung",
        "Text, Farben, Abstände, Schatten, Transitions",
    ),
    ("statisch/box-modell.md", "Box-Modell", "`margin`, `border`, `padding`, `content`"),
    (
        "statisch/flexible-layouts.md",
        "Flexible Layouts",
        "Flexbox & CSS Grid mit praktischen Beispielen",
    ),
    (
        "statisch/responsive-design.md",
        "Responsive Design",
        "Media Queries, Mobile Navigation, Breakpoints",
    ),
    ("statisch/bilder-grafiken.md", "Bilder & Grafiken", "Formate, Einbindung, Responsivität"),
    ("statisch/galerien.md", "Galerien", "Einfache Bildgalerie, Grid/Flex"),
    ("statisch/formulare.md", "Formulare & Auswertung", "Formulare erstellen & validieren"),
    ("dynamisch/js.md", "JavaScript Grundlagen", "Variablen, Funktionen, DOM, Events"),
    (
        "konzeption/git-versionsmanagement.md",
        "Git & Versionsmanagement",
        "Commits, Branches, Pull Requests, Workflows",
    ),
    (
        "konzeption/zielgruppenanalyse.md",
        "Zielgruppenanalyse",
        "User Personas, Customer Journey, Nutzerbedürfnisse",
    ),
    (
        "konzeption/corporate-design.md",
        "Corporate Design",
        "Logo, Farben, Typografie, Brand Guidelines",
    ),
    (
        "konzeption/konzeption-webdesign.md",
        "Konzeption & Webdesign",
        "Briefing, Sitemap, Wireframes, Mockups",
    ),
    ("dynamisch/react.md", "React Einstieg", "Komponenten, Props, State"),
    ("dynamisch/python.md", "Python (Flask)", "Minimales API Backend"),
    ("dynamisch/php.md", "PHP Grundlagen", "Serverseitige Skripte, Ausgabe, Verarbeitung"),
    (
        "programmierung/grundlagen/README.md",
        "Programmier-Grundlagen (neu)",
        "Sprachübergreifende Architektur für Fundamentals",
    ),
    (
        "programmierung/grundlagen/php/README.md",
        "PHP Fundamentals (modular)",
        "Ausgaben, Variablen, Kontrollstrukturen, Dateien",
    ),
    (
        "programmierung/grundlagen/python/README.md",
        "Python Fundamentals (modular)",
        "Grundlagenpfad in Python-Struktur",
    ),
    (
        "programmierung/grundlagen/javascript/README.md",
        "JavaScript Fundamentals (modular)",
        "Grundlagenpfad in JavaScript-Struktur",
    ),
    (
        "dynamisch/php-lokal-testen.md",
        "**PHP lokal testen**",
        "**PHP-Dateien von der Console aus testen**",
    ),
    ("dynamisch/datenbank.md", "Datenbank (MySQL)", "Tabellen, Abfragen, Verbindung"),
    (
        "dynamisch/algorithmen-datenstrukturen.md",
        "Algorithmen & Datenstrukturen",
        "Listen, Arrays, Sortieren, Suchen",
    ),
    ("dynamisch/testen.md", "Testen", "Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit)"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aktualisiert die Lernpfad-Tabelle in README.md oder prüft auf Abweichungen."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Nur prüfen, ob README.md Änderungen benötigen würde (Exit-Code 2 bei Abweichung).",
    )
    return parser.parse_args()


def generate_table() -> str:
    """Generiert die Markdown-Tabelle für die Dokumentationen."""
    table_lines = [
        "## Inhalt / Lernpfade",
        "",
        "| Bereich | Datei / Link | Kurzbeschreibung |",
        "|--------|---------------|------------------|",
    ]

    for filename, bereich, beschreibung in DOC_METADATA:
        doc_path = DOCS_DIR / filename
        if doc_path.exists():
            link = f"[`docs/{filename}`](docs/{filename})"
            table_lines.append(f"| {bereich} | {link} | {beschreibung} |")

    return "\n".join(table_lines)


def build_updated_readme(current_content: str, new_table: str) -> str:
    return replace_markdown_section(current_content, "## Inhalt / Lernpfade", new_table)


def _is_separator_cell(cell: str) -> bool:
    stripped = cell.strip()
    return bool(stripped) and all(char in "-: " for char in stripped)


def parse_table_rows(markdown_section: str) -> List[Tuple[str, str, str]]:
    rows: List[Tuple[str, str, str]] = []
    for line in markdown_section.splitlines():
        stripped_line = line.strip()
        if not stripped_line.startswith("|"):
            continue

        cells = [cell.strip() for cell in stripped_line.strip("|").split("|")]
        if len(cells) < 3:
            continue

        first_three = cells[:3]
        if all(_is_separator_cell(cell) for cell in first_three):
            continue
        if first_three[0] == "Bereich" and first_three[1] == "Datei / Link":
            continue

        rows.append((first_three[0], first_three[1], first_three[2]))

    return rows


def main() -> int:
    args = parse_args()

    print("📝 Generiere Dokumentations-Tabelle...")

    if not DOCS_DIR.exists():
        print(f"❌ Fehler: docs/ Ordner nicht gefunden: {DOCS_DIR}")
        return 1

    existing_docs = [f for f, _, _ in DOC_METADATA if (DOCS_DIR / f).exists()]
    print(f"📋 Gefundene Dokumentationen: {len(existing_docs)}/{len(DOC_METADATA)}")

    new_table = generate_table()

    try:
        current_content = read_readme()
        current_section = get_markdown_section(current_content, "## Inhalt / Lernpfade")
        new_content = build_updated_readme(current_content, new_table)
    except Exception as error:
        print(f"❌ Fehler beim Aktualisieren: {error}")
        return 1

    expected_rows = parse_table_rows(new_table)
    current_rows = parse_table_rows(current_section)
    changed = expected_rows != current_rows

    if args.check:
        if changed:
            print("⚠️ README.md ist nicht aktuell (Lernpfad-Tabelle weicht ab).")
            return 2
        print("✅ README.md ist aktuell.")
        return 0

    if not changed:
        print("ℹ️ README.md ist bereits aktuell. Keine Änderung nötig.")
        return 0

    write_readme(new_content)
    print("✅ README.md erfolgreich aktualisiert!")
    print(f"✨ Fertig! {len(existing_docs)} Einträge in der Tabelle.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
