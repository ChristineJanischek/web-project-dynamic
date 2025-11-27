# Version 3: Bilder, Galerien & Formulare

**Status:** ✅ Bereit zum Lernen!

## 🎯 Lernziele

Nach Abschluss dieser Version kannst du:
- ✅ Bilder responsive und optimiert einbinden
- ✅ Moderne Bildgalerien mit CSS Grid erstellen
- ✅ Formulare mit HTML5-Validierung gestalten
- ✅ JavaScript-Formular-Validierung implementieren
- ✅ Lightbox-Effekte für Bildvergrößerung nutzen
- ✅ Verschiedene Bildformate gezielt einsetzen

## 📋 Voraussetzungen

- Abgeschlossene **Version 1** (HTML-Grundgerüst & CSS-Basics)
- Abgeschlossene **Version 2** (Box-Modell & Responsive Design)
- Grundkenntnisse in JavaScript (DOM-Manipulation)
- Verständnis von CSS Grid und Flexbox

---

## 📚 Aufgabenübersicht

### Teil 1: Responsive Bilder (60 Min)
📖 **Theorie:** [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md)

**Lernziele:**
- Verschiedene Bildformate kennen (JPG, PNG, SVG, WebP)
- Bilder responsive einbinden
- Alt-Texte richtig schreiben
- `object-fit` und `object-position` nutzen

**Aufgaben:**
1. Hero-Bild mit `object-fit: cover` erstellen
2. Logo als SVG einbinden
3. Responsive Bilder mit `srcset` implementieren
4. Picture-Element für Art Direction nutzen

---

### Teil 2: Bildgalerie mit Grid (90 Min)
📖 **Theorie:** [`docs/galerien.md`](../docs/galerien.md)

**Lernziele:**
- CSS Grid für automatisch responsive Galerien
- Hover-Effekte für Interaktivität
- Verschiedene Galerie-Layouts umsetzen

**Aufgaben:**
1. Einfache Grid-Galerie mit 6-9 Bildern
2. Unterschiedliche Bildgrößen im Grid
3. Hover-Effekt mit Scale & Shadow
4. Masonry-Layout (optional)

---

### Teil 3: Lightbox implementieren (60 Min)
📖 **Theorie:** [`docs/galerien.md`](../docs/galerien.md) (Abschnitt "Lightbox")

**Lernziele:**
- Modal/Overlay mit CSS erstellen
- JavaScript Event-Listener für Bildklicks
- Navigation zwischen Bildern
- Schließen mit Escape-Taste

**Aufgaben:**
1. Lightbox HTML-Struktur erstellen
2. CSS für Overlay und Bild-Vergrößerung
3. JavaScript für Öffnen/Schließen
4. Pfeiltasten-Navigation implementieren

---

### Teil 4: Kontaktformular (90 Min)
📖 **Theorie:** [`docs/formulare.md`](../docs/formulare.md)

**Lernziele:**
- Formular-Grundstruktur verstehen
- HTML5-Validierung nutzen
- Formular-Styling mit CSS
- JavaScript-Validierung implementieren

**Aufgaben:**
1. Kontaktformular erstellen (Name, Email, Nachricht)
2. HTML5-Validierung (required, email, minlength)
3. Custom Styling für Inputs und Buttons
4. JavaScript-Validierung bei Submit
5. Erfolgs-/Fehlermeldungen anzeigen

---

## 🛠️ Schritt-für-Schritt Implementierungsanleitung

### Vorbereitung

**📖 Vor dem Start empfohlen:**
- [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md) - Bildformate & Responsive Bilder
- [`docs/galerien.md`](../docs/galerien.md) - Grid-Galerien & Lightbox
- [`docs/formulare.md`](../docs/formulare.md) - Formular-Grundlagen & Validierung

1. **Workspace vorbereiten**
   - Öffne den Ordner `version3/aufgabe/` in deinem Editor
   - Stelle sicher, dass die Dateistruktur vollständig ist:
     - `index.html`
     - `css/style.css`
     - `js/script.js`
     - `images/` (füge 6-9 Beispielbilder hinzu)

