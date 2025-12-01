# Version 2: Box-Modell & Responsive Layout

**Status:** 🚧 In Planung

## Lernziele

Nach Abschluss dieser Version kannst du:
- ✅ Das CSS Box-Modell verstehen und anwenden
- ✅ Margin, Padding und Border gezielt einsetzen
- ✅ Responsive Layouts mit Media Queries erstellen
- ✅ Mobile Navigation (Hamburger-Menü) implementieren
- ✅ Flexbox für flexible Layouts nutzen

## Voraussetzungen

- Abgeschlossene **Version 1** (HTML-Grundgerüst & CSS-Basics)
- Grundkenntnisse in HTML und CSS
- Verständnis von Selektoren und Eigenschaften

## Aufgabenstellung

### Teil 1: Box-Modell verstehen

📖 **Theorie:** [`docs/box-modell.md`](../docs/box-modell.md)

1. **Erstelle drei verschiedene Boxen** mit unterschiedlichen:
   - Padding-Werten
   - Border-Stilen
   - Margin-Abständen

2. **Experimentiere mit `box-sizing`**:
   - Eine Box mit `content-box`
   - Eine Box mit `border-box`
   - Vergleiche die Unterschiede

**Implementierungsbeispiele:** Siehe Abschnitt "Praktisches Beispiel" in `box-modell.md`

### Teil 2: Responsive Layout

📖 **Theorie:** [`docs/responsive-design.md`](../docs/responsive-design.md) & [`docs/flexible-layouts.md`](../docs/flexible-layouts.md)

1. **Desktop-Layout** (> 1024px):
   - 3-spaltiges Grid
   - Breite Navigation oben
   
2. **Tablet-Layout** (768px - 1024px):
   - 2-spaltiges Grid
   - Kompaktere Navigation

3. **Mobile-Layout** (< 768px):
   - 1-spaltig
   - Hamburger-Menü

**Implementierungsbeispiele:** 
- Grid-Layouts: `flexible-layouts.md` → Beispiel 1-4
- Media Queries: `responsive-design.md` → Abschnitt 2

### Teil 3: Mobile Navigation

📖 **Theorie:** [`docs/responsive-design.md`](../docs/responsive-design.md) (Abschnitt 5) & [`docs/js.md`](../docs/js.md)

Implementiere ein funktionierendes Hamburger-Menü mit:
- Toggle-Button (☰)
- Slide-in Animation
- JavaScript für Interaktivität

**Implementierungsbeispiele:**
- Vollständiges HTML/CSS/JS: `responsive-design.md` → Abschnitt 5 "Mobile Navigation"
- JavaScript Toggle-Funktion: `js.md` → DOM-Manipulation

## Zeitaufwand

- **Teil 1**: 1-2 Stunden
- **Teil 2**: 2-3 Stunden
- **Teil 3**: 1-2 Stunden
- **Gesamt**: Ca. 4-7 Stunden

---

## 🛠️ Schritt-für-Schritt Implementierungsanleitung

> **💡 Wichtig:** Diese Anleitung verweist auf Theorie-Dokumente im `docs/` Ordner. Lies die empfohlenen Abschnitte, um die Konzepte besser zu verstehen!

### Vorbereitung

**📖 Vor dem Start empfohlen:**
- [`docs/box-modell.md`](../docs/box-modell.md) - Grundlagen des CSS Box-Modells
- [`docs/responsive-design.md`](../docs/responsive-design.md) - Mobile-First Ansatz und Breakpoints
- [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) - Flexbox und CSS Grid Übersicht

1. **Workspace vorbereiten**
   - Öffne den Ordner `version2/aufgabe/` in deinem Editor
   - Stelle sicher, dass die Dateistruktur vollständig ist:
     - `index.html`
     - `css/style.css`
     - `js/script.js`
     - `images/` (Ordner für Logo)

2. **Browser-Vorschau öffnen**
   - Öffne `index.html` im Browser
   - Öffne die Browser DevTools (F12)
   - Halte diese Ansicht während der Entwicklung offen

---

### Schritt 1: CSS Global Styles (30 Min)

