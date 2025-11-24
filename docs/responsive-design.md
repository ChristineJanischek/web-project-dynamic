# Responsive Design

Responsive Design bedeutet, dass eine Webseite auf **allen Geräten** (Desktop, Tablet, Smartphone) gut aussieht und funktioniert. Eine responsive Webseite passt sich automatisch an verschiedene Bildschirmgrößen an.

## Warum Responsive Design?

- **60%+ der Web-Nutzer** sind mobil unterwegs
- **Google bevorzugt** mobile-freundliche Seiten (SEO!)
- **Eine Website** für alle Geräte (statt separate mobile Version)
- **Bessere Nutzererfahrung** auf allen Geräten

---

## 1. Viewport Meta-Tag

**WICHTIG!** Dieses Tag **muss** im `<head>` stehen:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Was macht das?**
- `width=device-width` → Breite = Gerätebreite
- `initial-scale=1.0` → Kein Zoom beim Laden

**Ohne dieses Tag:** Mobile Browser zeigen Desktop-Version verkleinert!

---

## 2. Media Queries

Media Queries ermöglichen unterschiedliche CSS-Regeln für verschiedene Bildschirmgrößen.

### Syntax

```css
@media (bedingung) {
  /* CSS nur wenn Bedingung erfüllt */
}
```

### Praktisches Beispiel

```css
/* Standard: Desktop (gilt immer) */
.container {
  width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.nav {
  display: flex;
  justify-content: space-between;
}

/* Tablet: Bis 1024px */
@media (max-width: 1024px) {
  .container {
    width: 90%;
  }
}

/* Mobile: Bis 768px */
@media (max-width: 768px) {
  .container {
    width: 100%;
    padding: 10px;
  }
  
  .nav {
    flex-direction: column;
  }
}

/* Sehr kleine Handys: Bis 480px */
@media (max-width: 480px) {
  .container {
    padding: 5px;
  }
}
```

### Breakpoints (Richtwerte)

```css
/* Extra Small Devices (Phones, < 576px) */
@media (max-width: 575px) { }

/* Small Devices (Phones, 576px - 767px) */
@media (min-width: 576px) and (max-width: 767px) { }

/* Medium Devices (Tablets, 768px - 991px) */
@media (min-width: 768px) and (max-width: 991px) { }

/* Large Devices (Desktops, 992px - 1199px) */
@media (min-width: 992px) and (max-width: 1199px) { }

/* Extra Large Devices (Large Desktops, ≥ 1200px) */
@media (min-width: 1200px) { }
```

**Tipp:** Nutze diese Standard-Breakpoints (Bootstrap-Konvention)

---

## 3. Mobile First vs Desktop First

### Desktop First (traditionell)

```css
/* Standard: Desktop */
.box { width: 1000px; }

/* Dann: Kleiner machen */
@media (max-width: 768px) {
  .box { width: 100%; }
}
```

### Mobile First (modern, empfohlen!)

```css
/* Standard: Mobile */
.box { width: 100%; }

/* Dann: Größer machen */
@media (min-width: 768px) {
  .box { width: 700px; }
}

@media (min-width: 1200px) {
  .box { width: 1000px; }
}
```

**Vorteile Mobile First:**
- Performance: Mobile Geräte laden weniger CSS
- Zwingt zu Priorisierung (was ist wirklich wichtig?)
- Einfacher zu erweitern als zu reduzieren

---

## 4. Flexible Layouts mit Flexbox & Grid

### Flexbox - Für 1D-Layouts (Reihen oder Spalten)

```css
.nav {
  display: flex;
  flex-wrap: wrap;        /* Umbruch erlauben */
  gap: 20px;
}

.nav-item {
  flex: 1 1 200px;        /* Wachsen | Schrumpfen | Basis */
}
```

**Responsive Navigation:**
```css
/* Desktop: Horizontal */
.nav {
  display: flex;
  justify-content: space-between;
}

/* Mobile: Vertikal */
@media (max-width: 768px) {
  .nav {
    flex-direction: column;
  }
}
```

### Grid - Für 2D-Layouts (Reihen UND Spalten)

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

**Was macht das?**
- `repeat(auto-fit, ...)` → So viele Spalten wie möglich
- `minmax(250px, 1fr)` → Mindestens 250px, maximal gleichmäßig verteilt
- **Automatisch responsive!** Ohne Media Queries!

---

## 5. Mobile Navigation (Hamburger-Menü)

### HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Navigation</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">MeineLogo</div>
      
      <!-- Hamburger Button (nur mobil sichtbar) -->
      <button class="nav-toggle" id="navToggle" aria-label="Navigation umschalten">
        <span></span>
        <span></span>
        <span></span>
      </button>
      
      <!-- Navigation -->
      <nav class="nav" id="mainNav">
        <a href="#home">Home</a>
        <a href="#about">Über uns</a>
        <a href="#services">Services</a>
        <a href="#contact">Kontakt</a>
      </nav>
    </div>
  </header>
  
  <script src="script.js"></script>
</body>
</html>
```

### CSS

```css
/* Container */
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Logo */
.logo {
  font-size: 24px;
  font-weight: bold;
}

/* Desktop Navigation */
.nav {
  display: flex;
  gap: 30px;
}

.nav a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s;
}

.nav a:hover {
  color: #0b5cad;
}

