# GitHub Classroom Autograding - Schritt-für-Schritt Anleitung

## 📋 Voraussetzungen

- ✅ GitHub Classroom Assignment erstellt
- ✅ Template Repository (web-project-dynamic) verknüpft
- ✅ Workflows im Repository vorhanden (`.github/workflows/`)

---

## 🎯 Autograding Tests hinzufügen

### Schritt 1: Assignment öffnen

1. Gehe zu **GitHub Classroom**: https://classroom.github.com
2. Wähle dein **Classroom** aus
3. Klicke auf die **Assignment** (z.B. "Web Project - Version 1")
4. Klicke auf **"Edit assignment"** (oben rechts)

---

### Schritt 2: Autograding aktivieren

1. Scrolle zum Abschnitt **"Grading and feedback"**
2. Aktiviere ✓ **"Add autograding tests"**
3. Klicke auf **"Add test"** Button

---

### Schritt 3: Test-Typ auswählen

GitHub Classroom bietet 3 Test-Typen:

#### **Option A: Run Command Test** (Empfohlen für HTML-Validierung)

**Verwendung:** Shell-Befehle ausführen (npm scripts, Python, etc.)

**Konfiguration:**

| Feld | Wert | Beschreibung |
|------|------|--------------|
| **Test name** | `HTML Validierung` | Name des Tests (sichtbar für Schüler) |
| **Setup command** | `npm install -g html-validate` | Installiert Dependencies |
| **Run command** | `html-validate version1/aufgabe/index.html` | Führt Test aus |
| **Timeout** | `10` | Maximale Laufzeit in Minuten |
| **Points** | `10` | Punkte bei erfolgreichem Test |

**Beispiel-Commands:**

```bash
# HTML Validierung
Setup: npm install -g html-validate
Run: html-validate version*/aufgabe/index.html

# CSS Validierung
Setup: npm install -g stylelint stylelint-config-standard
Run: stylelint version*/aufgabe/css/style.css

# JavaScript Lint
Setup: npm install -g eslint
Run: eslint version*/aufgabe/js/script.js

# Custom Script
Setup: chmod +x scripts/validate.sh
Run: ./scripts/validate.sh
```

---

#### **Option B: I/O Test** (Für Programme mit Ein-/Ausgabe)

**Verwendung:** Testet Programme, die Input lesen und Output produzieren

**Konfiguration:**

| Feld | Wert |
|------|------|
| **Test name** | `Python Script Test` |
| **Setup command** | `pip install -r requirements.txt` |
| **Run command** | `python3 script.py` |
| **Input** | `test input data` |
| **Expected output** | `expected result` |
| **Comparison** | `exact` / `included` / `regex` |
| **Timeout** | `5` |
| **Points** | `15` |

---

#### **Option C: Repository Test** (Für Datei-/Ordner-Checks)

**Verwendung:** Prüft, ob bestimmte Dateien/Ordner existieren

**Konfiguration:**

| Feld | Wert |
|------|------|
| **Test name** | `Dateistruktur Check` |
| **File** | `version1/aufgabe/index.html` |
| **Points** | `5` |

**Mehrere Dateien testen:**
- Klicke auf **"Add test"** für jede Datei
- Vergib Teilpunkte pro Datei

---

### Schritt 4: Multiple Tests hinzufügen

Für ein vollständiges Web-Projekt:

#### Test 1: HTML Validierung (10 Punkte)
```
Test name: HTML Validierung
Setup: npm install -g html-validate
Run: html-validate version1/aufgabe/index.html
Points: 10
```

#### Test 2: CSS Syntax Check (10 Punkte)
```
Test name: CSS Syntax
Setup: npm install -g stylelint stylelint-config-standard
Run: stylelint version1/aufgabe/css/style.css
Points: 10
```

#### Test 3: Dateien vorhanden (5 Punkte)
```
Test name: index.html existiert
File: version1/aufgabe/index.html
Points: 5
```

#### Test 4: Accessibility Check (15 Punkte)
```
Test name: Accessibility (pa11y)
Setup: npm install -g pa11y-ci
Run: pa11y-ci version1/aufgabe/index.html
Points: 15
```

#### Test 5: Lighthouse Performance (20 Punkte)
```
Test name: Lighthouse
Setup: npm install -g @lhci/cli
Run: lhci autorun --config=.lighthouserc.json
Points: 20
```

---

### Schritt 5: Gesamtpunktzahl festlegen

1. Scrolle zu **"Total points"**
2. Das System berechnet automatisch: `10 + 10 + 5 + 15 + 20 = 60`
3. Optional: Setze **"Passing grade"** (z.B. `40` für 2/3 der Punkte)

---

### Schritt 6: Feedback-Optionen konfigurieren

| Option | Empfehlung | Beschreibung |
|--------|------------|--------------|
| **Enable feedback pull requests** | ✓ | Erstellt automatisch PR mit Feedback |
| **Update existing feedback** | ✓ | Aktualisiert PR bei neuem Push |
| **Pull request template** | Leer lassen | Nutzt Default-Template |

---

### Schritt 7: Speichern & Testen

1. Klicke **"Update assignment"** (unten)
2. Teste mit einem **Test-Student-Account**:
   - Akzeptiere die Assignment
   - Push Code zu deinem Test-Repo
   - Prüfe **Actions**-Tab für Test-Ergebnisse

---

## 🔧 Fortgeschrittene Konfiguration

### Custom Grading Script

Erstelle `scripts/grade.sh`:

