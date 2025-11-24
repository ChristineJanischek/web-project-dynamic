# Bildgalerien erstellen

Bildgalerien sind ein beliebtes Element auf Webseiten. Hier lernst du, wie du mit modernen CSS-Techniken ansprechende und responsive Galerien erstellst.

## Einfache Grid-Galerie

Die einfachste Methode ist CSS Grid - automatisch responsive ohne Media Queries!

### HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bildgalerie</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <h1>Meine Fotogalerie</h1>
    
    <div class="gallery">
      <img src="images/foto1.jpg" alt="Strand bei Sonnenuntergang">
      <img src="images/foto2.jpg" alt="Berge mit Schnee">
      <img src="images/foto3.jpg" alt="Stadtansicht bei Nacht">
      <img src="images/foto4.jpg" alt="Wald im Herbst">
      <img src="images/foto5.jpg" alt="Meer mit Wellen">
      <img src="images/foto6.jpg" alt="Blumenwiese">
      <img src="images/foto7.jpg" alt="Wüstenlandschaft">
      <img src="images/foto8.jpg" alt="Polarlichter">
    </div>
  </main>
</body>
</html>
```

### CSS

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f5f5f5;
  padding: 20px;
}

main {
  max-width: 1400px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 40px;
  color: #333;
}

/* Grid Galerie */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.gallery img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.gallery img:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}
```

**Was macht `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`?**
- **repeat**: Wiederhole Spalten
- **auto-fit**: So viele wie möglich in eine Zeile
- **minmax(250px, 1fr)**: Mindestens 250px, maximal gleichmäßig verteilt
- **Ergebnis**: Automatisch 1-6 Spalten je nach Bildschirmbreite!

---

## Galerie mit unterschiedlichen Bildgrößen

Für interessantere Layouts kannst du Bilder unterschiedlich groß darstellen:

### HTML

```html
<div class="gallery-masonry">
  <img src="images/foto1.jpg" alt="Bild 1" class="tall">
  <img src="images/foto2.jpg" alt="Bild 2">
  <img src="images/foto3.jpg" alt="Bild 3" class="wide">
  <img src="images/foto4.jpg" alt="Bild 4">
  <img src="images/foto5.jpg" alt="Bild 5" class="tall">
  <img src="images/foto6.jpg" alt="Bild 6">
</div>
```

### CSS

```css
.gallery-masonry {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-rows: 200px;
  gap: 15px;
}

.gallery-masonry img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

/* Spezielle Größen */
.gallery-masonry img.tall {
  grid-row: span 2;  /* 2 Zeilen hoch */
}

.gallery-masonry img.wide {
  grid-column: span 2;  /* 2 Spalten breit */
}
```

---

## Flexbox-Galerie

Alternative mit Flexbox (etwas weniger flexibel als Grid):

### CSS

```css
.gallery-flex {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.gallery-flex img {
  flex: 1 1 calc(33.333% - 15px);  /* 3 Spalten */
  height: 250px;
  object-fit: cover;
  border-radius: 8px;
}

/* Responsive */
@media (max-width: 900px) {
  .gallery-flex img {
    flex: 1 1 calc(50% - 15px);  /* 2 Spalten */
  }
}

@media (max-width: 600px) {
  .gallery-flex img {
    flex: 1 1 100%;  /* 1 Spalte */
  }
}
```

---

## Galerie mit Lightbox-Effekt

Klickbare Bilder, die größer angezeigt werden:

### HTML

```html
<div class="gallery">
  <img src="images/foto1.jpg" alt="Strand" onclick="openLightbox(this)">
  <img src="images/foto2.jpg" alt="Berge" onclick="openLightbox(this)">
  <img src="images/foto3.jpg" alt="Stadt" onclick="openLightbox(this)">
</div>

<!-- Lightbox Overlay -->
<div id="lightbox" class="lightbox" onclick="closeLightbox()">
  <span class="close">&times;</span>
  <img id="lightbox-img" src="" alt="">
</div>
```

### CSS

```css
/* Galerie (wie oben) */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.gallery img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.3s;
}

.gallery img:hover {
  opacity: 0.8;
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  z-index: 1000;
  justify-content: center;
  align-items: center;
}

.lightbox.active {
  display: flex;
}

.lightbox img {
  max-width: 90%;
  max-height: 90%;
  border-radius: 8px;
  box-shadow: 0 0 50px rgba(255, 255, 255, 0.3);
}

.lightbox .close {
  position: absolute;
  top: 30px;
  right: 50px;
  color: white;
  font-size: 50px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s;
}

.lightbox .close:hover {
  color: #ccc;
}
```

### JavaScript

```javascript
function openLightbox(img) {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  
  lightboxImg.src = img.src;
  lightboxImg.alt = img.alt;
  lightbox.classList.add('active');
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  lightbox.classList.remove('active');
}

// ESC-Taste zum Schließen
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeLightbox();
  }
});
```

---

## Galerie mit Bildunterschriften

### HTML

```html
<div class="gallery-captions">
  <figure>
    <img src="images/foto1.jpg" alt="Strand">
    <figcaption>Sonnenuntergang am Strand</figcaption>
  </figure>
  
  <figure>
    <img src="images/foto2.jpg" alt="Berge">
    <figcaption>Alpenpanorama im Winter</figcaption>
  </figure>
  
  <figure>
    <img src="images/foto3.jpg" alt="Stadt">
    <figcaption>Stadtlichter bei Nacht</figcaption>
  </figure>
</div>
```

