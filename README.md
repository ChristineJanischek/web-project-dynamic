# Web Project Dynamic

Ein modernes Ausbildungs-Template für **GitHub Classroom**: Vom ersten HTML-Grundgerüst bis zur vollständigen Webanwendung mit React, PHP, Python (Flask), JavaScript, CSS und MySQL-Datenbankanbindung.

**🎯 Ziel:** Schüler ohne Vorkenntnisse schrittweise zur professionellen Webentwicklung befähigen - mit umfangreicher Dokumentation, praktischen Beispielen und automatischer Code-Validierung.

**✨ Features:**

- 📚 Umfassende Dokumentation zu allen Web-Technologien
- 🔄 Versioniertes Lernsystem (v1.0, v2.0, ...)
- 🤖 Automatische HTML-Validierung via GitHub Actions
- 📱 Responsive Design von Anfang an
- 💡 Praktische Beispiele mit TODO-Kommentaren
- 🎓 Best Practices für GitHub Classroom
- 🚀 Live Server vorinstalliert für sofortiges Testen

## 🆕 Was ist neu? (Stand: 23.02.2026)

- ✅ Neue modulare Grundlagenpfade für [PHP](docs/programmierung/grundlagen/php/README.md), [Python](docs/programmierung/grundlagen/python/README.md) und [JavaScript](docs/programmierung/grundlagen/javascript/README.md)
- ✅ Python-Kapitel zu Algorithmen und Dateiverarbeitung ergänzt
- ✅ Unterrichtsmaterial von `ka_grundlagen/` nach [material/ka_grundlagen](material/ka_grundlagen) migriert
- ✅ Verweise in der zentralen Dokumentation auf die neue Struktur aktualisiert

---

## 🚀 Erste Schritte - Setup für Schüler

### 1️⃣ VS Code öffnen

Öffne dieses Projekt in Visual Studio Code:

- **In GitHub Codespaces:** Bereits geöffnet! ✅ Alle Extensions werden **automatisch installiert**! 🎉
- **Lokal:** `File` → `Open Folder` → Wähle den Projektordner

### 2️⃣ Extensions installieren

**📦 In GitHub Codespaces (empfohlen):**

- ✅ **Automatisch installiert!** Dank `.devcontainer/devcontainer.json` sind alle benötigten Extensions bereits da!
- ⚡ Kein manueller Setup erforderlich
- 📖 Details siehe [.devcontainer/README.md](.devcontainer/README.md)

**💻 Lokale Installation:**

Beim ersten Öffnen erscheint unten rechts eine Benachrichtigung:

```
📦 Dieses Repository empfiehlt Extensions
[Details anzeigen] [Alle installieren] [Ignorieren]
```

**Klicke auf "Alle installieren"** - dann werden automatisch installiert:

- ✅ **Live Server** - Zum sofortigen Testen deiner Website
- ✅ **Prettier** - Automatische Code-Formatierung
- ✅ **HTML CSS Support** - Bessere IntelliSense
- ✅ **Auto Rename Tag** - HTML-Tags automatisch umbenennen
- ✅ **ESLint** - JavaScript-Fehler erkennen
- ✅ **Python** & **Pylance** - Für spätere Backend-Entwicklung

**Für PHP-Entwicklung:**

- ✅ **PHP Intelephense** (`bmewburn.vscode-intelephense-client`) - Code-Intelligence für PHP mit Autovervollständigung, Go-to-Definition und Fehlerprüfung
- ✅ **PHP Debug** (`xdebug.php-debug`) - Debuggen mit Xdebug
- ✅ **PHP DocBlocker** (`neilbrayfield.php-docblocker`) - Automatische PHPDoc-Kommentare
- ✅ **PHP Namespace Resolver** (`MehediDracula.php-namespace-resolver`) - Import von Klassen
- ✅ **PHP CS Fixer** (`junstyle.php-cs-fixer`) - Code-Formatierung nach Standards

**Falls die Benachrichtigung nicht erscheint:**

