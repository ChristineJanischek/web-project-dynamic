# Exam-System: Programmiergrundlagen

> **Skalierbar, wartbar, erweiterbar** – Exams für JavaScript, PHP und Python

Dieses System liefert druckbare und potentiell online-fähige Exams zu den Grundlagen der Programmierung. Die Aufgaben sind handschriftlich lösbar und folgen einheitlichen Bewertungsrubriken über alle Sprachen hinweg.

## 🎯 Überblick

- **3 Sprachen:** JavaScript, PHP, Python
- **Themen:** Basics (weitere: Datenstrukturen, Funktionen, Kontrollstrukturen, Dateien, Datenbank geplant)
- **Mindestens 4 Varianten** pro Thema (weitere Varianten möglich)
- **Zentrale Rubriken:** Konsistente Bewertung über alle Sprachen
- **25 Punkte** pro Exam (A: 5.0, B: 7.5, C: 6.0, D: 6.5)

## 📁 Verzeichnisstruktur

\`\`\`
exams/
├── README.md (diese Datei)
├── ARCHITECTURE.md (technische Dokumentation)
│
├── shared/ # Zentrale Ressourcen
│ ├── rubrics.json # Bewertungsrubriken (DRY-Prinzip)
│ ├── variation_knowledge_base.json # Aufgaben-Fingerprints
│ ├── templates/ # Vorlagen für neue Exams
│ └── structogramme/ # Allgemeine Standards
│
├── javascript/ # JavaScript-spezifische Exams
│ ├── README.md
│ └── basics/
│ ├── exam.md # Hauptversion (v1)
│ ├── exam_v2.md # Nachschreib-Variante 2
│ ├── exam_v3.md # Nachschreib-Variante 3
│ ├── exam_v4.md # Nachschreib-Variante 4
│ ├── solutions.md # Lösungen v1
│ ├── solutions_v2.md # Lösungen v2
│ ├── solutions_v3.md # Lösungen v3
│ ├── solutions_v4.md # Lösungen v4
│ └── structogramme/
│
├── php/ # PHP-spezifische Exams
│ ├── README.md
│ └── basics/
│ └── [gleiche Struktur wie JavaScript]
│
└── python/ # Python-spezifische Exams
├── README.md
└── basics/
└── [gleiche Struktur wie JavaScript]
\`\`\`

## 🚀 Schnellstart

### Exam durchführen

1. **Wähle Sprache und Thema:**
   - [JavaScript Basics](javascript/basics/exam.md)
   - [PHP Basics](php/basics/exam.md)
   - [Python Basics](python/basics/exam.md)

2. **Wähle Variante** (bei Nachschreibern):
   - \`exam.md\` = Hauptversion
   - \`exam_v2.md\` bis \`exam_vN.md\` = Nachschreib-Varianten

3. **Ausdrucken oder digital nutzen**

4. **Bewertung:** Siehe entsprechende \`solutions.md\` Datei

### Neues Thema erstellen

\`\`\`bash

# 1. Template kopieren

cp shared/templates/exam_template.md javascript/datenstrukturen/exam.md

# 2. Exam anpassen (Kontext, Zahlen, Syntax)

# 3. Varianten erstellen (v2, v3, v4, ...)

# 4. Lösungen schreiben

# 5. Validierung + Duplikatcheck + Wissensdatenbank

python3 scripts/validate_exams.py --write-knowledge-base
\`\`\`

## 📊 Bewertungssystem

Alle Exams folgen der **gleichen Rubrik** (definiert in \`shared/rubrics.json\`):

| Aufgabe    | Thema                       | Punkte   |
| ---------- | --------------------------- | -------- |
| **A**      | Variablen + Ein/Ausgabe     | 5.0      |
| **B**      | Funktionen mit Berechnungen | 7.5      |
| **C**      | Fallunterscheidungen        | 6.0      |
| **D**      | Schleifen + Datenstrukturen | 6.5      |
| **Gesamt** |                             | **25.0** |

**Bewertungsschlüssel:** \`prozent = (punkte / 25) \* 100\`

## 🔄 Nachschreib-Varianten

Jedes Thema hat **mindestens 4 vergleichbare Varianten**:

| Variante | Aufgabe A                | Aufgabe B             | Aufgabe C              | Aufgabe D                       |
| -------- | ------------------------ | --------------------- | ---------------------- | ------------------------------- |
| **v1**   | Vorname/Alter            | Rechteck, °C→°F       | Punkte-Klassifizierung | Gerade/Positive                 |
| **v2**   | Produkt/Preis            | Kreisumfang, °F→°C    | Altersklassifizierung  | Ungerade/Negative               |
| **v3**   | Stadt/Einwohner          | Würfel, km→Meilen     | Temperatur             | Maximum/Summe                   |
| **v4**   | Buch/Seiten              | Dreieck, Meilen→km    | Geschwindigkeit        | Minimum/Positive                |
| **v5**   | Film/Dauer (PHP)         | Durchschnitt, min→sek | Luftfeuchte            | Teilbar-durch-3 + Mittelwert    |
| **v6**   | Event/Teilnehmende (PHP) | Restbudget, m→cm      | Akkustand              | Bereichszaehlung + Absolutsumme |

**Design-Prinzipien:**

- ✅ Gleiche Struktur (A, B, C, D)
- ✅ Identische Punkteverteilung
- ✅ Vergleichbare Schwierigkeit
- ✅ Unterschiedliche Kontexte (fair für Nachschreiber)

## 🎨 Themen

### ✅ Verfügbar (Basics)

- **Variablen & Ein/Ausgabe**
- **Funktionen** (einfache Berechnungen)
- **Fallunterscheidungen** (if-else, Validierung)
- **Schleifen & Datenstrukturen** (Arrays, Iteration)

### ⏳ Geplant

- **Datenstrukturen** (Arrays, Listen, Dictionaries, Sets)
- **Funktionen** (Parameter, Scope, Rekursion, Higher-Order)
- **Kontrollstrukturen** (Loops, Switch, Ternär)
- **Dateien** (Read/Write, Parsing, Error Handling)
- **Datenbank** (SQL, CRUD, Joins, Transactions)

## 🛠️ Wartung & Validierung

### Validierung ausführen

\`\`\`bash

# Alle Exams prüfen

python3 scripts/validate_exams.py

# Nur eine Sprache prüfen

python3 scripts/validate_exams.py --language javascript

# Ausführliche Ausgabe

python3 scripts/validate_exams.py --verbose

# Wissensdatenbank mit Fingerprints aktualisieren

python3 scripts/validate_exams.py --write-knowledge-base
\`\`\`

**Prüft:**

- ✅ Verzeichnisstruktur vollständig
- ✅ Mindestens 4 Varianten vorhanden
- ✅ Lösungen für alle Varianten
- ✅ Punktesumme = 25.0
- ✅ rubrics.json valide
- ✅ Datei-Benennungen korrekt
- ✅ Keine identischen Aufgabenstellungen zwischen Varianten

### Neue Sprache hinzufügen

\`\`\`bash

# 1. Verzeichnis erstellen

mkdir -p [sprache]/basics
mkdir -p [sprache]/basics/structogramme

# 2. Templates anpassen

cp shared/templates/exam_template.md [sprache]/basics/exam.md

# 3. Alle Varianten erstellen (v2, v3, v4, ...)

# 4. README für Sprache schreiben

cp javascript/README.md [sprache]/README.md

# 5. Validierung

python3 scripts/validate_exams.py --language [sprache]
\`\`\`

## 📖 Dokumentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** – Technische Dokumentation, Design-Prinzipien, Roadmap
- **[AUTOGRADING_RUBRICS.md](AUTOGRADING_RUBRICS.md)** – Bewertungslogik, Wissensdatenbanken, Schema-Vertraege
- **[shared/rubrics.json](shared/rubrics.json)** – Zentrale Bewertungsrubriken
- **[scripts/validate_exams.py](../../../../../../scripts/validate_exams.py)** – Validierungs-Script

### Sprach-spezifische READMEs

- **[JavaScript](javascript/README.md)** – JavaScript-Exams Übersicht
- **[PHP](php/README.md)** – PHP-Exams Übersicht
- **[Python](python/README.md)** – Python-Exams Übersicht

## 🌐 Online-Readiness

Das System ist für **zukünftige Online-Exams** vorbereitet:

| Thema                  | Online-Modus                               | Status      |
| ---------------------- | ------------------------------------------ | ----------- |
| **Basics**             | ✅ Vollständig (Code-Execution in Sandbox) | Ready       |
| **Datenstrukturen**    | ✅ Vollständig                             | Ready       |
| **Funktionen**         | ✅ Vollständig                             | Ready       |
| **Kontrollstrukturen** | ✅ Vollständig                             | Ready       |
| **Dateien**            | 🔶 Mit Sandbox (File-System-Zugriff)       | Vorbereitet |
| **Datenbank**          | 🔶 Mit Mock-API                            | Vorbereitet |

## 📅 Roadmap

### Phase 1: Fundament ✅ (abgeschlossen)

- [x] Verzeichnisstruktur
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
- [ ] Export nach HTML/PDF
- [ ] Generator-Script
- [ ] Metadata-Automatisierung

### Phase 4: Online-System 🎯 (langfristig)

- [ ] Exam-Runner (Code-Execution)
- [ ] Auto-Grading
- [ ] Webinterface
- [ ] Dashboard
- [ ] LMS-Integration

## 📝 Lizenz & Credits

- **Projekt:** web-project-dynamic
- **Owner:** ChristineJanischek
- **Erstellt:** 2026-03-01
- **Lizenz:** Siehe Root-Verzeichnis

## 🤝 Beitragen

Neue Themen, Varianten oder Sprachen sind willkommen:

1. **Issue erstellen** mit Themen-Beschreibung
2. **Template verwenden** aus \`shared/templates/\`
3. **Validierung ausführen**
4. **Pull Request** einreichen

---

**Letzte Aktualisierung:** 2026-03-12
