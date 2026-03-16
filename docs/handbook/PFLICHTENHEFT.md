# Pflichtenheft

# Projekt: Intelligentes webbasiertes eLearning-Kurseditor-System für Informatik

Geplant Repositories:

1. edu-code-lab-core
2. edu-code-lab-courses

Version: 1.0  
Status: Konzept / Architekturentwurf  
Datum: 2026

---

# 1 Projektvision

Ziel des Projekts ist die Entwicklung eines webbasierten intelligenten eLearning-Kurseditor-Systems speziell für Informatikunterricht.

Das System soll kein klassisches Learning Management System wie Moodle sein.

Stattdessen soll es ein pädagogisch intelligenter Kurseditor sein, der Lehrern und Schülern ermöglicht:

- Informatik-E-Learnings zu erstellen
- Codeaufgaben direkt im System zu bearbeiten
- Modellierungsaufgaben zu integrieren
- automatisierte Qualitätsprüfung zu nutzen
- eine kontinuierlich wachsende Wissensdatenbank aufzubauen
- Lernpfade intelligent zu strukturieren

Der Fokus liegt auf praktischem Informatikunterricht.

---

# 2 Projektziele

## Pädagogische Ziele

Das System soll:

- Informatik handlungsorientiert vermitteln
- selbstgesteuertes Lernen ermöglichen
- strukturierte Lernpfade anbieten
- praktische Programmieraufgaben integrieren
- moderne Themen wie KI und Machine Learning, Software Engineering integrieren

---

## Technische Ziele

Das System muss folgende Qualitätsmerkmale erfüllen:

- Erweiterbarkeit
- Wartbarkeit
- Wiederverwendbarkeit
- Sicherheit
- hohe Usability
- klare Struktur
- vollständige Dokumentation
- keine Redundanzen
- Online Examen (Prüfungen)
- sprachübergreifende Nutzbarkeit (mindestens HTML/CSS/JavaScript, PHP, Python, Java)
- reproduzierbare lokale Live-Test-Umgebung
- standardisierte Toolchain für VS Code (inklusive Extension-Management)
- optionaler Betrieb auf eigenem Webserver ohne Vendor-Lock-in

---

# 3 Zielgruppe

Primäre Zielgruppe:

- Informatiklehrer
- Schüler Sekundarstufe II
- Berufskollegs
- Berufliche Gymnasien, Schulen

Sekundäre Zielgruppe:

- Informatik-Fachschaften
- Schulen mit GitHub Classroom
- Entwickler von Bildungssoftware

---

# 4 Einsatzbereiche

Das System soll Kurse ermöglichen für:

- Programmierung
- Softwareentwicklung/-Management (Git und Github)
- BPMN / Geschäftsprozessmodellierung
- Mockups / UI-Design Integration
- Künstliche Intelligenz
- Machine Learning
- Datenbanken,
- eERM
- Webentwicklung
- OOP
- UML Klassendiagramme erstellen
- Struktogramme erstellen
- Code Generierung Bidirektional Modellierung/UI Design

---

# 5 Machbarkeitsanalyse

## Technische Machbarkeit

Die Umsetzung ist realistisch, da folgende Technologien bereits existieren:

| Bereich            | Technologie                     |
| ------------------ | ------------------------------- |
| Repository         | GitHub                          |
| Kollaboration      | GitHub Classroom                |
| Codeeditor         | VS Code                         |
| Dokumentation      | Markdown                        |
| Diagramme          | Draw.io                         |
| Automatisierung    | GitHub Actions                  |
| KI-Integration     | LLM APIs                        |
| Export             | Pandoc                          |
| Programmiersprache | Java 21 LTS (OpenJDK / Temurin) |
| Build-Tool         | Maven 4.x                       |
| Test-Framework     | JUnit 5                         |
| GUI-Technologie    | Java Swing                      |
| Browser-GUI-Zugang | noVNC (Port 6080)               |
| Containerisierung  | Docker & Docker Compose         |
| Datenbank          | MySQL (containerisiert)         |