1. Drücke `Ctrl+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (Mac)
2. Tippe: `Extensions: Show Recommended Extensions`
3. Klicke auf "Install Workspace Recommended Extensions" ⬇️

### 3️⃣ Live Server nutzen

So testest du deine Website in Echtzeit:

**Methode 1 - Rechtsklick (empfohlen):**

1. Öffne eine HTML-Datei (z.B. `version1/aufgabe/index.html`)
2. **Rechtsklick** in den Editor → `Open with Live Server`
3. Deine Website öffnet sich automatisch im Browser! 🎉

**Methode 2 - Status Bar:**

1. Öffne eine HTML-Datei
2. Klicke unten rechts auf **"Go Live"**
3. Website wird gestartet!

**Methode 3 - Keyboard Shortcut:**

- Windows/Linux: `Alt+L Alt+O`
- Mac: `Cmd+L Cmd+O`

**🔄 Änderungen sehen:**

- Speichere deine HTML/CSS/JS-Datei (`Ctrl+S` / `Cmd+S`)
- Der Browser aktualisiert sich **automatisch**! ✨

**❌ Server stoppen:**

- Klicke auf **"Port: 5500"** in der Status Bar unten rechts
- Oder drücke: `Alt+L Alt+C` (Windows/Linux) / `Cmd+L Cmd+C` (Mac)

### 4️⃣ Auto-Save aktivieren (optional aber empfohlen)

Damit du nicht ständig speichern musst:

1. `File` → `Preferences` → `Settings` (oder `Ctrl+,`)
2. Suche nach: `Auto Save`
3. Wähle: `afterDelay`
4. Deine Dateien werden jetzt automatisch gespeichert! 💾

**Oder:** Bereits vorkonfiguriert in `.vscode/settings.json`! ✅

---

## 🆘 Troubleshooting

### ❌ "Go Live" Button erscheint nicht

**Lösung:**

1. Stelle sicher, dass Live Server installiert ist
2. Öffne eine `.html`-Datei (nicht `.md` oder andere Dateien)
3. Reload VS Code: `Ctrl+Shift+P` → `Reload Window`

### ❌ Browser öffnet sich nicht automatisch

**Lösung:**

- Öffne manuell: `http://localhost:5500`
- Oder ändere Browser in Settings: Live Server → Custom Browser

### ❌ Port 5500 bereits belegt

**Lösung:**

1. Stoppe andere Live Server Instanzen
2. Oder ändere den Port in `.vscode/settings.json`: `"liveServer.settings.port": 5501`

### ❌ Änderungen werden nicht angezeigt

**Lösung:**

1. **Hard Refresh:** `Ctrl+Shift+R` (Windows) / `Cmd+Shift+R` (Mac)
2. Stelle sicher, dass die Datei gespeichert wurde
3. Prüfe die Browser-Konsole auf Fehler: `F12` → Console

---

## 📝 Musterklausur

**📋 [Klassenarbeit (DOCX): SchoolCodeInnovations 2025](material/ka_grundlagen/KA02_BKWI1_WEB_VERSION1_LSG_2025_2026.docx)**

Inhaltlich gleichwertige Klassenarbeit zum Thema Webentwicklung Fundamentals basierend auf dem Konzept der Schülerfirma "SchoolCodeInnovations". Umfang: 60 Minuten, 76 Punkte + 5 Bonuspunkte.

**🎯 [Musterlösung als vollständiges Website-Projekt](version3/loesung_schoolcodeinnovations/)**

Vollständig funktionierendes Projekt mit HTML, CSS, JavaScript und SVG-Grafiken - zum Vergleich nach der Klassenarbeit.

---

## Inhalt / Lernpfade

