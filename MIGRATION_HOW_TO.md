# 🚀 Handbook Migration - PRAKTISCHE ANLEITUNG

**Ziel:** Handbook-Dateien von `web-project-dynamic` → `edu-code-lab-core` + `edu-code-lab-courses`

---

## 📋 Voraussetzung

```bash
# Du bist im web-project-dynamic Verzeichnis
cd /workspaces/web-project-dynamic

# Migration schon durchgeführt?
ls migration_output/core_handbook/
ls migration_output/courses_handbook/
```

---

## 1️⃣ CORE-Repo - Dateien übertragen

### Option A: Falls du noch kein core-Repo hast

```bash
# Gehe eine Ebene rauf
cd ..

# Clone das core-Repo (oder erstelle es)
git clone https://github.com/ChristineJanischek/edu-code-lab-core.git

# Falls nicht vorhanden, erstelle das Verzeichnis
cd edu-code-lab-core
mkdir -p docs/handbook
cd ..
```

### Option B: Falls du das core-Repo schon hast

```bash
cd edu-code-lab-core
```

### ✅ Schritt 1: Dateien kopieren

```bash
# Von web-project-dynamic Bundle → core-Repo
cp -r ../web-project-dynamic/migration_output/core_handbook/* docs/handbook/

# Prüfung: 11 Dateien sollten jetzt da sein
ls -la docs/handbook/ | wc -l
# → sollte ~15 sein (inkl. . und ..)
```

### ✅ Schritt 2: Links validieren

```bash
# Zurück nach web-project-dynamic für Link-Checker
cd ../web-project-dynamic

# Link-Validator für core ausführen
python3 scripts/update_handbook_links.py --target core --mode validate

# Falls Fehler → Dateien in core anpassen (manuell oder mit --fix)
```

### ✅ Schritt 3: Commiten & Pushen

```bash
cd ../edu-code-lab-core

# Status prüfen
git status

# Alle Dateien hinzufügen
git add docs/handbook/

# Commit mit Nachricht
git commit -m "docs: add handbook documentation from template

- ARCHITECTURE.md: technische Validierung
- BACKUP_STRATEGY.md: Backup-/Git-Bundle-Strategie
- REPO_GOVERNANCE.md: Branch-Protection & Admin-Governance
- ROADMAP_CORE.md: technischer Phasenplan
- SETUP_REPOSITORIES.md: Erstkonfiguration
- DOCS_NAVIGATION_RULES.md: Navigations-Standards
- TEMPLATE_SYNC.md: Template-Update-Workflow
- TEMPLATE_UPDATE_STRATEGY.md: Auto-Sync-Überlegungen
- WORKSPACE_LIVE_TEST_SETUP.md: VS Code Extension Setup
- QUICKSTART_LIVE_SERVER.md: Schüler-Onboarding
- architektur-prinzipien.md: Lernmaterial

Source: web-project-dynamic/migration_output/core_handbook/"

# Pushen
git push origin main
```

---

## 2️⃣ COURSES-Repo - Dateien übertragen

### Option A: Falls du noch kein courses-Repo hast

```bash
# Gehe eine Ebene rauf
cd ..

# Clone das courses-Repo
git clone https://github.com/ChristineJanischek/edu-code-lab-courses.git

# Falls nicht vorhanden, erstelle das Verzeichnis
cd edu-code-lab-courses
mkdir -p docs/handbook
cd ..
```

### Option B: Falls du das courses-Repo schon hast

```bash
cd edu-code-lab-courses
```

### ✅ Schritt 1: Dateien kopieren

```bash
# Von web-project-dynamic Bundle → courses-Repo
cp -r ../web-project-dynamic/migration_output/courses_handbook/* docs/handbook/

# Prüfung: 3 Dateien sollten jetzt da sein
ls -la docs/handbook/
```

### ✅ Schritt 2: Links validieren

```bash
# Zurück nach web-project-dynamic für Link-Checker
cd ../web-project-dynamic

# Link-Validator für courses ausführen
python3 scripts/update_handbook_links.py --target courses --mode validate

# Falls Fehler → in courses anpassen
```

### ✅ Schritt 3: Commiten & Pushen

```bash
cd ../edu-code-lab-courses

git add docs/handbook/

git commit -m "docs: add handbook documentation from template

- COURSES_THEMENPLAN.md: Themenstruktur & Lernziele
- ROADMAP_COURSES.md: didaktischer Marschplan
- GITHUB_CLASSROOM_AUTOGRADING.md: Autograding-Integration

Source: web-project-dynamic/migration_output/courses_handbook/"

git push origin main
```

---

## 3️⃣ Zurück in Template-Repo: Finalisieren

```bash
cd ../web-project-dynamic

# Optional: Migration-Output archivieren
tar -czf migration_archive.tar.gz migration_output/

# Committen
git add docs/handbook/README.md scripts/migrate_handbook.py scripts/update_handbook_links.py migration_archive.tar.gz

git commit -m "docs: migrate handbook files to core & courses repos

- Added handbook distribution index (docs/handbook/README.md)
- Added migration automation tools (scripts/migrate_handbook.py, update_handbook_links.py)
- Archived migration bundles (migration_archive.tar.gz)

Core: 11 files → edu-code-lab-core/docs/handbook/
Courses: 3 files → edu-code-lab-courses/docs/handbook/"

git push origin main
```

---

## ✅ Validierungs-Checkliste (Nach allen Transfers)

```bash
# 1. CORE-Repo: 11 Dateien prüfen
cd ../edu-code-lab-core
ls docs/handbook/ | wc -l
# → sollte 11 sein

# 2. COURSES-Repo: 3 Dateien prüfen
cd ../edu-code-lab-courses
ls docs/handbook/ | wc -l
# → sollte 3 sein

# 3. Links funktionieren?
grep -r "COURSES_THEMENPLAN" ../edu-code-lab-core/docs/handbook/
grep -r "ROADMAP_CORE" ../edu-code-lab-courses/docs/handbook/

# 4. Alle Repos gepusht?
cd ../edu-code-lab-core && git log -1 --oneline
cd ../edu-code-lab-courses && git log -1 --oneline
cd ../web-project-dynamic && git log -1 --oneline
```

---

## 🐛 Wenn etwas schiefgeht:

```bash
# 1. Migration-Bundles neugenerieren
cd /workspaces/web-project-dynamic
python3 scripts/migrate_handbook.py

# 2. Links prüfen & automatisch fixen
python3 scripts/update_handbook_links.py --target core --mode fix

# 3. Dateien einzeln prüfen
head -20 migration_output/core_handbook/ARCHITECTURE.md
head -20 migration_output/courses_handbook/COURSES_THEMENPLAN.md
```

---

**Fertig! 🎉 Die Handbook ist nun verteilt auf core + courses Repos**