### CSS

```css
.gallery-captions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
}

.gallery-captions figure {
  margin: 0;
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.gallery-captions img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
}

.gallery-captions figure:hover img {
  transform: scale(1.1);
}

.gallery-captions figcaption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: white;
  padding: 20px;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.gallery-captions figure:hover figcaption {
  transform: translateY(0);
}
```

---

## Pinterest-Style (Masonry mit CSS)

```css
.gallery-masonry-columns {
  column-count: 3;
  column-gap: 20px;
}

.gallery-masonry-columns img {
  width: 100%;
  margin-bottom: 20px;
  border-radius: 8px;
  break-inside: avoid;  /* Verhindert Bild-Splitting */
}

/* Responsive */
@media (max-width: 900px) {
  .gallery-masonry-columns {
    column-count: 2;
  }
}

@media (max-width: 600px) {
  .gallery-masonry-columns {
    column-count: 1;
  }
}
```

---

## Lazy Loading für Performance

Lade Bilder erst, wenn sie sichtbar werden:

```html
<img src="placeholder.jpg" 
     data-src="images/foto1.jpg" 
     alt="Strand" 
     loading="lazy"
     class="lazy">
```

### Moderne Methode (HTML5)

```html
<img src="images/foto1.jpg" alt="Strand" loading="lazy">
```

**Browser lädt Bild erst**, wenn es in den Viewport kommt!

---

## Vollständiges responsives Beispiel

### HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Galerie</title>
  <link rel="stylesheet" href="gallery.css">
</head>
<body>
  <header>
    <h1>Meine Fotogalerie</h1>
    <p>Klicke auf ein Bild für Vollansicht</p>
  </header>
  
  <main>
    <div class="gallery">
      <img src="images/1.jpg" alt="Natur" loading="lazy" onclick="openLightbox(this)">
      <img src="images/2.jpg" alt="Stadt" loading="lazy" onclick="openLightbox(this)">
      <img src="images/3.jpg" alt="Meer" loading="lazy" onclick="openLightbox(this)">
      <img src="images/4.jpg" alt="Berge" loading="lazy" onclick="openLightbox(this)">
      <img src="images/5.jpg" alt="Wald" loading="lazy" onclick="openLightbox(this)">
      <img src="images/6.jpg" alt="Wüste" loading="lazy" onclick="openLightbox(this)">
    </div>
  </main>
  
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="close">&times;</span>
    <img id="lightbox-img" src="" alt="">
  </div>
  
  <script src="gallery.js"></script>
</body>
</html>
```

### CSS (`gallery.css`)

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  padding: 20px;
}

header {
  text-align: center;
  color: white;
  margin-bottom: 40px;
}

header h1 {
  font-size: 3rem;
  margin-bottom: 10px;
}

main {
  max-width: 1400px;
  margin: 0 auto;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.gallery img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.gallery img:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
}

/* Lightbox */
.lightbox {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.95);
  z-index: 1000;
  justify-content: center;
  align-items: center;
}

.lightbox.active {
  display: flex;
}

.lightbox img {
  max-width: 90%;
  max-height: 90%;
  border-radius: 8px;
  box-shadow: 0 0 50px rgba(255, 255, 255, 0.2);
}

.close {
  position: absolute;
  top: 30px;
  right: 50px;
  color: white;
  font-size: 50px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s;
}

.close:hover {
  color: #ccc;
}

/* Responsive */
@media (max-width: 768px) {
  header h1 {
    font-size: 2rem;
  }
  
  .gallery {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px;
  }
  
  .gallery img {
    height: 200px;
  }
  
  .close {
    top: 15px;
    right: 20px;
    font-size: 35px;
  }
}
```

### JavaScript (`gallery.js`)

```javascript
function openLightbox(img) {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  
  lightboxImg.src = img.src;
  lightboxImg.alt = img.alt;
  lightbox.classList.add('active');
  document.body.style.overflow = 'hidden';  // Scrolling verhindern
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  lightbox.classList.remove('active');
  document.body.style.overflow = 'auto';  // Scrolling wieder erlauben
}

// ESC-Taste zum Schließen
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeLightbox();
  }
});
```

---

## Best Practices

✅ **Alt-Texte** für jedes Bild (Barrierefreiheit!)  
✅ **Lazy Loading** nutzen (`loading="lazy"`)  
✅ **Bilder komprimieren** (< 200KB pro Bild)  
✅ **object-fit: cover** für einheitliche Größen  
✅ **Responsive** mit Grid oder Flexbox  
✅ **Hover-Effekte** für Interaktivität  
✅ **Bildunterschriften** wo sinnvoll  

---

## Nächste Schritte

- **Formulare** → `formulare.md` - Interaktive Formulare erstellen
- **JavaScript** → `js.md` - Erweiterte Galerie-Funktionen
- **Responsive Design** → `responsive-design.md` - Weitere Optimierungen

---

## Ressourcen

- [Unsplash](https://unsplash.com) - Kostenlose Stockfotos
- [Pexels](https://pexels.com) - Weitere kostenlose Bilder
- [TinyPNG](https://tinypng.com) - Bilder komprimieren
- [CSS Grid Generator](https://cssgrid-generator.netlify.app/) - Grid-Layouts erstellen