| Bereich                           | Datei / Link                                                                                                 | Kurzbeschreibung                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Einstieg & Überblick              | [`docs/intro.md`](docs/intro.md)                                                                             | Was ist das Web? Rollen von Client/Server              |
| HTML Grundgerüst                  | [`docs/html-grundgeruest.md`](docs/html-grundgeruest.md)                                                     | Aufbau von `<!DOCTYPE html>`, Grundtags, Validierung   |
| Seitenstrukturelemente            | [`docs/seitenstrukturelemente.md`](docs/seitenstrukturelemente.md)                                           | Semantische Tags (`header`,`nav`,`main`,`section`,...) |
| CSS einbinden                     | [`docs/css-einbinden.md`](docs/css-einbinden.md)                                                             | Externe, interne & inline CSS, Best Practices          |
| CSS Basis                         | [`docs/css-basis.md`](docs/css-basis.md)                                                                     | Selektoren, Eigenschaften, erste Styles                |
| CSS Formatierung                  | [`docs/css-formatierung.md`](docs/css-formatierung.md)                                                       | Text, Farben, Abstände, Schatten, Transitions          |
| Box-Modell                        | [`docs/box-modell.md`](docs/box-modell.md)                                                                   | `margin`, `border`, `padding`, `content`               |
| Flexible Layouts                  | [`docs/flexible-layouts.md`](docs/flexible-layouts.md)                                                       | Flexbox & CSS Grid mit praktischen Beispielen          |
| Responsive Design                 | [`docs/responsive-design.md`](docs/responsive-design.md)                                                     | Media Queries, Mobile Navigation, Breakpoints          |
| Bilder & Grafiken                 | [`docs/bilder-grafiken.md`](docs/bilder-grafiken.md)                                                         | Formate, Einbindung, Responsivität                     |
| Galerien                          | [`docs/galerien.md`](docs/galerien.md)                                                                       | Einfache Bildgalerie, Grid/Flex                        |
| Formulare & Auswertung            | [`docs/formulare.md`](docs/formulare.md)                                                                     | Formulare erstellen & validieren                       |
| JavaScript Grundlagen             | [`docs/js.md`](docs/js.md)                                                                                   | Variablen, Funktionen, DOM, Events                     |
| Git & Versionsmanagement          | [`docs/git-versionsmanagement.md`](docs/git-versionsmanagement.md)                                           | Commits, Branches, Pull Requests, Workflows            |
| Zielgruppenanalyse                | [`docs/zielgruppenanalyse.md`](docs/zielgruppenanalyse.md)                                                   | User Personas, Customer Journey, Nutzerbedürfnisse     |
| Corporate Design                  | [`docs/corporate-design.md`](docs/corporate-design.md)                                                       | Logo, Farben, Typografie, Brand Guidelines             |
| Konzeption & Webdesign            | [`docs/konzeption-webdesign.md`](docs/konzeption-webdesign.md)                                               | Briefing, Sitemap, Wireframes, Mockups                 |
| React Einstieg                    | [`docs/react.md`](docs/react.md)                                                                             | Komponenten, Props, State                              |
| Python (Flask)                    | [`docs/python.md`](docs/python.md)                                                                           | Minimales API Backend                                  |
| PHP Grundlagen                    | [`docs/php.md`](docs/php.md)                                                                                 | Serverseitige Skripte, Ausgabe, Verarbeitung           |
| Programmier-Grundlagen (neu)      | [`docs/programmierung/grundlagen/README.md`](docs/programmierung/grundlagen/README.md)                       | Sprachübergreifende Architektur für Fundamentals       |
| PHP Fundamentals (modular)        | [`docs/programmierung/grundlagen/php/README.md`](docs/programmierung/grundlagen/php/README.md)               | Ausgaben, Variablen, Kontrollstrukturen, Dateien       |
| Python Fundamentals (modular)     | [`docs/programmierung/grundlagen/python/README.md`](docs/programmierung/grundlagen/python/README.md)         | Grundlagenpfad in Python-Struktur                      |
| JavaScript Fundamentals (modular) | [`docs/programmierung/grundlagen/javascript/README.md`](docs/programmierung/grundlagen/javascript/README.md) | Grundlagenpfad in JavaScript-Struktur                  |
| **PHP lokal testen**              | [`docs/php-lokal-testen.md`](docs/php-lokal-testen.md)                                                       | **PHP-Dateien von der Console aus testen**             |
| Datenbank (MySQL)                 | [`docs/datenbank.md`](docs/datenbank.md)                                                                     | Tabellen, Abfragen, Verbindung                         |
| Algorithmen & Datenstrukturen     | [`docs/algorithmen-datenstrukturen.md`](docs/algorithmen-datenstrukturen.md)                                 | Listen, Arrays, Sortieren, Suchen                      |
| Testen                            | [`docs/testen.md`](docs/testen.md)                                                                           | Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit)  |

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

### 🎓 Version 5: JavaScript & Interaktivität ⚡

**Status:** In Planung

**Geplante Themen:**

- DOM-Manipulation
- Event-Handling
- AJAX/Fetch API
- Lokaler Storage
- Einfache Animationen

---

## 📂 Projektstruktur

> **💡 Automatisches Setup:** Dieses Projekt nutzt DevContainers für automatische Tool-Installation in Codespaces!  
> Details siehe [.devcontainer/CODESPACES_SETUP.md](.devcontainer/CODESPACES_SETUP.md)