Diese Technologien ermöglichen eine skalierbare Architektur.

## Ergänzende technische Machbarkeit für Mehrsprachen-Webprojekte

Für den im Repository gelebten Unterrichtsbetrieb (statisch + dynamisch) sind zusätzlich folgende Technologien verbindlich zu berücksichtigen:

| Bereich                     | Technologie / Standard                            |
| --------------------------- | ------------------------------------------------- |
| Live-Test statischer Seiten | VS Code Live Server                               |
| PHP-Live-Test               | PHP Built-in Server (`php -S`)                    |
| Python-Live-Test            | Flask Development Server (`flask run`)            |
| Frontend Tooling            | Node.js + npm (Skripte, Qualitätschecks)          |
| Extension-Management        | zentrales Manifest + Sync/Check-Skripte           |
| Browser-Test                | moderne Chromium/Firefox-basierte Browser         |
| Zielbetrieb Webserver       | Apache oder Nginx (bei Bedarf mit PHP-FPM / WSGI) |

Damit ist sichergestellt, dass das System nicht nur für eine einzelne Sprache, sondern für höhere Programmiersprachen im Unterrichtseinsatz geeignet ist.

## Systemvoraussetzungen

Für den Betrieb und die Entwicklung sind folgende Softwarekomponenten erforderlich:

| Komponente     | Version                          | Zweck                           |
| -------------- | -------------------------------- | ------------------------------- |
| Java (OpenJDK) | 21 LTS                           | Laufzeitumgebung und Compiler   |
| Maven          | 4.x                              | Build, Abhängigkeits­verwaltung |
| Docker         | aktuell                          | Container-Laufzeitumgebung      |
| Docker Compose | aktuell                          | Multi-Container-Orchestrierung  |
| Git            | beliebig                         | Versionskontrolle               |
| Browser        | modern (Chrome / Firefox / Edge) | noVNC-GUI-Zugang                |

**Installation Docker (Ubuntu/Debian):**

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

**Installation Java 21 (Ubuntu/Debian):**

```bash
sudo apt-get install -y openjdk-21-jdk-headless
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
```

Getestete Betriebssysteme:

- Ubuntu 24.04 LTS
- Ubuntu 22.04 LTS
- Linux (allgemein) mit Java 21
- macOS und Windows (JAVA_HOME manuell setzen)

## Verbindliche Betriebsprofile (Live-Test und Deployment)

Es sind zwei Betriebsprofile verbindlich zu unterstützen:

### Profil A: Lokaler Live-Test im Unterricht

Mindestanforderungen:

- VS Code muss als primäre Entwicklungsumgebung nutzbar sein
- notwendige Extensions werden zentral gepflegt und per Task/Skript installierbar gemacht
- statische Inhalte sind live im Browser testbar (Live Reload)
- dynamische Inhalte sind lokal testbar:
  - PHP über Built-in Server
  - Python über Flask-Dev-Server
- Port-Konflikte müssen in der Dokumentation behandelt werden (Ersatzports)

Verbindliche Nachweise:

- One-Click-Task für Live-Test-Extension-Installation
- CI-Check gegen Drift zwischen Extension-Manifest und Workspace-Empfehlungen
- didaktische Kurzanleitung für Schüler und Setup-Anleitung für Lehrkräfte

### Profil B: Betrieb auf eigenem Webserver (Self-Hosted)

Mindestanforderungen:

- Deployment ohne proprietäre Plattformabhängigkeit möglich
- Zielumgebung mindestens Linux-Server mit Apache oder Nginx
- Sprach-Laufzeiten müssen trennbar betreibbar sein (z. B. PHP-FPM, Python-App-Server)
- Konfigurierbare Datenbankanbindung (z. B. MySQL)
- Trennung von Entwicklungs- und Produktionsmodus dokumentiert

Verbindliche Nachweise:

- Deployment-Runbook mit Beispielkonfigurationen
- Sicherheits-Baseline (Secrets, HTTPS, minimale Rechte, Logging)
- Restore-fähige Backup-Strategie für Inhalte und Datenbank

