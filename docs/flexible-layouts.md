# Flexible Layouts mit Flexbox & CSS Grid

Moderne Webseiten benötigen **flexible Layouts**, die sich automatisch an verschiedene Bildschirmgrößen anpassen. Die beiden wichtigsten Techniken dafür sind **Flexbox** (eindimensional) und **CSS Grid** (zweidimensional).

---

## 1. Flexbox – Für eindimensionale Layouts

**Flexbox** ist perfekt für Layouts in **einer Richtung** (horizontal ODER vertikal).

### Wann Flexbox verwenden?

- **Navigation** (horizontal oder vertikal)
- **Buttons nebeneinander**
- **Zentrieren von Elementen**
- **Gleichmäßige Abstände zwischen Elementen**
- **Footer immer am Seitenende**

### Grundkonzept

```css
.container {
  display: flex;          /* Flex-Container aktivieren */
  flex-direction: row;    /* Richtung: row | column */
  justify-content: center;/* Horizontal: flex-start | flex-end | center | space-between | space-around */
  align-items: center;    /* Vertikal: flex-start | flex-end | center | stretch */
  gap: 20px;              /* Abstand zwischen Items */
}
```

---

## 2. Flexbox Beispiele

### Beispiel 1: Horizontale Navigation

#### HTML
```html
<nav class="nav-horizontal">
  <a href="#home">Home</a>
  <a href="#about">Über uns</a>
  <a href="#services">Services</a>
  <a href="#contact">Kontakt</a>
</nav>
```

#### CSS
```css
.nav-horizontal {
  display: flex;
  justify-content: space-between;  /* Gleichmäßig verteilt */
  align-items: center;
  background-color: #0b5cad;
  padding: 20px;
  gap: 15px;
}

.nav-horizontal a {
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  transition: background-color 0.3s;
}

.nav-horizontal a:hover {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
}

/* Responsive: Mobile vertikal */
@media (max-width: 768px) {
  .nav-horizontal {
    flex-direction: column;  /* Vertikal stapeln */
    align-items: stretch;     /* Volle Breite */
  }
}
```

---

### Beispiel 2: Zentrierte Card

#### HTML
```html
<div class="centered-card">
  <div class="card">
    <h2>Willkommen!</h2>
    <p>Diese Card ist perfekt zentriert.</p>
    <button>Mehr erfahren</button>
  </div>
</div>
```

#### CSS
```css
.centered-card {
  display: flex;
  justify-content: center;  /* Horizontal zentriert */
  align-items: center;      /* Vertikal zentriert */
  min-height: 100vh;        /* Volle Viewport-Höhe */
  background-color: #f0f0f0;
}

.card {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 400px;
}

.card button {
  margin-top: 20px;
  padding: 12px 24px;
  background-color: #0b5cad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
```

---

### Beispiel 3: Flexible Cards mit flex-wrap

#### HTML
```html
<div class="card-container">
  <div class="card-item">Card 1</div>
  <div class="card-item">Card 2</div>
  <div class="card-item">Card 3</div>
  <div class="card-item">Card 4</div>
  <div class="card-item">Card 5</div>
  <div class="card-item">Card 6</div>
</div>
```

#### CSS
```css
.card-container {
  display: flex;
  flex-wrap: wrap;           /* Umbruch erlauben */
  gap: 20px;                 /* Abstand zwischen Cards */
  padding: 20px;
}

.card-item {
  flex: 1 1 250px;           /* Wachsen | Schrumpfen | Basisbreite */
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 30px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Desktop: Mindestens 3 pro Reihe */
/* Tablet: 2 pro Reihe (automatisch) */
/* Mobile: 1 pro Reihe (automatisch) */
```

**Erklärung `flex: 1 1 250px;`**
- **1** = Darf wachsen (nimmt freien Platz ein)
- **1** = Darf schrumpfen (passt sich an)
- **250px** = Minimale Basisbreite

---

## 3. CSS Grid – Für zweidimensionale Layouts

**CSS Grid** ist perfekt für Layouts mit **Zeilen UND Spalten**.

### Wann CSS Grid verwenden?

- **Galerien** (Bilder in Reihen und Spalten)
- **Komplexe Layouts** (Header, Sidebar, Main, Footer)
- **Dashboard-Layouts**
- **Magazine-Layouts**

### Grundkonzept

```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;  /* 3 gleiche Spalten */
  grid-template-rows: auto;             /* Automatische Zeilenhöhe */
  gap: 20px;                            /* Abstand zwischen Zellen */
}
```

---

## 4. CSS Grid Beispiele

### Beispiel 1: Einfaches 3-Spalten Grid

#### HTML
```html
<div class="simple-grid">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>
</div>
```

