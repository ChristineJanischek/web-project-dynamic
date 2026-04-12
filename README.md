# Web Project Dynamic

Ein modernes Ausbildungs-Template für **GitHub Classroom**: Vom ersten HTML-Grundgerüst bis zur vollständigen Webanwendung mit React, PHP, Python (Flask), JavaScript, CSS und MySQL-Datenbankanbindung.

**🎯 Ziel:** Schüler ohne Vorkenntnisse schrittweise zur professionellen Webentwicklung befähigen - mit umfangreicher Dokumentation, praktischen Beispielen und automatischer Code-Validierung.

**✨ Features:**

- 📚 Umfassende Dokumentation zu allen Web-Technologien
- 🔄 Versioniertes Lernsystem (v1.0, v2.0, ...)
- 🤖 Automatische HTML-Validierung via GitHub Actions
- 🔒 Owner-only Bewertungsassistenz mit separatem Secure-Workspace als Architekturgrundlage
- 📱 Responsive Design von Anfang an
- 💡 Praktische Beispiele mit TODO-Kommentaren
- 🎓 Best Practices für GitHub Classroom
- 🚀 Live Server vorinstalliert für sofortiges Testen

## 🆕 Was ist neu? (Stand: 12.04.2026)
- ✅ Neue modulare Grundlagenpfade für [PHP](docs/programmierung/grundlagen/php/README.md), [Python](docs/programmierung/grundlagen/python/README.md) und [JavaScript](docs/programmierung/grundlagen/javascript/README.md)
- ✅ Python-Kapitel zu Algorithmen und Dateiverarbeitung ergänzt
- ✅ Unterrichtsmaterial von `ka_grundlagen/` nach [material/ka_grundlagen](material/ka_grundlagen) migriert
- ✅ Verweise in der zentralen Dokumentation auf die neue Struktur aktualisiert

---

## 🚀 Schnellstart (empfohlen)

### Für Schüler:innen in 5 Minuten

1. Projekt in VS Code öffnen (Codespaces oder lokal)
2. Bei lokaler Nutzung One-Click-Task ausführen: `Tasks: Run Task` → `Setup: Install Live-Test Extensions`
3. Erste Datei öffnen: [version1/aufgabe/index.html](version1/aufgabe/index.html)
4. Mit Live Server starten (`Open with Live Server`)
5. Änderungen speichern und direkt im Browser prüfen

### Detaillierte Setup-Anleitungen

- Codespaces Zero-Setup: [.devcontainer/CODESPACES_SETUP.md](.devcontainer/CODESPACES_SETUP.md)
- DevContainer Details: [.devcontainer/README.md](.devcontainer/README.md)
- Live Server Quickstart: [docs/handbook/QUICKSTART_LIVE_SERVER.md](docs/handbook/QUICKSTART_LIVE_SERVER.md)
- Workspace Live-Test Setup (neu): [docs/handbook/WORKSPACE_LIVE_TEST_SETUP.md](docs/handbook/WORKSPACE_LIVE_TEST_SETUP.md)
- Beitragsregeln & Workflow: [CONTRIBUTING.md](CONTRIBUTING.md)
- Bewertungsassistenz-Architektur: [docs/handbook/ASSESSMENT_ASSISTANT_ARCHITECTURE.md](docs/handbook/ASSESSMENT_ASSISTANT_ARCHITECTURE.md)
- Security-und-Safety-Konzept (Owner-only Korrekturhilfe): [docs/SECURITY_SAFETY_KORREKTURHILFE_KONZEPT.md](docs/SECURITY_SAFETY_KORREKTURHILFE_KONZEPT.md)

### Kurz-Troubleshooting

- Kein `Go Live` sichtbar → Extensions prüfen und VS Code-Fenster neu laden
- Browser öffnet nicht → manuell `http://localhost:5500` aufrufen
- Änderungen fehlen → Hard Refresh + gespeicherte Datei + Browser-Konsole prüfen

---

## 📝 Musterklausur

**📋 [Klassenarbeit (DOCX): SchoolCodeInnovations 2025](material/ka_grundlagen/KA02_BKWI1_WEB_VERSION1_LSG_2025_2026.docx)**

