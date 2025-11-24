# Bilder & Grafiken

Bilder sind ein zentraler Bestandteil moderner Webseiten. Hier lernst du, wie du sie richtig einbindest und optimierst.

## Bildformate im Web

| Format | Wofür? | Vorteile | Nachteile |
|--------|--------|----------|-----------|
| **JPG/JPEG** | Fotos, komplexe Bilder | Kleine Dateigröße, gute Kompression | Keine Transparenz, Qualitätsverlust |
| **PNG** | Logos, Icons, Grafiken | Transparenz möglich, verlustfrei | Größere Dateien als JPG |
| **GIF** | Einfache Animationen | Animationen, kleine Dateien | Nur 256 Farben, veraltet |
| **WebP** | Alles (modern) | Klein & schnell, Transparenz | Nicht alle Browser (alte) |
| **SVG** | Logos, Icons, Vektoren | Skalierbar, klein, editierbar | Nicht für Fotos geeignet |

**Empfehlung:**
- Fotos → **JPG** oder **WebP**
- Logos/Icons → **SVG** oder **PNG**
- Animationen → **GIF** oder **WebP** (besser)

---

## Bilder einbinden

### Grundsyntax

```html
<img src="pfad/zum/bild.jpg" alt="Beschreibung des Bildes">
```

**Wichtig:**
- `src` = Quelle (Source) - Pfad zur Bilddatei
- `alt` = Alternativtext - **Pflicht für Barrierefreiheit!**

### Alt-Text richtig schreiben

```html
<!-- ✅ Gut: Beschreibend -->
<img src="hund.jpg" alt="Golden Retriever spielt im Park">

<!-- ❌ Schlecht: Zu generisch -->
<img src="hund.jpg" alt="Bild">

<!-- ✅ Dekorativ: Leer lassen -->
<img src="deko-linie.png" alt="">
```

### Absolute vs. Relative Pfade

```html
<!-- Relativ (empfohlen) -->
<img src="bilder/foto.jpg" alt="Foto">
<img src="../images/logo.png" alt="Logo">

<!-- Absolut -->
<img src="/assets/bilder/header.jpg" alt="Header">

<!-- Extern -->
<img src="https://example.com/bild.jpg" alt="Externes Bild">
```

---

## Responsive Bilder

Bilder sollten sich an verschiedene Bildschirmgrößen anpassen!

### CSS: Max-Width Methode

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

**Was passiert:**
- Bild wird nie breiter als sein Container
- Höhe passt sich automatisch an (behält Seitenverhältnis)
- `display: block` verhindert ungewollte Abstände

### HTML: srcset für verschiedene Auflösungen

```html
<img 
  src="bild-klein.jpg" 
  srcset="bild-klein.jpg 400w,
          bild-mittel.jpg 800w,
          bild-gross.jpg 1200w"
  sizes="(max-width: 600px) 400px,
         (max-width: 1000px) 800px,
         1200px"
  alt="Landschaft">
```

**Browser wählt automatisch** die passende Bildgröße!

### Picture Element

Für verschiedene Bildformate oder Bildausschnitte:

```html
<picture>
  <source srcset="bild.webp" type="image/webp">
  <source srcset="bild.jpg" type="image/jpeg">
  <img src="bild.jpg" alt="Fallback">
</picture>
```

---

## Praktisches Beispiel

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bilder Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <img src="images/logo.svg" alt="Firmenlogo" class="logo">
  </header>
  
  <main>
    <section class="hero">
      <img src="images/hero.jpg" alt="Berglandschaft bei Sonnenuntergang" class="hero-image">
    </section>
    
    <section class="gallery">
      <h2>Galerie</h2>
      <div class="gallery-grid">
        <img src="images/foto1.jpg" alt="Strand">
        <img src="images/foto2.jpg" alt="Berge">
        <img src="images/foto3.jpg" alt="Stadt">
        <img src="images/foto4.jpg" alt="Wald">
      </div>
    </section>
  </main>
</body>
</html>
```

### CSS
```css
/* Globale Bild-Regel */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Logo */
.logo {
  width: 150px;
  margin: 20px auto;
}

/* Hero-Bild */
.hero {
  width: 100%;
  max-height: 500px;
  overflow: hidden;
}

.hero-image {
  width: 100%;
  height: 500px;
  object-fit: cover;  /* Bild füllt Container, behält Proportionen */
}

/* Galerie */
.gallery {
  max-width: 1200px;
  margin: 40px auto;
  padding: 20px;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.gallery-grid img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.gallery-grid img:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}
```

---

## Object-fit Eigenschaft

Bestimmt, wie ein Bild in seinen Container passt:

```css
.bild {
  width: 300px;
  height: 300px;
  object-fit: cover;
}
```

### Object-fit Werte

```css
/* Füllt Container, beschneidet Überschuss */
object-fit: cover;