**Ziel:** Box-Modell Grundlagen setzen und globale Styles definieren

#### Zu implementieren in `css/style.css`:

```css
* {
    box-sizing: border-box;  /* Wichtig für Box-Modell! */
    margin: 0;
    padding: 0;
}

body {
    background-color: #f4f4f4;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}
```

**✅ Testen:**
- Öffne DevTools → Tab "Computed"
- Wähle ein Element aus
- Prüfe: `box-sizing` sollte `border-box` sein
- Verändere Browserfenster → Container bleibt zentriert

**📖 Hinweis:** Lies [`docs/box-modell.md`](../docs/box-modell.md) Abschnitt 1-2 für Grundlagen zum Box-Modell

---

### Schritt 2: Header & Desktop Navigation (45 Min)

**Ziel:** Horizontale Navigation mit Flexbox erstellen

#### Zu implementieren in `css/style.css`:

```css
header {
    position: sticky;
    top: 0;
    z-index: 1000;
}

header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav {
    display: flex;
    gap: 30px;
}

.nav a {
    text-decoration: none;
    color: white;
    padding: 10px 15px;
    transition: background-color 0.3s ease;
}

.nav a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}
```

**✅ Testen:**
- Navigation sollte horizontal ausgerichtet sein
- Hover-Effekt auf Links funktioniert
- Header bleibt beim Scrollen oben (sticky)
- DevTools → Wähle `.nav` → Sollte `display: flex` zeigen

**📖 Hinweis:** Lies [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) Abschnitt über Flexbox und [`docs/css-basis.md`](../docs/css-basis.md) für CSS-Selektoren und Pseudo-Klassen (`:hover`)

---

### Schritt 3: Box-Modell Demonstrationen (60 Min)

**Ziel:** Unterschied zwischen `content-box` und `border-box` verstehen

#### Zu implementieren in `css/style.css`:

```css
.boxes {
    display: flex;
    gap: 30px;
    flex-wrap: wrap;
}

/* Box 1: content-box */
.box-1 {
    box-sizing: content-box;
    width: 200px;
    padding: 30px;
    border: 3px solid #52B788;
    margin: 20px;
}

/* Box 2: border-box */
.box-2 {
    box-sizing: border-box;
    width: 200px;
    padding: 30px;
    border: 3px dashed #2D6A4F;
    margin: 20px;
}

/* Box 3: Mit Effekten */
.box-3 {
    padding: 25px;
    border: 2px solid #2D6A4F;
    box-shadow: 0 4px 6px rgba(45, 106, 79, 0.15);
    border-radius: 16px;
}
```

**✅ Testen:**
- DevTools → Wähle `.box-1` → Tab "Computed"
- Scrolle zum "Box Model" Diagramm
- Vergleiche die **Gesamtbreite** von Box 1 vs. Box 2:
  - Box 1 (`content-box`): 200px + 60px (padding) + 6px (border) = **266px**
  - Box 2 (`border-box`): **200px** gesamt (Padding/Border inkludiert)
- Hover über Box 3 → Schatten sollte sich ändern

**📖 Theorie-Vertiefung:** Lies [`docs/box-modell.md`](../docs/box-modell.md) Abschnitt 3

---

### Schritt 4: Responsive Grid (60 Min)

**Ziel:** Grid-Layout, das sich an Bildschirmgröße anpasst

#### Zu implementieren in `css/style.css`:

```css
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.card {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Tablet */
@media (max-width: 1024px) {
    .grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Mobile */
@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}
```

**✅ Testen:**
- DevTools → Toggle Device Toolbar (Strg+Shift+M)
- Wähle verschiedene Geräte:
  - **Desktop (> 1024px)**: 3 Spalten
  - **Tablet (768-1024px)**: 2 Spalten
  - **Mobile (< 768px)**: 1 Spalte
- Verändere Viewport-Breite manuell → Grid passt sich an

**📖 Hinweis:** Lies [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) für CSS Grid und [`docs/responsive-design.md`](../docs/responsive-design.md) Abschnitt 2 für Media Queries

---

### Schritt 5: Hamburger-Menü CSS (45 Min)

