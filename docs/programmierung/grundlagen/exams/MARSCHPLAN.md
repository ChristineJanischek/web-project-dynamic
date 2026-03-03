# 🎯 Marschplan: Exam-System Phase 2–4

> **Ziel:** Hochwertiges, skalierbares Exam-System mit erstklassigem Design  
> **Status:** Phase 1 ✅ abgeschlossen | Phase 2 ⏳ laufend (Start: 03.03.2026)  
> **Qualität:** Softwaredesign-Prinzipien + Buch-blätter-stil Layout

---

## 📅 Tägliche Checkliste

**Jeden Morgen:**

1. ✅ `git pull origin main` – Änderungen holen
2. ✅ Diese Datei öffnen → heutiges TODO prüfen
3. ✅ `python3 scripts/validate_exams.py` – System-Status prüfen
4. ✅ Aufgabe starten (siehe unten)

**Jeden Abend:**

1. ✅ Validierung laufen lassen
2. ✅ Commit mit Conventional Commits Pattern
3. ✅ `git push origin main`
4. ✅ Marschplan aktualisieren (✅/⏳ Status)

---

## 🗓️ Phase 2: Themen-Ausbau (Wochen 1–4)

**Zeitrahmen:** 02.03.2026 – 29.03.2026 (4 Wochen)  
**Ziel:** 5 weitere Themen × 3 Sprachen × 4 Varianten = 60 neue Exam-Dateien

### Woche 1: Datenstrukturen (03.03. – 09.03.)

#### Tag 1 (Mo, 03.03.) – Template & JavaScript v1

- [ ] **08:00–09:00** Template `exam_datenstrukturen_template.md` finalisieren
  - Aufgaben: Arrays/Listen, Dictionaries/Objects, Sets, Nested Structures
  - Rubrics anpassen (falls nötig)
- [ ] **09:00–11:00** JavaScript `datenstrukturen/exam.md` (v1) schreiben
  - Aufgabe A: Array-Operationen (push, pop, slice) – 5.0 Pkt
  - Aufgabe B: Dictionary/Object-Zugriff – 7.5 Pkt
  - Aufgabe C: Nested Arrays durchsuchen – 6.0 Pkt
  - Aufgabe D: Sets & Unique Values – 6.5 Pkt
- [ ] **11:00–12:00** Lösungen `solutions.md` schreiben
- [ ] **14:00–15:00** Validierung + Commit
  - `git commit -m "feat(exams): add javascript datenstrukturen v1"`

#### Tag 2 (Di, 04.03.) – JavaScript v2–v4

- [ ] **08:00–10:00** `exam_v2.md` erstellen (Kontext ändern)
- [ ] **10:00–12:00** `exam_v3.md` erstellen
- [ ] **14:00–16:00** `exam_v4.md` erstellen
- [ ] **16:00–17:00** Lösungen für v2–v4 schreiben
- [ ] **17:00–17:30** Validierung + Commit

#### Tag 3 (Mi, 05.03.) – PHP Datenstrukturen

- [ ] **08:00–10:00** PHP `exam.md` (v1) – Arrays, assoziative Arrays
- [ ] **10:00–12:00** PHP `exam_v2.md`
- [ ] **14:00–16:00** PHP `exam_v3.md` + `exam_v4.md`
- [ ] **16:00–17:00** Lösungen + Validierung + Commit

#### Tag 4 (Do, 06.03.) – Python Datenstrukturen

- [ ] **08:00–10:00** Python `exam.md` (v1) – Listen, Tuples, Dictionaries
- [ ] **10:00–12:00** Python `exam_v2.md`
- [ ] **14:00–16:00** Python `exam_v3.md` + `exam_v4.md`
- [ ] **16:00–17:00** Lösungen + Validierung + Commit

#### Tag 5 (Fr, 07.03.) – Design & Qualität

- [ ] **08:00–10:00** Layout-Review: Alle Datenstrukturen-Exams
  - Formatierung einheitlich?
  - Buch-Stil: Seitenumbrüche, Typografie, Whitespace
  - Code-Blöcke: Syntax-Highlighting korrekt?
- [ ] **10:00–11:00** Peer-Review (selbst durchführen):
  - Schwierigkeit vergleichbar über Varianten?
  - Punkteverteilung fair?
  - Lösungen vollständig?