```
web-project-dynamic/
├── .github/
│   └── workflows/
│       └── validate-html.yml      # 🤖 Automatische HTML-Validierung
├── docs/                          # 📚 Umfassende Dokumentation
│   ├── intro.md                   # ✅ Einstieg ins Web
│   ├── html-grundgeruest.md       # ✅ HTML5 Basics
│   ├── seitenstrukturelemente.md  # ✅ Semantisches HTML
│   ├── css-einbinden.md           # ✅ CSS Integration
│   ├── css-basis.md               # ✅ CSS Grundlagen
│   ├── css-formatierung.md        # ✅ Text & Farben
│   ├── box-modell.md              # ✅ Margin, Padding, Border
│   ├── responsive-design.md       # ✅ Media Queries, Mobile-First
│   ├── bilder-grafiken.md         # ✅ Bilder responsive
│   ├── galerien.md                # ✅ Grid-Galerien, Lightbox
│   ├── formulare.md               # ✅ Forms & Validation
│   ├── js.md                      # 🚧 JavaScript (geplant)
│   ├── react.md                   # 🚧 React (geplant)
│   ├── python.md                  # 🚧 Flask Backend (geplant)
│   ├── php.md                     # 🚧 PHP (geplant)
│   ├── php-lokal-testen.md        # ✅ PHP von Console aus testen
│   ├── datenbank.md               # 🚧 MySQL (geplant)
│   └── testen.md                  # 🚧 Testing (geplant)
├── shared-examples/               # 💡 Vollständiges Demo-Projekt
│   ├── index.html                 # Responsive Beispiel-Seite
│   ├── css/
│   │   └── style.css              # Modernes CSS mit Media Queries
│   ├── js/
│   │   └── script.js              # Interaktive Navigation
│   └── images/
│       └── schildkroete_echse.jpg
├── version1/                      # 🎓 Version 1: HTML & CSS Basics
│   ├── README.md                  # Aufgabenstellung (v1.0-release)
│   ├── aufgabe/                   # Arbeitsbereich für Studierende
│   │   ├── index.html
│   │   └── css/style.css
│   └── loesung/                   # Musterlösung
│       ├── index.html
│       ├── README.md
│       └── css/style.css
├── version2/                      # 🎓 Version 2: Box-Modell & Responsive
│   ├── README.md                  # Aufgabenstellung
│   ├── aufgabe/                   # Starter-Template mit TODOs
│   │   ├── index.html             # HTML-Gerüst mit Kommentaren
│   │   ├── css/style.css          # CSS-Template mit Lernhilfen
│   │   └── js/script.js           # JavaScript-Vorlage
│   └── loesung/                   # Musterlösung
│       ├── index.html
│       ├── css/style.css
│       ├── js/script.js
│       └── images/logo_final.png
├── version3/                      # 🎓 Version 3: MiFa - Mission Future Academy
│   ├── README.md                  # Aufgabenstellung & Überblick
│   ├── PFADE.md                   # Pfadstruktur-Dokumentation
│   ├── aufgabe/                   # Arbeitsbereich für Schüler
│   │   ├── README.md              # Detaillierte Anleitung
│   │   ├── phase1-concept/        # Phase 1: Konzeption
│   │   │   ├── AUFGABEN.md        # Schritt-für-Schritt Phase 1
│   │   │   ├── results/           # Ergebnisse (names.json)
│   │   │   └── templates/         # Vorlagen (Personas, Design, Wireframes)
│   │   ├── phase2-implementation/ # Phase 2: Implementierung
│   │   │   ├── index-starter.html # HTML-Starter
│   │   │   ├── css/style-starter.css
│   │   │   └── js/script-starter.js
│   │   ├── concept/               # Mockups & Assets
│   │   │   └── Mockups_MiFa.odp   # LibreOffice Präsentation
│   │   ├── images/                # Grafiken (Logo, Startbild, Icon)
│   │   │   ├── Logo_farbig.jpg
│   │   │   ├── startbild.png
│   │   │   └── ic_launcher.png
│   │   ├── surveys/               # Partizipative Namensfindung
│   │   │   ├── name_survey/       # Schülerfirma-Name
│   │   │   │   ├── form.html
│   │   │   │   └── process.py
│   │   │   └── app_names/         # App-Namen
│   │   │       ├── form.html
│   │   │       └── process.py
│   │   ├── projects/              # App-Detailseiten
│   │   │   ├── rideshare.html     # Mitfahr-App
│   │   │   ├── mindlink.html      # MindLink
│   │   │   └── co2.html           # CO2-Tracker
│   │   └── reference/             # Referenz-Implementierung
│   │       └── complete-example/
│   └── loesung/                   # Musterlösung (Lehrende)
│       ├── README.md              # Bewertung & Begründungen
│       ├── loesung_phase1.md      # Phase 1 Konzept-Dokumentation
│       ├── loesung_phase2.md      # Phase 2 Implementierungs-Dokumentation
│       ├── index.html             # Vollständige HTML-Implementierung
│       ├── css/style.css          # Design-System mit Custom Properties
│       ├── js/script.js           # Navigation, Validierung, Scroll-Effekte
│       └── images/                # Alle Grafiken
│           ├── Logo_farbig.jpg
│           ├── startbild.png
│           ├── ic_launcher.png
│           ├── team-emma.svg      # Team-Avatare
│           ├── team-luca.svg
│           ├── team-max.svg
│           └── team-sophie.svg
├── version4/                      # 🎓 Version 4: BMI-Rechner mit MVC (PHP)
│   ├── README.md                  # Aufgabenstellung & Überblick
│   ├── AUFGABE_0_ERKUNDUNG.md     # 📘 Aufgabe 0: Vorlage erkunden (Verständnis)
│   ├── AUFGABE_1_VIEW.md          # 📝 Aufgabe 1: HTML-Formular (View)
│   ├── AUFGABE_2_MODEL.md         # 🧮 Aufgabe 2: BMI-Berechnung (Model)
│   ├── AUFGABE_3_CONTROLLER.md    # 🎮 Aufgabe 3: Controller & Ablauf
│   ├── index.php                  # Einstiegspunkt
│   ├── controllers/
│   │   └── RechnerController.php  # Controller für Ablaufsteuerung
│   ├── models/
│   │   └── RechnerModel.php       # Model für Geschäftslogik & BMI-Berechnung
│   ├── views/
│   │   └── RechnerView.php        # View für HTML-Rendering
│   ├── layouts/
│   │   ├── head.php               # HTML-Header
│   │   ├── header.php             # Website-Header
│   │   ├── nav.php                # Navigation
│   │   ├── main.php               # Hauptinhalt (Formular & Ergebnis)
│   │   └── footer.php             # Footer
│   └── css/
│       └── style.css              # Styling für BMI-Rechner
├── scripts/                       # Utility-Scripts
│   ├── run_accessibility.sh       # pa11y Runner
│   ├── validate_names.py          # JSON Validator
│   └── update_readme_docs.py      # README Generator
├── templates/                     # Polyrepo Templates
│   ├── rideshare-template/        # MiFaRide Template
│   ├── mindlink-template/         # MindLink Template
│   └── co2-tracker-template/      # CO2-Tracker Template
├── .github/                       # GitHub Actions
│   └── workflows/
│       ├── validate-html.yml      # HTML Validierung
│       ├── quality.yml            # Lighthouse + pa11y
│       ├── validate-names.yml     # JSON Schema Check
│       └── template-sync.yml      # Template-Update Notification
├── .gitignore                     # Ignoriert IDE-Dateien, node_modules, etc.
├── .lighthouserc.json             # Lighthouse CI Konfiguration
├── package.json                   # npm Dependencies (pa11y, Lighthouse)
├── docs/handbook/                 # Repo-Handbook (Architektur, Template-Sync, Autograding)
│   ├── ARCHITECTURE.md
│   ├── TEMPLATE_SYNC.md
│   ├── TEMPLATE_UPDATE_STRATEGY.md
│   └── GITHUB_CLASSROOM_AUTOGRADING.md
├── CONTRIBUTING.md                # 📖 Git-Workflow für Studierende
└── README.md                      # Diese Datei
```

