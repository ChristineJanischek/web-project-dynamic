# CI-Setup für Exam-System Validierung

Dieses Dokument erklärt die Continuous Integration (CI) Validierung des Exam-Systems.

## 🔍 Überblick

Das Exam-System wird automatisch geprüft auf:

- ✅ Mindestens 4 Varianten pro Theme/Sprache
- ✅ Konsistenz zwischen Aufgaben und Lösungen
- ✅ Keine identischen Aufgabenstellungen zwischen Varianten
- ✅ Gültige Punkte-Summen (25 Punkte)
- ✅ Aktuelle Wissensdatenbank (Fingerprints)

## 🚀 Lokales Setup (Pre-Commit Hook)

### Installation

```bash
# 1. pre-commit installieren (einmalig)
pip install pre-commit

# 2. Hooks aktivieren
pre-commit install

# 3. (Optional) Existierende Commits prüfen
pre-commit run --all-files
```

### Workflow

Beim `git commit`:

1. Hook führt `validate_exams.py --write-knowledge-base` aus
2. Falls Fehler: Commit wird blockiert, Fehler angezeigt
3. Falls OK: Commit geht durch, Knowledge-Base aktualisiert

### Manuell prüfen

```bash
# Alle Dateien prüfen
python3 scripts/validate_exams.py

# Mit Duplikat-Check + Know ledge-Base-Update
python3 scripts/validate_exams.py --write-knowledge-base

# Nur eine Sprache
python3 scripts/validate_exams.py --language php --verbose
```

## 🐙 Entferntes Setup (GitHub Actions)

### Automatische Checks bei Push/PR

Die Datei `.github/workflows/validate-exams.yml` definiert:

| Event        | Trigger                 | Action                              |
| ------------ | ----------------------- | ----------------------------------- |
| Push         | Branch `main`/`develop` | Validierung + Knowledge-Base-Update |
| Pull Request | Gegen `main`/`develop`  | Validierung (kein Auto-Commit)      |

### Ergebnis

✅ **Erfolg**: All Checks bestanden → Merge erlaubt
❌ **Fehler**: Validierung fehlgeschlagen → Merge blockiert

## 📋 Best Practices

### 1. Neue Variante erstellen

```bash
# 1. Datei schreiben
nano docs/programmierung/grundlagen/exams/php/basics/exam_v7.md

# 2. Lösungen schreiben
nano docs/programmierung/grundlagen/exams/php/basics/solutions_v7.md

# 3. Lokal testen
python3 scripts/validate_exams.py --language php --verbose

# 4. Commit + Push
git add docs/programmierung/grundlagen/exams/php/basics/exam_v7.md
git add docs/programmierung/grundlagen/exams/php/basics/solutions_v7.md
git commit -m "feat: add PHP Basics v7"
# Pre-Commit Hook wird automatisch ausgeführt
```

### 2. Fehler beheben

Wenn Pre-Commit Hook blockiert:

```bash
# 1. Fehler lesen
# "Identische Aufgabenstellung erkannt (Aufgabe A): exam_v5.md, exam_v7.md"

# 2. Aufgabe anpassen
nano docs/programmierung/grundlagen/exams/php/basics/exam_v7.md

# 3. Erneut testen
python3 scripts/validate_exams.py --language php

# 4. Commit erneut versuchen
git commit -m "feat: add PHP Basics v7"
```

### 3. Knowledge-Base aktualisieren

```bash
# Wird automatisch bei jedem Commit aktualisiert
# Aber bei Bedarf manuell:
python3 scripts/validate_exams.py --write-knowledge-base

# Dann committen
git add docs/programmierung/grundlagen/exams/shared/variation_knowledge_base.json
git commit -m "chore: update variation_knowledge_base.json"
```

## 🔧 Konfiguration

### `.pre-commit-config.yaml`

Definiert lokale Hooks:

- Hook ID: `validate-exams`
- Trigger: Änderungen in `docs/programmierung/grundlagen/exams/**/*.md`
- Aktion: `validate_exams.py --write-knowledge-base`

### `.github/workflows/validate-exams.yml`

Definiert GitHub Actions:

- Trigger: Push/PR auf `main`/`develop`
- Python: 3.9
- Aktion: Validierung + Knowledge-Base-Update (nur auf main auto-commit)

## 📖 Dokumentation

- **[ARCHITECTURE.md](../docs/programmierung/grundlagen/exams/ARCHITECTURE.md)** – System-Design
- **[README.md](../docs/programmierung/grundlagen/exams/README.md)** – Benutzer-Dokumentation
- **[validate_exams.py](validate_exams.py)** – Validierungs-Script
- **[variation_knowledge_base.json](../docs/programmierung/grundlagen/exams/shared/variation_knowledge_base.json)** – Aufgaben-Fingerprints

## ⚠️ Troubleshooting

### Pre-Commit Hook ist nicht installiert

```bash
pre-commit install
```

### Hook wird nicht ausgeführt

```bash
# Skip Hook (nur im Notfall!)
git commit --no-verify -m "message"

# Oder: Hook manuell ausführen
pre-commit run --all-files
```

### Validierung schlägt fehl, aber sollte nicht

```bash
# Verbose Modus
python3 scripts/validate_exams.py --verbose

# Nur eine Sprache
python3 scripts/validate_exams.py --language php --verbose
```

### Knowledge-Base ist veraltet

```bash
python3 scripts/validate_exams.py --write-knowledge-base
git add docs/programmierung/grundlagen/exams/shared/variation_knowledge_base.json
git commit -m "chore: update knowledge-base"
```

## 🎯 Ziel

Das CI-Setup stellt sicher:

- ✅ Keine Duplikate zwischen Varianten
- ✅ Alle Examen sind konsistent strukturiert
- ✅ Knowledge-Base ist immer aktuell
- ✅ Main-Branch bleibt qualitativ hochwertig

---

**Letzte Aktualisierung:** 2026-03-12
