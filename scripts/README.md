# Automatisierungs-Scripts und Qualitätssicherung

Dieses Projekt enthält verschiedene Automatisierungsskripte für Dokumentation, Examen-System und Qualitätssicherung.

## 🚀 Quick Links

- **[CI-Setup (Exam-System Validierung)](README_CI_SETUP.md)** – Pre-Commit Hooks + GitHub Actions
- **[Exam-System Dokumentation](../docs/programmierung/grundlagen/exams/)** – Examen, Varianten, Validierung

## Bewertungsmodul Start mit Uploads

Wenn in `material/uploads` ein Projekt-Archiv (`.zip`) und ein Bewertungsbogen (`.docx` oder `.md`) liegen, kann die Ingestion direkt gestartet werden:

```bash
python3 scripts/process_assessment_uploads.py
```

Der Bewertungslauf fuehrt standardmaessig vorab ein Live-Test-Setup aus:

- Sync der Workspace-Empfehlungen aus dem zentralen Manifest
- Installation der benoetigten VS-Code-Extensions aus dem Profil `live-test`

Nur falls noetig kann das Setup explizit uebersprungen werden:

```bash
python3 scripts/process_assessment_uploads.py --skip-live-test-setup
```

Alternativ ueber npm:

```bash
npm run assessment:ingest
```

Wenn ein standardisiertes Bewertungsprofil genutzt wird, kann der Lauf auch nur mit einem Projekt-Archiv gestartet werden. Dann werden die Kriterien direkt aus dem Profil geladen.

Der Lauf erstellt im owner-only Workspace unter `~/Downloads/edu-assessment-owner`:

- Ablage der Uploads in `eingang/` und `boegen/`
- Entpackte Projektquellen in `entpackt/`
- Rubrik-Rohtext als Markdown in `ausgang/`
- Startbericht fuer die weitere Bewertungsimplementierung in `ausgang/`
- Strukturierte Erstbewertung als JSON-Draft in `ausgang/`
- Lesbare Erstbewertung als Markdown-Draft in `ausgang/`
- HTML-Draft fuer Copy-Paste nach Word in `ausgang/`
- Bewertungsuebersicht als `bewertungsuebersicht.md` und `bewertungsuebersicht.html`
- Rangliste als `rangliste.md` und `rangliste.html`

Hinweis:

- Die Markdown-Datei bleibt die kanonische Bewertungsquelle.
- Die HTML-Datei ist ein generiertes Ausgabeformat fuer die Weiterverarbeitung in Word.
- Ohne separate Rubrikdatei wird der Rubrik-Rohtext nicht erzeugt; der Startbericht verweist dann auf die verwendete Profilbewertung.
- Alle HTML-Dateien aus `ausgang/` werden standardmaessig nach `~/Downloads/edu-assessment-html` kopiert.

Optional:

```bash
python3 scripts/process_assessment_uploads.py --skip-html-export
python3 scripts/process_assessment_uploads.py --download-html-dir ~/Downloads
```

Batch-Lauf fuer alle Projekte im Upload-Ordner (inklusive Live-Test-Setup vorab):

```bash
python3 scripts/batch_assess.py --uploads-dir material/uploads --profile-id webprojekte
```

Optional ohne Live-Test-Setup:

```bash
python3 scripts/batch_assess.py --uploads-dir material/uploads --profile-id webprojekte --skip-live-test-setup
```

Guard-Check fuer CI und lokale Vorabpruefung:

```bash
python3 scripts/check_live_test_preflight_guard.py
```

## 📋 Übersicht

Dieses Projekt enthält Scripts zur:

- Automatischen Dokumentations-Updates
- Exam-System-Validierung (Duplikat-Prüfung, Konsistenz)
- Architektur-Checks
- Navigation-Validierung

Wenn neue `.md`-Dateien zu `docs/` hinzugefügt werden, muss die Tabelle unter **"## Inhalt / Lernpfade"** in der Haupt-README aktualisiert werden.

## 🤖 Automatische Methoden

### Methode -2.6: Architektur-Checks zentral ausführen

**Ziel:**

