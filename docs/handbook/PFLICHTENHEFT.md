# Pflichtenheft

# Projekt: Intelligentes webbasiertes eLearning-Kurseditor-System fuer Informatik

**Geplante Repository-Struktur:**

1. `edu-code-lab-core` - Systemplattform, Tools, Infrastruktur
2. `edu-code-lab-courses` - Kursinhalte, Aufgaben, Lernmaterialien

**Version:** 1.3 (Repository Split)
**Status:** In Entwicklung - neu strukturiert
**Datum:** Maerz 2026
**Letzte Aktualisierung:** 19. Maerz 2026

**Weiterfuehrende Dokumente:**

- [SETUP_REPOSITORIES.md](SETUP_REPOSITORIES.md) - Konfigurationsanleitung fuer beide Repositories
- [ROADMAP_CORE.md](ROADMAP_CORE.md) - Marschplan fuer `edu-code-lab-core`
- [ROADMAP_COURSES.md](ROADMAP_COURSES.md) - Marschplan fuer `edu-code-lab-courses`
- [COURSES_THEMENPLAN.md](COURSES_THEMENPLAN.md) - themenspezifische und kursspezifische Feinheiten

---

# 1 Zweck und Abgrenzung

Dieses Pflichtenheft definiert die verbindlichen Anforderungen auf **Systemebene** und trennt konsequent zwischen:

- **core**: technische Plattformfaehigkeiten
- **courses**: didaktischer Inhalt und fachliche Auspraegung

Detaillierte inhaltliche Feinheiten werden bewusst aus diesem Dokument ausgelagert.

---

# 2 Verbindlicher Scope je Repository

## 2.1 `edu-code-lab-core` (Plattform)

`edu-code-lab-core` muss folgende Bestandteile bereitstellen:

- Editor- und Rendering-Bausteine
- Aufgaben-/Template-Engine
- Import-/Export-Services
- Validierungs- und Qualitaets-Tooling
- CI-Vorlagen, Hook-Templates, Automatisierungen
- Integrationsschnittstellen (z. B. KI-Adapter, VCS, Klassenraum-Workflows)

Nicht Teil von core:

- fachspezifische Aufgabeninhalte
- konkrete Kurse, Varianten und Loesungstexte

## 2.2 `edu-code-lab-courses` (Inhalt)

`edu-code-lab-courses` muss folgende Bestandteile bereitstellen:

- Kurse, Module und Lernpfade
- Aufgaben, Loesungen, Bewertungsschemata
- fachliche Beispiele, Medien, Diagramme
- didaktische Hinweise fuer Lehrkraefte und Lernende
- inhaltliche Versionierung und Pflegeprozesse

Nicht Teil von courses:

- Plattform-Tooling als dauerhafte Quellwahrheit (wandert langfristig nach core)

---

# 3 Muss-Anforderungen (MVP)

## 3.1 Muss-Anforderungen fuer core

1. Ein reproduzierbares lokales Setup fuer Entwickler muss dokumentiert und automatisierbar sein.
2. Build-, Test- und Qualitaetspruefungen muessen als CI-Workflows vorliegen.
3. Hook-Templates (`pre-commit`, optional `pre-push`) muessen bereitgestellt werden.
4. Ein standardisiertes Aufgaben-Schema muss als Vorlage fuer courses auslieferbar sein.
5. Exporte (mindestens Markdown/HTML) muessen ueber eine klar definierte Schnittstelle bereitstehen.
6. Integrationspunkte fuer Mehrsprachen-Runtimes muessen klar dokumentiert sein.

## 3.2 Muss-Anforderungen fuer courses

1. Inhalte muessen strikt entlang des in [COURSES_THEMENPLAN.md](COURSES_THEMENPLAN.md) definierten Themenkatalogs strukturierbar sein.
2. Jede Aufgabe muss Metadaten (Lernziel, Schwierigkeit, Punkte, Dauer) enthalten.
3. Jede Aufgabe muss mindestens eine validierbare Musterloesung enthalten.
4. Inhalte muessen mit den bereitgestellten core-Validierungen pruefbar sein.
5. Sprachpfade (HTML/CSS/JS, PHP, Python, Java) duerfen sich gegenseitig nicht blockieren.
6. Kursinhalte muessen didaktisch versionierbar und releasefaehig sein.

