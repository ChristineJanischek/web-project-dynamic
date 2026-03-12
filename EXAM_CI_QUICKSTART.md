# CI/CD Setup für Exam-System – Quickstart

> **5 Minuten Einrichtung für automatische Validierung beim Commit**

## Installation

```bash
# 1. Into Scripts-Verzeichnis
cd /workspaces/web-project-dynamic

# 2. Setup-Script ausführen
bash scripts/setup_exam_ci.sh

# Fertig! Pre-Commit Hooks sind aktiviert
```

## Was wurde installiert?

| Komponente          | Zweck                 | Trigger                      |
| ------------------- | --------------------- | ---------------------------- |
| **Pre-Commit Hook** | Lokale Validierung    | Vor jedem `git commit`       |
| **GitHub Actions**  | Remote Validierung    | Push/PR auf main/develop     |
| **Knowledge-Base**  | Aufgaben-Fingerprints | Auto-Update nach Validierung |

## Erste Verwendung

### 1. Test: Neue Variante erstellen

```bash
# Datei erstellen
cp docs/programmierung/grundlagen/exams/php/basics/exam_v4.md \
   docs/programmierung/grundlagen/exams/php/basics/exam_v5.md

# Anpassen (neue Aufgaben, nicht identisch!)
nano docs/programmierung/grundlagen/exams/php/basics/exam_v5.md

# Lösungen kopieren und anpassen
cp docs/programmierung/grundlagen/exams/php/basics/solutions_v4.md \
   docs/programmierung/grundlagen/exams/php/basics/solutions_v5.md
nano docs/programmierung/grundlagen/exams/php/basics/solutions_v5.md
```

### 2. Committen

```bash
git add docs/programmierung/grundlagen/exams/php/basics/exam_v5.md
git add docs/programmierung/grundlagen/exams/php/basics/solutions_v5.md
git commit -m "feat: add PHP Basics v5"
```

**Was passiert:**

```
↓
Pre-Commit Hook wird ausgeführt
  1. Validierung Struktur
  2. Duplikat-Check (Aufgabe A-D)
  3. Konsistenz Exam ↔ Solutions
  4. Update Wissensdatenbank
↓
✓ Erfolgreich → Commit geht durch
✗ Fehler → Commit blockiert → Fehler beheben → Erneut versuchen
```

### 3. Push

```bash
git push
```

**Was passiert:**

```
↓
GitHub Actions wird ausgeführt
  1. Validierung (wie Pre-Commit)
  2. Auto-Commit Knowledge-Base (nur auf main)
↓
✓ Alle Checks bestanden → Merge erlaubt
✗ Fehler → Merge blockiert → In PR erneut versuchen
```

## Hilfreiche Befehle

```bash
# Validierung manuell ausführen
python3 scripts/validate_exams.py

# Mit ausführlichem Output
python3 scripts/validate_exams.py --verbose

# Nur eine Sprache
python3 scripts/validate_exams.py --language php

# Knowledge-Base aktualisieren
python3 scripts/validate_exams.py --write-knowledge-base

# Pre-Commit Hook umgehen (nur Notfall!)
git commit --no-verify -m "message"

# Alle Dateien mit Hook prüfen
pre-commit run --all-files
```

## Troubleshooting

### Hook wird nicht ausgeführt

```bash
# Neu installieren
pre-commit install

# Oder manuell prüfen
pre-commit run --all-files
```

### Validierung schlägt fehl

```bash
# Detaillierte Meldung
python3 scripts/validate_exams.py --verbose

# Spezifische Sprache
python3 scripts/validate_exams.py --language javascript --verbose
```

### Knowledge-Base ist veraltet

```bash
python3 scripts/validate_exams.py --write-knowledge-base
git add docs/programmierung/grundlagen/exams/shared/variation_knowledge_base.json
git commit -m "chore: update knowledge-base"
```

## Dokumentation

- **Vollständige Anleitung:** [scripts/README_CI_SETUP.md](README_CI_SETUP.md)
- **Exam-System:** [docs/programmierung/grundlagen/exams/README.md](../docs/programmierung/grundlagen/exams/README.md)
- **Validierungs-Script:** [scripts/validate_exams.py](validate_exams.py)

---

**Fertig!** 🎉 Die Automatisierung ist einsatzbereit.