---

Probleme im Informatikunterricht heute:

- Materialien sind unstrukturiert
- Aufgaben existieren redundant
- Materialien sind schwer wiederverwendbar
- unterschiedliche Dokumentformate
- wenig Automatisierung
- hoher manueller Aufwand

---

# 7 Konkurrenzanalyse

| System           | Bewertung                     |
| ---------------- | ----------------------------- |
| Moodle           | LMS, kein Kurseditor          |
| GitHub Classroom | Codeplattform, keine Didaktik |
| CodeRunner       | nur Aufgabenprüfung           |
| Jupyter          | gut für Data Science          |

Ergebnis:

Es existiert derzeit kein System, das Kurseditor, Codeplattform, Wissensdatenbank, KI-Assistenz und GitHub-Integration kombiniert.

---

# 8 Systemarchitektur

Die Architektur besteht aus fünf Ebenen.

Frontend  
↓  
Kurseditor  
↓  
Content Engine  
↓  
Wissensdatenbank  
↓  
GitHub Repository

## MVC-Architekturmuster

Alle Kursanwendungen und interaktiven Codeaufgaben folgen dem **Model-View-Controller (MVC)**-Muster:

| Schicht        | Aufgabe                              | Beispiel im Referenz-Projekt   |
| -------------- | ------------------------------------ | ------------------------------ |
| **Model**      | Daten, Geschäftslogik, Berechnungen  | `Bmirechner.java`              |
| **View**       | GUI, Darstellung, Benutzeroberfläche | `MainWindow.java` (Java Swing) |
| **Controller** | Vermittlung zwischen Model und View  | `BmiManager.java`              |

Das Single-Entry-Point-Prinzip (SEP) ist verbindlich: Jede Anwendung hat genau eine `main`-Methode als Einstiegspunkt. Alle Initialisierungen, Security-Checks und Konfigurationen laufen zentral über diesen Einstiegspunkt.

## Containerisierung

Anwendungen werden als Docker-Container ausgeliefert:

- **Dockerfile** – definiert das Basis-Image (Alpine-basiert für Produktion)
- **Dockerfile.novnc** – GUI im Browser via noVNC (Port 6080)
- **docker-compose.yml** – Orchestrierung: Anwendung + MySQL-Datenbank

Vorteile:

- plattformunabhängige Ausführung
- reproduzierbare Entwicklungsumgebungen
- einfache Verteilung an Schüler (kein lokales Java-Setup nötig)
- Datenbankdienste containerisiert und isoliert

---

# 9 Kernfunktionen

## Kurseditor

Lehrer und Schüler können:

- Kurse erstellen
- Aufgaben definieren
- Lösungen hinterlegen
- Lernpfade strukturieren
- Gleichwertige Aufgaben mit Lösungen generieren und im System integrieren lassen

---

## Code Integration

Unterstützte Sprachen:

- Python
- Java
- HTML
- CSS
- JavaScript
- PHP

Verbindliche Integrationsanforderungen:

- Für jede unterstützte Sprache existiert mindestens ein lauffähiger Referenzpfad im Repository
- Für jede unterstützte Sprache ist ein lokaler Teststart dokumentiert
- CI- und Qualitätsroutinen dürfen sprachspezifische Lernpfade nicht gegenseitig blockieren
- Aufgaben-Templates müssen sprachneutral strukturierbar sein (gemeinsame Metadaten, sprachspezifische Laufzeit)

---

## Modellierung

Unterstützung für:

- Struktogramme
- BPMN -> Mockups -> Quellcode
- UML

Integration über Draw.io.

---

# 10 Wissensdatenbank

Alle Inhalte werden zentral gespeichert.

Eigenschaften:

- versioniert
- strukturiert
- wiederverwendbar
- keine Redundanzen

---

# 11 Aufgabenstruktur

Jede Aufgabe nutzt ein Template.

Titel  
Thema  
Beschreibung  
Aufgabe  
Codebox  
Bewertung  
Häufige Fehler  
Lösung

Metadaten:

