# Exam-System Architektur

> **Version:** 1.0  
> **Datum:** 2026-03-01  
> **Status:** Production-Ready (Phase 1 abgeschlossen)

## Überblick

Dieses Exam-System ist so konzipiert, dass es **skalierbar**, **wartbar** und **erweiterbar** ist. Es folgt dem DRY-Prinzip (Don't Repeat Yourself) und ermöglicht die einfache Erstellung von Exams für mehrere Programmiersprachen und Themen.

## Design-Prinzipien

### 1. **Sprachunabhängige Rubriken**

Alle Exams verwenden die gleiche Bewertungsstruktur (A: 5.0, B: 7.5, C: 6.0, D: 6.5 Punkte), um Sprachen vergleichbar zu machen.

### 2. **Zentrale Verwaltung**

Rubriken, Templates und Standards sind in `shared/` zentralisiert, um Redundanz zu vermeiden.

### 3. **Nachschreib-Varianten**

Jedes Thema hat mindestens 4 vergleichbare Varianten (exam.md = v1, exam_v2.md, exam_v3.md, exam_v4.md, optional weitere wie exam_v5.md) mit identischer Struktur aber unterschiedlichen Kontexten.

### 4. **Online-Readiness**

Das System ist vorbereitet für zukünftige Online-Exams durch strukturierte Metadaten und maschinell lesbare Formate.

## Verzeichnisstruktur

```
docs/programmierung/grundlagen/exams/
│
├── README.md                    # Überblick für Nutzer
├── ARCHITECTURE.md              # Diese Datei (technische Dokumentation)
│
├── shared/                      # Zentrale Ressourcen
│   ├── README.md               # Dokumentation zu shared/
│   ├── rubrics.json            # Zentrale Bewertungsrubriken
│   ├── variation_knowledge_base.json # Aufgaben-Fingerprints
│   ├── variation_knowledge_base_schema.json # Schema fuer Aufgaben-Fingerprints
│   ├── solution_rubrics_knowledge_base.json # Bewertungslogik fuer Auto-Grading
│   ├── solution_rubrics_schema.json # Schema fuer Bewertungslogik
│   ├── templates/              # Vorlagen für neue Exams
│   │   ├── exam_template.md
│   │   ├── exam_datenstrukturen_template.md
│   │   ├── exam_funktionen_template.md
│   │   └── exam_kontrollstrukturen_template.md
│   └── structogramme/          # Allgemeine Structogramm-Standards
│       └── README.md
│
├── javascript/                  # JavaScript-spezifische Exams
│   ├── README.md               # Übersicht aller JS-Exams
│   ├── basics/
│   │   ├── exam.md             # Hauptversion (= v1)
│   │   ├── exam_v2.md          # Nachschreib-Variante 2
│   │   ├── exam_v3.md          # Nachschreib-Variante 3
│   │   ├── exam_v4.md          # Nachschreib-Variante 4
│   │   ├── solutions.md        # Lösungen zu v1
│   │   ├── solutions_v2.md
│   │   ├── solutions_v3.md
│   │   ├── solutions_v4.md
│   │   ├── metadata.json       # Metadaten (optional, für Online-System)
│   │   └── structogramme/      # Structogramme für dieses Thema
│   ├── datenstrukturen/        # Zukünftiges Thema
│   ├── funktionen/             # Zukünftiges Thema
│   └── kontrollstrukturen/     # Zukünftiges Thema
│
├── php/                         # PHP-spezifische Exams
│   ├── README.md
│   ├── basics/
│   │   ├── exam.md ... exam_vN.md
│   │   ├── solutions.md ... solutions_vN.md
│   │   └── structogramme/
│   └── [weitere Themen...]
│
└── python/                      # Python-spezifische Exams
    ├── README.md
    ├── basics/
    └── [weitere Themen...]
```

## Dateinamens-Konventionen

### Exam-Dateien

- **Hauptversion:** `exam.md` (= Variante 1)
- **Nachschreib-Varianten:** `exam_v2.md` bis `exam_vN.md`

### Lösungen

- **Entsprechend:** `solutions.md`, `solutions_v2.md` bis `solutions_vN.md`

### Metadata (optional, für Online-System)

- **Pro Thema:** `metadata.json`

## Rubriken-System

Alle Bewertungsrubriken sind in `shared/rubrics.json` definiert. Dies ermöglicht:

- **Konsistenz:** Alle Sprachen verwenden die gleiche Struktur
- **Wartbarkeit:** Änderungen an Rubriken nur an einer Stelle
- **Vergleichbarkeit:** Gleiche Punkteverteilung über alle Sprachen
- **Maschinelle Lesbarkeit:** Validierung und Export möglich

### Struktur der Rubriken

```json
{
  "aufgabe_a": {
    "title": "Variablen, Ein/Ausgabe, Grundkonzepte",
    "points": 5.0,
    "criteria": { ... }
  },
  "aufgabe_b": { "points": 7.5 },
  "aufgabe_c": { "points": 6.0 },
  "aufgabe_d": { "points": 6.5 }
}
```

**Gesamt:** 25.0 Punkte pro Exam

## Nachschreib-Varianten

Jedes Thema hat **mindestens 4 Varianten**, um faire Nachschreiber-Prüfungen zu ermöglichen.

### Design-Prinzipien für Varianten:

1. **Gleiche Struktur:** Alle Varianten haben identische Aufgabentypen
2. **Vergleichbare Schwierigkeit:** Unterschiedliche Zahlen/Kontexte, aber gleiches Niveau
3. **Keine Redundanz:** Verschiedene Beispiele verhindern Abschreiben

### Beispiel (Basics):

| Variante | Aufgabe A          | Aufgabe B             | Aufgabe C              | Aufgabe D                       |
| -------- | ------------------ | --------------------- | ---------------------- | ------------------------------- |
| v1       | Vorname/Alter      | Rechteck, °C→°F       | Punkte-Klassifizierung | Gerade/Positive                 |
| v2       | Produkt/Preis      | Kreisumfang, °F→°C    | Altersklassifizierung  | Ungerade/Negative               |
| v3       | Stadt/Einwohner    | Würfel, km→Meilen     | Temperatur             | Maximum/Summe                   |
| v4       | Buch/Seiten        | Dreieck, Meilen→km    | Geschwindigkeit        | Minimum/Positive                |
| v5 (PHP) | Film/Dauer         | Durchschnitt, min→sek | Luftfeuchte            | Teilbar-durch-3 + Mittelwert    |
| v6 (PHP) | Event/Teilnehmende | Restbudget, m→cm      | Akkustand              | Bereichszaehlung + Absolutsumme |

## Themen-Erweiterung

### Geplante Themen

1. ✅ **Basics** (implementiert)
2. ⏳ **Datenstrukturen** (Array, List, Dictionary, Set)
3. ⏳ **Funktionen** (Parameter, Return, Scope, Rekursion)
4. ⏳ **Kontrollstrukturen** (Loops, Switch, Ternär)
5. ⏳ **Dateien** (Read/Write, Parsing, Error Handling)
6. ⏳ **Datenbank** (SQL, CRUD, Joins, Transactions)

### Neues Thema hinzufügen

**Schritte:**

1. **Verzeichnis erstellen:**

   ```bash
   mkdir -p [sprache]/[thema]
   mkdir -p [sprache]/[thema]/structogramme
   ```

2. **Template verwenden:**

   ```bash
   cp shared/templates/exam_template.md [sprache]/[thema]/exam.md
   ```

3. **Exam anpassen** (Kontext, Zahlen, sprachspezifische Syntax)

4. **Varianten erstellen:** exam_v2.md, exam_v3.md, exam_v4.md, ...

5. **Lösungen schreiben:** solutions.md, solutions_v2.md, etc.

6. **Metadata hinzufügen (optional):**

   ```json
   {
     "theme": "datenstrukturen",
     "language": "javascript",
     "variants": 4,
     "online_ready": true,
     "time_limit_minutes": 60
   }
   ```

7. **Validierung ausführen:**
   ```bash
   python3 scripts/validate_exams.py --write-knowledge-base
   ```

## Online-Readiness

### Stufen der Online-Readiness

| Stufe                | Beschreibung                  | Online-Modus                 |
| -------------------- | ----------------------------- | ---------------------------- |
| **true**             | Vollständig autonom bewertbar | ✅ Code-Execution in Sandbox |
| **false**            | Nur für Papier-Exams geeignet | ❌ Keine Online-Execution    |
| **sandbox_required** | Benötigt isolierte Umgebung   | 🔶 Mit Sandbox möglich       |
| **api_based**        | Benötigt externe Ressourcen   | 🔶 Mit Mock-API möglich      |

### Themen nach Online-Readiness

- ✅ **Basics:** true (reine Code-Logik)
- ✅ **Datenstrukturen:** true (Array/List-Operationen)
- ✅ **Funktionen:** true (reine Funktionen)
- ✅ **Kontrollstrukturen:** true (Loops, Conditions)
- 🔶 **Dateien:** sandbox_required (File-System-Zugriff)
- 🔶 **Datenbank:** api_based (Mock-DB oder API)

## Validierung & Qualitätssicherung

Das System enthält automatisierte Validierung:

```bash
python3 scripts/validate_exams.py
python3 scripts/validate_exams.py --write-knowledge-base
```

**Prüft:**

- ✅ Alle Sprachen haben die gleichen Themen
- ✅ Jedes Thema hat mindestens 4 Varianten + passende Lösungen
- ✅ Punktesumme = 25.0
- ✅ Dateinamen folgen Konventionen
- ✅ Rubriken sind in rubrics.json definiert
- ✅ Metadata.json ist valide (falls vorhanden)
- ✅ Keine identischen Aufgabenstellungen in Varianten
- ✅ Jede Musterlösung enthält Punktbewertung und haeufige Fehler
- ✅ Wissensdatenbanken entsprechen ihren JSON-Schemata
- ✅ Kriterien-Summen passen zur Aufgabensumme

## Auto-Grading-Bausteine

Die langfristige Bewertungsarchitektur ist in [AUTOGRADING_RUBRICS.md](AUTOGRADING_RUBRICS.md) beschrieben.

Kernartefakte:

- `shared/solution_rubrics_knowledge_base.json`
- `shared/solution_rubrics_schema.json`
- `shared/variation_knowledge_base.json`
- `shared/variation_knowledge_base_schema.json`

## Zukunfts-Roadmap

### Phase 1: Fundament ✅ (abgeschlossen)

- [x] Architektur definieren
- [x] Verzeichnisstruktur aufbauen
- [x] Zentrale Rubriken (rubrics.json)
- [x] Basics für 3 Sprachen × mindestens 4 Varianten
- [x] Validierungs-Script

### Phase 2: Themen-Ausbau ⏳ (nächste Wochen)

- [ ] Datenstrukturen-Exams
- [ ] Funktionen-Exams
- [ ] Kontrollstrukturen-Exams
- [ ] Dateien-Exams
- [ ] Datenbank-Exams

### Phase 3: Export & Generation ⏳ (mittelfristig)

- [ ] Export nach JSON (für API)
- [ ] Export nach HTML (für Druck)
- [ ] Generator-Script (neue Exams automatisch)
- [ ] Metadata-Füllung automatisieren

### Phase 4: Online-System 🎯 (langfristig)

- [ ] Exam-Runner (Code-Execution)
- [ ] Auto-Grading (Teilbewertung)
- [ ] Webinterface (Schüler-Ansicht)
- [ ] Dashboard (Lehrkräfte-Auswertung)
- [ ] LMS-Integration (Moodle, etc.)

## Wartung & Best Practices

### Rubriken ändern

1. `shared/rubrics.json` bearbeiten
2. Alle betroffenen Exam-Dateien prüfen
3. Konsistenz mit `validate_exams.py` sicherstellen

### Neue Variante hinzufügen

1. Bestehende Variante als Vorlage verwenden
2. Kontext/Zahlen ändern, aber Struktur beibehalten
3. Lösungen entsprechend erstellen
4. Validierung ausführen

### Sprache hinzufügen

1. Neues Verzeichnis: `[sprache]/`
2. README für Sprach-Übersicht
3. Alle Themen analog zu bestehenden Sprachen
4. Templates an Syntax anpassen
5. Validierung ausführen

## Technische Details

### Verwendete Formate

- **Markdown:** Exam-Dateien (human-readable)
- **JSON:** Rubriken, Metadata (machine-readable)
- **Python:** Scripts für Validierung & Generation

### Abhängigkeiten (Scripts)

- Python 3.8+
- Standard-Library (json, os, pathlib, argparse)
- Keine externen Dependencies

### Git-Integration

- Alle Migrationen mit `git mv` (History-Preservation)
- Strukturierte Commits mit conventional commits
- Branch-Protection für `main`

## Support & Kontribution

### Neue Themen vorschlagen

1. Issue erstellen mit Themen-Beschreibung
2. Rubriken-Anpassung diskutieren
3. Template erstellen
4. Pull Request mit allen Varianten

### Fehler melden

1. Validierungs-Script ausführen
2. Issue mit Fehlerbeschreibung + Validierungs-Output
3. Pull Request mit Fix

## Lizenz & Credits

- **Projekt:** web-project-dynamic
- **Owner:** ChristineJanischek
- **Lizenz:** Siehe Root-Verzeichnis
- **Erstellt:** 2026-03-01 (Phase 1)

---

**Changelog:**

- 2026-03-01: Initial Architecture (Phase 1 abgeschlossen)
