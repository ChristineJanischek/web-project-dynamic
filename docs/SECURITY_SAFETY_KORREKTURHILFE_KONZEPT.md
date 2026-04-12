# Security-und-Safety-Konzept fuer Owner-only Korrekturhilfe

## 1. Zweck und Schutzanspruch

Dieses Dokument beschreibt das Sicherheits- und Safety-Konzept fuer die Korrekturhilfe-Funktion im Repository.

Ziel ist ein maximal robuster Schutz gegen unbeabsichtigte Offenlegung von Bewertungsdaten bei:
- Nutzung des Repositories durch Dritte
- Download oder Fork des Repositories
- Nutzung als Template
- normaler Teamarbeit mit Git, CI und lokalen Entwicklungsumgebungen

Schutzgut:
- Bewertungen, Zwischenstaende, Rankings, Uebersichten, Korrekturhilfe-Reports
- Schueler-ZIPs und entpackte Projektinhalte
- Owner-spezifische Konfigurationen und sensible Metadaten

Kernanforderung:
- Nur der Owner darf Zugriff auf Bewertungsdaten erhalten.

## 2. Sicherheitsprinzipien

1. Strikte Trennung von Code und sensiblen Laufzeitdaten
2. Fail-closed statt fail-open: Bei Unsicherheit wird blockiert
3. Mehrschichtige Kontrollen (Defense in Depth)
4. Automatisierte Durchsetzung vor menschlicher Disziplin
5. Nachweisbarkeit und Revisionsfaehigkeit
6. Minimalprinzip fuer erlaubte Dateien (Allowlist)

## 3. Bedrohungsmodell

### 3.1 Relevante Risiken

1. Versehentlicher Commit sensibler Bewertungsdateien
2. Versehentlicher Push durch lokale oder automatisierte Workflows
3. Leakage in Pull Requests, Forks oder Templates
4. Mitkopieren sensibler Dateien in Export- oder Upload-Pfaden
5. Historische Altartefakte mit altem Namensschema

### 3.2 Auswirkung ohne Schutz

- Vertraulichkeitsverletzung gegenueber Schuelerinnen und Schuelern
- rechtliche und organisatorische Risiken (Datenschutz, Fairness, Pruefungsintegritaet)
- Vertrauensverlust und Anfechtbarkeit der Bewertungspraxis

## 4. Implementierte Schutzmechanismen (Ist-Stand)

## 4.1 Architektur-Schutz: Owner-only Workspace ausserhalb des Repositories

Implementierung:
- [scripts/assessment_assistant/config.py](scripts/assessment_assistant/config.py)
- [scripts/assessment_assistant/bootstrap.py](scripts/assessment_assistant/bootstrap.py)
- [scripts/assessment_assistant/security.py](scripts/assessment_assistant/security.py)

Wirkung:
- Sensible Laufzeitdaten liegen standardmaessig unter Home/Downloads/edu-assessment-owner
- Dieser Speicherort liegt ausserhalb des Repository-Baums
- Verzeichnisrechte werden auf 700 gesetzt
- sensible Konfigurationsdateien werden auf 600 gesetzt
- Ein Pfad innerhalb des Repositories wird aktiv abgewiesen

Sicherheitsnutzen:
- Repo-Download, Fork oder Template-Nutzung enthalten keine Owner-Daten
- Trennung von Verteillogik und Bewertungsdaten ist technisch erzwungen

## 4.2 Git-Schutz: Harte Ignore-Regeln fuer sensible Artefakte

Implementierung:
- [.gitignore](.gitignore)

Blockierte Muster (Auszug):
- alle Korrekturhilfe-Drafts und Startberichte
- alte Bewertungsmuster (Rueckwaertskompatibilitaet)
- Uebersichten und Ranglisten
- lokale Download-, Export- und Owner-Bereiche

Sicherheitsnutzen:
- reduziert das Risiko versehentlicher Aufnahme in den Git-Index

Wichtige Grenze:
- Gitignore allein ist kein absoluter Schutz, wenn Dateien bereits getrackt wurden.

## 4.3 Aktiver Leak-Blocker: Sensitivdaten-Check ueber getrackte Dateien

Implementierung:
- [scripts/check_sensitive_assessment_data.py](scripts/check_sensitive_assessment_data.py)

Funktionsweise:
- liest den real getrackten Zustand via git ls-files
- prueft auf verbotene Pfad- und Dateimuster
- nutzt bei Uploads eine strikte Allowlist
- bricht bei Verstoessen mit Exit-Code 1 ab

Sicherheitsnutzen:
- erkennt auch Faelle, die Gitignore nicht mehr verhindern kann
- verhindert das Weiterarbeiten mit unsicherem Repo-Zustand

## 4.4 Lokaler Commit-Blocker: Pre-Commit Hook

Implementierung:
- [.pre-commit-config.yaml](.pre-commit-config.yaml)

Funktionsweise:
- fuehrt den Sensitivdaten-Check vor jedem Commit aus
- blockiert den Commit bei Verstoessen

Sicherheitsnutzen:
- frueheste technische Kontrollstufe direkt am Entwicklerarbeitsplatz

## 4.5 Remote-Blocker: CI Security Gate auf Push und Pull Request