**Ziel:** Mobile Navigation mit Slide-in Effekt

#### Zu implementieren in `css/style.css`:

```css
/* Hamburger Button */
.nav-toggle {
    display: none;  /* Versteckt auf Desktop */
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
}

.nav-toggle span {
    width: 25px;
    height: 3px;
    background-color: white;
    margin: 3px 0;
    transition: all 0.3s ease;
}

/* Mobile Media Query */
@media (max-width: 768px) {
    .nav-toggle {
        display: flex;
    }
    
    .nav {
        position: fixed;
        right: -100%;
        top: 0;
        height: 100vh;
        width: 70%;
        flex-direction: column;
        transition: right 0.3s ease;
    }
    
    .nav.active {
        right: 0;
    }
    
    /* Hamburger zu X Animation */
    .nav-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }
    
    .nav-toggle.active span:nth-child(2) {
        opacity: 0;
    }
    
    .nav-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -6px);
    }
}
```

**✅ Testen (vorerst ohne JavaScript):**
- DevTools → Mobile-Ansicht
- Hamburger-Button sollte sichtbar sein
- Desktop-Navigation sollte verschwunden sein
- Füge **manuell** die Klasse `active` zu `.nav` in den DevTools hinzu:
  - Rechtsklick auf `<nav>` → "Edit as HTML"
  - Ändere zu: `<nav class="nav active" id="mainNav">`
  - Navigation sollte von rechts einsliden

**📖 Hinweis:** Lies [`docs/responsive-design.md`](../docs/responsive-design.md) Abschnitt 5 für vollständiges Hamburger-Menü Beispiel und [`docs/css-formatierung.md`](../docs/css-formatierung.md) für Transitions und Animationen

---

### Schritt 6: JavaScript Toggle (30 Min)

**Ziel:** Hamburger-Menü interaktiv machen

#### Zu implementieren in `js/script.js`:

```javascript
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

// Toggle bei Klick auf Hamburger-Button
navToggle.addEventListener('click', function() {
    mainNav.classList.toggle('active');
    navToggle.classList.toggle('active');
});

// Menü schließen bei Klick auf Link
const navLinks = mainNav.querySelectorAll('a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        mainNav.classList.remove('active');
        navToggle.classList.remove('active');
    });
});
```

**✅ Testen:**
- DevTools → Mobile-Ansicht (< 768px)
- Klicke auf Hamburger-Button:
  - Navigation sollte von rechts einsliden
  - Hamburger sollte sich zu "X" transformieren
- Klicke auf einen Navigationslink:
  - Menü sollte sich schließen
- DevTools → Console → Sollte keine Fehler zeigen
- Teste auf echtem Smartphone (falls möglich)

**📖 Hinweis:** Lies [`docs/js.md`](../docs/js.md) → DOM-Manipulation, Event Listeners und querySelector für JavaScript-Grundlagen

---

### Schritt 7: Feinschliff & Optimierung (30 Min)

**Zusätzliche Features:**

```css
/* Hero Section responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}
```

**✅ Finaler Test:**
- [ ] Alle 3 Breakpoints funktionieren (Desktop, Tablet, Mobile)
- [ ] Box-Modell Boxen zeigen unterschiedliche Breiten
- [ ] Hamburger-Menü öffnet/schließt korrekt
- [ ] Navigation ist sticky
- [ ] Keine Fehler in der Konsole
- [ ] Teste in mehreren Browsern (Chrome, Firefox, Safari)

---

## 🧪 Test-Checkliste

### Desktop (> 1024px)
- [ ] Navigation horizontal mit 4 Links
- [ ] Grid zeigt 3 Spalten
- [ ] Hamburger-Button ist versteckt
- [ ] Sticky Header funktioniert

### Tablet (768px - 1024px)
- [ ] Grid zeigt 2 Spalten
- [ ] Navigation noch horizontal
- [ ] Responsive Bilder skalieren

### Mobile (< 768px)
- [ ] Grid zeigt 1 Spalte
- [ ] Hamburger-Button ist sichtbar
- [ ] Navigation slide-in von rechts
- [ ] Links schließen Menü beim Klick
- [ ] Hero-Text ist lesbar (kleinere Schrift)