**Hinweis:** Backend-Ordner (`backend-python/`, `backend-php/`, `db/`) werden in Version 4+ hinzugefügt.

---

## 🎓 Für Lehrkräfte: Classroom Setup

- **Template-Repository:** Als Template auf GitHub markieren
- **GitHub Classroom:** Repository als Assignment verteilen
- **Auto-Grading:** GitHub Actions läuft automatisch
- **Feedback:** Über Pull Requests und Code Reviews
- **Lösungen:** Optional `*/loesung/` in `.gitignore` für Studenten

## 🧪 Wie teste ich meine Webseite?

### Methode 1: Direkt im Browser öffnen (Einfachste Methode)

1. Öffne den Datei-Explorer deines Computers
2. Navigiere zu: `web-project-dynamic/shared-examples/`
3. **Rechtsklick** auf `index.html`
4. Wähle "Öffnen mit" → Dein Browser (Chrome, Firefox, Edge, Safari)
5. Die Seite wird sofort angezeigt!

**Tipp**: Bei Änderungen am Code einfach die Browser-Seite **neu laden** (F5 oder Strg+R / Cmd+R).

### Methode 2: VS Code Live Server (Empfohlen für Entwicklung)

1. Installiere die Extension "Live Server" in VS Code:
   - Klicke auf das Extensions-Symbol (links in der Seitenleiste)
   - Suche nach "Live Server" (von Ritwick Dey)
   - Klicke auf "Install"