#### CSS
```css
.simple-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 3 gleichgroße Spalten */
  gap: 20px;
  padding: 20px;
}

.grid-item {
  background-color: #0b5cad;
  color: white;
  padding: 40px;
  text-align: center;
  border-radius: 8px;
  font-size: 24px;
}

/* Tablet: 2 Spalten */
@media (max-width: 1024px) {
  .simple-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Mobile: 1 Spalte */
@media (max-width: 768px) {
  .simple-grid {
    grid-template-columns: 1fr;
  }
}
```

---

### Beispiel 2: Auto-Responsive Grid (ohne Media Queries!)

#### CSS
```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

.auto-grid-item {
  background-color: white;
  border: 2px solid #0b5cad;
  padding: 30px;
  border-radius: 8px;
  text-align: center;
}
```

**Was macht das?**
- `repeat(auto-fit, ...)` → So viele Spalten wie möglich
- `minmax(250px, 1fr)` → Mindestens 250px, maximal gleichmäßig
- **Automatisch responsive!** Passt sich ohne Media Queries an!

---

### Beispiel 3: Komplexes Layout (Holy Grail Layout)

#### HTML
```html
<div class="holy-grail">
  <header class="header">Header</header>
  <aside class="sidebar">Sidebar</aside>
  <main class="main">Main Content</main>
  <aside class="ads">Ads</aside>
  <footer class="footer">Footer</footer>
</div>
```

#### CSS
```css
.holy-grail {
  display: grid;
  grid-template-columns: 200px 1fr 200px;  /* Sidebar | Main | Ads */
  grid-template-rows: auto 1fr auto;       /* Header | Content | Footer */
  grid-template-areas:
    "header header header"
    "sidebar main ads"
    "footer footer footer";
  gap: 20px;
  min-height: 100vh;
}

.header {
  grid-area: header;
  background-color: #0b5cad;
  color: white;
  padding: 20px;
}

.sidebar {
  grid-area: sidebar;
  background-color: #f0f0f0;
  padding: 20px;
}

.main {
  grid-area: main;
  background-color: white;
  padding: 20px;
}

.ads {
  grid-area: ads;
  background-color: #f0f0f0;
  padding: 20px;
}

.footer {
  grid-area: footer;
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
}

/* Tablet: Sidebar unten */
@media (max-width: 1024px) {
  .holy-grail {
    grid-template-columns: 1fr 200px;
    grid-template-areas:
      "header header"
      "main ads"
      "sidebar sidebar"
      "footer footer";
  }
}

/* Mobile: Alles untereinander */
@media (max-width: 768px) {
  .holy-grail {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "ads"
      "footer";
  }
}
```

---

### Beispiel 4: Bildgalerie mit Grid

#### HTML
```html
<div class="gallery">
  <img src="images/bild1.jpg" alt="Bild 1">
  <img src="images/bild2.jpg" alt="Bild 2">
  <img src="images/bild3.jpg" alt="Bild 3">
  <img src="images/bild4.jpg" alt="Bild 4">
  <img src="images/bild5.jpg" alt="Bild 5">
  <img src="images/bild6.jpg" alt="Bild 6">
</div>
```

#### CSS
```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  padding: 20px;
}

.gallery img {
  width: 100%;
  height: 200px;
  object-fit: cover;      /* Bild beschneiden, Proportionen beibehalten */
  border-radius: 8px;
  transition: transform 0.3s;
}

.gallery img:hover {
  transform: scale(1.05);  /* Zoom-Effekt */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
```

---

## 5. Flexbox vs. Grid – Wann was?

| **Kriterium** | **Flexbox** | **CSS Grid** |
|--------------|------------|-------------|
| **Dimensionen** | 1D (Reihe ODER Spalte) | 2D (Reihen UND Spalten) |
| **Use Case** | Navigation, Buttons, Zentrieren | Layouts, Galerien, Dashboards |
| **Flexibilität** | Items passen sich dynamisch an | Präzise Kontrolle über Zellen |
| **Komplexität** | Einfacher für kleine Komponenten | Besser für komplexe Layouts |

**Faustregel:**
- **Flexbox** → Für Komponenten (Nav, Cards in Reihe)
- **Grid** → Für Seitenlayouts (Header, Main, Sidebar, Footer)

---

## 6. Kombinierte Beispiele

### Beispiel: Grid-Layout mit Flexbox-Navigation

#### HTML
```html
<div class="page-layout">
  <header class="header">
    <nav class="nav">
      <a href="#home">Home</a>
      <a href="#about">Über uns</a>
      <a href="#contact">Kontakt</a>
    </nav>
  </header>
  <main class="main-content">
    <h1>Hauptinhalt</h1>
    <p>Grid für Layout, Flexbox für Navigation!</p>
  </main>
  <footer class="footer">Footer</footer>
</div>
```

#### CSS
```css
/* Grid für Gesamtlayout */
.page-layout {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

/* Flexbox für Navigation */
.nav {
  display: flex;
  justify-content: space-around;
  background-color: #0b5cad;
  padding: 15px;
}

.nav a {
  color: white;
  text-decoration: none;
  padding: 10px 20px;
}

.main-content {
  padding: 40px;
  background-color: #f9f9f9;
}

.footer {
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
}
```