- Schwierigkeit
- Lernziel
- Punkte
- Erwartungshorizont
- Dauer

---

# 12 Bewertungssystem

Jede Aufgabe enthält:

Bewertung:

- Punkteverteilung
- Bewertungskriterien
- Teilpunkte

Häufige Fehler:

Liste typischer Schülerfehler.

Nutzen:

- schnellere Korrektur
- gerechte Bewertung

---

# 13 KI Unterstützung

Das System soll KI nutzen für:

- Aufgabenvariationen
- Qualitätsprüfung
- Codeoptimierung
- Lernpfadempfehlungen
- Generierung neuer Aufgaben

---

# 14 Qualitätssicherung

Automatische Prüfungen:

- Codequalität
- Duplikate
- Redundanzen
- Architekturprüfung
- Sicherheitsprüfung

Diese Prüfungen laufen über GitHub Actions.

Verbindliche CI-Prüfungen umfassen zusätzlich:

- Exam-Validierung (Variantenanzahl, Konsistenz Aufgabe/Lösung, Duplikatprüfung je Aufgabe, Punktelogik)
- Navigationsprüfung der Grundlagen-Dokumentation (zentrale Regelkonfiguration)
- Namenskonventionen und Strukturvalidierung
- Drift-Prüfung der VS-Code-Extension-Empfehlungen gegen zentrales Manifest
- Accessibility- und Lighthouse-Qualitätschecks für Web-Projekte
- Automatisierte Synchronisation der Aufgabenstellungen in Musterlösungen:
  - Aufgabenstellungen werden ausschließlich in den Aufgaben-Dateien (exam\*.md) gepflegt
  - Ein zentrales Skript übernimmt die Aufgabenstellungen automatisiert in die zugehörigen Musterlösungen (solutions\*.md)
  - Bei jeder Änderung an Aufgabenstellungen wird die Synchronisation verpflichtend ausgeführt (z.B. als Pre-Commit-Hook oder CI-Check)
  - Redundanzen und Inkonsistenzen zwischen Aufgaben und Lösungen werden so dauerhaft vermieden
- Umlaut- und Sonderzeichen-Prüfung für Aufgaben- und Lösungsdateien:
  - Alle Markdown-Dateien in `docs/programmierung/grundlagen/exams/` müssen korrekte Unicode-Zeichen verwenden (ä, ö, ü, ß statt ae, oe, ue, ss)
  - Die Prüfung ist integraler Bestandteil von `scripts/validate_exams.py` (Funktion `check_unicode_umlauts`); kein separates Skript erforderlich
  - Die Prüfung läuft als Pre-Commit-Hook und als verbindlicher CI-Check
  - Verstöße blockieren den Commit bzw. schlagen den CI-Workflow fehl
- Smoke-Test-Checkliste für lokale Laufzeitprofile (statisch, PHP, Python)

## Unit-Tests mit JUnit 5

Alle Klassen der Geschäftslogik (Model) müssen durch automatisierte Unit-Tests abgedeckt sein.

Anforderungen:

- Test-Framework: **JUnit 5**
- Build-Ausführung: `mvn test`
- Grenzwerttests für Algorithmen (z. B. BMI-Kategorien) sind verpflichtend
- Tests müssen im CI-Workflow (GitHub Actions) automatisch laufen
- Testergebnisse blockieren den Push bei Fehler (Pre-Push-Hook)

## Git Hooks

Zur lokalen Qualitätssicherung sind folgende Git Hooks einzurichten:

| Hook          | Zweck                                                                |
| ------------- | -------------------------------------------------------------------- |
| `pre-commit`  | Prüft Umlaute/Unicode in Exam-Dateien; blockiert bei ASCII-Kodierung |
| `pre-push`    | Führt `mvn test` aus; blockiert bei Fehler                           |
| `post-commit` | Auto-Push nach erfolgreichem Commit (optional)                       |

Die Hooks sind als Teil des Template-Repositories bereitzustellen und in der Onboarding-Dokumentation zu beschreiben.

Lokale Qualitätssicherung:

