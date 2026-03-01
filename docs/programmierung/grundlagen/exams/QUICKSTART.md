# ⚡ Quick Start: Täglich

> **Öffne diese Datei jeden Morgen** – 2 Minuten Orientierung

---

## ☀️ Morgen-Routine

```bash
# 1. Repository aktualisieren
cd /workspaces/web-project-dynamic
git pull origin main

# 2. System-Status prüfen
python3 scripts/validate_exams.py

# 3. Heute-Datei öffnen
cat docs/programmierung/grundlagen/exams/HEUTE.md
```

---

## 📄 Wichtige Dateien

| Datei                                          | Zweck                | Wann öffnen?         |
| ---------------------------------------------- | -------------------- | -------------------- |
| **[HEUTE.md](HEUTE.md)**                       | Tagesplan            | ⭐ Jeden Morgen      |
| **[MARSCHPLAN.md](MARSCHPLAN.md)**             | Gesamtplan (81 Tage) | Montags + bei Fragen |
| **[ARCHITECTURE.md](ARCHITECTURE.md)**         | Technische Doku      | Bei Design-Fragen    |
| **[README.md](README.md)**                     | Benutzer-Doku        | Für Überblick        |
| **[shared/rubrics.json](shared/rubrics.json)** | Bewertungsrubriken   | Beim Exam-Schreiben  |

---

## 🎯 Aktueller Stand

**Phase:** 1 ✅ | 2 ⏳ (Start: 03.03.)  
**Woche:** 1 (Datenstrukturen)  
**Nächster Meilenstein:** 09.03. (Datenstrukturen complete)

---

## ⚡ Shortcuts

### Validierung

```bash
# Alle Exams
python3 scripts/validate_exams.py

# Nur eine Sprache
python3 scripts/validate_exams.py --language javascript

# Verbose Output
python3 scripts/validate_exams.py --verbose
```

### Git-Workflow

```bash
# Status prüfen
git status

# Staged Files ansehen
git diff --cached

# Commit (Conventional Commits)
git commit -m "feat(exams): add [sprache] [thema] [variant]"
git commit -m "fix(exams): correct points in [file]"
git commit -m "docs(exams): update [readme/architecture]"

# Push
git push origin main
```

### Exam erstellen

```bash
# Verzeichnis vorbereiten
mkdir -p docs/programmierung/grundlagen/exams/[sprache]/[thema]

# Template kopieren
cp shared/templates/exam_template.md \
   [sprache]/[thema]/exam.md

# Varianten erstellen
cp [sprache]/[thema]/exam.md \
   [sprache]/[thema]/exam_v2.md
# ... anpassen ...
```

---

## 🔍 Debug-Checkliste

**Bei Problemen:**

1. ✅ Validierung laufen lassen → Fehler lesen
2. ✅ Git Status prüfen → Ungespeicherte Änderungen?
3. ✅ Datei-Benennung korrekt? (`exam.md`, `exam_v2.md`, etc.)
4. ✅ Punktesumme = 25.0?
5. ✅ Markdown-Syntax korrekt?

---

## 📊 Progress-Übersicht

### Phase 1: ✅ Abgeschlossen (01.03.2026)

- Struktur, Migration, Validierung, Doku

### Phase 2: ⏳ In Planung (03.03.–29.03.2026)

```
Woche 1: Datenstrukturen     [        ]  0%
Woche 2: Funktionen          [        ]  0%
Woche 3: Kontrollstrukturen  [        ]  0%
Woche 4: Dateien + DB        [        ]  0%
```

### Phase 3: ⏳ Geplant (31.03.–26.04.2026)

- Export (JSON, HTML, PDF), Generator

### Phase 4: ⏳ Geplant (28.04.–21.06.2026)

- Online-System, API, Dashboard

---

## 💪 Motivation

> "Der beste Weg, die Zukunft vorherzusagen, ist, sie zu erschaffen."  
> – **Peter Drucker**

**Du baust etwas Großartiges:**

- ✅ Skalierbares System (3 Sprachen, 6+ Themen)
- ✅ Wiederverwendbar (4 Varianten pro Thema)
- ✅ Wartbar (DRY, SOLID, zentrale Rubriken)
- ✅ Erweiterbar (neue Sprachen in <1 Tag)
- ✅ Professionell (Buch-Stil, Validierung, CI/CD)

**Heute ist ein guter Tag zum Coden!** 🚀

---

**Letzte Aktualisierung:** 01.03.2026
