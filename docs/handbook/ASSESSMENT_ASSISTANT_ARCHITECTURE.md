# Assessment Assistant Architektur

> Status: Phase 0 bis 1 vorbereitet  
> Zweck: Owner-only Korrekturhilfe und Feedback-Assistenz fuer Web-Projekte und spaeter weitere Projekttypen wie ML

## Zielbild

Das Modul erweitert dieses Repository um eine langfristig wachsende Bewertungsplattform mit vier harten Leitplanken:

1. Bewertungsdaten bleiben strikt owner-only.
2. Fachlogik bleibt wiederverwendbar und projektart-unabhaengig.
3. Konfiguration, Rubrik, Auswertung und Export sind getrennte Schichten.
4. Markdown ist die kanonische Bewertungsquelle, HTML ist ein generiertes Ausgabeformat.

## Sicherheitsmodell

Bewertungen, Schuelerarchive, entpackte Projekte und generierte Berichte duerfen nicht Teil des geteilten Template-Inhalts sein.
Deshalb werden sensible Laufzeitdaten bewusst ausserhalb des Repositorys gehalten.

### Verbindliche Regel

- Modulcode, Schemata und neutrale Templates liegen im Repository.
- Sensible Laufzeitdaten liegen in einem owner-only Workspace unter Downloads.
- Der Workspace muss ausserhalb des Repositorys liegen.
- Verzeichnisse erhalten Modus 700.
- Owner-Konfigurationsdateien erhalten Modus 600.

### Warum diese Trennung notwendig ist

Ein Repository allein kann nicht garantieren, dass lokale Bewertungsdaten fuer andere Nutzer unsichtbar bleiben, wenn diese Daten eingecheckt oder innerhalb geteilter Template-Strukturen abgelegt werden.
Vertraulichkeit entsteht hier nur durch eine Kombination aus:

- owner-only Ablage ausserhalb des Repos
- Git-Ignorierung als Schutz vor versehentlichem Commit
- Code Owners und Branch-Protection fuer den Codebereich

## Owner-only Workspace

Standardpfad:

- ~/Downloads/edu-assessment-owner

Verzeichnisstruktur:

```text
edu-assessment-owner/
├── archiv/              # abgeschlossene oder ersetzte Datenstaende
├── ausgang/             # generierte Reports: .md, .html, spaeter .docx
├── batch_bewertungen/   # zusammengefuehrte Batch-Auswertungen
├── boegen/              # hochgeladene Bewertungsboegen (.docx, spaeter .md)
├── config/              # owner_profile.json und spaetere Provider-Konfigurationen
├── eingang/             # ZIP-Dateien der Schuelerprojekte
├── entpackt/            # isolierte Arbeitskopien der ZIP-Inhalte
└── logs/                # technische Laufprotokolle ohne fachliche Offenlegung nach aussen
```

Hinweis:

- Im Nutzerwunsch wurde eingang doppelt genannt. Die Architektur fuehrt es genau einmal.
- Fuer die operative Verarbeitung wird zusaetzlich entpackt benoetigt.

## Schichtenmodell

### 1. Ingestion

- Annahme von ZIP-Dateien mit Projektquellcode
- Annahme von Bewertungsboegen als .docx
- spaeter: sichere Vorpruefung von Dateinamen, Dateitypen und Archivstruktur

### 2. Normalisierung

- Entpacken in owner-only Arbeitskopien
- Umwandlung des Bewertungsbogens in ein maschinenlesbares internes Modell
- Extraktion einer kanonischen Bewertungsmatrix als Markdown und JSON

### 3. Analyse

- Projektart-spezifische Checks, aber auf gemeinsamer Vertragsbasis
- Kombination aus heuristischen Regeln, Vergleich mit Musterloesung, spaeter KI-Assistenz
- Ergebnis pro Kriterium: Punkte, Status, Anmerkung, Treffer/Evidenz

### 4. Reporting

- kanonischer Bewertungsreport als Markdown
- daraus generiertes HTML fuer fehlerfreies Copy-Paste nach Word
- spaeter optional direkter DOCX-Export

## Kanonische Datenvertraege

Das Modul sollte dauerhaft auf stabilen, projektart-unabhaengigen Verträgen aufbauen.

### Konfiguration

Owner-Profile definieren:

- Workspace-Pfad
- erlaubte Eingabeformate
- Verzeichniszuordnungen
- Sicherheitsregeln
- Notenskala
- Exportziele

### Rubrikmodell

Jedes Kriterium benoetigt langfristig mindestens:

- criterion_id
- title
- max_points
- awarded_points
- status
- note
- evidence

### Reportmodell

Jeder Bericht benoetigt langfristig mindestens:

- report_id
- rubric_id
- project_type
- student_project_name
- max_points
- awarded_points
- grade
- summary
- criteria[]
- recommendation_plan

## Bewertungslogik

Verbindliche Vorgaben fuer dieses Modul:

- linearer Notenschluessel
- Notenskala 1.00 bis 6.00
- Ausgabe mit zwei Nachkommastellen
- Kriterienausgabe mit Punkte, Status, Anmerkung und Treffer

Formel fuer die Note:

- prozent = awarded_points / max_points
- note = 6.0 - (prozent \* 5.0)
- Untergrenze 1.0, Obergrenze 6.0
- Rundung auf zwei Nachkommastellen

Damit gilt:

- 100 Prozent = 1.00
- 0 Prozent = 6.00

## Wiederverwendung ueber Web hinaus

Die Kernarchitektur bleibt absichtlich generisch.
Nur die Analysemodule werden projekttyp-spezifisch.

Beispiele spaeterer Adapter:

- web_project
- ml_project
- data_project
- python_cli_project

Gemeinsam bleiben:

- Intake
- Sicherheitsregeln
- Rubrikmodell
- Reportmodell
- Markdown-zu-HTML-Export
- Batch-Verarbeitung

## Erste Repo-Artefakte in dieser Phase

- Python-Paket fuer Assessment-Assistenz unter scripts/assessment_assistant/
- Bootstrap-Skript fuer den owner-only Workspace
- Konfigurations-Template fuer Owner-Profile
- Git-Schutz gegen lokale Bewertungsdaten im Repo

## Naechste Schritte nach Upload von Bewertungsbogen und Musterprojekt

1. Bewertungsbogen analysieren und in Rubrikvertrag ueberfuehren.
2. Musterloesung extrahieren und projekttyp-spezifische Trefferlogik definieren.
3. Markdown-Reportstruktur und HTML-Renderer implementieren.
4. Routine fuer kurz-, mittel- und langfristige Handlungsempfehlungen ergaenzen.
5. Batch-Verarbeitung fuer mehrere ZIP-Dateien aufsetzen.