- Architekturqualität strukturiert prüfen (Abstraktion, MVC, Sicherheit, Wartbarkeit)
- Prüfroutine auf mehrere Bereiche anwenden (`version1`-`version5`, `templates`, `shared-examples`, `src`)
- Ergebnisse zentral und wiederverwendbar im Report-Ordner ablegen

**Nutzung:**

```bash
python3 scripts/check_architecture.py
```

**Optionen:**

```bash
# Nur bestimmte Pfade prüfen
python3 scripts/check_architecture.py --paths version4 version5 src

# Alternativen Ausgabeordner verwenden
python3 scripts/check_architecture.py --output-dir reports/quality
```

**Output:**

- `reports/architecture_report.md`
- `reports/architecture_details.json`

### Methode -2.5: Docs-Navigation prüfen (Grundlagen)

**Ziel:**

- Konsistente Rück-/Weiter-Navigation in den Kapiteldateien
- Einheitliche Kapitelreihenfolge in JS/Python/PHP
- Vermeidung von redundanter Pflege durch zentrale Konfiguration

**Zentrale Dateien:**

- Konfiguration: `scripts/config/docs_navigation_rules.json`
- Check-Skript: `scripts/check_docs_navigation.py`
- Handbook: `docs/handbook/DOCS_NAVIGATION_RULES.md`

**Nutzung:**

```bash
python3 scripts/check_docs_navigation.py
```

**Alternativ über npm:**

```bash
npm run docs:navigation:check
```

**Exit-Codes:**

- `0`: erfolgreich
- `2`: Regelverletzungen gefunden
- `1`: Fehler (z. B. fehlende Konfiguration)

### Methode -2: VS-Code-Extensions zentral verwalten (Live-Test)

**Ziel:**

- Eine zentrale Quelle für alle empfohlenen Extensions
- One-Click-Installation für Live-Tests
- CI-Check gegen Drift zwischen Manifest und `.vscode/extensions.json`

**Zentrale Dateien:**

- Manifest: `scripts/config/vscode_extensions.json`
- CLI: `scripts/manage_vscode_extensions.py`
- Workspace-Task: `.vscode/tasks.json`

**Nutzung:**

```bash
# Empfehlungen aus Manifest nach .vscode/extensions.json schreiben
python3 scripts/manage_vscode_extensions.py sync

# Konsistenz prüfen (CI-freundlich, Exit-Code 2 bei Abweichung)
python3 scripts/manage_vscode_extensions.py check

# Nur Live-Test Extensions installieren
python3 scripts/manage_vscode_extensions.py install --profile live-test

# Vollständiges Set installieren
python3 scripts/manage_vscode_extensions.py install --profile full
```

**Alternativ über npm:**

```bash
npm run setup:live-test
npm run setup:extensions
npm run setup:extensions:sync
npm run setup:extensions:check
```

### Methode -1.5: Branch Protection (Admin-only Push auf main)

**Ziel:**

- Push auf `main` auf Admin-Account einschränken
- Code-Owner-Review verpflichtend machen

**Nutzung (einmalig als Admin):**

```bash
chmod +x scripts/configure_branch_protection.sh
./scripts/configure_branch_protection.sh ChristineJanischek web-project-dynamic main ChristineJanischek
```

### Methode -1: Backup-Snapshot erstellen

**Was passiert:**

- Erstellt ein vollständiges `git bundle` (inkl. Historie)
- Erstellt ein `tar.gz`-Archiv des aktuellen `HEAD`
- Schreibt `manifest.txt` und `SHA256SUMS.txt` zur Integritätsprüfung

**Lokal ausführen:**

```bash
chmod +x scripts/create_backup_snapshot.sh
./scripts/create_backup_snapshot.sh
```

**Optionales Zielverzeichnis:**

```bash
./scripts/create_backup_snapshot.sh /pfad/zum/backup
```

**Automatisierung:**

- Workflow: `.github/workflows/backup-snapshot.yml`
- Trigger: wöchentlich + manuell
- Ergebnis: Artifact `repo-backup-snapshot` (30 Tage)

### Methode 0: Datumsstand in "Was ist neu?" aktualisieren

**Was passiert:**