---

## 7. Praktische Tipps

### Gap statt Margin

❌ **Alt (umständlich):**
```css
.item {
  margin-right: 20px;
}
.item:last-child {
  margin-right: 0;  /* Letztes Element ohne Margin */
}
```

✅ **Neu (einfacher):**
```css
.container {
  display: flex;
  gap: 20px;  /* Automatischer Abstand zwischen allen Items */
}
```

### Zentrieren leicht gemacht

```css
/* Flexbox: Horizontal & Vertikal zentrieren */
.center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* Grid: Alternative */
.center-grid {
  display: grid;
  place-items: center;  /* Kurzform für align + justify */
  min-height: 100vh;
}
```

### Responsive ohne Media Queries

```css
/* Auto-responsive Grid */
.auto-responsive {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* Flex mit Umbruch */
.auto-flex {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.auto-flex > * {
  flex: 1 1 250px;  /* Mindestens 250px */
}
```

---

## 8. Häufige Fehler vermeiden

❌ **Fehler 1: Feste Breiten**
```css
.item {
  width: 300px;  /* Nicht flexibel! */
}
```

✅ **Besser:**
```css
.item {
  flex: 1 1 300px;  /* Flexibel, aber mindestens 300px */
}
```

❌ **Fehler 2: Zu viele Media Queries**
```css
@media (max-width: 1200px) { ... }
@media (max-width: 1100px) { ... }
@media (max-width: 1000px) { ... }
```

✅ **Besser: Auto-responsive Grid nutzen**
```css
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

❌ **Fehler 3: Flexbox für 2D-Layouts**
```css
/* Kompliziert mit Flexbox! */
.container {
  display: flex;
  flex-wrap: wrap;
}
```

✅ **Besser: Grid verwenden**
```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

---

## 9. Browser DevTools nutzen

**Flexbox & Grid visualisieren:**

1. **Chrome/Edge DevTools**: F12 öffnen
2. Element mit `display: flex` oder `display: grid` auswählen
3. In der HTML-Ansicht erscheint ein `flex` oder `grid` Badge
4. Klicke darauf → Sichtbare Grid-/Flexbox-Linien im Browser!

**Tipp:** Experimentiere live in den DevTools!

---

## 10. Vollständiges Beispiel: Responsive Card-Layout

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flexibles Card-Layout</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Unsere Services</h1>
    <div class="card-grid">
      <div class="card">
        <h3>Webdesign</h3>
        <p>Modernes und responsives Design für Ihre Website.</p>
        <button>Mehr erfahren</button>
      </div>
      <div class="card">
        <h3>SEO</h3>
        <p>Optimierung für Suchmaschinen und bessere Rankings.</p>
        <button>Mehr erfahren</button>
      </div>
      <div class="card">
        <h3>Marketing</h3>
        <p>Effektive Online-Marketing-Strategien.</p>
        <button>Mehr erfahren</button>
      </div>
      <div class="card">
        <h3>Support</h3>
        <p>24/7 technischer Support für Ihre Projekte.</p>
        <button>Mehr erfahren</button>
      </div>
    </div>
  </div>
</body>
</html>
```

### CSS (style.css)
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f0f0;
  padding: 40px 20px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 40px;
  color: #0b5cad;
}

/* Grid für Cards */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  
  /* Flexbox für Card-Inhalt */
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.card h3 {
  color: #0b5cad;
  font-size: 24px;
}

.card p {
  color: #666;
  line-height: 1.6;
  flex-grow: 1;  /* Text nimmt verfügbaren Platz */
}

.card button {
  padding: 12px 24px;
  background-color: #0b5cad;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  align-self: flex-start;  /* Button linksbündig */
}

.card button:hover {
  background-color: #094a8f;
}

/* Responsive Anpassungen */
@media (max-width: 768px) {
  .card-grid {
    gap: 20px;
  }
  
  .card {
    padding: 20px;
  }
}
```

---

## Nächste Schritte

- **Responsive Design** → `responsive-design.md` - Media Queries & Mobile-First
- **Box-Modell** → `box-modell.md` - Padding, Margin, Border
- **Bilder & Grafiken** → `bilder-grafiken.md` - Responsive Bilder in Layouts
- **Galerien** → `galerien.md` - Bildgalerien mit Grid

---

## Ressourcen

- [CSS Tricks: Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Tricks: Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Flexbox Froggy](https://flexboxfroggy.com/) - Spielerisch Flexbox lernen
- [Grid Garden](https://cssgridgarden.com/) - Spielerisch Grid lernen
- [Can I Use](https://caniuse.com/) - Browser-Kompatibilität

---

**Tipp:** Nutze die Browser DevTools (F12), um Flexbox und Grid live zu visualisieren und zu experimentieren!