2. Öffne `shared-examples/index.html` in VS Code
3. **Rechtsklick** im Editor → "Open with Live Server"
4. Dein Browser öffnet sich automatisch mit der Seite
5. **Vorteil**: Änderungen werden automatisch im Browser aktualisiert!

### Methode 3: Python HTTP Server (Terminal)

Falls Python installiert ist:

```bash
cd shared-examples
python3 -m http.server 8000
```

Dann im Browser öffnen: `http://localhost:8000`

### Methode 4: VS Code Simple Browser (Integriert)

1. Öffne `shared-examples/index.html` in VS Code
2. Drücke `Strg+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (Mac)
3. Tippe: "Simple Browser: Show"
4. Gib ein: `file:///DEIN_PFAD/web-project-dynamic/shared-examples/index.html`

### 📱 Mobile-Ansicht testen (Responsive Design)

**Im Browser (Chrome/Firefox/Edge)**:

1. Öffne die Webseite
2. Drücke `F12` für Developer Tools
3. Klicke auf das **Smartphone-Symbol** (Toggle Device Toolbar)
4. Wähle verschiedene Geräte aus dem Dropdown (iPhone, iPad, Samsung...)
5. Teste das Hamburger-Menü (☰) und die Anpassung der Layouts

**Tastenkombinationen**:

- Chrome: `Strg+Shift+M` / `Cmd+Shift+M`
- Firefox: `Strg+Shift+M` / `Cmd+Shift+M`

### ✅ Was solltest du testen?

- [ ] Seite lädt ohne Fehler
- [ ] Alle Bilder werden angezeigt
- [ ] CSS wird korrekt angewendet (Farben, Layout)
- [ ] JavaScript funktioniert (Button-Klick zeigt Alert)
- [ ] Navigation funktioniert (Links springen zu Sektionen)
- [ ] **Mobile**: Hamburger-Menü öffnet/schließt Navigation
- [ ] **Mobile**: Cards stapeln sich untereinander
- [ ] **Tablet**: Cards zeigen sich in 2 Spalten
- [ ] **Desktop**: Cards zeigen sich in 3 Spalten

### 🐛 Fehlersuche (Debugging)

Wenn etwas nicht funktioniert:

1. Öffne Developer Tools (`F12`)
2. Schaue in die **Console** (zeigt JavaScript-Fehler)
3. Schaue in den **Network**-Tab (zeigt fehlende Dateien)
4. Prüfe Dateinamen und Pfade (Groß-/Kleinschreibung beachten!)

Häufige Fehler:

- CSS wird nicht geladen → Pfad in `<link href="css/style.css">` prüfen
- JS funktioniert nicht → Pfad in `<script src="js/script.js">` prüfen
- Bilder fehlen → URL oder Pfad prüfen

## 🔍 Testen & Ansehen der Webseite

Es gibt mehrere Möglichkeiten, deine Arbeit im Browser zu testen:

### **Methode 1: Live Preview in VS Code (Empfohlen für Anfänger)**

1. **Live Server Extension installieren:**
   - Klicke links auf das Extensions-Symbol (vier Quadrate) oder drücke `Strg+Shift+X`
   - Suche nach "Live Server" (von Ritwick Dey)
   - Klicke auf "Install"