2. **Beispielbilder hinzufügen**
   - Lade kostenlose Bilder von [Unsplash](https://unsplash.com) oder [Pexels](https://pexels.com)
   - Oder nutze Platzhalter: `https://picsum.photos/400/300`
   - Benenne sie: `bild1.jpg`, `bild2.jpg`, etc.

---

### Schritt 1: HTML-Grundstruktur (30 Min)

**Ziel:** Vollständige HTML-Struktur mit allen Sektionen

#### Zu implementieren in `index.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Version 3: Bilder, Galerien & Formulare</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Header mit Navigation -->
    <header>
        <div class="container">
            <h1>Mein Portfolio</h1>
            <nav>
                <ul class="nav">
                    <li><a href="#hero">Start</a></li>
                    <li><a href="#galerie">Galerie</a></li>
                    <li><a href="#kontakt">Kontakt</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section mit Hintergrundbild -->
    <section id="hero" class="hero">
        <div class="hero-content">
            <h2>Willkommen in meiner Bildergalerie</h2>
            <p>Entdecke atemberaubende Fotografie</p>
        </div>
    </section>

    <!-- Hauptinhalt -->
    <main>
        <div class="container">
            <!-- Galerie-Sektion -->
            <section id="galerie" class="gallery-section">
                <h2>Meine Galerie</h2>
                <div class="gallery">
                    <!-- TODO: 6-9 Bilder hier einfügen -->
                </div>
            </section>

            <!-- Kontaktformular-Sektion -->
            <section id="kontakt" class="contact-section">
                <h2>Kontakt</h2>
                <form id="contactForm" class="contact-form">
                    <!-- TODO: Formularfelder hier einfügen -->
                </form>
                <div id="formMessage" class="form-message"></div>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2025 Mein Portfolio</p>
        </div>
    </footer>

    <!-- Lightbox (Modal) -->
    <div id="lightbox" class="lightbox">
        <!-- TODO: Lightbox-Struktur hier einfügen -->
    </div>

    <script src="js/script.js"></script>
</body>
</html>
```

**✅ Testen:**
- HTML-Datei im Browser öffnen
- Sollte grundlegende Struktur zeigen (noch ohne Styling)

---

### Schritt 2: Hero-Bild & Responsive Bilder (45 Min)

**Ziel:** Hero-Section mit Hintergrundbild und responsive Bilder in der Galerie

#### Zu implementieren in `index.html` (Galerie-Sektion):

```html
<section id="galerie" class="gallery-section">
    <h2>Meine Galerie</h2>
    <div class="gallery">
        <img src="images/bild1.jpg" alt="Landschaft mit Bergen" class="gallery-img">
        <img src="images/bild2.jpg" alt="Sonnenuntergang am Meer" class="gallery-img">
        <img src="images/bild3.jpg" alt="Stadtansicht bei Nacht" class="gallery-img">
        <img src="images/bild4.jpg" alt="Wald im Herbst" class="gallery-img">
        <img src="images/bild5.jpg" alt="Wüstenlandschaft" class="gallery-img">
        <img src="images/bild6.jpg" alt="Polarlichter" class="gallery-img">
    </div>
</section>
```

#### Zu implementieren in `css/style.css`:

```css
/* Reset & Grundstyles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Hero Section */
.hero {
    height: 70vh;
    background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                      url('../images/hero.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed; /* Parallax-Effekt */
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
}

.hero-content h2 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-content p {
    font-size: 1.5rem;
}

/* Responsive Bilder */
img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

**✅ Testen:**
- Hero-Section sollte Hintergrundbild zeigen
- Bei Fehlendem Bild: Platzhalter `https://picsum.photos/1920/1080` nutzen
- Bilder sollten nicht über Container hinausragen

**📖 Hinweis:** Lies [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md) für mehr zu Bildformaten und `object-fit`

---

### Schritt 3: Grid-Galerie (45 Min)

**Ziel:** Responsive Bildgalerie mit automatischem Layout

#### Zu implementieren in `css/style.css`:

```css
/* Galerie-Sektion */
.gallery-section {
    padding: 60px 0;
}

.gallery-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 40px;
    color: #2c3e50;
}

/* Grid-Galerie */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.gallery-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-img:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Responsive Anpassungen */
@media (max-width: 768px) {
    .gallery {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }
    
    .gallery-img {
        height: 200px;
    }
}
```

**✅ Testen:**
- DevTools → Responsive Mode
- **Desktop**: Mehrere Bilder nebeneinander
- **Mobile**: 1-2 Bilder pro Zeile
- **Hover**: Bild vergrößert sich und bekommt Schatten

**📖 Hinweis:** Lies [`docs/galerien.md`](../docs/galerien.md) für verschiedene Galerie-Layouts

---

### Schritt 4: Lightbox HTML & CSS (60 Min)

**Ziel:** Modal zum Vergrößern der Bilder

#### Zu implementieren in `index.html` (Lightbox-Bereich):

```html
<div id="lightbox" class="lightbox">
    <span class="lightbox-close">&times;</span>
    <span class="lightbox-prev">&#10094;</span>
    <span class="lightbox-next">&#10095;</span>
    <img src="" alt="" id="lightbox-img" class="lightbox-content">
    <div class="lightbox-caption"></div>
</div>
```

#### Zu implementieren in `css/style.css`:

```css
/* Lightbox */
.lightbox {
    display: none; /* Versteckt bis geöffnet */
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    align-items: center;
    justify-content: center;
}

.lightbox.active {
    display: flex;
}

.lightbox-content {
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
    border-radius: 8px;
}

/* Schließen-Button */
.lightbox-close {
    position: absolute;
    top: 20px;
    right: 40px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    transition: color 0.3s ease;
}

.lightbox-close:hover {
    color: #ff6b6b;
}

/* Navigation */
.lightbox-prev,
.lightbox-next {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: white;
    font-size: 60px;
    font-weight: bold;
    cursor: pointer;
    user-select: none;
    padding: 20px;
    transition: background-color 0.3s ease;
}

.lightbox-prev {
    left: 20px;
}

.lightbox-next {
    right: 20px;
}

.lightbox-prev:hover,
.lightbox-next:hover {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
}

/* Caption */
.lightbox-caption {
    position: absolute;
    bottom: 30px;
    color: white;
    text-align: center;
    width: 100%;
    font-size: 1.2rem;
}
```

**✅ Testen:**
- DevTools → Füge `.active` Klasse zu `.lightbox` hinzu
- Lightbox sollte Vollbild-Overlay zeigen
- Schließen-Button (X) sollte oben rechts sein
- Pfeile sollten links/rechts sein

---

### Schritt 5: Lightbox JavaScript (60 Min)

**Ziel:** Interaktive Lightbox mit Bild-Navigation

#### Zu implementieren in `js/script.js`:

```javascript
// Lightbox Funktionalität
const galleryImages = document.querySelectorAll('.gallery-img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.querySelector('.lightbox-caption');
const closeBtn = document.querySelector('.lightbox-close');
const prevBtn = document.querySelector('.lightbox-prev');
const nextBtn = document.querySelector('.lightbox-next');

let currentImageIndex = 0;

// Bild in Lightbox öffnen
function openLightbox(index) {
    currentImageIndex = index;
    const img = galleryImages[index];
    lightboxImg.src = img.src;
    lightboxCaption.textContent = img.alt;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden'; // Scrollen verhindern
}

// Lightbox schließen
function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Nächstes Bild
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Vorheriges Bild
function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Event Listener für Galerie-Bilder
galleryImages.forEach((img, index) => {
    img.addEventListener('click', () => openLightbox(index));
});

// Event Listener für Lightbox-Controls
closeBtn.addEventListener('click', closeLightbox);
prevBtn.addEventListener('click', prevImage);
nextBtn.addEventListener('click', nextImage);

// Klick außerhalb des Bildes schließt Lightbox
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        closeLightbox();
    }
});

// Tastatur-Navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') nextImage();
    if (e.key === 'ArrowLeft') prevImage();
});
```

**✅ Testen:**
- Klicke auf ein Galerie-Bild → Lightbox öffnet sich
- Klicke auf X → Schließt
- Klicke auf Pfeile → Navigiert zwischen Bildern
- Tastatur:
  - **Escape** → Schließt Lightbox
  - **← →** → Navigiert zwischen Bildern
- Klick außerhalb des Bildes → Schließt Lightbox

**📖 Hinweis:** Lies [`docs/js.md`](../docs/js.md) für Event Handling und DOM-Manipulation

---

### Schritt 6: Kontaktformular HTML (30 Min)

**Ziel:** Formular mit allen wichtigen Feldern

#### Zu implementieren in `index.html` (Contact-Form):

```html
<form id="contactForm" class="contact-form">
    <div class="form-group">
        <label for="name">Name *</label>
        <input 
            type="text" 
            id="name" 
            name="name" 
            required 
            minlength="2"
            placeholder="Dein Name">
    </div>

    <div class="form-group">
        <label for="email">E-Mail *</label>
        <input 
            type="email" 
            id="email" 
            name="email" 
            required
            placeholder="deine@email.de">
    </div>

    <div class="form-group">
        <label for="subject">Betreff</label>
        <input 
            type="text" 
            id="subject" 
            name="subject"
            placeholder="Worum geht es?">
    </div>

    <div class="form-group">
        <label for="message">Nachricht *</label>
        <textarea 
            id="message" 
            name="message" 
            rows="5" 
            required
            minlength="10"
            placeholder="Deine Nachricht..."></textarea>
    </div>

    <button type="submit" class="btn-submit">Absenden</button>
</form>
<div id="formMessage" class="form-message"></div>
```

**✅ Testen:**
- Formular sollte 4 Felder zeigen
- `*` markiert Pflichtfelder

---

### Schritt 7: Formular-Styling (45 Min)

**Ziel:** Modernes, ansprechendes Formular-Design

#### Zu implementieren in `css/style.css`:

```css
/* Kontakt-Sektion */
.contact-section {
    padding: 60px 0;
    background-color: #f8f9fa;
}

.contact-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 40px;
    color: #2c3e50;
}

/* Formular */
.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #2c3e50;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #667eea;
}

.form-group textarea {
    resize: vertical;
}

/* Submit Button */
.btn-submit {
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.3s ease;
}

.btn-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-submit:active {
    transform: translateY(0);
}

/* Erfolgsmeldung */
.form-message {
    max-width: 600px;
    margin: 20px auto;
    padding: 15px;
    border-radius: 4px;
    text-align: center;
    display: none;
}

.form-message.success {
    display: block;
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.form-message.error {
    display: block;
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
```

**✅ Testen:**
- Formular sollte zentriert und mit weißem Hintergrund sein
- Fokus auf Input → Blauer Rand
- Button hat Gradient-Hintergrund
- Hover über Button → Hebt sich leicht an

**📖 Hinweis:** Lies [`docs/formulare.md`](../docs/formulare.md) für mehr zu Formular-Styling

---

### Schritt 8: JavaScript Formular-Validierung (60 Min)

**Ziel:** Custom Validierung und Feedback bei Submit

#### Zu implementieren in `js/script.js`:

```javascript
// Formular-Validierung
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Verhindert Standard-Submit
    
    // Formular-Daten auslesen
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        subject: document.getElementById('subject').value.trim(),
        message: document.getElementById('message').value.trim()
    };
    
    // Validierung
    if (!validateForm(formData)) {
        showMessage('Bitte fülle alle Pflichtfelder korrekt aus!', 'error');
        return;
    }
    
    // Simuliere erfolgreichen Versand
    showMessage('Danke für deine Nachricht! Ich melde mich bald.', 'success');
    contactForm.reset();
    
    // In Realität: Hier würde AJAX/Fetch zum Backend gehen
    // fetch('/api/contact', { method: 'POST', body: JSON.stringify(formData) })
});

// Validierungs-Funktion
function validateForm(data) {
    // Name mindestens 2 Zeichen
    if (data.name.length < 2) {
        return false;
    }
    
    // E-Mail Format prüfen
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        return false;
    }
    
    // Nachricht mindestens 10 Zeichen
    if (data.message.length < 10) {
        return false;
    }
    
    return true;
}

// Nachricht anzeigen
function showMessage(text, type) {
    formMessage.textContent = text;
    formMessage.className = `form-message ${type}`;
    
    // Nach 5 Sekunden ausblenden
    setTimeout(() => {
        formMessage.className = 'form-message';
    }, 5000);
}
```

**✅ Testen:**
- Formular leer absenden → Fehlermeldung (HTML5-Validierung)
- Ungültige Email → Fehlermeldung
- Name zu kurz (< 2 Zeichen) → Fehlermeldung
- Nachricht zu kurz (< 10 Zeichen) → Fehlermeldung
- Alle Felder korrekt → Erfolgsmeldung (grün)
- Formular wird zurückgesetzt

---

### Schritt 9: Header & Navigation (30 Min)

**Ziel:** Sticky Header mit Smooth Scrolling

#### Zu implementieren in `css/style.css`:

```css
/* Header */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 1.8rem;
}

/* Navigation */
.nav {
    display: flex;
    gap: 30px;
    list-style: none;
}

.nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.nav a:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}
```

**✅ Testen:**
- Header bleibt beim Scrollen oben (sticky)
- Navigation-Links haben Hover-Effekt
- Klick auf Link → Smooth Scroll zur Sektion

---

### Schritt 10: Footer & Mobile Optimierung (30 Min)

**Ziel:** Footer und responsive Anpassungen

#### Zu implementieren in `css/style.css`:

```css
/* Footer */
footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 30px 0;
    margin-top: 60px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    header .container {
        flex-direction: column;
        gap: 20px;
    }
    
    .nav {
        flex-direction: column;
        gap: 10px;
        text-align: center;
    }
    
    .hero-content h2 {
        font-size: 2rem;
    }
    
    .hero-content p {
        font-size: 1.2rem;
    }
    
    .contact-form {
        padding: 20px;
    }
}
```

**✅ Finaler Test:**
- [ ] Alle Bilder laden korrekt
- [ ] Galerie ist responsive (1-4 Spalten)
- [ ] Lightbox funktioniert vollständig
- [ ] Formular validiert und zeigt Meldungen
- [ ] Smooth Scrolling zu Sektionen
- [ ] Mobile Ansicht optimiert
- [ ] Keine Fehler in der Console

---

## 🧪 Test-Checkliste

### Desktop (> 1024px)
- [ ] Hero-Bild wird angezeigt (Parallax-Effekt)
- [ ] Galerie zeigt 3-4 Bilder pro Zeile
- [ ] Lightbox öffnet beim Klick auf Bild
- [ ] Navigation zwischen Bildern (Pfeile, Tastatur)
- [ ] Formular ist zentriert und gut lesbar
- [ ] Header ist sticky

### Tablet (768px - 1024px)
- [ ] Galerie zeigt 2-3 Bilder pro Zeile
- [ ] Formular passt sich an
- [ ] Alle Funktionen verfügbar

### Mobile (< 768px)
- [ ] Galerie zeigt 1-2 Bilder pro Zeile
- [ ] Navigation untereinander
- [ ] Hero-Text skaliert herunter
- [ ] Formular ist gut bedienbar
- [ ] Lightbox nutzt vollen Bildschirm

### Bilder & Galerie
- [ ] Alle Bilder haben Alt-Texte
- [ ] `object-fit: cover` funktioniert
- [ ] Hover-Effekt auf Bildern (Scale, Shadow)
- [ ] Lightbox zeigt Bild in voller Auflösung
- [ ] Caption zeigt Alt-Text

### Formular
- [ ] HTML5-Validierung aktiv (required, email)
- [ ] JavaScript-Validierung funktioniert
- [ ] Erfolgsmeldung (grün) bei korrekter Eingabe
- [ ] Fehlermeldung (rot) bei Fehler
- [ ] Formular wird nach Submit zurückgesetzt
- [ ] Focus-State sichtbar (blauer Rand)

### Interaktivität
- [ ] Smooth Scrolling funktioniert
- [ ] Lightbox:
  - [ ] Öffnet bei Klick
  - [ ] Schließt bei X, Escape, Außenklick
  - [ ] Pfeile navigieren zwischen Bildern
  - [ ] Tastatur (← →) funktioniert
- [ ] Formular Submit verhindert Neuladen

---

## 💡 Debugging-Tipps

**Problem: Bilder werden nicht angezeigt**
- Prüfe Pfade in `src` Attribut
- DevTools → Network Tab → Rote Einträge = fehlende Dateien
- Groß-/Kleinschreibung beachten!

**Problem: Lightbox öffnet nicht**
- Console → JavaScript-Fehler?
- IDs korrekt? (`lightbox`, `lightbox-img`)
- `script.js` eingebunden?

**Problem: Formular sendet trotz Fehler**
- `e.preventDefault()` vorhanden?
- Validierungs-Funktion wird aufgerufen?

**Problem: Galerie nicht responsive**
- `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))` gesetzt?
- Media Queries aktiv?

---

## 📚 Hilfsmittel & Dokumentation

### Theorie & Konzepte
- [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md) - Bildformate, responsive Bilder, `object-fit`
- [`docs/galerien.md`](../docs/galerien.md) - Grid-Galerien, Lightbox, Masonry
- [`docs/formulare.md`](../docs/formulare.md) - Formular-Grundlagen, Validierung, Styling

### JavaScript & Interaktivität
- [`docs/js.md`](../docs/js.md) - DOM-Manipulation, Events, Validierung

### CSS & Layout
- [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) - CSS Grid für Galerien
- [`docs/responsive-design.md`](../docs/responsive-design.md) - Media Queries

### Zusätzliche Ressourcen
- [`shared-examples/`](../shared-examples/) - Vollständiges Beispiel
- **Browser DevTools (F12)** - Element Inspector, Console, Network
- **[Unsplash](https://unsplash.com)** - Kostenlose Bilder
- **[Can I Use](https://caniuse.com)** - Browser-Kompatibilität

---

## 🎯 Bewertungskriterien

- [ ] Korrekte Verwendung von Bildformaten
- [ ] Responsive Bilder (max-width, srcset)
- [ ] Funktionale Grid-Galerie
- [ ] Vollständig funktionierende Lightbox
- [ ] Formular mit HTML5 & JS-Validierung
- [ ] Code-Qualität und Kommentare
- [ ] Mobile-Optimierung
- [ ] Barrierefreiheit (Alt-Texte, Labels)

---

## 🌟 Bonus-Aufgaben (Optional)

- [ ] Lazy Loading für Bilder implementieren
- [ ] Unterschiedliche Bildgrößen im Grid (Featured Images)
- [ ] Formular-Daten mit LocalStorage speichern
- [ ] Dark Mode Toggle
- [ ] Bildfilter mit CSS (`filter` Property)
- [ ] Masonry-Layout statt Grid
- [ ] Formular mit PHP/Node.js Backend verbinden

---

## ➡️ Weiterführende Themen

Nach Abschluss dieser Version kannst du mit folgenden Themen weitermachen:

- [`docs/js.md`](../docs/js.md) - Fortgeschrittenes JavaScript
- **Version 4**: JavaScript & Interaktivität (AJAX, Fetch API, Single Page App)
- **Version 5**: Backend Integration (PHP oder Python Flask)
- **Version 6**: Datenbank-Anbindung (MySQL)

---

## 📊 Zeitaufwand

- **Teil 1 (Bilder)**: 60 Min
- **Teil 2 (Galerie)**: 90 Min
- **Teil 3 (Lightbox)**: 60 Min
- **Teil 4 (Formular)**: 90 Min
- **Gesamt**: Ca. 5-6 Stunden

---

**Viel Erfolg!** 🚀 Bei Fragen schaue in die `docs/` oder frage deinen Mentor.