- [ ] **11:00–12:00** Theme-Adaptations in `rubrics.json` ergänzen
- [ ] **14:00–15:00** Dokumentation aktualisieren:
  - READMEs (JavaScript, PHP, Python) → Datenstrukturen eintragen
  - ARCHITECTURE.md → Phase 2 Progress
- [ ] **15:00–16:00** Validierung + Final Commit
  - `git commit -m "feat(exams): complete datenstrukturen theme (3 lang × 4 var)"`

#### Wochenende (Sa/So, 08.–09.03.) – Puffer & Reflexion

- [ ] Optional: Verbesserungen aus Woche 1
- [ ] Optional: Vorarbeit für Woche 2 (Funktionen)

### Woche 2: Funktionen (10.03. – 16.03.)

#### Tag 6 (Mo, 10.03.) – Template & JavaScript

- [ ] **08:00–09:00** Template `exam_funktionen_template.md` finalisieren
  - Aufgaben: Parameter, Return, Scope, Higher-Order Functions
- [ ] **09:00–12:00** JavaScript `funktionen/exam.md` (v1) + Lösungen
  - Aufgabe A: Funktionsdeklaration & Parameter – 5.0 Pkt
  - Aufgabe B: Return-Werte & Berechnungen – 7.5 Pkt
  - Aufgabe C: Scope & Closures – 6.0 Pkt
  - Aufgabe D: Arrow Functions & Callbacks – 6.5 Pkt
- [ ] **14:00–17:00** JavaScript v2–v4 + Lösungen

#### Tag 7 (Di, 11.03.) – PHP Funktionen

- [ ] **08:00–12:00** PHP `exam.md` (v1) + v2 + Lösungen
- [ ] **14:00–17:00** PHP v3–v4 + Lösungen + Validierung

#### Tag 8 (Mi, 12.03.) – Python Funktionen

- [ ] **08:00–12:00** Python `exam.md` (v1) + v2 + Lösungen
- [ ] **14:00–17:00** Python v3–v4 + Lösungen + Validierung

#### Tag 9 (Do, 13.03.) – Design-Review & Dokumentation

- [ ] **08:00–12:00** Layout-Review + Qualitätsprüfung
- [ ] **14:00–17:00** Dokumentation + Commit

#### Tag 10 (Fr, 14.03.) – Puffer

- [ ] Nacharbeiten, Verbesserungen

### Woche 3: Kontrollstrukturen (17.03. – 23.03.)

#### Tag 11–15 (Mo–Fr) – Analog zu Woche 2

- [ ] **Mo:** Template + JavaScript
- [ ] **Di:** PHP
- [ ] **Mi:** Python
- [ ] **Do:** Design-Review
- [ ] **Fr:** Puffer

**Thema:** Loops, Switch, Ternär-Operator, Break/Continue

### Woche 4: Dateien & Datenbank (24.03. – 29.03.)

#### Tag 16–18 (Mo–Mi) – Dateien

- [ ] **Mo:** Template + JavaScript (File API)
- [ ] **Di:** PHP (fopen, fread, fwrite)
- [ ] **Mi:** Python (open, with, JSON/CSV)

#### Tag 19–20 (Do–Fr) – Datenbank

- [ ] **Do:** Template + JavaScript (fetch, localStorage)
- [ ] **Fr:** PHP (MySQLi, PDO) + Python (sqlite3)

#### Tag 21 (Sa, 29.03.) – Phase 2 Abschluss

- [ ] **08:00–10:00** Vollständige Validierung aller 6 Themen
- [ ] **10:00–12:00** Dokumentation finalisieren
- [ ] **14:00–15:00** Release Notes schreiben
- [ ] **15:00–16:00** Commit + Tag erstellen
  - `git tag -a v2.0.0 -m "Phase 2: 6 Themen × 3 Sprachen × 4 Varianten"`
  - `git push origin main --tags`

---

## 🗓️ Phase 3: Export & Generation (Wochen 5–8)

**Zeitrahmen:** 31.03.2026 – 26.04.2026 (4 Wochen)  
**Ziel:** Automatisierung + professionelle Ausgabe-Formate

### Woche 5: JSON-Export (31.03. – 06.04.)

#### Tag 22 (Mo, 31.03.) – Export-Script Grundgerüst

- [ ] **08:00–10:00** Script `scripts/export_exams.py` erstellen
  - Argument-Parsing: `--format json|html|pdf`
  - Exam-Parsing: Markdown → Python-Dict