- Aktualisiert in `README.md` die Überschrift `## 🆕 Was ist neu? (Stand: TT.MM.JJJJ)` auf das heutige Datum
- Läuft automatisch über GitHub Actions bei Doku-/Material-Änderungen auf `main`

**Workflow:**

- `.github/workflows/update-whats-new-date.yml`

**Lokal ausführen:**

```bash
python3 scripts/update_whats_new_date.py
python3 scripts/update_whats_new_date.py --check
```

**Hinweis:**

- Das Skript ändert ausschließlich die Datumsangabe in der "Was ist neu?"-Überschrift.
- `--check` liefert Exit-Code `2`, wenn eine Änderung nötig wäre (CI-freundlich).
- Der Tabellenabgleich erfolgt semantisch (Spalteninhalte), nicht über reine Markdown-Formatierung.

### Methode 1: GitHub Actions (Empfohlen)

**Was passiert:**

- Bei jedem Push von `.md`-Dateien in `docs/` wird die README automatisch aktualisiert
- Commit erfolgt automatisch durch GitHub Bot

**Status:** ✅ Bereits konfiguriert in `.github/workflows/update-docs-table.yml`

**Manueller Trigger:**

1. Gehe zu GitHub → Actions → "Auto-Update Dokumentations-Tabelle"
2. Klicke "Run workflow"

### Methode 2: Python-Skript (Lokal)

**Verwendung:**

```bash
# Im Projekt-Root ausführen
python3 scripts/update_readme_docs.py
python3 scripts/update_readme_docs.py --check
```

**Voraussetzungen:**

- Python 3.7+

**Ausgabe:**

```
📝 Generiere Dokumentations-Tabelle...
📋 Gefundene Dokumentationen: 19/19
✅ README.md erfolgreich aktualisiert!
✨ Fertig! 19 Einträge in der Tabelle.
```

**Exit-Codes (beide Python-Skripte):**

- `0`: erfolgreich (inkl. "keine Änderung nötig")
- `1`: Fehler
- `2`: `--check` meldet notwendige Änderungen

### Methode 3: Bash-Skript (Linux/Mac)

**Verwendung:**

```bash
# Skript ausführbar machen
chmod +x scripts/update-readme-docs.sh

# Ausführen
./scripts/update-readme-docs.sh
```

**Voraussetzungen:**

- Bash 4.0+
- Standard Linux/Mac Tools (awk, sed)

## 📝 Neue Dokumentation hinzufügen

### Schritt 1: Datei erstellen

```bash
# Neue .md Datei in docs/ erstellen
touch docs/neue-dokumentation.md
```

### Schritt 2: Metadaten hinzufügen

**Python-Skript:** Editiere `scripts/update_readme_docs.py`

```python
DOC_METADATA: List[Tuple[str, str, str]] = [
    # ... bestehende Einträge ...
    ("neue-dokumentation.md", "Neues Thema", "Kurzbeschreibung des Themas"),
]
```

**Bash-Skript:** Editiere `scripts/update-readme-docs.sh`

```bash
doc_info["neue-dokumentation.md"]="Neues Thema|Kurzbeschreibung des Themas"

ordered_docs=(
    # ... bestehende Einträge ...
    "neue-dokumentation.md"
)
```

### Schritt 3: Tabelle aktualisieren

```bash
# Python (empfohlen)
python3 scripts/update_readme_docs.py

# ODER Bash
./scripts/update-readme-docs.sh
```

### Schritt 4: Committen

```bash
git add docs/neue-dokumentation.md scripts/ README.md
git commit -m "docs: Neue Dokumentation hinzugefügt"
git push
```

## 🔧 Funktionsweise

### Gemeinsame Utilities (`scripts/lib/readme_utils.py`)

- Enthält zentrale Pfadkonstanten (`PROJECT_ROOT`, `README_FILE`, `DOCS_DIR`)
- Bündelt wiederverwendbare README-Operationen (lesen, schreiben, Abschnitt ersetzen)
- Vermeidet doppelte Regex-/Pfadlogik in mehreren Skripten
- Erleichtert Erweiterungen für weitere README-Automationen

