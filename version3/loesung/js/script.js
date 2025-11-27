// ===================================
// VERSION 3: BILDER, GALERIEN & FORMULARE
// MUSTERLÖSUNG - JAVASCRIPT
// ===================================

/* ===================================
   LIGHTBOX FUNKTIONALITÄT
   =================================== */

// Lightbox-Elemente selektieren
const galleryImages = document.querySelectorAll('.gallery-img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.querySelector('.lightbox-caption');
const closeBtn = document.querySelector('.lightbox-close');
const prevBtn = document.querySelector('.lightbox-prev');
const nextBtn = document.querySelector('.lightbox-next');

let currentImageIndex = 0;

/**
 * Öffnet die Lightbox mit dem ausgewählten Bild
 * @param {number} index - Index des Bildes im Array
 */
function openLightbox(index) {
    currentImageIndex = index;
    const img = galleryImages[index];
    lightboxImg.src = img.src;
    lightboxCaption.textContent = img.alt;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden'; // Scrollen verhindern
}

/**
 * Schließt die Lightbox
 */
function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
}

/**
 * Zeigt das nächste Bild in der Galerie
 */
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
    openLightbox(currentImageIndex);
}

/**
 * Zeigt das vorherige Bild in der Galerie
 */
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


/* ===================================
   FORMULAR-VALIDIERUNG
   =================================== */

const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

/**
 * Behandelt das Formular-Submit Event
 */
contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Verhindert Standard-Submit (Seite neu laden)
    
    // Formular-Daten auslesen
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        subject: document.getElementById('subject').value.trim(),
        message: document.getElementById('message').value.trim()
    };
    
    // Validierung durchführen
    if (!validateForm(formData)) {
        showMessage('Bitte fülle alle Pflichtfelder korrekt aus!', 'error');
        return;
    }
    
    // Erfolgreiche Validierung
    console.log('Formular-Daten:', formData);
    showMessage('Danke für deine Nachricht! Ich melde mich bald bei dir.', 'success');
    contactForm.reset();
    
    // In einer echten Anwendung würden hier die Daten an ein Backend gesendet:
    // fetch('/api/contact', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(formData)
    // })
    // .then(response => response.json())
    // .then(data => showMessage('Nachricht erfolgreich gesendet!', 'success'))
    // .catch(error => showMessage('Fehler beim Senden. Bitte versuche es erneut.', 'error'));
});

/**
 * Validiert die Formular-Daten
 * @param {Object} data - Die Formular-Daten
 * @returns {boolean} - True wenn valid, sonst false
 */
function validateForm(data) {
    // Name mindestens 2 Zeichen
    if (data.name.length < 2) {
        console.error('Name zu kurz');
        return false;
    }
    
    // E-Mail Format prüfen
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        console.error('Ungültiges E-Mail Format');
        return false;
    }
    
    // Nachricht mindestens 10 Zeichen
    if (data.message.length < 10) {
        console.error('Nachricht zu kurz');
        return false;
    }
    
    return true;
}

/**
 * Zeigt eine Erfolgs- oder Fehlermeldung an
 * @param {string} text - Die anzuzeigende Nachricht
 * @param {string} type - 'success' oder 'error'
 */
function showMessage(text, type) {
    formMessage.textContent = text;
    formMessage.className = `form-message ${type}`;
    
    // Nach 5 Sekunden automatisch ausblenden
    setTimeout(() => {
        formMessage.className = 'form-message';
    }, 5000);
    
    // Scroll zur Nachricht für bessere Sichtbarkeit
    formMessage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}


/* ===================================
   ZUSÄTZLICHE FEATURES (OPTIONAL)
   =================================== */

// Smooth Scroll für Navigation-Links (falls Browser es nicht unterstützt)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Konsolen-Ausgabe für Debugging
console.log('✅ Version 3 JavaScript geladen');
console.log(`📸 ${galleryImages.length} Bilder in der Galerie gefunden`);