Inhaltlich gleichwertige Klassenarbeit zum Thema Webentwicklung Fundamentals basierend auf dem Konzept der Schülerfirma "SchoolCodeInnovations". Umfang: 60 Minuten, 76 Punkte + 5 Bonuspunkte.

**🎯 [Musterlösung als vollständiges Website-Projekt](version3/loesung_schoolcodeinnovations/)**

Vollständig funktionierendes Projekt mit HTML, CSS, JavaScript und SVG-Grafiken - zum Vergleich nach der Klassenarbeit.

---

## Inhalt / Lernpfade

| Bereich                           | Datei / Link                                                                                                 | Kurzbeschreibung                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Docs-Startseite                   | [`docs/README.md`](docs/README.md)                                                                           | Navigation über statisch, dynamisch, konzeption, programmierung und handbook |
| Doku-Struktur                     | [`docs/STRUKTUR.md`](docs/STRUKTUR.md)                                                                       | Ablageregeln, Link-Regeln und Wartungsroutine für langfristige Pflege        |
| Backup-Strategie                  | [`docs/handbook/BACKUP_STRATEGY.md`](docs/handbook/BACKUP_STRATEGY.md)                                       | Best-Practice für lokale und automatisierte Repository-Snapshots             |
| Einstieg & Überblick              | [`docs/statisch/intro.md`](docs/statisch/intro.md)                                                           | Was ist das Web? Rollen von Client/Server                                    |
| HTML Grundgerüst                  | [`docs/statisch/html-grundgeruest.md`](docs/statisch/html-grundgeruest.md)                                   | Aufbau von `<!DOCTYPE html>`, Grundtags, Validierung                         |
| Sonderzeichen & Umlaute in HTML   | [`docs/statisch/sonderzeichen-und-umlaute-in-html.md`](docs/statisch/sonderzeichen-und-umlaute-in-html.md)   | UTF-8, Copy/Paste-Fallen und korrektes Escaping in der Praxis                |
| Seitenstrukturelemente            | [`docs/statisch/seitenstrukturelemente.md`](docs/statisch/seitenstrukturelemente.md)                         | Semantische Tags (`header`,`nav`,`main`,`section`,...)                       |
| CSS einbinden                     | [`docs/statisch/css-einbinden.md`](docs/statisch/css-einbinden.md)                                           | Externe, interne & inline CSS, Best Practices                                |
| CSS Basis                         | [`docs/statisch/css-basis.md`](docs/statisch/css-basis.md)                                                   | Selektoren, Eigenschaften, erste Styles                                      |
| CSS Formatierung                  | [`docs/statisch/css-formatierung.md`](docs/statisch/css-formatierung.md)                                     | Text, Farben, Abstände, Schatten, Transitions                                |
| Box-Modell                        | [`docs/statisch/box-modell.md`](docs/statisch/box-modell.md)                                                 | `margin`, `border`, `padding`, `content`                                     |
| Flexible Layouts                  | [`docs/statisch/flexible-layouts.md`](docs/statisch/flexible-layouts.md)                                     | Flexbox & CSS Grid mit praktischen Beispielen                                |
| Responsive Design                 | [`docs/statisch/responsive-design.md`](docs/statisch/responsive-design.md)                                   | Media Queries, Mobile Navigation, Breakpoints                                |
| Bilder & Grafiken                 | [`docs/statisch/bilder-grafiken.md`](docs/statisch/bilder-grafiken.md)                                       | Formate, Einbindung, Responsivität                                           |
| Galerien                          | [`docs/statisch/galerien.md`](docs/statisch/galerien.md)                                                     | Einfache Bildgalerie, Grid/Flex                                              |
| Formulare & Auswertung            | [`docs/statisch/formulare.md`](docs/statisch/formulare.md)                                                   | Formulare erstellen & validieren                                             |
| JavaScript Grundlagen             | [`docs/dynamisch/js.md`](docs/dynamisch/js.md)                                                               | Variablen, Funktionen, DOM, Events                                           |
| Git & Versionsmanagement          | [`docs/konzeption/git-versionsmanagement.md`](docs/konzeption/git-versionsmanagement.md)                     | Commits, Branches, Pull Requests, Workflows                                  |
| Zielgruppenanalyse                | [`docs/konzeption/zielgruppenanalyse.md`](docs/konzeption/zielgruppenanalyse.md)                             | User Personas, Customer Journey, Nutzerbedürfnisse                           |
| Corporate Design                  | [`docs/konzeption/corporate-design.md`](docs/konzeption/corporate-design.md)                                 | Logo, Farben, Typografie, Brand Guidelines                                   |
| Konzeption & Webdesign            | [`docs/konzeption/konzeption-webdesign.md`](docs/konzeption/konzeption-webdesign.md)                         | Briefing, Sitemap, Wireframes, Mockups                                       |
| React Einstieg                    | [`docs/dynamisch/react.md`](docs/dynamisch/react.md)                                                         | Komponenten, Props, State                                                    |
| Python (Flask)                    | [`docs/dynamisch/python.md`](docs/dynamisch/python.md)                                                       | Minimales API Backend                                                        |
| PHP Grundlagen                    | [`docs/dynamisch/php.md`](docs/dynamisch/php.md)                                                             | Serverseitige Skripte, Ausgabe, Verarbeitung                                 |
| Programmier-Grundlagen (neu)      | [`docs/programmierung/grundlagen/README.md`](docs/programmierung/grundlagen/README.md)                       | Sprachübergreifende Architektur für Fundamentals                             |
| PHP Fundamentals (modular)        | [`docs/programmierung/grundlagen/php/README.md`](docs/programmierung/grundlagen/php/README.md)               | Ausgaben, Variablen, Kontrollstrukturen, Dateien                             |
| Python Fundamentals (modular)     | [`docs/programmierung/grundlagen/python/README.md`](docs/programmierung/grundlagen/python/README.md)         | Grundlagenpfad in Python-Struktur                                            |
| JavaScript Fundamentals (modular) | [`docs/programmierung/grundlagen/javascript/README.md`](docs/programmierung/grundlagen/javascript/README.md) | Grundlagenpfad in JavaScript-Struktur                                        |
| **PHP lokal testen**              | [`docs/dynamisch/php-lokal-testen.md`](docs/dynamisch/php-lokal-testen.md)                                   | **PHP-Dateien von der Console aus testen**                                   |
| Datenbank (MySQL)                 | [`docs/dynamisch/datenbank.md`](docs/dynamisch/datenbank.md)                                                 | Tabellen, Abfragen, Verbindung                                               |
| Algorithmen & Datenstrukturen     | [`docs/dynamisch/algorithmen-datenstrukturen.md`](docs/dynamisch/algorithmen-datenstrukturen.md)             | Listen, Arrays, Sortieren, Suchen                                            |
| Testen                            | [`docs/dynamisch/testen.md`](docs/dynamisch/testen.md)                                                       | Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit)                        |