### Box-Modell Verständnis
- [ ] Box 1 ist breiter als 200px (content-box)
- [ ] Box 2 ist genau 200px breit (border-box)
- [ ] Box 3 hat Schatten und Hover-Effekt

### Browser-Kompatibilität
- [ ] Chrome/Edge: Alles funktioniert
- [ ] Firefox: Grid und Flexbox korrekt
- [ ] Safari: Transitions smooth
- [ ] Mobile Browser: Touch funktioniert

---

## 💡 Debugging-Tipps

**Problem:** Navigation öffnet nicht
- Prüfe JavaScript-Konsole auf Fehler
- Überprüfe IDs: `navToggle` und `mainNav` müssen übereinstimmen
- Stelle sicher, dass `script.js` im HTML eingebunden ist

**Problem:** Grid zeigt nicht 3 Spalten
- DevTools → Wähle `.grid` → Sollte `display: grid` sein
- Prüfe ob Media Queries aktiv sind (DevTools → "Toggle Device Toolbar")

**Problem:** Box-Modell Boxen sehen gleich aus
- DevTools → "Computed" Tab → Box Model Diagramm
- Prüfe `box-sizing` Wert für jede Box

**Problem:** Sticky Header funktioniert nicht
- Manche Browser benötigen Fallback: `-webkit-sticky`
- Prüfe ob `top: 0` gesetzt ist

**Weitere Hilfe benötigt?**
- [`docs/testen.md`](../docs/testen.md) - Debugging-Strategien und Browser-Tools
- [`docs/css-basis.md`](../docs/css-basis.md) - CSS-Spezifität und Fehlersuche

---

## Hilfsmittel & Dokumentation

### Theorie & Konzepte
- [`docs/box-modell.md`](../docs/box-modell.md) - **Box-Modell** verstehen: Content, Padding, Border, Margin
- [`docs/responsive-design.md`](../docs/responsive-design.md) - **Responsive Design**: Media Queries, Breakpoints, Mobile-First
- [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) - **Flexbox & Grid**: Flexible Layouts mit praktischen Beispielen
- [`docs/css-basis.md`](../docs/css-basis.md) - CSS Grundlagen: Selektoren, Eigenschaften, Spezifität
- [`docs/css-einbinden.md`](../docs/css-einbinden.md) - CSS einbinden: Inline, Internal, External

### JavaScript & Interaktivität
- [`docs/js.md`](../docs/js.md) - JavaScript Grundlagen für interaktive Navigation

### Versionsverwaltung
- [`docs/git-versionsmanagement.md`](../docs/git-versionsmanagement.md) - Git & GitHub Workflow

### Zusätzliche Ressourcen
- [`shared-examples/`](../shared-examples/) - Vollständiges Beispiel zum Vergleich
- **Browser DevTools (F12)** - Box-Modell visualisieren & Grid/Flexbox anzeigen
- **Responsive Design Checker** - Testen auf verschiedenen Geräten

## Bewertungskriterien

- [ ] Korrektes Verständnis des Box-Modells
- [ ] Saubere Media Queries ohne Überlappungen
- [ ] Funktionierendes Hamburger-Menü
- [ ] Responsive Bilder (max-width: 100%)
- [ ] Code-Qualität und Kommentare
- [ ] Browser-Kompatibilität

## Bonus-Aufgaben (Optional)

- Smooth Scroll-Verhalten
- Sticky Navigation
- Dark Mode mit Media Query
- CSS Grid statt Flexbox

---

## Weiterführende Themen

Nach Abschluss dieser Version kannst du mit folgenden Themen weitermachen:

- [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md) - Responsive Bilder & `object-fit`
- [`docs/galerien.md`](../docs/galerien.md) - Bildgalerien mit Grid
- [`docs/formulare.md`](../docs/formulare.md) - Responsive Formulare gestalten
- [`docs/css-formatierung.md`](../docs/css-formatierung.md) - Typografie & Farben

---

**Viel Erfolg!** Bei Fragen schaue in die `docs/` oder frage deinen Mentor.
