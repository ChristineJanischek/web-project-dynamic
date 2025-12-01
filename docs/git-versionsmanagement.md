# Git & Versionsmanagement

## Was ist Versionsmanagement?

Versionsmanagement (Version Control) erlaubt es dir, Änderungen an deinem Code nachzuvollziehen, zu verschiedenen Versionen zurückzukehren und im Team zusammenzuarbeiten.

**Git** ist das weltweit meistgenutzte Versionskontrollsystem.  
**GitHub** ist eine Plattform, die Git-Repositories hostet und zusätzliche Features wie Issues, Pull Requests und Actions bietet.

---

## Grundbegriffe

| Begriff | Bedeutung |
|---------|-----------|
| **Repository (Repo)** | Ordner mit versionierter Projekthistorie |
| **Commit** | Gespeicherter Snapshot deiner Änderungen |
| **Branch** | Parallele Entwicklungslinie (z.B. `main`, `feature/login`) |
| **Clone** | Lokale Kopie eines Remote-Repos erstellen |
| **Pull** | Änderungen vom Remote-Repo holen |
| **Push** | Lokale Commits zum Remote-Repo hochladen |
| **Merge** | Zwei Branches zusammenführen |
| **Pull Request (PR)** | Anfrage, um Änderungen in einen Branch zu mergen |

---

## Grundlegende Git-Befehle

### 1. Repo klonen (einmalig)
```bash
git clone https://github.com/dein-username/dein-repo.git
cd dein-repo
```

### 2. Status prüfen
```bash
git status
```
Zeigt geänderte, neue und gelöschte Dateien.

### 3. Änderungen hinzufügen (Staging)
```bash
# Einzelne Datei
git add index.html

# Alle Dateien im aktuellen Ordner
git add .

# Alle geänderten Dateien
git add -A
```

### 4. Commit erstellen
```bash
git commit -m "feat: Hero-Section hinzugefügt"
```

**Commit-Message-Konventionen:**
- `feat:` – neues Feature
- `fix:` – Bugfix
- `docs:` – Dokumentation
- `style:` – Formatierung (keine Code-Änderung)
- `refactor:` – Code-Umstrukturierung
- `test:` – Tests hinzufügen
- `chore:` – Build/Config-Änderungen

### 5. Änderungen hochladen
```bash
git push
```

Falls dein Branch noch nicht remote existiert:
```bash
git push -u origin dein-branch-name
```

### 6. Änderungen vom Server holen
```bash
git pull
```

---

## Branching-Strategie für Schülerprojekte

### Main Branch
- `main` – Stabiler, funktionierender Code
- Nur durch Pull Requests aktualisiert

### Feature Branches
Für jede neue Aufgabe/Feature einen eigenen Branch erstellen:

```bash
# Branch erstellen und wechseln
git checkout -b feature/kontaktformular

# Änderungen machen, committen
git add .
git commit -m "feat: Kontaktformular mit Validierung"

# Push zum Remote
git push -u origin feature/kontaktformular
```

Auf GitHub: Pull Request erstellen → Review → Merge in `main`.

---

## Wichtige Workflows

### Workflow 1: Neue Aufgabe starten
```bash
# Aktuellen Stand holen
git checkout main
git pull

# Neuen Branch erstellen
git checkout -b feature/meine-aufgabe

# Arbeiten, committen, pushen
git add .
git commit -m "feat: Aufgabe XY implementiert"
git push -u origin feature/meine-aufgabe
```

### Workflow 2: Zwischenergebnisse sichern
```bash
# Häufig committen!
git add .
git commit -m "wip: Hero-Section Grundstruktur"
git push
```
**Tipp:** Auch unfertige Arbeit committen mit Präfix `wip:` (work in progress).

### Workflow 3: Fehler rückgängig machen

**Noch nicht committed:**
```bash
# Datei auf letzten Commit zurücksetzen
git checkout -- index.html

# Alle Änderungen verwerfen
git reset --hard
```

**Bereits committed:**
```bash
# Letzten Commit rückgängig (Änderungen bleiben)
git reset --soft HEAD~1

# Letzten Commit komplett löschen
git reset --hard HEAD~1
```

**Änderungen von Remote überschreiben:**
```bash
git fetch origin
git reset --hard origin/main
```

