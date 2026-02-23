# Doku-Struktur & Pflege-Regeln

Diese Seite definiert verbindliche Regeln für die Ablage und Pflege der Dokumentation.

## Ziel

- Inhalte klar auffindbar halten
- Redundanzen vermeiden
- Link-Stabilität bei Änderungen sicherstellen
- Erweiterungen planbar und wartbar machen

## Verzeichnislogik

- `docs/statisch/`
  - Grundlagen zu HTML/CSS und statischer Frontend-Struktur
- `docs/dynamisch/`
  - JavaScript, PHP, Python, Datenbank, Tests
- `docs/konzeption/`
  - Zielgruppenanalyse, Corporate Design, Projektkonzeption, Git-Workflow
- `docs/programmierung/`
  - Sprachübergreifende und modulare Programmier-Grundlagen
- `docs/handbook/`
  - Leitfäden für Lehrende, Architektur, Template-Strategie

## Ablageregeln

1. Neue Datei zuerst dem inhaltlich passenden Bereich zuordnen.
2. Keine Duplikate in mehreren Bereichen anlegen.
3. Sprachspezifische Inhalte in den Sprachpfad (`docs/programmierung/grundlagen/...`) legen.
4. Lehrenden-spezifische Prozessdokus ins `handbook`.
5. Bei Grenzfällen in `docs/README.md` kurz verlinken und begründen.

## Benennungsregeln

- Dateinamen in `kebab-case` (z. B. `responsive-design.md`)
- Klarer fachlicher Name statt projektinterner Kürzel
- Nur `.md` für Lern-/Handbuchdokumente

## Link-Regeln

- Nur relative Links innerhalb des Repos
- Bei Verschiebungen immer alle Markdown-Verweise repo-weit aktualisieren
- Nach Änderungen Linkcheck durchführen (siehe unten)

## Wartungsroutine (Pflicht)

1. Struktur- oder Doku-Änderung durchführen
2. Tabelle synchronisieren:
   - `python3 scripts/update_readme_docs.py`
3. Konsistenz prüfen:
   - `python3 scripts/update_readme_docs.py --check`
4. Repo-weiten Markdown-Linkcheck ausführen
5. Erst danach committen/pushen

## Erweiterungsstrategie

- Neue Hauptkategorie nur bei klarer inhaltlicher Trennung einführen
- Vor einer neuen Kategorie prüfen, ob ein Unterordner in bestehender Kategorie reicht
- Bei neuen Kategorien `docs/README.md` und `scripts/update_readme_docs.py` mitpflegen

## Verantwortlichkeit

- Jede Strukturänderung enthält:
  - Migrationsmapping (alt → neu)
  - Verweis-Update im gleichen Commit oder direktem Folgecommit
  - Abschlussnachweis: Linkcheck ohne Defekte
