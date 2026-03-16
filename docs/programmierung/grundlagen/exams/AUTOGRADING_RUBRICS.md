# Auto-Grading und Rubrics-Architektur

> Ziel: Das Exam-System so strukturieren, dass faire manuelle Korrektur und spaeteres automatisches Grading auf derselben fachlichen Grundlage arbeiten.

## Zielbild

Die Bewertungslogik wird in drei Schichten gepflegt:

1. Markdown-Quelle: `solutions*.md`
2. Maschinenlesbare Wissensdatenbank: `shared/solution_rubrics_knowledge_base.json`
3. Strukturvertrag: `shared/solution_rubrics_schema.json`

Parallel dazu existiert für Aufgabenvariation:

1. Markdown-Quelle: `exam*.md`
2. Variations-Wissensdatenbank: `shared/variation_knowledge_base.json`
3. Strukturvertrag: `shared/variation_knowledge_base_schema.json`

Diese Trennung ist absichtlich:

- keine doppelte Fachpflege
- klare Source of Truth
- wiederverwendbar für Papierkorrektur, LMS, Reporting und Analytics
- robust gegen inkonsistente manuelle Einzelanpassungen

## Kernkomponenten

### 1. Musterlösungen als fachliche Primärquelle

In jeder Aufgabe einer `solutions*.md` müssen vorhanden sein:

- `### Punktbewertung`
- `### Haeufige Fehler`

`Punktbewertung` beschreibt die fachliche Teilpunktelogik.
`Haeufige Fehler` dokumentiert typische Abweichungen für schnelle und gerechte Korrektur.

### 2. Rubrics-Wissensdatenbank

Datei: `shared/solution_rubrics_knowledge_base.json`

Diese Datei wird aus den Musterlösungen erzeugt und enthält pro Aufgabe:

- `entry_id`: stabile Aufgabennummer für Verarbeitung
- `task_id`: stabile Aufgaben-ID auf Variantenebene
- `points_total`: Gesamtpunkte der Aufgabe
- `criteria`: Bewertungsregeln mit Punkten
- `common_errors`: typische Fehlerbilder

Jedes Kriterium enthält stabile IDs:

- `criterion_id`
- `criterion_family_id`
- `criterion_key`

### 3. Schema-Dateien

Dateien:

- `shared/solution_rubrics_schema.json`
- `shared/variation_knowledge_base_schema.json`

Die Schema-Dateien definieren die technische Mindeststruktur der Wissensdatenbanken.
Damit kann die Generierung automatisiert validiert werden, ohne externe Bibliotheken vorauszusetzen.

## Stabile Bewertungs-IDs

Format für `criterion_id`:

`language.theme.variant.task.index.slug`

Beispiel:

`php.basics.solutions_v5.b.01.funktion-1-signatur`

Zweck:

- stabile Referenzen für LMS-Regeln
- konsistente Analytics über mehrere Runs
- Mapping von Feedbackbausteinen auf Bewertungskriterien

Format für `criterion_family_id`:

`language.theme.task.slug`

Zweck:

- semantisches Gruppieren aehnlicher Kriterien über Varianten hinweg
- Auswertung auf Themenebene statt nur auf Variantenebene

## Validierungsroutine

Script: `scripts/validate_exams.py`

Die Routine prueft jetzt zusätzlich:

- jede Lösung enthält pro Aufgabe `Punktbewertung`
- jede Lösung enthält pro Aufgabe `Haeufige Fehler`
- Bewertungskriterien sind maschinell parsebar
- Summe der Kriterien entspricht der Aufgabensumme
- beide Wissensdatenbanken entsprechen ihren JSON-Schemata
- Kriteriums-IDs und Entry-IDs sind eindeutig

Ausführung:

```bash
python3 scripts/validate_exams.py --write-knowledge-base
python3 scripts/validate_exams.py --write-knowledge-base --verbose
```

## Best Practices für neue Exams

### Neue Variante anlegen

1. `exam*.md` schreiben
2. `solutions*.md` mit Musterlösung schreiben
3. pro Aufgabe `Punktbewertung` und `Haeufige Fehler` ausfüllen
4. Validierung laufen lassen
5. generierte Wissensdatenbanken mit committen

### Neue Bewertungskriterien formulieren

- kurz, fachlich eindeutig, beobachtbar
- keine zusammengedrueckten Mischkriterien, wenn Teilpunkte getrennt bewertbar sind
- Hinweise nur in `hint`, nicht im Kriteriennamen verstecken
- gleiche Kriteriumslogik möglichst konsistent über Varianten halten

### Häufige Fehler formulieren

- reale Schülerfehler, keine theoretischen Randfälle
- kurz und korrigierbar beschrieben
- keine Dopplung von Bewertungskriterien

## Sicherheits- und Wartungsprinzipien

- Markdown bleibt die fachliche Primärquelle.
- JSON-Dateien sind generierte Artefakte, nicht manuell zu pflegen.
- Schema-Dateien definieren den technischen Vertrag für Folgeprozesse.
- Validierung muss ohne Fremdbibliotheken laufen.
- IDs werden deterministisch erzeugt, nicht zufaellig.

## Gedächtnis- und Wissensstruktur

Das System nutzt drei Ebenen:

1. Repository-Dokumentation in `docs/programmierung/grundlagen/exams/`
2. Generierte Wissensdatenbanken in `docs/programmierung/grundlagen/exams/shared/`
3. Repo-Memory für Agentenarbeit in `/memories/repo/` als nicht-kanonische Arbeitsnotizen

Wichtig:

- Kanonische Fachregeln gehoeren in `docs/`.
- Agent-Memory dient nur der Arbeitsunterstuetzung, nicht der offiziellen Dokumentation.

## Langfristige Anschlussfaehigkeit

Diese Architektur ist vorbereitet für:

- teilautomatisches Teacher-Support-Grading
- vollautomatisches LMS-Grading für strukturierte Aufgaben
- criterion-level analytics
- Fehlercluster pro Aufgabe und Variante
- Export in APIs oder Lernplattformen

## Zugehoerige Dateien

- `scripts/validate_exams.py`
- `shared/solution_rubrics_knowledge_base.json`
- `shared/solution_rubrics_schema.json`
- `shared/variation_knowledge_base.json`
- `shared/variation_knowledge_base_schema.json`
- `shared/templates/solutions_template.md`

## Aenderungshistorie

- 2026-03-12: Rubrics-Wissensdatenbank eingeführt
- 2026-03-12: stabile Kriteriums-IDs eingeführt
- 2026-03-12: Schema-Validierung für Wissensdatenbanken eingeführt