- Pre-Commit-Hooks müssen für prüfungsrelevante Inhalte aktivierbar sein
- Umlaut-/Unicode-Check muss als Pre-Commit-Hook ohne manuelle Aktivierung greifen
- Wissensdatenbank/Fingerprints für Aufgabenvarianten müssen automatisiert aktualisierbar sein
- Setup-Checks für Live-Test-Umgebung müssen ohne manuelle Nacharbeit reproduzierbar sein

---

# 15 Exportfunktionen

Aufgaben können exportiert werden als:

- PDF
- DOCX
- HTML
- XML
- Markdown

Nutzen:

- Offline Prüfungen
- Ausdrucke
- Archivierung

---

# 16 GitHub Repository Strategie

Empfohlene Struktur:

elearning-core  
│  
├── platform  
├── templates  
├── knowledge-base  
├── courses  
└── tools

## Template-Repository-System

Kursaufgaben werden als **GitHub Template-Repositories** bereitgestellt. Jedes Template enthält:

- vollständige Projektstruktur (MVC, Build-Skripte, Tests)
- versionierte Branches für schrittweisen Lernfortschritt
- Docker-Setup für lokale und containerisierte Ausführung
- vorkonfigurierte Git Hooks und CI-Workflows

## GitHub Classroom Integration

Das System ist explizit für die Nutzung mit **GitHub Classroom** konzipiert:

- Jede Aufgabe wird als Template-Repository (z.B. Versionierte Lernbranches) auf GitHub bereitgestellt
- GitHub Classroom verteilt das Repository automatisch an Schüler (eigene Kopie je Schüler)
- Autograding erfolgt über `mvn test` (JUnit 5 Tests liefern automatisierte Bewertungsgrundlage)
- Lehrer sehen alle Abgaben zentral im GitHub Classroom Dashboard
- Branch Protection verhindert unbeabsichtigtes Überschreiben von Musterlösungen

---

# 17 Branch Strategie

main  
development  
content  
experiment

Zusätzlich thematische Branches:

core-programming  
core-ai  
core-software-engineering

---

# 18 Repository Governance

Nur der Projektverantwortliche darf:

- pushen
- committen
- mergen

Branch Protection Regeln:

- Pull Requests erforderlich
- CI Checks erforderlich
- Reviews verpflichtend

Erweiterte Governance-Anforderungen:

- `main` ist als geschützter Branch zu führen; direkte Push-Rechte sind auf die Projektadministration zu begrenzen
- Code-Owner-Review muss für Merge nach `main` verpflichtend sein
- Offene Review-Konversationen müssen vor Merge aufgelöst sein
- Governance-Einstellungen sind regelmäßig gegen die dokumentierte Zielkonfiguration zu prüfen

---

# 19 Meilensteinplan

Phase 1 – Konzept (1–2 Monate)

- Architekturdefinition
- Repositorystruktur
- Template-System

Phase 2 – Minimalversion (3–4 Monate)

- funktionaler Kurseditor
- Markdown Aufgaben
- GitHub Integration

Phase 3 – Wissensdatenbank (6 Monate)

- Aufgabenbibliothek
- automatische Strukturprüfung
- Versionierung

Phase 4 – KI Integration (9 Monate)

- Aufgabenvariationen
- Empfehlungssystem
- Qualitätsprüfung

---

# 20 Start ToDo Liste

- Repository erstellen
- Struktur definieren
- Templates definieren
- GitHub Actions einrichten
- Wissensschema entwickeln
- Kurseditor Konzept erstellen
- Exam-CI einrichten (Pre-Commit, Remote-Validierung, Knowledge-Base-Update)
- Backup-Workflow aktivieren und regelmäßige Restore-Tests planen
- Docs-Navigation-Regeln zentral konfigurieren und automatisiert prüfen
- VS-Code-Extension-Manifest synchronisieren und CI-Check aktivieren
- Template-Update-Benachrichtigung und Release-Kommunikation etablieren
- Deployment-Runbook für eigenen Webserver (Apache/Nginx) erstellen und regelmäßig testen
- Laufzeit-Startanleitungen für PHP/Python/Frontend in einer zentralen Checkliste zusammenführen

