# Automatisches Update der Dokumentations-Tabelle

Dieses Projekt enthält Automatisierungsskripte, um die Dokumentations-Tabelle in `README.md` automatisch zu aktualisieren.

## 📋 Übersicht

Wenn neue `.md`-Dateien zu `docs/` hinzugefügt werden, muss die Tabelle unter **"## Inhalt / Lernpfade"** in der Haupt-README aktualisiert werden.

## 🤖 Automatische Methoden

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

**Wichtig:** Bei neuen Dokumentationen die Reihenfolge in den Metadaten beachten!

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
  - 'docs/*.md'  # Überwachter Pfad
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