### Python-Skript (`update_readme_docs.py`)

1. **Liest Metadaten:** Definierte Liste von Dokumentationen mit Namen, Bereich, Beschreibung
2. **Prüft Existenz:** Nur vorhandene Dateien werden in die Tabelle aufgenommen
3. **Generiert Tabelle:** Markdown-Tabelle mit Links und Beschreibungen
4. **Aktualisiert README:** Ersetzt Abschnitt zwischen "## Inhalt / Lernpfade" und nächstem "##"

### GitHub Action (`update-docs-table.yml`)

1. **Trigger:** Bei Push in `docs/*.md` oder manuell
2. **Checkout:** Repository auschecken
3. **Python Setup:** Python 3.11 installieren
4. **Skript ausführen:** `update_readme_docs.py` starten
5. **Commit:** Änderungen automatisch committen (falls vorhanden)

## 📊 Reihenfolge der Dokumentationen

Die Reihenfolge in der Tabelle entspricht dem **empfohlenen Lernpfad**:

1. Grundlagen (HTML, CSS)
2. Layout & Design (Box-Modell, Flexbox, Grid, Responsive)
3. Medien (Bilder, Galerien)
4. Interaktivität (Formulare, JavaScript)
5. Frameworks (React)
6. Backend (Python, PHP, Datenbank)
7. Erweitert (Algorithmen, Testing)
8. Rechtliche Aspekte (privat, kommerziell, KI-Inhalte)

**Wichtig:** Bei neuen Dokumentationen die Reihenfolge in den Metadaten beachten!

### ⚖️ Kapitel: Rechtliche Aspekte (privat/kommerziell + KI-Inhalte)

Dieses Kapitel soll Schüler:innen befähigen, rechtliche Risiken früh zu erkennen und ihre Projekte sauber zu dokumentieren.

#### Theoretische Basis (was man wissen muss)

1. **Privat vs. kommerziell:**
   - Private Nutzung im Unterricht ist oft weniger risikobehaftet, aber nicht automatisch frei von Rechten Dritter.
   - Bei Veröffentlichung, Wettbewerb, Schulwebsite oder Kundenbezug gelten strengere Anforderungen wie bei kommerzieller Nutzung.
2. **Urheberrecht & Lizenzen:**
   - Texte, Bilder, Icons, Audio, Videos, Code-Snippets und Fonts sind in der Regel urheberrechtlich geschützt.
   - Erlaubt ist nur Nutzung mit passender Lizenz (z. B. MIT, Apache-2.0, CC BY, CC BY-SA) und unter Einhaltung der Lizenzbedingungen.
3. **Persönlichkeitsrechte & Datenschutz:**
   - Fotos/Videos mit Personen nur mit Einwilligung.
   - Personenbezogene Daten (Name, E-Mail, IP, Umfrageantworten) nur mit klarer Zweckbindung und möglichst sparsam erfassen.
4. **KI-generierte Inhalte:**
   - KI-Ergebnisse sind rechtlich nicht automatisch „frei nutzbar“.
   - Prompts, Trainingsdatenherkunft und Tool-Nutzungsbedingungen können Auswirkungen auf die Weiterverwendung haben.

#### Praktische Umsetzung im Schülerprojekt

1. **Asset-Check vor Nutzung:** Quelle, Lizenz, Autor:in und Nutzungszweck für jedes externe Asset dokumentieren.
2. **Lizenzkompatibilität prüfen:** Bei Mischung mehrerer Quellen auf kompatible Lizenzen achten.
3. **Quellen sichtbar machen:** Abschnitt „Quellen & Lizenzen“ in der Projekt-README ergänzen.
4. **KI-Nutzung transparent machen:** Eigene Sektion „Einsatz von KI“ mit Umfang und Zweck der KI-Unterstützung anlegen.
5. **Eigenleistung kennzeichnen:** Klar trennen zwischen eigener Arbeit, adaptiertem Material und KI-Vorschlägen.

#### Mindeststandard für die Dokumentation (empfohlen)

In jeder Projekt-README sollten mindestens diese Blöcke enthalten sein:

