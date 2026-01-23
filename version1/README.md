# Version 1: HTML-Grundgerüst und erste CSS-Formatierung

## 🎯 Lernziele
Nach dieser Aufgabe kannst du:
- Ein korrektes HTML5-Grundgerüst erstellen
- Semantische Seitenstrukturelemente verwenden
- Eine externe CSS-Datei einbinden
- Grundlegende CSS-Formatierungen anwenden

## 📋 Aufgabenstellung

### Aufgabe 1: HTML-Grundgerüst erstellen (30 Min)

Erstelle eine Datei `index.html` mit einem vollständigen HTML5-Grundgerüst:

**Anforderungen:**
- [ ] `<!DOCTYPE html>` Deklaration
- [ ] `<html>` Element mit deutscher Sprache (`lang="de"`)
- [ ] `<head>` Bereich mit:
  - [ ] Zeichensatz UTF-8
  - [ ] Viewport Meta-Tag für Responsive Design
  - [ ] Aussagekräftiger Titel (z.B. "Meine erste Webseite")
- [ ] Leerer `<body>` Bereich

**Hilfe:**
- Lies `docs/html-grundgeruest.md`
- Schaue dir die Beispiele an

---

### Aufgabe 2: Seitenstrukturelemente implementieren (45 Min)

Füge im `<body>` folgende semantische Strukturelemente hinzu:

**Anforderungen:**
- [ ] `<header>` mit:
  - [ ] Hauptüberschrift `<h1>` mit deinem Namen oder "Meine Webseite"
  - [ ] Navigation `<nav>` mit 3 Links (Home, Über mich, Kontakt)
  
- [ ] `<main>` mit:
  - [ ] Mindestens 2 `<section>` Bereiche:
    - **Section 1**: Begrüßung mit `<h2>` und einem Absatz `<p>`
    - **Section 2**: Hobbys/Interessen mit `<h2>` und einer Liste `<ul>` mit 3-5 Punkten
  
- [ ] `<footer>` mit:
  - [ ] Copyright-Hinweis (z.B. "© 2025 Mein Name")

**Hilfe:**
- Lies `docs/seitenstrukturelemente.md`
- Semantische Tags helfen Suchmaschinen und Screenreadern!

---

### Aufgabe 3: CSS-Datei einbinden (15 Min)

**Anforderungen:**
- [ ] Erstelle einen Ordner `css/`
- [ ] Erstelle darin eine Datei `style.css`
- [ ] Verlinke die CSS-Datei im `<head>` deiner HTML-Datei mit:
  ```html
  <link rel="stylesheet" href="css/style.css">
  ```
- [ ] Teste, ob die Verlinkung funktioniert (füge z.B. `body { background: lightblue; }` in die CSS-Datei ein)

**Hilfe:**
- Lies `docs/css-einbinden.md`
- Achte auf den korrekten Pfad!

---

### Aufgabe 4: Erste CSS-Formatierungen (45 Min)

Formatiere deine Webseite in der `css/style.css`:

**Anforderungen:**

**Allgemein:**
- [ ] `body`: Schriftart (z.B. Arial), Textfarbe, Hintergrundfarbe
- [ ] Maximale Breite für bessere Lesbarkeit (z.B. `max-width: 800px; margin: 0 auto;`)

**Header:**
- [ ] Hintergrundfarbe für den `<header>`
- [ ] Textfarbe für die Überschrift `<h1>`
- [ ] Padding/Abstand oben und unten

**Navigation:**
- [ ] Links (`<a>`) ohne Unterstreichung
- [ ] Hover-Effekt (andere Farbe beim Drüberfahren)
- [ ] Abstände zwischen den Links

**Main-Bereich:**
- [ ] Überschriften `<h2>` in einer anderen Farbe
- [ ] Absätze `<p>` mit Zeilenhöhe für bessere Lesbarkeit (z.B. `line-height: 1.6`)
- [ ] Liste `<ul>` formatieren

**Footer:**
- [ ] Hintergrundfarbe
- [ ] Text zentriert
- [ ] Padding oben und unten

**Hilfe:**
- Lies `docs/css-basis.md` und `docs/css-formatierung.md`
- Experimentiere mit Farben und Abständen!

---

## ✅ Checkliste zum Abschluss

- [ ] HTML validiert (keine Fehler in den DevTools)
- [ ] CSS wird korrekt geladen
- [ ] Seite sieht ansprechend aus
- [ ] Alle semantischen Elemente verwendet
- [ ] Code ist sauber eingerückt und lesbar
- [ ] Änderungen mit Git committed (`git add .` & `git commit -m "feat: Version 1 abgeschlossen"`)

**📖 Git-Hilfe:** Lies [`docs/git-versionsmanagement.md`](../docs/git-versionsmanagement.md) für Git-Grundlagen!

---

## 🧪 Testen

1. Öffne `index.html` im Browser
2. Drücke F12 → Console: Keine Fehler?
3. Drücke F12 → Network: style.css wird geladen?
4. Ändere etwas im CSS, speichere und lade neu (F5)

---

## 💡 Tipps

- **Klein anfangen**: Erst HTML, dann CSS
- **Oft testen**: Nach jedem Schritt im Browser ansehen
- **DevTools nutzen**: Rechtsklick → Untersuchen
- **Farben**: Nutze [coolors.co](https://coolors.co) oder HTML-Farbnamen
- **Fragen?**: Schaue in die `docs/` Dateien oder frage deine KI!

---

## 📁 Erwartete Dateistruktur

```
version1/
├── aufgabe/
│   ├── index.html
│   └── css/
│       └── style.css
```

Viel Erfolg! 🚀