- [ ] **10:00–12:00** JSON-Schema definieren
  ```json
  {
    "exam_id": "javascript-basics-v1",
    "language": "javascript",
    "theme": "basics",
    "variant": 1,
    "aufgaben": [...]
  }
  ```
- [ ] **14:00–17:00** Parser implementieren + Tests

#### Tag 23 (Di, 01.04.) – Metadata-Extraktion

- [ ] **08:00–12:00** Frontmatter-Parser (YAML in Markdown)
  - Beispiel:
    ```yaml
    ---
    exam_id: javascript-basics-v1
    version: 1.0
    date: 2026-03-01
    ---
    ```
- [ ] **14:00–17:00** Rubrics-Integration (aus `shared/rubrics.json`)

#### Tag 24 (Mi, 02.04.) – JSON-Output

- [ ] **08:00–12:00** JSON-Writer implementieren
- [ ] **14:00–17:00** Tests: Alle Exams → JSON exportieren
  - Validierung: JSON-Schema korrekt?

#### Tag 25 (Do, 03.04.) – API-Kompatibilität

- [ ] **08:00–12:00** API-Endpunkt-Schema definieren (für zukünftiges Online-System)
- [ ] **14:00–17:00** JSON-Export an API anpassen

#### Tag 26 (Fr, 04.04.) – Dokumentation & Commit

- [ ] **08:00–12:00** `scripts/README.md` aktualisieren
- [ ] **14:00–15:00** Commit: `feat(export): add JSON export functionality`

### Woche 6: HTML-Export (07.04. – 13.04.)

#### Tag 27 (Mo, 07.04.) – HTML-Template

- [ ] **08:00–12:00** Jinja2-Template `templates/exam.html` erstellen
  - **Buch-Stil:**
    - A4-Format, Seitenumbrüche
    - Serif-Font (Georgia, Times)
    - Angemessene Margins (2.5cm)
    - Kopf-/Fußzeilen
- [ ] **14:00–17:00** CSS-Stylesheet `templates/exam.css`
  - Print-Styles: `@media print`
  - Code-Highlighting: Prism.js oder Highlight.js

#### Tag 28 (Di, 08.04.) – HTML-Generator

- [ ] **08:00–12:00** HTML-Export implementieren
  - Markdown → HTML (mit Python-Markdown)
  - Template-Rendering (Jinja2)
- [ ] **14:00–17:00** Tests: Alle Exams → HTML

#### Tag 29 (Mi, 09.04.) – Design-Refinement

- [ ] **08:00–12:00** Typografie-Optimierung
  - Line-height, Font-sizes, Headings
  - Code-Block-Formatierung
- [ ] **14:00–17:00** Responsive Design (für Web-View)

#### Tag 30 (Do, 10.04.) – PDF-Export (Vorbereitung)

- [ ] **08:00–12:00** WeasyPrint oder wkhtmltopdf evaluieren
- [ ] **14:00–17:00** PDF-Generator Prototyp

#### Tag 31 (Fr, 11.04.) – PDF-Export (Finalisierung)

- [ ] **08:00–12:00** PDF-Export implementieren
  - HTML → PDF Conversion
  - Seitenumbrüche korrekt?
- [ ] **14:00–17:00** Batch-Export: Alle Exams → PDF
  - Output: `output/pdf/javascript/basics/exam_v1.pdf`

### Woche 7: Generator-Script (14.04. – 20.04.)

#### Tag 32 (Mo, 14.04.) – Exam-Generator

- [ ] **08:00–12:00** Script `scripts/generate_exam.py` erstellen
  - Interaktiv: Sprache, Thema, Variante wählen
  - Template automatisch ausfüllen
- [ ] **14:00–17:00** Kontext-Variation
  - Zufällige Zahlen generieren
  - Kontexte aus Pool wählen (Namen, Städte, Produkte)

#### Tag 33 (Di, 15.04.) – Varianten-Generator

- [ ] **08:00–12:00** Automatische Varianten-Erstellung
  - `--variants 4` → Generiert 4 Varianten
  - Schwierigkeit anpassen (leicht/mittel/schwer)
- [ ] **14:00–17:00** Tests + Qualitätsprüfung

#### Tag 34 (Mi, 16.04.) – Lösungen-Generator

- [ ] **08:00–12:00** Automatische Lösungen (wenn möglich)
  - Bei Berechnungen: Ergebnisse automatisch
  - Bei Code: Templates mit Platzhaltern