---

## .gitignore – Dateien ausschließen

Erstelle eine `.gitignore`-Datei im Repo-Root:

```gitignore
# Dependencies
node_modules/
venv/
__pycache__/

# Build Outputs
dist/
build/
*.pyc

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets
.env
*.key
```

---

## Merge-Konflikte lösen

Wenn zwei Branches dieselbe Datei ändern:

```bash
git merge feature/xyz
# CONFLICT in index.html
```

1. Öffne `index.html` im Editor
2. Suche nach Konfliktmarkern:
   ```html
   <<<<<<< HEAD
   <h1>Version A</h1>
   =======
   <h1>Version B</h1>
   >>>>>>> feature/xyz
   ```
3. Entscheide, welche Version behalten wird oder kombiniere beide
4. Lösche die Marker (`<<<<<<<`, `=======`, `>>>>>>>`)
5. Speichern und committen:
   ```bash
   git add index.html
   git commit -m "fix: merge conflict resolved"
   ```

---

## GitHub Classroom Integration

### Aufgaben-Workflow
1. **Assignment akzeptieren** → Repo wird automatisch erstellt
2. **Klonen:**
   ```bash
   git clone <dein-classroom-repo-url>
   cd <repo-name>
   ```
3. **Arbeiten in Branches:**
   ```bash
   git checkout -b aufgabe-1
   # ... Code schreiben ...
   git add .
   git commit -m "feat: Aufgabe 1 gelöst"
   git push -u origin aufgabe-1
   ```
4. **Pull Request erstellen** (auf GitHub)
5. **Feedback erhalten**, ggf. nachbessern
6. **Merge** durch Lehrkraft oder Automerge

### Autograding
- GitHub Classroom kann automatisch Tests ausführen
- Prüft z.B. HTML-Validität, CSS-Lint, JS-Syntax
- Ergebnisse sichtbar im Pull Request

---

## Best Practices

### ✅ Do's
- **Häufig committen** (kleine, logische Schritte)
- **Aussagekräftige Commit-Messages** schreiben
- **Vor dem Push testen** (HTML im Browser öffnen)
- **Branches für Features** nutzen
- **Pull Requests für Review** erstellen
- **.gitignore** pflegen

### ❌ Don'ts
- **Große Binärdateien** (Videos, große Bilder) committen
- **Passwörter/API-Keys** ins Repo pushen
- **Direkt in `main` pushen** ohne Review
- **`git push --force`** in shared Branches (überschreibt History)
- **Viele Dateien in einem Commit** mischen

---

## Nützliche Aliase

Füge in `~/.gitconfig` hinzu:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD --
    last = log -1 HEAD
    lg = log --oneline --graph --all
```

Dann kannst du z.B. `git st` statt `git status` nutzen.

---

## Weitere Ressourcen

- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **GitHub Docs:** https://docs.github.com
- **Interactive Git Tutorial:** https://learngitbranching.js.org
- **Git Visualizer:** https://git-school.github.io/visualizing-git/

---

## Häufige Fehler & Lösungen

### Problem: "Permission denied (publickey)"
**Lösung:** SSH-Key einrichten oder HTTPS verwenden:
```bash
git remote set-url origin https://github.com/username/repo.git
```

### Problem: "Your branch is behind 'origin/main'"
**Lösung:**
```bash
git pull --rebase
```

### Problem: "Merge conflict"
**Lösung:** Siehe Abschnitt "Merge-Konflikte lösen"

### Problem: Versehentlich große Datei committed
**Lösung:**
```bash
# Datei aus letztem Commit entfernen (noch nicht gepusht)
git rm --cached large-file.mp4
git commit --amend -m "fix: große Datei entfernt"

# Falls schon gepusht: BFG Repo-Cleaner nutzen
```

---

## Zusammenfassung

Git ist mächtig, aber die Basics sind einfach:

1. **Clone** → Projekt holen
2. **Branch** → Feature-Zweig erstellen
3. **Add** → Änderungen stagen
4. **Commit** → Snapshot speichern
5. **Push** → Hochladen
6. **Pull Request** → Review & Merge

**Tipp:** Übung macht den Meister! Probiere Befehle in einem Test-Repo aus, bevor du sie im echten Projekt nutzt.