---

# 21 Langfristige Vision

Ein offenes System für Schulen:

- offene Wissensdatenbank
- automatisierte Kursentwicklung
- intelligente Lernpfade
- KI-gestützte Informatikdidaktik

Das System soll langfristig eine Plattform für moderne Informatiklehre werden.

---

# 22 Repositories

Trennung System und Inhalt

Zu 1. edu-code-lab-core.
Hier gehört alles hinein, was das System technisch bereitstellt.

Also zum Beispiel:

- Kurseditor
- Renderer
- Import-/Export-Logik
- Template-Engine
- GUI-Komponenten
- Rollen-/Rechtestruktur
- Codeboxen
- Prüf- und Validierungsroutinen
- KI-gestützte Qualitätschecks
- Synchronisationslogik
- Duplikatserkennung
- Modellierungsfunktionen
- Struktogramm-Generatoren
- Draw.io-/XML-/SVG-Schnittstellen
- Code-Generatoren aus Modellen
- Code-Analyse und Best-Practice-Checks
- GitHub-Anbindung
- Automatisierungen / CI / Prüfjobs

Zu 2. edu-code-lab-courses.
Hier gehört alles hinein, was fachlicher Inhalt ist.

Also:

- Kurse
- Module
- Lernpfade
- Aufgaben
- Lösungen
- Prüfungen
- Varianten
- Bewertungsschemata
- häufige Fehler
- Lehrerhinweise
- Schülerhinweise

---

# 23 Anforderungszuordnung: core vs. courses

## Leitprinzipien

| Kriterium     | edu-code-lab-core                  | edu-code-lab-courses              |
| ------------- | ---------------------------------- | --------------------------------- |
| Art           | Systemcode, Tooling, Infrastruktur | Fachlicher Inhalt, Lernmaterial   |
| Wer ändert    | Entwickler, DevOps                 | Lehrkräfte, Fachdidaktiker        |
| Versionierung | Plattform-Releases (SemVer)        | Kurs-/Inhaltsversionen unabhängig |
| CI/CD-Fokus   | Build, Test, Deploy der Plattform  | Content-Validierung, Exam-Checks  |
| Abhängigkeit  | wird von courses konsumiert        | hängt von core ab                 |

## Anforderungsmatrix