```bash
#!/bin/bash

SCORE=0

# Test 1: HTML vorhanden (10 Punkte)
if [ -f "version1/aufgabe/index.html" ]; then
    SCORE=$((SCORE + 10))
    echo "✅ HTML gefunden (+10)"
else
    echo "❌ HTML fehlt"
fi

# Test 2: CSS vorhanden (10 Punkte)
if [ -f "version1/aufgabe/css/style.css" ]; then
    SCORE=$((SCORE + 10))
    echo "✅ CSS gefunden (+10)"
else
    echo "❌ CSS fehlt"
fi

# Test 3: Semantisches HTML (20 Punkte)
if grep -q "<header>" version1/aufgabe/index.html && \
   grep -q "<main>" version1/aufgabe/index.html && \
   grep -q "<footer>" version1/aufgabe/index.html; then
    SCORE=$((SCORE + 20))
    echo "✅ Semantische Elemente vorhanden (+20)"
else
    echo "❌ Semantische Elemente fehlen"
fi

# Test 4: Meta-Tags (10 Punkte)
if grep -q 'charset="UTF-8"' version1/aufgabe/index.html && \
   grep -q 'viewport' version1/aufgabe/index.html; then
    SCORE=$((SCORE + 10))
    echo "✅ Meta-Tags korrekt (+10)"
else
    echo "❌ Meta-Tags fehlen"
fi

echo ""
echo "==========================="
echo "Gesamtpunktzahl: $SCORE / 50"
echo "==========================="

# Exit mit 0 wenn bestanden (>= 30 Punkte)
if [ $SCORE -ge 30 ]; then
    exit 0
else
    exit 1
fi
```

**In Classroom:**
```
Setup: chmod +x scripts/grade.sh
Run: ./scripts/grade.sh
Points: 50
```

---

### GitHub Actions Workflow nutzen

Wenn bereits Workflows vorhanden sind:

**In Classroom:**
```
Test name: Alle Workflows
Setup: # leer
Run: echo "Workflows laufen automatisch"
Points: 0
```

Die Workflows laufen automatisch, Classroom zeigt nur Status.

---

## 📊 Bewertungsmatrix für Web-Projekt

### Version 1: HTML & CSS Basics (60 Punkte)

| Test | Punkte | Command |
|------|--------|---------|
| Dateistruktur | 10 | Repository Test (index.html, style.css) |
| HTML Validierung | 15 | `html-validate version1/aufgabe/index.html` |
| CSS Syntax | 10 | `stylelint version1/aufgabe/css/style.css` |
| Semantisches HTML | 15 | Custom Script (grep für header, main, footer) |
| Meta-Tags | 10 | Custom Script (charset, viewport) |

### Version 2: Responsive Design (80 Punkte)

| Test | Punkte | Command |
|------|--------|---------|
| Media Queries | 20 | Custom Script (grep für @media) |
| Flexbox/Grid | 20 | Custom Script (grep für display: flex/grid) |
| Mobile Navigation | 15 | Custom Script (Hamburger-Menü vorhanden) |
| Lighthouse Mobile | 25 | `lhci autorun --preset=mobile` |

### Version 3: Vollständiges Projekt (100 Punkte)

| Test | Punkte | Command |
|------|--------|---------|
| Phase 1: Konzept | 30 | Custom Script (names.json, personas vorhanden) |
| Phase 2: HTML | 20 | html-validate + semantic checks |
| Phase 2: CSS | 20 | stylelint + responsive checks |
| Phase 2: JS | 15 | eslint + funktionale Tests |
| Accessibility | 15 | pa11y-ci |

---

## ⚠️ Häufige Fehler

### Problem 1: "Setup command failed"

**Lösung:**
```bash
# Statt:
npm install -g html-validate

# Verwende:
npm install html-validate && npx html-validate ...
```

### Problem 2: "Timeout"

**Lösung:** Erhöhe Timeout auf 10-15 Minuten für komplexe Tests

### Problem 3: "Test passed but students see failure"

**Lösung:** Prüfe Exit-Code des Scripts (muss 0 sein bei Erfolg)

```bash
# Am Ende des Scripts:
exit 0  # Erfolg
# oder
exit 1  # Fehler
```

---

## 🎓 Best Practices

### 1. **Starte einfach**
- Beginne mit 2-3 Tests
- Erweitere schrittweise

### 2. **Klare Test-Namen**
- ✅ "HTML Validierung (W3C)"
- ❌ "Test 1"

### 3. **Sinnvolle Punktzahl**
- Wichtige Tests: 15-20 Punkte
- Basis-Checks: 5-10 Punkte

### 4. **Feedback aktivieren**
- Pull Requests zeigen Details
- Schüler sehen, was falsch ist

### 5. **Testbar lokal**
- Schüler sollten Tests lokal ausführen können
- Dokumentiere Commands in README

---

## 📝 Beispiel-Konfiguration für dein Projekt

```yaml
# Empfohlene Tests für "Web Project Dynamic"

Version 1 Assignment:
├── Test 1: Dateistruktur (10 Punkte)
│   └── Files: index.html, css/style.css
├── Test 2: HTML Validierung (15 Punkte)
│   └── html-validate version1/aufgabe/index.html
├── Test 3: CSS Syntax (10 Punkte)
│   └── stylelint version1/aufgabe/css/style.css
├── Test 4: Semantisches HTML (15 Punkte)
│   └── ./scripts/check-semantic.sh
└── Test 5: Meta-Tags (10 Punkte)
    └── ./scripts/check-meta.sh

Total: 60 Punkte
Passing: 40 Punkte (66%)
```

---

## 🚀 Nächste Schritte

1. ✅ Erstelle Assignment in Classroom
2. ✅ Füge 2-3 einfache Tests hinzu
3. ✅ Teste mit eigenem Account
4. ✅ Dokumentiere Tests in Assignment-README
5. ✅ Verteile Assignment an Schüler

---

**Erstellt:** Dezember 2025  
**Für:** GitHub Classroom Autograding  
**Projekt:** web-project-dynamic
