# 📋 Handbook Migration - Implementierungs-Checkliste

**Status:** ✅ Migration-Bundles vorbereitet  
**Datum:** 22.03.2026  
**Quelle:** web-project-dynamic (Template)  
**Ziele:** edu-code-lab-core, edu-code-lab-courses

---

## ✅ Phase 1: Vorbereitung (ABGESCHLOSSEN)

- [x] Dateien klassifiziert (core vs. courses)
- [x] Migrations-Skript erstellt: `scripts/migrate_handbook.py`
- [x] Migration-Bundles generiert: `migration_output/`
- [x] Template-README aktualisiert: `docs/handbook/README.md`
- [x] Migration-Report erstellt: `migration_output/MIGRATION_REPORT.json`

**Bundles ready:**

```
✓ core_handbook/     (11 Dateien) → edu-code-lab-core/docs/handbook/
✓ courses_handbook/  (3 Dateien)  → edu-code-lab-courses/docs/handbook/
```

---

## 📦 Phase 2: Transfer in Core-Repo

**Repository:** `edu-code-lab-core`

### Schritt 1: Ordner vorbereiten

```bash
mkdir -p docs/handbook
```

### Schritt 2: Core-Dateien kopieren

```bash
# Von web-project-dynamic
cp -r migration_output/core_handbook/* ../edu-code-lab-core/docs/handbook/
```

### Schritt 3: Links validieren & anpassen

| Datei                    | Link-Check                                                  | Status  |
| ------------------------ | ----------------------------------------------------------- | ------- |
| SETUP_REPOSITORIES.md    | Verlinkt auf `COURSES_THEMENPLAN.md` → Link zu courses-Repo | ⏳ TODO |
| ROADMAP_CORE.md          | Verlinkt auf `ROADMAP_COURSES.md` → Link zu courses-Repo    | ⏳ TODO |
| DOCS_NAVIGATION_RULES.md | `../../scripts/config/docs_navigation_rules.json`           | ⏳ TODO |
| Alle Dateien             | Relative Links zu `scripts/`                                | ⏳ TODO |

### Schritt 4: Commit & Push

```bash
cd edu-code-lab-core
git add docs/handbook/
git commit -m "docs: add handbook documentation from template

- ARCHITECTURE.md: technische Validierung
- BACKUP_STRATEGY.md: Sicherungsstrategie
- REPO_GOVERNANCE.md: Admin-Governance
- ROADMAP_CORE.md: technischer Marschplan
- ... (11 weitere)

Migration source: web-project-dynamic/migration_output/core_handbook/
"
git push origin main
```

---

## 📚 Phase 3: Transfer in Courses-Repo

**Repository:** `edu-code-lab-courses`

### Schritt 1: Ordner vorbereiten

```bash
mkdir -p docs/handbook
```

### Schritt 2: Courses-Dateien kopieren

```bash
# Von web-project-dynamic
cp -r migration_output/courses_handbook/* ../edu-code-lab-courses/docs/handbook/
```

### Schritt 3: Links validieren & anpassen

| Datei                           | Link-Check                          | Status  |
| ------------------------------- | ----------------------------------- | ------- |
| ROADMAP_COURSES.md              | Verlinkt auf `core/ROADMAP_CORE.md` | ⏳ TODO |
| COURSES_THEMENPLAN.md           | Selbstständig, keine ext. Links     | ✓ OK    |
| GITHUB_CLASSROOM_AUTOGRADING.md | Selbstständig                       | ✓ OK    |

### Schritt 4: Commit & Push

```bash
cd edu-code-lab-courses
git add docs/handbook/
git commit -m "docs: add handbook documentation from template

- COURSES_THEMENPLAN.md: Themenstruktur & Lernziele
- ROADMAP_COURSES.md: didaktischer Marschplan
- GITHUB_CLASSROOM_AUTOGRADING.md: Autograding-Integration

Migration source: web-project-dynamic/migration_output/courses_handbook/
"
git push origin main
```

---

## 🔗 Phase 4: Cross-Repo Links aktualisieren

Nach beiden Transfers:

### In `edu-code-lab-core/docs/handbook/SETUP_REPOSITORIES.md`:

```markdown
# Siehe auch

- [edu-code-lab-courses/docs/handbook/COURSES_THEMENPLAN.md](https://github.com/ChristineJanischek/edu-code-lab-courses/blob/main/docs/handbook/COURSES_THEMENPLAN.md)
- [edu-code-lab-courses/docs/handbook/ROADMAP_COURSES.md](https://github.com/ChristineJanischek/edu-code-lab-courses/blob/main/docs/handbook/ROADMAP_COURSES.md)
```

### In `edu-code-lab-courses/docs/handbook/ROADMAP_COURSES.md`:

```markdown
# Abhängigkeiten

- [edu-code-lab-core/docs/handbook/ROADMAP_CORE.md](https://github.com/ChristineJanischek/edu-code-lab-core/blob/main/docs/handbook/ROADMAP_CORE.md)
```

---

## ✨ Phase 5: Template-Repo finalisieren

**Zurück in:** `web-project-dynamic`

### Schritt 1: Migration-Output archivieren (optional)

```bash
# Falls Migration erfolgreich:
rm -rf migration_output/

# Oder archivieren für Dokumentation:
tar -czf migration_archive.tar.gz migration_output/
git add migration_archive.tar.gz
```

### Schritt 2: Commit

```bash
git add docs/handbook/README.md scripts/migrate_handbook.py
git commit -m "docs: add handbook migration index and automation

- docs/handbook/README.md: index to core/courses repos
- scripts/migrate_handbook.py: automated migration tool

Handbook files distributed to:
- edu-code-lab-core/docs/handbook/ (11 files)
- edu-code-lab-courses/docs/handbook/ (3 files)
"
git push origin main
```

---

## 🧪 Validierungs-Checkliste

Nach allen Transfers:

- [ ] `edu-code-lab-core/docs/handbook/` enthält alle 11 Core-Dateien
- [ ] `edu-code-lab-courses/docs/handbook/` enthält alle 3 Courses-Dateien
- [ ] Alle relativen Links funktionieren (zu `scripts/`, etc.)
- [ ] Cross-Repo Links validiert (mit vollständigen GitHub URLs)
- [ ] README.md in allen Repos aktualisiert
- [ ] Migration-Dokumente archiviert
- [ ] Alle Commits gepusht

---

## 📞 Unterstützung

**Wenn etwas schiefgeht:**

1. Migration-Report prüfen: `migration_output/MIGRATION_REPORT.json`
2. Original-Bundles sind erhalten in `migration_output/`
3. Skript neu ausführen: `python3 scripts/migrate_handbook.py --dry-run`
4. Dateien einzeln validieren: `ls -la migration_output/core_handbook/`

---

**Erstellt:** 22.03.2026 21:47  
**Tool:** `scripts/migrate_handbook.py`