/* Hamburger Button (versteckt auf Desktop) */
.nav-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
}

.nav-toggle span {
  width: 25px;
  height: 3px;
  background-color: #333;
  margin: 3px 0;
  transition: 0.3s;
}

/* MOBILE: Bis 768px */
@media (max-width: 768px) {
  /* Hamburger Button zeigen */
  .nav-toggle {
    display: flex;
  }
  
  /* Navigation verstecken & umstrukturieren */
  .nav {
    position: fixed;
    top: 70px;
    right: -100%;           /* Ausgeblendet */
    width: 250px;
    height: calc(100vh - 70px);
    background-color: white;
    flex-direction: column;
    padding: 20px;
    box-shadow: -2px 0 10px rgba(0,0,0,0.1);
    transition: right 0.3s ease;
    gap: 0;
  }
  
  .nav a {
    padding: 15px 0;
    border-bottom: 1px solid #eee;
  }
  
  /* Navigation sichtbar wenn .active */
  .nav.active {
    right: 0;
  }
  
  /* Hamburger Animation */
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

### JavaScript

```javascript
// script.js
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

navToggle.addEventListener('click', function() {
  // Toggle active class
  mainNav.classList.toggle('active');
  navToggle.classList.toggle('active');
});

// Menü schließen beim Klick auf Link
const navLinks = mainNav.querySelectorAll('a');
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    mainNav.classList.remove('active');
    navToggle.classList.remove('active');
  });
});
```

---

## 6. Responsive Bilder

```css
/* Grundregel */
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

Mehr dazu in `bilder-grafiken.md`!

---

## 7. Responsive Typografie

```css
/* Desktop */
body {
  font-size: 16px;
  line-height: 1.6;
}

h1 {
  font-size: 3rem;    /* 48px */
}

/* Tablet */
@media (max-width: 1024px) {
  h1 {
    font-size: 2.5rem; /* 40px */
  }
}

/* Mobile */
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
  
  h1 {
    font-size: 2rem;   /* 32px */
  }
}
```

### Fluid Typography (fortgeschritten)

```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
  /* Min: 2rem, Bevorzugt: 5% Viewport, Max: 4rem */
}
```

---

## 8. Touch-Friendly Design

### Mindestgrößen für Buttons

```css
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
}
```

**Apple & Google Empfehlung:** Mindestens 44×44px für Touch-Ziele!

### Abstände vergrößern

```css
/* Desktop */
.nav a {
  padding: 10px 15px;
}

/* Mobile */
@media (max-width: 768px) {
  .nav a {
    padding: 15px 20px;  /* Größer für Finger */
  }
}
```

---

## 9. Testen & Debugging

### Browser DevTools

1. **Öffne DevTools** (F12)
2. **Toggle Device Toolbar** (Strg+Shift+M / Cmd+Shift+M)
3. **Wähle Gerät** aus Dropdown (iPhone, iPad, etc.)
4. **Teste** Navigation, Scrolling, Touch

### Verschiedene Geräte testen

```css
/* iPhone SE (375px) */
@media (max-width: 375px) { }

/* iPad (768px) */
@media (min-width: 768px) and (max-width: 1024px) { }

/* Desktop HD (1920px) */
@media (min-width: 1920px) { }
```

---

## 10. Vollständiges Beispiel

Siehe `shared-examples/index.html` für ein **vollständiges responsives Beispiel** mit:
- ✅ Flexible Navigation (Desktop/Mobile)
- ✅ Responsive Grid
- ✅ Touch-friendly Buttons
- ✅ Optimierte Bilder
- ✅ Mobile-First CSS

---

## Best Practices Checkliste

✅ **Viewport Meta-Tag** im `<head>`  
✅ **Mobile First** Ansatz nutzen  
✅ **Flexible Einheiten** (`%`, `rem`, `em`, `vw/vh`)  
✅ **max-width statt width** für Container  
✅ **Bilder**: `max-width: 100%`  
✅ **Touch-Ziele**: Mind. 44×44px  
✅ **Hamburger-Menü** für Mobile  
✅ **Testen** auf echten Geräten  
✅ **Performance**: Weniger Code für Mobile  

---

## Häufige Fehler

❌ **Viewport Meta-Tag vergessen**
```html
<!-- Fehlt! Seite wird auf Handy verkleinert dargestellt -->
```

❌ **Feste Pixel-Breiten**
```css
.container { width: 1200px; }  /* Zu breit für Mobile! */
```

✅ **Besser:**
```css
.container { max-width: 1200px; width: 100%; }
```

❌ **Zu kleine Touch-Ziele**
```css
.button { width: 20px; height: 20px; }  /* Zu klein! */
```

❌ **Hover-Effekte ohne Touch-Alternative**
```css
.button:hover { background: blue; }  /* Funktioniert nicht auf Touch! */
```

✅ **Auch :active für Touch:**
```css
.button:hover,
.button:active { background: blue; }
```

---

## Nächste Schritte

- **Bilder & Grafiken** → `bilder-grafiken.md` - Responsive Bilder
- **Galerien** → `galerien.md` - Responsive Bildgalerien
- **Formulare** → `formulare.md` - Responsive Formulare

---

## Ressourcen

- [Responsive Design Checker](https://responsivedesignchecker.com/)
- [Can I Use](https://caniuse.com/) - Browser-Kompatibilität
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [CSS Tricks: Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Tricks: Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