Implementierung:
- [.github/workflows/assessment-security.yml](.github/workflows/assessment-security.yml)

Funktionsweise:
- startet bei Push und Pull Request auf main
- fuehrt denselben Sensitivdaten-Check serverseitig aus
- verhindert unbemerkte Leaks im zentralen Repository

Sicherheitsnutzen:
- unabhaengige zweite Kontrollinstanz
- Schutz auch dann, wenn lokale Hooks umgangen wurden

## 4.6 Namensschema und Rueckwaertsschutz

Umsetzung:
- aktuelles Namensschema nutzt Korrekturhilfe
- alte Bewertungsmuster werden weiterhin blockiert

Sicherheitsnutzen:
- verhindert Leaks aus Alt-Workflows und gemischten Staenden

## 5. Safety-Aspekte (Betriebssicherheit und Fehlertoleranz)

1. Deterministische Regeln statt stiller Heuristik fuer den Leak-Check
2. Explizite Fehlermeldungen mit Abhilfehinweis
3. Idempotente Pruefungen (mehrfach ausfuehrbar, gleiche Aussage)
4. Trennung von Schutzpruefung und Fachbewertungslogik
5. Verhinderung von stillen Teilerfolgen: bei Verstoss klares Stop-Signal

## 6. Verteidigungs- und Rechtfertigungsargumentation

Diese Punkte koennen in Gespraechen mit Schulleitung, Pruefungsaufsicht oder Datenschutzbeauftragten genutzt werden.

1. Technische Trennung ist erzwungen, nicht nur organisatorisch empfohlen.
2. Mehrstufige Kontrollen existieren lokal und serverseitig.
3. Es gibt aktive Blocker gegen versehentliche Offenlegung.
4. Das Konzept ist revisionsfaehig, da es auf versionierten Regeln basiert.
5. Auch Altdatenmuster sind explizit in den Schutz aufgenommen.
6. Das Restrisiko ist transparent benannt und durch Prozesse minimiert.

## 7. Nachweisfuehrung und Audit-Checkliste

Empfohlene Nachweise vor Freigabe oder Pruefung:

1. Lokaler Sicherheitscheck erfolgreich:
   - python3 scripts/check_sensitive_assessment_data.py
2. Pre-commit Hook aktiv:
   - pre-commit install
3. CI Security Gate gruener Status auf main
4. Keine sensiblen Dateien in git ls-files
5. Bewertungsdaten liegen nur im Owner-only Workspace ausserhalb des Repositories

Empfohlene Archivierung fuer Audits:
- Screenshot oder Logauszug des erfolgreichen Sicherheitschecks
- Link auf erfolgreichen CI-Lauf
- Datum/Uhrzeit und Verantwortliche Person

## 8. Restrisiken und Grenzen

1. Ein bewusst boeswilliger Nutzer mit Owner-Rechten kann lokal Daten exfiltrieren.
2. Manuelle Uploads in externe Systeme ausserhalb des Repositories sind nicht technisch verhindert.
3. Historische Leaks in frueheren Commits muessen separat bereinigt werden.

Bewertung:
- Das verbleibende Risiko liegt primaer ausserhalb der Repo-internen technischen Kontrollen.

## 9. Notfallprozess bei vermutetem Leak

1. Sofortiger Stop weiterer Pushes
2. Betroffene Dateien identifizieren (git ls-files, git log, PR-Historie)
3. Dateien aus Tracking entfernen (git rm --cached)
4. Neue Sicherheitspruefung lokal und in CI
5. Falls bereits veroeffentlicht: Incident-Dokumentation und ggf. History-Cleanup
6. Kommunikation an betroffene Stakeholder nach interner Richtlinie

## 10. Betriebsrichtlinie (Kurzfassung)

1. Korrekturhilfe-Daten niemals im Repository speichern
2. Ausschliesslich Owner-only Workspace fuer Laufzeitdaten verwenden
3. Vor jedem Release Sicherheitscheck ausfuehren
4. CI-Failures im Security Gate als Blocker behandeln
5. Aenderungen an Sicherheitsregeln nur per Review und mit Begruendung

## 11. Technische Referenzen

- [scripts/assessment_assistant/security.py](scripts/assessment_assistant/security.py)
- [scripts/assessment_assistant/bootstrap.py](scripts/assessment_assistant/bootstrap.py)
- [scripts/assessment_assistant/config.py](scripts/assessment_assistant/config.py)
- [.gitignore](.gitignore)
- [.pre-commit-config.yaml](.pre-commit-config.yaml)
- [scripts/check_sensitive_assessment_data.py](scripts/check_sensitive_assessment_data.py)
- [.github/workflows/assessment-security.yml](.github/workflows/assessment-security.yml)
- [docs/handbook/ASSESSMENT_ASSISTANT_ARCHITECTURE.md](docs/handbook/ASSESSMENT_ASSISTANT_ARCHITECTURE.md)

## 12. Versionierung

- Dokumenttyp: Security-und-Safety-Konzept
- Gueltig ab: 2026-04-11
- Verantwortlich: Repository-Owner
- Aenderungen an diesem Dokument sind revisionspflichtig
