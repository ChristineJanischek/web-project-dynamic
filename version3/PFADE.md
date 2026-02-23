# Pfadstruktur & Verlinkungen - Version 3

Dieses Dokument erklärt die Pfadangaben in allen Markdown-Dateien von Version 3.

## 📁 Verzeichnisstruktur

```
version3/
├── README.md                                    # Haupt-Übersicht
├── aufgabe/
│   ├── README.md                                # Aufgabenstellung (Hauptdokument)
│   ├── concept/                                 # Mockups & Assets
│   │   ├── Mockups_MiFa.odp
│   │   ├── Logo_farbig.jpg
│   │   ├── Startbild.png
│   │   └── ic_launcher.png
│   ├── phase1-concept/                          # Phase 1 Arbeitsbereich
│   │   ├── AUFGABEN.md                         # Schritt-für-Schritt Anleitung Phase 1
│   │   ├── results/                            # Ergebnisse (names.json etc.)
│   │   └── templates/                          # Vorlagen
│   │       ├── persona-template.md
│   │       ├── corporate-design-template.md
│   │       └── wireframe-vorlage.svg
│   ├── phase2-implementation/                   # Phase 2 Arbeitsbereich
│   │   ├── index-starter.html
│   │   ├── css/
│   │   │   └── style-starter.css
│   │   └── js/
│   │       └── script-starter.js
│   ├── surveys/                                 # Namensfindung Surveys
│   │   ├── name_survey/
│   │   │   ├── form.html
│   │   │   └── process.py
│   │   └── app_names/
│   │       ├── form.html
│   │       └── process.py
│   └── reference/                               # Referenz-Implementation
│       └── complete-example/
│           ├── index.html
│           ├── css/style.css
│           └── js/script.js
└── loesung/                                     # Musterlösung (Lehrende)
    ├── README.md                                # Begründungen & Bewertung
    ├── loesung_phase1.md                       # Phase 1 Konzept ausgearbeitet
    ├── index.html
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🔗 Verlinkungen zwischen Dateien

### Von `version3/aufgabe/README.md` aus:

**Interne Verweise (innerhalb version3/aufgabe/):**

- `phase1-concept/AUFGABEN.md` ✅
- `phase2-implementation/index-starter.html` ✅
- `concept/Mockups_MiFa.odp` ✅
- `concept/images/Logo_farbig.jpg` ✅
- `images/` Ordner ✅

**Dokumentations-Verweise (nach ../../docs/):**

- `../../docs/zielgruppenanalyse.md` ✅
- `../../docs/konzeption-webdesign.md` ✅
- `../../docs/corporate-design.md` ✅
- `../../docs/seitenstrukturelemente.md` ✅
- `../../docs/js.md` ✅
- `../../docs/formulare.md` ✅
- `../../docs/bilder-grafiken.md` ✅
- `../../docs/responsive-design.md` ✅
- `../../docs/flexible-layouts.md` ✅

### Von `version3/aufgabe/phase1-concept/AUFGABEN.md` aus:

**Survey-Formulare (ein Ordner höher, dann in surveys/):**

- `../surveys/name_survey/form.html` ✅
- `../surveys/app_names/form.html` ✅

**Ergebnisse (im selben Ordner):**

- `results/names.json` ✅
- `results/firmenname_<datum>.json` ✅

**Git-Befehle (vollständiger Pfad vom Repo-Root):**

- `git add version3/aufgabe/phase1-concept/results/` ✅

**Python-Skripte (Terminal-Befehle vom Repo-Root):**

```bash
cd version3/aufgabe/surveys/name_survey
python3 process.py
```

### Von `version3/loesung/loesung_phase1.md` aus:

**Referenzen zu Aufgaben-Assets:**

- `../aufgabe/concept/images/Logo_farbig.jpg` ✅

### Von `version3/loesung/README.md` aus:

**Interne Struktur (relativ zum loesung/ Ordner):**

- `index.html` ✅
- `css/style.css` ✅
- `js/script.js` ✅
- `loesung_phase1.md` ✅

**Deployment-Pfad:**

- `http://localhost:8000/version3/loesung/` ✅

## ⚠️ Häufige Fehler vermeiden

### 1. Relative Pfade von phase1-concept/ aus

❌ **Falsch:**

```markdown
Öffne `surveys/name_survey/form.html`
```

✅ **Korrekt:**

```markdown
Öffne `../surveys/name_survey/form.html`
```

**Warum?** Die Datei liegt in `version3/aufgabe/phase1-concept/AUFGABEN.md`, daher:

- `../` → hoch nach `version3/aufgabe/`
- `surveys/` → rein in `surveys/`

### 2. Git-Pfade immer vollständig

❌ **Falsch:**

```bash
git add phase1-concept/results/
```

✅ **Korrekt:**

```bash
git add version3/aufgabe/phase1-concept/results/
```

**Warum?** Git-Befehle werden vom Repository-Root ausgeführt.

### 3. Dokumentations-Links von version3/aufgabe/ aus

❌ **Falsch:**

```markdown
[Zielgruppenanalyse](../docs/konzeption/zielgruppenanalyse.md)
```

✅ **Korrekt:**

```markdown
[Zielgruppenanalyse](../docs/konzeption/zielgruppenanalyse.md)
```

**Warum?** Von `version3/aufgabe/` aus:

- `../../` → hoch nach Repository-Root
- `docs/` → rein in `docs/`

### 4. Assets von Musterlösung referenzieren

❌ **Falsch:**

```markdown
Logo: `images/Logo_farbig.jpg`
```

✅ **Korrekt:**

```markdown
Logo: `../aufgabe/concept/images/Logo_farbig.jpg`
```

**Warum?** Die Musterlösung liegt in `version3/loesung/`, Assets sind in `version3/aufgabe/concept/`.

## 📋 Checkliste: Pfade prüfen

Beim Erstellen neuer Markdown-Dateien:

- [ ] Bin ich im richtigen Verzeichnis?
- [ ] Wie viele Ebenen muss ich hoch (`../`)?
- [ ] Verweise ich auf Ordner im gleichen Verzeichnis oder woanders?
- [ ] Sind Git-Pfade vom Repository-Root aus angegeben?
- [ ] Funktioniert der Link, wenn ich im Browser teste?

## 🧪 Testen von Links

```bash
# Prüfe alle Markdown-Links (benötigt markdown-link-check)
npm install -g markdown-link-check
find version3 -name "*.md" -exec markdown-link-check {} \;
```

## ✅ Status

Alle Pfadangaben in folgenden Dateien geprüft und korrigiert:

- ✅ `version3/aufgabe/README.md`
- ✅ `version3/aufgabe/phase1-concept/AUFGABEN.md`
- ✅ `version3/loesung/README.md`
- ✅ `version3/loesung/loesung_phase1.md`
- ✅ `version3/README.md`

---

**Stand:** 30. November 2025  
**Geprüft:** Alle Markdown-Dateien in version3/
