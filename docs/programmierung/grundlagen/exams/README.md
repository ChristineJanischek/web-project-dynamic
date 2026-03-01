# Exam system Grundlagen (Fundamentals)

Diese Dokumente liefern druckbare Exams zu den Grundlagen der Programmierung fuer mehrere Sprachen. Sie sind so gestaltet, dass Schuelerinnen und Schueler die Aufgaben auch handschriftlich bearbeiten koennen.

## Ablageort

`docs/programmierung/grundlagen/exams/` ist bewusst in den sprachuebergreifenden Grundlagen abgelegt:

- Fachlicher Bezug: Grundlagen-Themen, die es in allen Sprachen gibt
- Keine Redundanz: Eine gemeinsame Struktur, je Sprache eine Variante
- Erweiterbar: Neue Sprachen lassen sich in derselben Struktur ergaenzen

## Struktur

### Basics (Fundamentals)

- `JavaScript_Grundlagen_Basics.md`
- `PHP_Grundlagen_Basics.md`
- `Python_Grundlagen_Basics.md`
- `JavaScript_Grundlagen_Basics_Loesungen.md`
- `PHP_Grundlagen_Basics_Loesungen.md`
- `Python_Grundlagen_Basics_Loesungen.md`

### Weitere Schwerpunkte (pro Sprache aufzulegen)

**Schablonen:**

- `TEMPLATE_Grundlagen_Basics.md`
- `TEMPLATE_Grundlagen_Funktionen.md`
- `TEMPLATE_Grundlagen_Kontrollstrukturen.md`
- `TEMPLATE_Grundlagen_Datenstrukturen.md`

**Ablage der Struktogramme**

- `structogramme/`
  - Ablage fuer spaetere Struktogramme (SVG)
  - Namenskonvention in `structogramme/README.md`

## Bewertungslogik (linear)

- Gesamtpunkte: 25
- Lineare Bewertung: `prozent = (punkte / 25) * 100`
- Teilpunkte sind zulaessig, Rundung in 0.5-Schritten

## Erweiterungseinschaetzung

Der Ausbau zu einem teil-automatisierten Online-Exam ist realistisch, wenn die Inhalte streng strukturiert bleiben. Ein formatstabiler Markdown-Exam ist eine gute Grundlage fuer spaetere Extraktion in JSON/HTML. Die groessten Risiken liegen in inkonsistenter Aufgabenstruktur, fehlender Metadatenpflege und unklaren Bewertungsregeln. Mit einer stabilen Schablone, klaren Metadaten und einer minimalen Ausfuehrungsumgebung (z. B. Runner pro Sprache) ist die Erweiterung gut planbar.

## Fahrplan (Milestones)

**M1: Druckbare Exams (jetzt)**

- Einheitliches Markdown-Layout pro Sprache
- Klare Punktevergabe je Aufgabenblock
- Fokus auf handschriftliche Loesbarkeit

**M2: Metadaten-Schicht**

- JSON-Metadaten je Exam (Themen, Punkte, Sprache, Zeitbedarf)
- Validationsskript fuer Struktur und Punkte

**M3: Generator**

- Markdown -> HTML/PDF Export
- Einheitlicher Header/Footer, Nummerierung, Punktetabellen

**M4: Online-Exam (Klick)**

- HTML-Form mit Aufgaben, Eingabefeldern, Beispiel-I/O
- Statische Auslieferung ueber GitHub Pages oder Classroom-Repo

**M5: Teilautomatische Bewertung**

- Abgleich von Code-Snippets gegen Loesungsskizzen
- Rubrik-basierte Teilpunktvergabe
- Review-Checkliste fuer Lehrkraefte

**M6: Reporting**

- Sammel-Export in CSV/JSON
- Zusammenfassung je Klasse/Schueler/in

## Wartungsroutinen

### Neue Sprache hinzufuegen

1. Fuer jeden Schwerpunkt eine neue Datei aus der TEMPLATE\_\* ablegen
2. Benennung: `<SPRACHE>_Grundlagen_<SCHWERPUNKT>.md`
3. Loesungsdatei erstellung (optional): `<SPRACHE>_Grundlagen_<SCHWERPUNKT>_Loesungen.md`
4. Bewertungsrubrik ergaenzen (Tabelle mit Teilpunkten)
5. Struktogramm-Platzhalter vorbereiten

### Exam-Inhalte aendern

- Neue Aufgaben als Variante (z. B. `..._v2.md`) anlegen
- Alt-Exam als Archiv mitnehmen
- Vor Aenderungen: pruefen, ob eine bestehende Schablone reicht oder ob neue Anforderungen die Schablone selbst aendern

### Allgemein

- Punkte stets in 0.5-Schritten vergeben (Rundung)
- Bewertungsrubrik immer mit konkreten Sprach-Beispielen versehen
- Bei Navigationsergaenzungen: `python3 scripts/update_readme_docs.py` ausfuehren