2. **HTML-Datei öffnen:**
   - Navigiere im Explorer zu `shared-examples/index.html`
   - Rechtsklick auf die Datei → **"Open with Live Server"**

3. **Automatisches Neuladen:**
   - Der Browser öffnet sich automatisch
   - Änderungen in HTML/CSS/JS werden sofort sichtbar (Auto-Reload)
   - Die Seite läuft auf `http://127.0.0.1:5500` oder ähnlich

4. **Responsive testen:**
   - Im Browser: `F12` für DevTools
   - Klicke auf das Handy/Tablet-Symbol (Toggle Device Toolbar)
   - Wähle verschiedene Geräte aus (iPhone, iPad, etc.)

### **Methode 2: Simple Browser in VS Code**

1. **HTML-Datei öffnen** (`shared-examples/index.html`)
2. Drücke `Strg+Shift+P` (Command Palette)
3. Tippe: **"Simple Browser: Show"**
4. Gib die URL ein: `file:///workspaces/web-project-dynamic/shared-examples/index.html`

⚠️ **Nachteil:** Kein automatisches Neuladen bei Änderungen.

### **Methode 3: Direkt im Browser öffnen**

1. **Datei-Explorer öffnen:**
   - Navigiere zu deinem Projektordner
   - Finde `shared-examples/index.html`

2. **Im Browser öffnen:**
   - Rechtsklick → "Öffnen mit" → Wähle deinen Browser (Chrome, Firefox, Edge)
   - Oder ziehe die Datei direkt ins Browser-Fenster

3. **Neuladen nach Änderungen:**
   - Nach jeder Änderung im Code drücke `F5` oder `Strg+R` im Browser

### **Methode 4: Python SimpleHTTPServer (Fortgeschritten)**

Falls Python installiert ist:

```bash
cd shared-examples
python3 -m http.server 8000
```

Dann öffne `http://localhost:8000` im Browser.

---

## 📱 Mobile Ansicht testen

1. **Browser DevTools öffnen:** `F12`
2. **Device Toolbar aktivieren:** `Strg+Shift+M` (Chrome/Edge) oder Icon oben links
3. **Gerät wählen:** iPhone, iPad, oder benutzerdefinierte Größe
4. **Hamburger-Menü testen:** Bei Bildschirmbreite < 768px erscheint das ☰ Symbol
5. **Touch-Simulation:** Klicke auf Links und Buttons, um Navigation zu testen

### Was du testen solltest:

- ✅ Funktioniert das Toggle-Menü auf kleinen Bildschirmen?
- ✅ Sind alle Texte lesbar?
- ✅ Passen Bilder sich an die Breite an?
- ✅ Sind Buttons groß genug zum Tippen (min. 44x44px)?
- ✅ Scrollen alle Bereiche korrekt?

---

## 🐛 Debugging-Tipps

**Problem: CSS wird nicht geladen**

- Prüfe den Pfad in `index.html`: `<link rel="stylesheet" href="css/style.css">`
- Öffne DevTools (F12) → Tab "Network" → Suche nach `style.css` (rot = Fehler)

**Problem: JavaScript funktioniert nicht**

- Öffne DevTools → Tab "Console" → Suche nach Fehlermeldungen (rot)
- Prüfe den Pfad: `<script src="js/script.js"></script>`

**Problem: Seite lädt nicht (Live Server)**

- Stelle sicher, dass Live Server Extension aktiv ist (unten rechts in VS Code)
- Stoppe Server (Rechtsklick auf Port) und starte neu

**Problem: Mobile Ansicht zeigt Desktop-Version**

- Prüfe ob `<meta name="viewport" content="width=device-width, initial-scale=1.0">` im `<head>` steht

---

## 📂 Dateistruktur (shared-examples/)

```
shared-examples/
├── index.html          # Haupt-HTML-Datei
├── css/
│   └── style.css       # Alle Styles + Media Queries
└── js/
    └── script.js       # Mobile Navigation + Interaktionen
```

**Wichtig:** Achte immer auf korrekte Pfade beim Einbinden von Dateien!

## 🎯 Lernpfad-Empfehlung

### Phase 1: Frontend Basics (Version 1-2)