## 📚 Aufgaben & Lernversionen

Jede Version baut auf der vorherigen auf und führt neue Konzepte ein. Arbeite sie nacheinander durch!

### 🎓 Version 1: HTML-Grundgerüst & CSS-Einbindung ✅

**Status:** Release v1.0 verfügbar 🎉

**Lernziele:**

- HTML5-Struktur verstehen und erstellen
- Semantische Elemente korrekt einsetzen
- Externe CSS-Datei einbinden
- Erste CSS-Formatierungen anwenden

**Dateien:**

- 📖 **Aufgabenstellung:** [`version1/README.md`](version1/README.md)
- 💡 **Arbeitsordner:** `version1/aufgabe/` (hier arbeitest du!)
- ✅ **Musterlösung:** `version1/loesung/` (zur Selbstkontrolle)

**Themen:**

- ✅ HTML-Grundgerüst (`<!DOCTYPE html>`, `<head>`, `<body>`)
- ✅ Semantische Strukturelemente (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- ✅ CSS extern einbinden
- ✅ Grundlegende CSS-Formatierungen (Farben, Schriften, Abstände)

**Zeitaufwand:** 2-3 Stunden  
**Git-Tag:** `v1.0-release`

---

### 🎓 Version 2: Box-Modell & Responsive Layout ✅

**Status:** Musterlösung verfügbar - Bereit zum Lernen! 🎉

**Lernziele:**

- CSS Box-Modell verstehen (`margin`, `border`, `padding`, `content`)
- Responsive Layouts mit Media Queries erstellen
- Mobile Navigation (Hamburger-Menü) implementieren
- Flexbox und Grid für moderne Layouts nutzen

**Dateien:**

- 📖 **Aufgabenstellung:** [`version2/README.md`](version2/README.md)
- 💡 **Arbeitsordner:** `version2/aufgabe/` (Starter-Template mit TODOs)
- ✅ **Musterlösung:** `version2/loesung/` (zur Selbstkontrolle)
- 🎯 **Lernhilfen:** Detaillierte Schritt-für-Schritt Anleitung

**Themen:**

- 📦 Box-Modell Experimente (`box-sizing`, `content-box`, `border-box`)
- 📱 Media Queries für Desktop, Tablet, Mobile
- ☰ Hamburger-Menü mit JavaScript
- 🎨 Responsive Grid-Layouts
- 🖼️ Logo als Background-Image

**Zeitaufwand:** 4-7 Stunden  
**Voraussetzung:** Version 1 abgeschlossen

---

### 🎓 Version 3: MiFa – Mission Future Academy Website ⚡

**Status:** Musterlösung verfügbar - Bereit zum Lernen! 🎉

**Schwerpunkte:**

- 60% Konzeption (Zielgruppenanalyse, Corporate Design, Sitemap/Wireframes)
- 40% Umsetzung (HTML/CSS/JS, Responsive Design, Formulare)
- Schülerbeteiligung: Online‑Befragungen zur Namensfindung mit Python‑Auswertung

**Dateien:**

- 📖 **Aufgabenstellung:** [`version3/README.md`](version3/README.md)
- 💡 **Arbeitsordner:** `version3/aufgabe/` (Starter-Templates mit Konzept-Vorlagen)
- ✅ **Musterlösung:** `version3/loesung/` (zur Selbstkontrolle für Lehrende)
- 🗳️ **Survey-Formulare:** `version3/aufgabe/surveys/` (Partizipative Namensfindung)

**Besondere Features:**

- 📊 **Partizipation:** Online-Befragungen mit Python-Auswertung
- 🎨 **Konzeptphase:** Personas, Corporate Design, Wireframes
- 🏗️ **Implementierung:** Vollständige Website mit Design-System
- 📱 **Responsive:** Mobile-First Design mit CSS Custom Properties

**Schnelleinstieg:**

- 🗳️ Survey (Schülerfirma‑Name): [`version3/aufgabe/surveys/name_survey/form.html`](version3/aufgabe/surveys/name_survey/form.html)
- 🗳️ Survey (App‑Namen): [`version3/aufgabe/surveys/app_names/form.html`](version3/aufgabe/surveys/app_names/form.html)
- 🧰 Auswertung (Python):
  - `python3 version3/aufgabe/surveys/name_survey/process.py`
  - `python3 version3/aufgabe/surveys/app_names/process.py`

**Themen:**

- 🎯 Zielgruppenanalyse & User Personas
- 🎨 Corporate Design (Logo, Farben, Typografie)
- 📐 Wireframes & Sitemaps
- 🌐 Vollständige Website-Implementierung
- 📱 Responsive Design & Accessibility
- 📝 Formulare mit Validierung
- 💡 JavaScript-Interaktionen

**Zeitaufwand:** 12-15 Stunden (aufgeteilt in Phase 1 + Phase 2)  
**Voraussetzung:** Version 1 & 2 abgeschlossen

### 🔧 Projektstruktur-Empfehlung für App‑Projekte

Für die drei Web‑Apps (Mitfahr‑App, MindLink, CO2‑Tracker) empfehlen wir eigene Repositories (Polyrepo) pro App:

- Bessere Trennung von Code, Issues, Releases und CI
- Unterschiedliche Tech‑Stacks/Deployment‑Ziele unabhängig verwalten
- Klarere Ownership für Schüler‑Teams

Alternative: Monorepo mit Sub‑Packages (z.B. via `pnpm`/Workspaces). Geeignet, wenn alle Apps denselben Tech‑Stack teilen und gemeinsame Libraries nutzen.

Praxisvorschlag:

- Dieses Classroom‑Repo bleibt als Kurs‑Template und Landing‑Page
- Für jede App ein eigenes Repo anlegen (z.B. `mifa-rideshare`, `mifa-mindlink`, `mifa-co2-tracker`)
- In `version3/aufgabe/index.html` werden die Live‑Deployments oder Repos verlinkt.

---

### 🎓 Version 4: BMI-Rechner mit MVC-Architektur (PHP) 🚀

**Status:** Release verfügbar - Zum Lernen bereit! 🎉

**Schwerpunkte:**

- **Pädagogischer Ansatz:** Schrittweise von Erkundung zu Funktionalität
- **MVC-Architektur:** Model-View-Controller mit echten PHP-Klassen
- **Praktische Fachkonzepte:** Datenstrukturen, Geschäftslogik, Präsentation trennen
- **Realistische Projektstruktur:** Das nutzen echte Entwickler!

**Lernziele:**

- ✅ MVC-Architektur verstehen und anwenden
- ✅ PHP-Klassen mit Methoden schreiben
- ✅ HTML-Formulare mit PHP verarbeiten
- ✅ Geschäftslogik vom Interface trennen
- ✅ Controller für Ablaufsteuerung nutzen

**Dateien:**

- 📖 **Aufgabenstellung:** [`version4/README.md`](version4/README.md)
- 📘 **Aufgabe 0:** [`version4/AUFGABE_0_ERKUNDUNG.md`](version4/AUFGABE_0_ERKUNDUNG.md) - Die Vorlage erkunden
- 📝 **Aufgabe 1:** [`version4/AUFGABE_1_VIEW.md`](version4/AUFGABE_1_VIEW.md) - Formular (View) erstellen
- 🧮 **Aufgabe 2:** [`version4/AUFGABE_2_MODEL.md`](version4/AUFGABE_2_MODEL.md) - BMI-Berechnung (Model) implementieren
- 🎮 **Aufgabe 3:** [`version4/AUFGABE_3_CONTROLLER.md`](version4/AUFGABE_3_CONTROLLER.md) - Controller verbinden & testen

**Aufgabenstruktur (Scaffolding):**

1. **Aufgabe 0 (Erkundung):** Ohne Code - Verstehen wie die Vorlage funktioniert
2. **Aufgabe 1 (View):** HTML-Formular mit Eingabefeldern
3. **Aufgabe 2 (Model):** BMI-Berechnung & Gewichtskategorien
4. **Aufgabe 3 (Controller):** Formulare verarbeiten & alles verbinden

**Themen:**

- 🔍 Erkundungsauftrag mit Verständnisfragen
- 📋 HTML-Formulare mit `<input>` und `<form>`
- 📐 Mathematische Formeln implementieren
- 🏗️ Klassen und Methoden schreiben
- 🔄 POST-Daten verarbeiten (`$_SERVER`, `$_POST`)
- 🎨 View für Ausgabe (HTML-Rendering)
- 📦 Model für Datenverarbeitung
- 🕹️ Controller für Logik

**Zeitaufwand:** 8-12 Stunden  
**Voraussetzung:** Version 1-3 sollten absolviert sein; Grundlagen PHP-Wissen

**🎓 Warum diese Version?**

> Diese Version lehrt Schüler die professionelle **Aufteilung von Verantwortlichkeiten** (Separation of Concerns):
>
> - **Model** speichert Daten und berechnet Logik
> - **View** kümmert sich nur um HTML-Ausgabe
> - **Controller** verbindet beide und verarbeitet Anfragen
>
> Dies ist der Weg, wie echte Webentwickler arbeiten und vorbereitet auf React, Django, Laravel, etc.!

---

### 🎓 Version 5: Notenrechner mit MVC-Transfer (PHP) ✅

**Status:** Release verfügbar - Transfertraining zu Version 4

**Schwerpunkte:**

- Reflexion der in Version 4 erlernten MVC-Struktur
- Transfer auf neues Fachproblem (Notendurchschnitt)
- Vertiefung von Verzweigungen über `pruefeNachhilfe()`

**Dateien:**

- 📖 **Aufgabenstellung:** [`version5/README.md`](version5/README.md)
- 📘 **Aufgabe 0:** [`version5/AUFGABE_0_ERKUNDUNG.md`](version5/AUFGABE_0_ERKUNDUNG.md)
- 📝 **Aufgabe 1:** [`version5/AUFGABE_1_VIEW.md`](version5/AUFGABE_1_VIEW.md)
- 🧮 **Aufgabe 2:** [`version5/AUFGABE_2_MODEL.md`](version5/AUFGABE_2_MODEL.md)
- 🎮 **Aufgabe 3:** [`version5/AUFGABE_3_CONTROLLER.md`](version5/AUFGABE_3_CONTROLLER.md)
- ✅ **Musterlösung:** [`src/04_PHP/README.md`](src/04_PHP/README.md)

**Grundlagenbezug:**

- [`docs/programmierung/grundlagen/php/README.md`](docs/programmierung/grundlagen/php/README.md)

---

## 📂 Projektstruktur

Die wichtigsten Bereiche im Überblick:

```text
web-project-dynamic/
├── docs/                 # zentrale Dokumentation + Handbook
├── scripts/              # Automationen und Wartungsroutinen
├── .github/workflows/    # CI/CD, Validierung, Qualitätschecks
├── .vscode/              # Workspace-Settings, Tasks, Extension-Empfehlungen
├── src/                  # Beispiele und Teilprojekte
├── shared-examples/      # Referenzbeispiel für Lernende
├── templates/            # Starter-Templates für App-Repositories
└── version1/..version5/  # aufeinander aufbauende Lernversionen
```

- `docs/` – zentrale Dokumentation (Start: [docs/README.md](docs/README.md))
  - `statisch/`, `dynamisch/`, `konzeption/`, `programmierung/`, `handbook/`
- [version1](version1/) bis [version5](version5/) – aufeinander aufbauende Lernversionen
- [shared-examples](shared-examples/) – vollständiges Beispielprojekt
- [scripts](scripts/) – Automationen (README-Update, Validierung, Backups)
- [.github/workflows](.github/workflows/) – CI/CD- und Qualitäts-Workflows

Detaillierte Strukturregeln: [docs/STRUKTUR.md](docs/STRUKTUR.md)

---

## 🎓 Für Lehrkräfte & Betrieb

- Classroom-Einrichtung: [docs/handbook/GITHUB_CLASSROOM_AUTOGRADING.md](docs/handbook/GITHUB_CLASSROOM_AUTOGRADING.md)
- Architektur & Wartung: [docs/handbook/ARCHITECTURE.md](docs/handbook/ARCHITECTURE.md)
- Workspace Live-Test Setup: [docs/handbook/WORKSPACE_LIVE_TEST_SETUP.md](docs/handbook/WORKSPACE_LIVE_TEST_SETUP.md)
- Governance (Admin-only Push): [docs/handbook/REPO_GOVERNANCE.md](docs/handbook/REPO_GOVERNANCE.md)
- Template-Synchronisierung: [docs/handbook/TEMPLATE_SYNC.md](docs/handbook/TEMPLATE_SYNC.md)
- Backup-Best-Practice: [docs/handbook/BACKUP_STRATEGY.md](docs/handbook/BACKUP_STRATEGY.md)

## 🧪 Testen & Vorschau

- Schnellster Weg für Lernende: [docs/handbook/QUICKSTART_LIVE_SERVER.md](docs/handbook/QUICKSTART_LIVE_SERVER.md)
- Direktes Übungsziel: [shared-examples/index.html](shared-examples/index.html)
- Qualitäts-Checks (automatisch): `.github/workflows/validate-html.yml` und weitere Workflows unter `.github/workflows/`

## 🎯 Lernpfad-Empfehlung

### Phase 1: Frontend Basics (Version 1-2)

1. ✅ **HTML-Grundgerüst** nachvollziehen → [`docs/statisch/html-grundgeruest.md`](docs/statisch/html-grundgeruest.md)
2. ✅ **CSS Box-Modell** verstehen → [`docs/statisch/box-modell.md`](docs/statisch/box-modell.md) + Browser DevTools
3. ✅ **Responsive Design** umsetzen → [`docs/statisch/responsive-design.md`](docs/statisch/responsive-design.md)
4. 💪 **Version 1 abschließen** → Eigenständige HTML+CSS Seite
5. 💪 **Version 2 starten** → Box-Modell & Responsive Layout

### Phase 2: Interaktivität (Version 3-4)

6. 📷 **Bilder & Galerien** → [`docs/statisch/bilder-grafiken.md`](docs/statisch/bilder-grafiken.md), [`docs/statisch/galerien.md`](docs/statisch/galerien.md)
7. 📝 **Formulare** erstellen → [`docs/statisch/formulare.md`](docs/statisch/formulare.md)
8. ⚡ **JavaScript Basics** → [`docs/dynamisch/js.md`](docs/dynamisch/js.md)
9. 🎨 **Fortgeschrittene Layouts** → CSS Grid, Flexbox-Mastery

### Phase 3: Backend & Fullstack (geplant)

10. 🔧 **React Komponenten** → [`docs/dynamisch/react.md`](docs/dynamisch/react.md)
11. 🐍 **Python/Flask Backend** → [`docs/dynamisch/python.md`](docs/dynamisch/python.md)
12. 🗄️ **Datenbank** anbinden → [`docs/dynamisch/datenbank.md`](docs/dynamisch/datenbank.md)
13. ✅ **Testing** → [`docs/dynamisch/testen.md`](docs/dynamisch/testen.md)

## 🤖 Automatisierung

- HTML-Validierung: `.github/workflows/validate-html.yml`
- Doku-Tabelle: `.github/workflows/update-docs-table.yml`
- Was-ist-neu-Datum: `.github/workflows/update-whats-new-date.yml`
- Backup-Snapshot: `.github/workflows/backup-snapshot.yml`

## 🧪 Testing (Roadmap)

Die Einführung in Teststrategien liegt in [`docs/dynamisch/testen.md`](docs/dynamisch/testen.md); weiterführende Stack-spezifische Beispiele werden schrittweise ergänzt.

## 🔄 Template-Updates für Student-Repos

Dieses Repository ist ein **GitHub Classroom Template**. Wenn du als Schüler:in damit arbeitest und später **neue Versionen** (z.B. Version 5) oder **Dokumentations-Updates** übernehmen möchtest:

📖 **Vollständige Anleitung:** [docs/handbook/TEMPLATE_SYNC.md](docs/handbook/TEMPLATE_SYNC.md)

**Quick-Start:**

```bash
# 1. Template als Remote hinzufügen (einmalig)
git remote add template https://github.com/ChristineJanischek/web-project-dynamic.git
git fetch template

# 2. Neue Inhalte übernehmen (z.B. Version 5)
git checkout template/main -- version5/ src/04_PHP/
git commit -m "✨ Version 5 vom Template hinzugefügt"
git push
```

⚠️ **Wichtig:** Überschreibe niemals deine eigenen Lösungen in `version*/aufgabe/`!

---

## 🤝 Mitmachen & Beiträge

Verbesserungen und Erweiterungen sind willkommen!

- Für Lehrkräfte & Mentor:innen: Pull Requests für Aufgaben, Docs und Qualitätsverbesserungen
- Für Studierende: Issues bei Fragen/Unklarheiten, gern mit reproduzierbarem Beispiel
- PR-Standard mit Governance-Checklist: [.github/pull_request_template.md](.github/pull_request_template.md)

## 📜 Lizenz & Nutzung

- **Verwendungszweck:** Unterricht & Bildung
- **GitHub Classroom:** Frei verwendbar
- **Kommerzielle Nutzung:** Bitte Kontakt aufnehmen
- **Credits:** Erwähnung erwünscht

## 📞 Support

- Fragen, Bugs und Verbesserungen bitte über Issues bzw. Pull Requests im Repository einreichen.

---

## 🏷️ Versions-Tags

- `v1.0-release` - Version 1 komplett (HTML + CSS Basics)
- `docs-complete` - Vollständige Frontend-Dokumentationen
- Weitere Tags folgen mit neuen Releases

---

**Dieses Projekt wächst kontinuierlich!** ⭐ Star uns auf GitHub wenn es dir hilft!

**Erstellt mit ❤️ für Web-Entwicklungs-Einsteiger**