- **Nutzungsart:** privat/unterrichtlich oder öffentlich/kommerziell geplant
- **Externe Ressourcen:** Tabelle mit Quelle, Lizenz, Link, Verwendungsort
- **KI-Deklaration:** eingesetztes Tool, Einsatzbereich, menschliche Prüfung/Anpassung
- **Zitation:** vollständige Quellenangaben mit Abrufdatum

Beispiel für eine kurze KI-Deklaration:

```md
## Einsatz von KI

- Tool: ChatGPT (GPT-5.3-Codex)
- Einsatz: Ideenfindung, Code-Refactoring, Textkorrektur
- Eigenleistung: Implementierung, Tests und Endentscheidung durch das Team
- Prüfung: Alle KI-Vorschläge wurden fachlich und rechtlich geprüft
```

Beispiel für Quellen/Zitation:

```md
## Quellen & Lizenzen

1. Foto "Campus" von Max Mustermann, Quelle: https://example.org/campus, Lizenz: CC BY 4.0, Abruf: 23.02.2026
2. Icon-Set "UI Pack", Quelle: https://example.org/icons, Lizenz: MIT, Verwendet in: navbar/footer
```

Hinweis: Dieses Kapitel vermittelt praxisnahe Orientierung für den Unterricht und ersetzt keine individuelle Rechtsberatung im Einzelfall.

## ⚙️ Konfiguration

### Pfade ändern

Falls Ordnerstruktur geändert wird:

**Python-Skript:**

```python
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
README_FILE = PROJECT_ROOT / "README.md"
```

**GitHub Action:**

```yaml
paths:
  - "docs/*.md" # Überwachter Pfad
```

### Tabellen-Format anpassen

**Header ändern:**

```python
table_lines = [
    "## Inhalt / Lernpfade",
    "",
    "| Bereich | Datei / Link | Kurzbeschreibung |",
    "|--------|---------------|------------------|",
]
```

**Zeilen-Format:**

```python
table_lines.append(f"| {bereich} | {link} | {beschreibung} |")
```

## 🐛 Troubleshooting

### Fehler: "README.md nicht gefunden"

**Lösung:**

```bash
# Prüfe aktuelles Verzeichnis
pwd

# Muss im Projekt-Root sein
cd /workspaces/web-project-dynamic

# Skript erneut ausführen
python3 scripts/update_readme_docs.py
```

### Fehler: "docs/ Ordner nicht gefunden"

**Lösung:**

```bash
# Prüfe ob docs/ existiert
ls -la docs/

# Falls nicht, erstellen
mkdir -p docs
```

### Tabelle wird nicht aktualisiert

**Mögliche Ursachen:**

1. Datei nicht in Metadaten aufgeführt
2. Markdown-Header falsch (muss exakt "## Inhalt / Lernpfade" sein)
3. Regex-Pattern greift nicht

**Lösung:**

```bash
# Backup erstellen
cp README.md README.md.backup

# Skript mit Debug-Modus ausführen
python3 -v scripts/update_readme_docs.py
```

### GitHub Action schlägt fehl

**Prüfen:**

1. Workflow-Permissions in GitHub Settings → Actions → General
2. Muss "Read and write permissions" haben
3. Log in GitHub → Actions → Failed workflow ansehen

## 📚 Weiterführende Informationen

- **Python Pathlib:** [docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
- **GitHub Actions:** [docs.github.com/actions](https://docs.github.com/en/actions)
- **Regex in Python:** [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)

## ✅ Checkliste: Neue Doku hinzufügen

- [ ] `.md`-Datei in `docs/` erstellt
- [ ] Inhalt geschrieben (mit Markdown-Formatierung)
- [ ] Metadaten in `scripts/update_readme_docs.py` ergänzt
- [ ] Reihenfolge im Lernpfad beachtet
- [ ] Skript lokal getestet: `python3 scripts/update_readme_docs.py`
- [ ] README.md überprüft (Tabelle aktualisiert?)
- [ ] Committet und gepusht
- [ ] GitHub Action erfolgreich? (Actions-Tab prüfen)

---

**Tipp:** Bei Fragen oder Problemen ein Issue auf GitHub erstellen!