- [ ] **14:00–17:00** Tests

#### Tag 35 (Do, 17.04.) – Metadata-Automatisierung

- [ ] **08:00–12:00** Automatische Metadata-Generierung
  - `exam_id`, `date`, `version` automatisch setzen
- [ ] **14:00–17:00** Frontmatter automatisch einfügen

#### Tag 36 (Fr, 18.04.) – Dokumentation & Commit

- [ ] **08:00–12:00** Generator-Dokumentation
- [ ] **14:00–15:00** Commit: `feat(generator): add exam generator script`

### Woche 8: Phase 3 Abschluss (21.04. – 26.04.)

#### Tag 37–41 (Mo–Fr) – Integration & Testing

- [ ] **Mo:** Alle Export-Formate testen
- [ ] **Di:** Generator-Script finalisieren
- [ ] **Mi:** Dokumentation vervollständigen
- [ ] **Do:** CI/CD-Pipeline (GitHub Actions)
  - Automatische Validierung bei Push
  - PDF-Generierung
- [ ] **Fr:** Release v3.0.0

---

## 🗓️ Phase 4: Online-System (Wochen 9–16)

**Zeitrahmen:** 28.04.2026 – 21.06.2026 (8 Wochen)  
**Ziel:** Webinterface + Auto-Grading + Dashboard

### Woche 9–10: Backend-API (28.04. – 11.05.)

#### Woche 9: API-Infrastruktur

- [ ] **Tag 42 (Mo):** Technologie-Auswahl
  - Backend: FastAPI oder Flask (Python)
  - Datenbank: PostgreSQL + SQLAlchemy
  - Auth: JWT-Tokens
- [ ] **Tag 43 (Di):** API-Endpunkte definieren
  - `GET /api/exams` – Liste aller Exams
  - `GET /api/exams/{exam_id}` – Einzelnes Exam
  - `POST /api/submissions` – Lösung einreichen
  - `GET /api/submissions/{id}/grade` – Bewertung abrufen
- [ ] **Tag 44 (Mi):** FastAPI-Setup + Skeleton
- [ ] **Tag 45 (Do):** Datenbank-Schema + Models
- [ ] **Tag 46 (Fr):** CRUD-Operationen (Exams)

#### Woche 10: Submission & Grading

- [ ] **Tag 47 (Mo):** Submission-Endpoint
- [ ] **Tag 48 (Di):** Code-Execution Sandbox (piston API oder Docker)
- [ ] **Tag 49 (Mi):** Auto-Grading Logik
  - Unit-Tests für Code-Aufgaben
  - Pattern-Matching für Text-Aufgaben
- [ ] **Tag 50 (Do):** Grading-Endpoint + Tests
- [ ] **Tag 51 (Fr):** API-Dokumentation (OpenAPI/Swagger)

### Woche 11–12: Frontend (12.05. – 25.05.)

#### Woche 11: React-Setup + Exam-View

- [ ] **Tag 52 (Mo):** React-App Setup (Vite + TypeScript)
- [ ] **Tag 53 (Di):** Routing + Navigation
- [ ] **Tag 54 (Mi):** Exam-List-Komponente
- [ ] **Tag 55 (Do):** Exam-Detail-Komponente
- [ ] **Tag 56 (Fr):** Code-Editor-Integration (Monaco oder CodeMirror)

#### Woche 12: Submission-Flow

- [ ] **Tag 57 (Mo):** Submission-Form
- [ ] **Tag 58 (Di):** Code-Execution UI
- [ ] **Tag 59 (Mi):** Results-Display
- [ ] **Tag 60 (Do):** Grading-Feedback UI
- [ ] **Tag 61 (Fr):** Design-Polishing (Buch-Stil auch im Web)

### Woche 13–14: Dashboard & LMS (26.05. – 08.06.)

#### Woche 13: Dashboard

- [ ] **Tag 62 (Mo):** User-Dashboard
  - Übersicht: abgeschlossene Exams, Punkte, Fortschritt
- [ ] **Tag 63 (Di):** Admin-Dashboard
  - Exam-Management, Statistiken
- [ ] **Tag 64 (Mi):** Charts & Visualisierung (Recharts)
- [ ] **Tag 65 (Do):** Export-Funktionen (PDF, CSV)
- [ ] **Tag 66 (Fr):** Benachrichtigungen

#### Woche 14: LMS-Integration

