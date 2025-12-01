#!/usr/bin/env python3
"""
Automatisches Update der Dokumentations-Tabelle in README.md
Scannt docs/ Ordner und aktualisiert die Lernpfad-Tabelle

Verwendung:
    python3 scripts/update_readme_docs.py
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Dokumentations-Metadaten (Reihenfolge = Lernpfad)
DOC_METADATA: List[Tuple[str, str, str]] = [
    ("intro.md", "Einstieg & Überblick", "Was ist das Web? Rollen von Client/Server"),
    ("html-grundgeruest.md", "HTML Grundgerüst", "Aufbau von `<!DOCTYPE html>`, Grundtags, Validierung"),
    ("seitenstrukturelemente.md", "Seitenstrukturelemente", "Semantische Tags (`header`,`nav`,`main`,`section`,...)"),
    ("css-einbinden.md", "CSS einbinden", "Externe, interne & inline CSS, Best Practices"),
    ("css-basis.md", "CSS Basis", "Selektoren, Eigenschaften, erste Styles"),
    ("css-formatierung.md", "CSS Formatierung", "Text, Farben, Abstände, Schatten, Transitions"),
    ("box-modell.md", "Box-Modell", "`margin`, `border`, `padding`, `content`"),
    ("flexible-layouts.md", "Flexible Layouts", "Flexbox & CSS Grid mit praktischen Beispielen"),
    ("responsive-design.md", "Responsive Design", "Media Queries, Mobile Navigation, Breakpoints"),
    ("bilder-grafiken.md", "Bilder & Grafiken", "Formate, Einbindung, Responsivität"),
    ("galerien.md", "Galerien", "Einfache Bildgalerie, Grid/Flex"),
    ("formulare.md", "Formulare & Auswertung", "Formulare erstellen & validieren"),
    ("js.md", "JavaScript Grundlagen", "Variablen, Funktionen, DOM, Events"),
    ("git-versionsmanagement.md", "Git & Versionsmanagement", "Commits, Branches, Pull Requests, Workflows"),
    ("zielgruppenanalyse.md", "Zielgruppenanalyse", "User Personas, Customer Journey, Nutzerbedürfnisse"),
    ("corporate-design.md", "Corporate Design", "Logo, Farben, Typografie, Brand Guidelines"),
    ("konzeption-webdesign.md", "Konzeption & Webdesign", "Briefing, Sitemap, Wireframes, Mockups"),
    ("react.md", "React Einstieg", "Komponenten, Props, State"),
    ("python.md", "Python (Flask)", "Minimales API Backend"),
    ("php.md", "PHP Grundlagen", "Serverseitige Skripte, Ausgabe, Verarbeitung"),
    ("datenbank.md", "Datenbank (MySQL)", "Tabellen, Abfragen, Verbindung"),
    ("algorithmen-datenstrukturen.md", "Algorithmen & Datenstrukturen", "Listen, Arrays, Sortieren, Suchen"),
    ("testen.md", "Testen", "Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit)"),
]

# Pfade
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
README_FILE = PROJECT_ROOT / "README.md"


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
        
        # Nur Dateien hinzufügen, die tatsächlich existieren
        if doc_path.exists():
            link = f"[`docs/{filename}`](docs/{filename})"
            table_lines.append(f"| {bereich} | {link} | {beschreibung} |")
    
    return "\n".join(table_lines)


def update_readme(new_table: str) -> None:
    """Aktualisiert die README.md mit der neuen Tabelle."""
    
    if not README_FILE.exists():
        raise FileNotFoundError(f"README.md nicht gefunden: {README_FILE}")
    
    # README.md lesen
    content = README_FILE.read_text(encoding="utf-8")
    
    # Finde Start und Ende der Tabelle
    # Pattern: Von "## Inhalt / Lernpfade" bis zum nächsten "##"
    pattern = r"(## Inhalt / Lernpfade.*?)(\n##\s|\Z)"
    
    # Ersetze die Tabelle
    def replace_table(match):
        # Bewahre den nächsten Abschnitt
        return new_table + "\n\n" + match.group(2)
    
    new_content = re.sub(pattern, replace_table, content, flags=re.DOTALL)
    
    # README.md schreiben
    README_FILE.write_text(new_content, encoding="utf-8")
    
    print("✅ README.md erfolgreich aktualisiert!")


def main():
    """Hauptfunktion."""
    
    print("📝 Generiere Dokumentations-Tabelle...")
    
    # Prüfe ob docs/ Ordner existiert
    if not DOCS_DIR.exists():
        print(f"❌ Fehler: docs/ Ordner nicht gefunden: {DOCS_DIR}")
        return 1
    
    # Anzahl vorhandener Dateien
    existing_docs = [f for f, _, _ in DOC_METADATA if (DOCS_DIR / f).exists()]
    print(f"📋 Gefundene Dokumentationen: {len(existing_docs)}/{len(DOC_METADATA)}")
    
    # Generiere Tabelle
    new_table = generate_table()
    
    # Aktualisiere README
    try:
        update_readme(new_table)
        print(f"✨ Fertig! {len(existing_docs)} Einträge in der Tabelle.")
        return 0
    except Exception as e:
        print(f"❌ Fehler beim Aktualisieren: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