1. ✅ **HTML-Grundgerüst** nachvollziehen → [`docs/html-grundgeruest.md`](docs/html-grundgeruest.md)
2. ✅ **CSS Box-Modell** verstehen → [`docs/box-modell.md`](docs/box-modell.md) + Browser DevTools
3. ✅ **Responsive Design** umsetzen → [`docs/responsive-design.md`](docs/responsive-design.md)
4. 💪 **Version 1 abschließen** → Eigenständige HTML+CSS Seite
5. 💪 **Version 2 starten** → Box-Modell & Responsive Layout

### Phase 2: Interaktivität (Version 3-4)

6. 📷 **Bilder & Galerien** → [`docs/bilder-grafiken.md`](docs/bilder-grafiken.md), [`docs/galerien.md`](docs/galerien.md)
7. 📝 **Formulare** erstellen → [`docs/formulare.md`](docs/formulare.md)
8. ⚡ **JavaScript Basics** → DOM-Manipulation, Events
9. 🎨 **Fortgeschrittene Layouts** → CSS Grid, Flexbox-Mastery

### Phase 3: Backend & Fullstack (geplant)

10. 🔧 **React Komponenten** → Wiederverwendbare UI-Elemente
11. 🐍 **Python/Flask Backend** → API erstellen
12. 🗄️ **Datenbank** anbinden → MySQL Integration
13. ✅ **Testing** → Jest, Pytest, PHPUnit

## 🤖 Automatische Validierung

Dieses Projekt nutzt **GitHub Actions** für automatische Code-Qualität:

- ✅ **HTML-Validierung** bei jedem Push
- 📊 **Ergebnisse** im "Actions"-Tab auf GitHub
- 🔴 **Fehler** werden automatisch angezeigt
- 🟢 **Erfolg** = Code ist valide

**Workflow-Datei:** `.github/workflows/validate-html.yml`

## 🧪 Testing (Überblick - Geplant)

Zukünftige Test-Beispiele:

- **Jest** - JavaScript/React Unit Tests
- **Pytest** - Python Flask API Tests
- **PHPUnit** - PHP Backend Tests
- **Cypress** - End-to-End Browser Tests

## 🔄 Template-Updates für Student-Repos

Dieses Repository ist ein **GitHub Classroom Template**. Wenn du als Schüler:in damit arbeitest und später **neue Versionen** (z.B. Version 4) oder **Dokumentations-Updates** übernehmen möchtest:

📖 **Vollständige Anleitung:** [docs/handbook/TEMPLATE_SYNC.md](docs/handbook/TEMPLATE_SYNC.md)

**Quick-Start:**

```bash
# 1. Template als Remote hinzufügen (einmalig)
git remote add template https://github.com/ChristineJanischek/web-project-dynamic.git
git fetch template

# 2. Neue Inhalte übernehmen (z.B. Version 4)
git checkout template/main -- version4/
git commit -m "✨ Version 4 vom Template hinzugefügt"
git push
```

⚠️ **Wichtig:** Überschreibe niemals deine eigenen Lösungen in `version*/aufgabe/`!

---

## 🤝 Mitmachen & Beiträge

Verbesserungen und Erweiterungen sind willkommen!

**Für Lehrkräfte & Mentoren:**

- Pull Requests für neue Aufgaben oder Docs
- Bitte klare, verständliche Sprache nutzen
- Code-Beispiele kommentieren
- Best Practices beachten

**Für Studierende:**

- Issues für Fragen oder Unklarheiten
- Verbesserungsvorschläge willkommen
- Teile deine Lösungen (optional)

## 📜 Lizenz & Nutzung

- **Verwendungszweck:** Unterricht & Bildung
- **GitHub Classroom:** Frei verwendbar
- **Kommerzielle Nutzung:** Bitte Kontakt aufnehmen
- **Credits:** Erwähnung erwünscht

## 📞 Support

- **Fragen?** → Erstelle ein Issue auf GitHub
- **Bugs?** → Bug Report im Issues-Tab
- **Verbesserungen?** → Pull Request erstellen

---

## 🏷️ Versions-Tags

- `v1.0-release` - Version 1 komplett (HTML + CSS Basics)
- `docs-complete` - Alle Frontend-Dokumentationen verfügbar
- Weitere Tags folgen mit neuen Releases

---

**Dieses Projekt wächst kontinuierlich!** ⭐ Star uns auf GitHub wenn es dir hilft!

**Erstellt mit ❤️ für Web-Entwicklungs-Einsteiger**