/* Passt komplett rein, kann Letterbox haben */
object-fit: contain;

/* Dehnt/staucht Bild (verzieht es!) */
object-fit: fill;

/* Behält Originalgröße */
object-fit: none;

/* Wie contain, aber verkleinert nur */
object-fit: scale-down;
```

**Meist verwendet:** `cover` für gleichmäßige Bilder in Grids!

---

## Hintergrundbilder (CSS)

Alternativ zu `<img>` kannst du Bilder als CSS-Hintergrund setzen:

```css
.hero {
  background-image: url('images/hero.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 500px;
}

/* Kurzform */
.hero {
  background: url('images/hero.jpg') center/cover no-repeat;
  height: 500px;
}
```

**Wann nutzen?**
- Dekorative Bilder
- Überlagerung mit Text
- Parallax-Effekte

**Wann NICHT nutzen?**
- Wichtige Inhaltsbilder (SEO!)
- Bilder, die heruntergeladen werden sollen

---

## Performance-Optimierung

### 1. Bildgröße optimieren

```bash
# Mit Online-Tools oder Software komprimieren:
# - TinyPNG (https://tinypng.com)
# - Squoosh (https://squoosh.app)
# - ImageOptim (Mac)
```

**Ziel:** JPG < 200KB, PNG < 100KB (je nach Größe)

### 2. Lazy Loading

Bilder erst laden, wenn sie sichtbar werden:

```html
<img src="bild.jpg" alt="Beschreibung" loading="lazy">
```

**Browser lädt Bild erst**, wenn User scrollt!

### 3. Richtige Größe bereitstellen

❌ **Schlecht:** 4000×3000px Bild für 400×300px Container

✅ **Besser:** Mehrere Größen bereitstellen (`srcset`)

---

## Bildunterschriften

Mit `<figure>` und `<figcaption>`:

```html
<figure>
  <img src="grafik.jpg" alt="Diagramm der Verkaufszahlen">
  <figcaption>Abb. 1: Verkaufszahlen 2024</figcaption>
</figure>
```

```css
figure {
  margin: 20px 0;
  text-align: center;
}

figcaption {
  font-style: italic;
  color: #666;
  margin-top: 10px;
  font-size: 0.9rem;
}
```

---

## SVG - Skalierbare Vektorgrafiken

SVG ist ideal für Logos und Icons!

### Als `<img>` einbinden

```html
<img src="logo.svg" alt="Logo" width="100">
```

### Inline SVG

```html
<svg width="100" height="100" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="#3498db" />
</svg>
```

**Vorteil:** Kann mit CSS gestylt werden!

```css
svg circle {
  fill: #e74c3c;
  transition: fill 0.3s;
}

svg:hover circle {
  fill: #2ecc71;
}
```

---

## Häufige Fehler

❌ **Fehlender Alt-Text**
```html
<img src="bild.jpg">  <!-- Schlecht für SEO & Barrierefreiheit! -->
```

✅ **Richtig:**
```html
<img src="bild.jpg" alt="Beschreibung">
```

❌ **Zu große Dateien**
```html
<img src="foto-5mb.jpg">  <!-- Lädt ewig! -->
```

✅ **Komprimieren:**
```html
<img src="foto-200kb.jpg">
```

❌ **Fester Width/Height in HTML**
```html
<img src="bild.jpg" width="800" height="600">  <!-- Nicht responsive! -->
```

✅ **In CSS steuern:**
```css
img { max-width: 100%; height: auto; }
```

---

## Barrierefreiheit

### Alt-Text Richtlinien

✅ **Informative Bilder:**
```html
<img src="produkt.jpg" alt="Rotes T-Shirt mit V-Ausschnitt">
```

✅ **Dekorative Bilder:**
```html
<img src="deko.png" alt="">  <!-- Leer, damit Screenreader überspringt -->
```

✅ **Funktionale Bilder (Buttons):**
```html
<button>
  <img src="menu-icon.svg" alt="Menü öffnen">
</button>
```

❌ **Redundant:**
```html
<!-- Bild von... ist überflüssig! -->
<img src="hund.jpg" alt="Bild von einem Hund">
```

---

## Nächste Schritte

- **Galerien** → `galerien.md` - Mehrere Bilder in Grids anordnen
- **Responsive Design** → `responsive-design.md` - Bilder für verschiedene Geräte
- **CSS Formatierung** → `css-formatierung.md` - Weitere Styling-Optionen

---

## Ressourcen

- [Can I Use](https://caniuse.com/) - Browser-Kompatibilität prüfen
- [TinyPNG](https://tinypng.com) - Bilder komprimieren
- [Unsplash](https://unsplash.com) - Kostenlose Stockfotos
- [SVG OMG](https://jakearchibald.github.io/svgomg/) - SVG optimieren