| Kapitel | Anforderungsbereich                             | core  | courses | Begründung                                               |
| ------- | ----------------------------------------------- | :---: | :-----: | -------------------------------------------------------- |
| 2       | Pädagogische Ziele                              |   —   |    ✓    | Beschreiben Inhaltsgestaltung, keine Systemfunktion      |
| 2       | Technische Ziele (Architektur, Toolchain)       |   ✓   |    —    | Plattformeigenschaften                                   |
| 3       | Zielgruppe                                      | beide |  beide  | Kontextinformation für beide Repos                       |
| 4       | Einsatzbereiche (Themenkatalog)                 |   —   |    ✓    | Kursinhalt, keine Systemfunktion                         |
| 5       | Technologiestack (Java, Docker, Maven)          |   ✓   |    —    | Laufzeit- und Build-Infrastruktur                        |
| 5       | Betriebsprofile (Live-Test, Self-Hosted)        |   ✓   |    —    | Deployment-Infrastruktur                                 |
| 6       | Problemanalyse                                  | beide |  beide  | Shared-Kontext                                           |
| 7       | Konkurrenzanalyse                               |   ✓   |    —    | Systementscheidung                                       |
| 8       | Systemarchitektur (MVC, Docker, Container)      |   ✓   |    —    | Plattformarchitektur                                     |
| 9       | Kurseditor-Anwendung                            |   ✓   |    —    | Systemkomponente                                         |
| 9       | Code-Integration (Runtimes, CI-Templates)       |   ✓   |    —    | Tooling / Infrastruktur                                  |
| 9       | Modellierung (Draw.io, UML, Struktogramme)      |   ✓   |    —    | Systemfunktion                                           |
| 10      | Wissensdatenbank – Schema, Infrastruktur        |   ✓   |    —    | Datenbankstruktur gehört zum System                      |
| 10      | Wissensdatenbank – Inhalte, Fingerprints (JSON) |   —   |    ✓    | Versionierter Kursinhalt                                 |
| 11      | Aufgabenstruktur – Template-Schema              |   ✓   |    —    | Strukturvorgabe ist Systemstandard                       |
| 11      | Aufgaben, Lösungen, Varianten (Inhalte)         |   —   |    ✓    | Fachlicher Inhalt                                        |
| 12      | Bewertungslogik (Kalkulation, Export)           |   ✓   |    —    | Systemfunktion                                           |
| 12      | Bewertungskriterien, Rubrics (Inhalte)          |   —   |    ✓    | Fachdidaktischer Inhalt                                  |
| 13      | KI-Services – API-Anbindung, Infrastruktur      |   ✓   |    —    | Systemkomponente                                         |
| 13      | KI-generierte Aufgabenvarianten (Ergebnis)      |   —   |    ✓    | Ergebnis = Kursinhalt                                    |
| 14      | QS-Tooling: Skripte, CI-Templates               |   ✓   |    —    | Systemwerkzeuge (siehe Grenzfall unten)                  |
| 14      | QS: Content-Prüfungen (Exam-Validierung)        |   —   |    ✓    | Laufen auf Kursinhalt; Workflows in courses              |
| 14      | QS: JUnit 5 / Maven-Tests                       |   ✓   |    —    | Plattform-Testframework                                  |
| 14      | Git Hooks (Templates)                           |   ✓   |    —    | Bereitgestellt von core, eingebunden in courses          |
| 15      | Export-Engine (PDF, DOCX, HTML)                 |   ✓   |    —    | Systemfunktion                                           |
| 16      | Template-Repository-Struktur                    |   ✓   |    —    | Systemstandard                                           |
| 16      | GitHub Classroom Integration                    |   ✓   |    —    | Systemfunktion                                           |
| 17      | Branch-Strategie                                | beide |  beide  | Jedes Repo definiert eigene Regeln nach demselben Muster |
| 18      | Repository Governance                           | beide |  beide  | Gilt separat für jedes Repo                              |
| 19      | Meilensteinplan                                 |   ✓   |    —    | Plattformentwicklung treibt den Plan                     |
| 20      | Start-ToDo                                      | beide |  beide  | Infrastruktur- und Inhaltsaufgaben parallel              |
| 21      | Langfristige Vision                             |   ✓   |    —    | Systemperspektive                                        |

## Besonderer Grenzfall: Validierungsskripte

Die aktuell in `scripts/` enthaltenen Python-Skripte (`validate_exams.py`, `check_docs_navigation.py` etc.) sind logisch **core**-Artefakte (Systemwerkzeuge), residieren jedoch vorübergehend im **courses**-Repo (`web-project-dynamic`), da die core-Plattform noch nicht existiert.

**Langfristige Empfehlung (Zielzustand):**

- Skripte wandern nach `edu-code-lab-core`
- `edu-code-lab-courses` konsumiert sie via Git Submodule, npm-Paket oder Docker-Image
- CI-Workflows in courses referenzieren die Tools aus core; kein Tooling-Code im courses-Repo

**Kurzfristige Lösung (aktueller Stand):**

- Skripte verbleiben im courses-Repo bis die core-Plattform realisiert ist
- Sie sind in `scripts/` klar gebündelt und als "temporär hier, logisch core" zu verstehen
- Beim Migration-Schritt entfällt `scripts/` aus courses ersatzlos; CI-Workflows werden auf core-Referenz umgestellt

- fachliche Dokumentation
- kursbezogene Medien
- kursbezogene Diagramme
- kursbezogene Beispiele
- Markdown-Dateien mit Inhalten

Kurz: alles, was didaktischer oder fachlicher Content ist, gehört in das Courses-Repo.