- [ ] **Tag 67 (Mo):** LTI-Standard evaluieren
- [ ] **Tag 68 (Di):** Moodle-Integration Prototyp
- [ ] **Tag 69 (Mi):** Grade-Passback
- [ ] **Tag 70 (Do):** Testing in Moodle-Instanz
- [ ] **Tag 71 (Fr):** Dokumentation

### Woche 15–16: Testing & Launch (09.06. – 21.06.)

#### Woche 15: Testing

- [ ] **Tag 72 (Mo):** Unit-Tests (Backend)
- [ ] **Tag 73 (Di):** Integration-Tests (API)
- [ ] **Tag 74 (Mi):** E2E-Tests (Frontend, Playwright)
- [ ] **Tag 75 (Do):** Security-Audit
- [ ] **Tag 76 (Fr):** Performance-Testing

#### Woche 16: Launch

- [ ] **Tag 77 (Mo):** Deployment-Setup (Docker + Kubernetes)
- [ ] **Tag 78 (Di):** Produktions-Deployment
- [ ] **Tag 79 (Mi):** Monitoring (Prometheus + Grafana)
- [ ] **Tag 80 (Do):** User-Onboarding + Training
- [ ] **Tag 81 (Fr):** Release v4.0.0 🎉
  - `git tag -a v4.0.0 -m "Phase 4: Online-System Launch"`
  - Öffentliche Ankündigung

---

## 📏 Qualitätskriterien

### Softwaredesign-Prinzipien

#### DRY (Don't Repeat Yourself)

- ✅ Zentrale `rubrics.json` (✓ implementiert)
- ✅ Templates für alle Themen
- ✅ Shared Resources (`shared/`)

#### SOLID

- **S** Single Responsibility: Ein Modul = Eine Aufgabe
- **O** Open/Closed: Erweiterbar ohne Änderung (neue Sprachen/Themen)
- **L** Liskov Substitution: Varianten austauschbar
- **I** Interface Segregation: Klare API-Endpunkte
- **D** Dependency Inversion: Abstrakte Interfaces (z.B. für Code-Execution)

#### KISS (Keep It Simple, Stupid)

- Markdown > komplexe Formate
- Python Scripts > Build-Tools
- Git mv > komplexe Migrationen

#### YAGNI (You Aren't Gonna Need It)

- Nur Features implementieren, die tatsächlich gebraucht werden
- Phase-by-Phase statt Big Bang

### Buch-blätter-stil Layout

#### Typografie

- **Fonts:**
  - Headlines: `Georgia`, `Garamond` (Serif)
  - Body: `Georgia` 11pt–12pt
  - Code: `Fira Code`, `Consolas` (Monospace)
- **Line-height:** 1.6–1.8 (für Lesbarkeit)
- **Margins:**
  - Print: 2.5cm oben/unten, 3cm links/rechts
  - Web: `max-width: 800px`, zentriert

#### Layout

- **Seitenumbrüche:**
  - Jede Aufgabe auf neuer Seite (optional)
  - Keine Aufgabe über 2 Seiten geteilt
- **Whitespace:**
  - Großzügig zwischen Aufgaben (2–3 Zeilen)
  - Absätze: 1.5em Abstand
- **Nummerierung:**
  - Aufgaben: **A**, **B**, **C**, **D** (fett, 14pt)
  - Teilaufgaben: 1., 2., 3. (normal)

#### Code-Blöcke

- **Syntax-Highlighting:** ja (Prism.js oder Highlight.js)
- **Background:** helles Grau (`#f5f5f5`)
- **Border:** 1px solid `#ddd`
- **Padding:** 1em
- **Border-radius:** 4px

#### Farben (Print-freundlich)

- **Akzente:** Dunkelblau (`#1e40af`), nicht zu grell
- **Fehler:** Rot (`#dc2626`)
- **Erfolg:** Grün (`#16a34a`)
- **Grau-Töne:** `#374151`, `#6b7280`, `#9ca3af`

#### PDF-Spezifika

- **Header:** Exam-Titel, Sprache, Variante (rechts)
- **Footer:** Seitenzahl (mittig)
- **Wasserzeichen:** Optional "Nachschreiber v2" (für Varianten)

---

## 🔍 Validierungs-Checkliste

**Vor jedem Commit:**