---

# 4 Soll-Anforderungen (Ausbaustufe)

## 4.1 Soll fuer core

- Plugin-Architektur fuer KI-gestuetzte Assistenz
- erweiterte Exportziele (PDF, DOCX)
- Deployment-Bausteine fuer Self-Hosting

## 4.2 Soll fuer courses

- themenspezifische Variantenbibliotheken
- differenzierte Lernpfade nach Schulform und Niveau
- kuratierte Fehlerkataloge je Themenfeld

---

# 5 Repository-Konfiguration (verbindlicher Verweis)

Die operative Einrichtung beider Repositories ist nicht in diesem Dokument ausformuliert.
Die verbindliche Schritt-fuer-Schritt-Konfiguration steht in:

- [SETUP_REPOSITORIES.md](SETUP_REPOSITORIES.md)

Dieses Dokument ist Bestandteil der Abnahmekriterien.

---

# 6 Getrennter Marschplan (verbindlicher Verweis)

Die getrennte Umsetzungsplanung erfolgt in zwei eigenstaendigen Roadmaps:

- [ROADMAP_CORE.md](ROADMAP_CORE.md)
- [ROADMAP_COURSES.md](ROADMAP_COURSES.md)

Beide Roadmaps muessen synchron geplant werden, duerfen aber unterschiedliche Releases und Geschwindigkeiten haben.

---

# 7 Auslagerung themenspezifischer Feinheiten

Alle themen-, kurs- und inhaltsspezifischen Detailanforderungen sind aus diesem Pflichtenheft ausgelagert nach:

- [COURSES_THEMENPLAN.md](COURSES_THEMENPLAN.md)

Dort werden verbindlich gepflegt:

- Themenbaum Informatik
- Lernziele pro Thema
- Aufgabenformate pro Thema
- empfohlene Reihenfolge und Vertiefungen

---

# 8 Governance und Verantwortlichkeiten

## 8.1 Verantwortlichkeiten

- `core`: primaer Entwicklerteam / Plattformverantwortung
- `courses`: primaer Lehrkraefte / Fachdidaktik

## 8.2 Branching und Schutz

- `main` ist in beiden Repositories geschuetzt
- Merge nur ueber Pull Requests
- erfolgreiche Pflichtchecks sind Merge-Voraussetzung
- offene Review-Konversationen muessen vor Merge aufgeloest sein

## 8.3 Qualitaet

- CI ist die verbindliche Schutzschicht
- lokale Hooks sind empfohlene Vorpruefung
- Abweichungen zwischen Dokumentation und Implementierung sind als Defect zu behandeln

---

# 9 Uebergangsregel (Ist -> Ziel)

Aktuell liegen einzelne Tooling-Skripte noch im courses-Kontext.
Bis zur vollstaendigen Trennung gilt:

1. Skripte bleiben voruebergehend an Ort und Stelle, werden aber als logische core-Artefakte gekennzeichnet.
2. Neue Tooling-Entwicklung erfolgt bevorzugt bereits mit Blick auf Migration nach core.
3. Nach Verfuegbarkeit von core werden Tooling-Artefakte migriert und in courses nur noch konsumiert.

---

# 10 Abnahmekriterien fuer diese Dokumentstruktur

Die Refaktorierung gilt als erfolgreich, wenn:

1. Die Trennung core/courses im Pflichtenheft ohne Mehrdeutigkeit erkennbar ist.
2. Eine praxistaugliche Setup-Anleitung fuer beide Repositories vorhanden ist.
3. Zwei getrennte Marschplaene (core und courses) vorhanden sind.
4. Themenspezifische Feinheiten in einer eigenen Datei ausgelagert sind.
5. Querverweise zwischen den Dokumenten konsistent und aktuell sind.