- [ ] `python3 scripts/validate_exams.py` → 0 Fehler
- [ ] `python3 scripts/check_architecture.py` → keine kritischen Findings
- [ ] `python3 scripts/check_docs_navigation.py` → Navigation konsistent
- [ ] Alle Dateien gespeichert
- [ ] Keine `TODO:` oder `FIXME:` im Code
- [ ] Commit-Message folgt Convention:
  - `feat(scope): description`
  - `fix(scope): description`
  - `docs(scope): description`
  - `refactor(scope): description`

**Vor jedem Release:**

- [ ] Alle Tests grün
- [ ] Architektur-Report erzeugt (`reports/architecture_report.md`)
- [ ] Wiederverwendbare Artefakte aktuell (`shared/`, `templates/`, `scripts/lib/`)
- [ ] Dokumentation vollständig
- [ ] CHANGELOG.md aktualisiert
- [ ] Version-Nummer hochgezählt (Semantic Versioning)
- [ ] Git-Tag erstellt

---

## 📊 Fortschritts-Tracking

### Phase 1: ✅ Abgeschlossen (01.03.2026)

- [x] Verzeichnisstruktur
- [x] 24 Dateien migriert (3 Sprachen × basics × 4 Varianten × 2 Files)
- [x] `shared/rubrics.json` (zentrale Rubriken)
- [x] `scripts/validate_exams.py` (Validierung)
- [x] ARCHITECTURE.md + READMEs
- [x] Commit + Push

### Phase 2: ⏳ Geplant (Start: 03.03.2026)

- [ ] Datenstrukturen (Woche 1)
- [ ] Funktionen (Woche 2)
- [ ] Kontrollstrukturen (Woche 3)
- [ ] Dateien + Datenbank (Woche 4)

### Phase 3: ⏳ Geplant (Start: 31.03.2026)

- [ ] JSON-Export (Woche 5)
- [ ] HTML/PDF-Export (Woche 6)
- [ ] Generator-Script (Woche 7)
- [ ] CI/CD (Woche 8)

### Phase 4: ⏳ Geplant (Start: 28.04.2026)

- [ ] Backend-API (Wochen 9–10)
- [ ] Frontend (Wochen 11–12)
- [ ] Dashboard + LMS (Wochen 13–14)
- [ ] Testing + Launch (Wochen 15–16)

---

## 🚨 Risiken & Mitigation

| Risiko                  | Wahrscheinlichkeit | Impact | Mitigation                                         |
| ----------------------- | ------------------ | ------ | -------------------------------------------------- |
| **Zeitüberschreitung**  | Hoch               | Mittel | Puffer-Tage einplanen, Scope reduzieren wenn nötig |
| **Qualität leidet**     | Mittel             | Hoch   | Review-Prozess, strikte Validierung                |
| **Tech-Stack-Probleme** | Niedrig            | Hoch   | Technologien vorher evaluieren (PoC)               |
| **Scope-Creep**         | Mittel             | Mittel | Strikte Phase-Grenzen, YAGNI-Prinzip               |
| **Burnout**             | Mittel             | Hoch   | Pausen einplanen, Wochenenden frei halten          |

---

## 📝 Notizen & Anpassungen

### Änderungslog (diese Datei)

| Datum      | Änderung                                                          | Grund                            |
| ---------- | ----------------------------------------------------------------- | -------------------------------- |
| 01.03.2026 | Marschplan erstellt                                               | Projekt-Setup                    |
| 03.03.2026 | Qualitätsroutinen ergänzt (Architektur/Navigation/Release-Checks) | Best-Practice, Reuse, Sicherheit |
|            |                                                                   |                                  |
|            |                                                                   |                                  |

### Offene Fragen

- [ ] Welche Programmiersprachen noch? (z.B. Java, C++)
- [ ] Deployment-Umgebung für Phase 4? (Heroku, AWS, self-hosted?)
- [ ] LMS-Präferenz? (Moodle, Canvas, Blackboard?)

---

## 🎯 Nächste Schritte (Heute, 03.03.2026)

**08:00–08:30:**

- Diese Datei durchlesen
- Kaffee ☕
- Motivation tanken

**08:30–09:00:**

- Template `exam_datenstrukturen_template.md` analysieren
- Beispiele sammeln (Gute Array/List-Aufgaben)

**09:00–Start:**

- Tag 1 beginnen: JavaScript Datenstrukturen v1
- Nachmittags Qualitätslauf: `validate_exams` + `check_architecture` + `check_docs_navigation`

---

**Viel Erfolg! 🚀**

**Letzte Aktualisierung:** 03.03.2026
