/**
 * MiFa - Mission Future Academy
 * JavaScript für Interaktivität und Formularvalidierung
 */

// ========================================
// 1. MOBILE NAVIGATION
// ========================================

/**
 * Mobile Navigation Toggle
 * Öffnet und schließt das Hamburger-Menü
 */
function initMobileNav() {
    const navToggle = document.getElementById('navToggle');
    const nav = document.getElementById('mainNav');
    
    if (!navToggle || !nav) return;
    
    // Toggle-Funktion
    navToggle.addEventListener('click', () => {
        const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
        
        navToggle.setAttribute('aria-expanded', !isExpanded);
        navToggle.classList.toggle('active');
        nav.classList.toggle('active');
    });
    
    // Schließe Menü bei Klick auf Navigation-Link
    const navLinks = nav.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            nav.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false');
        });
    });
    
    // Schließe Menü bei Klick außerhalb
    document.addEventListener('click', (e) => {
        if (!nav.contains(e.target) && !navToggle.contains(e.target)) {
            navToggle.classList.remove('active');
            nav.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false');
        }
    });
}

// ========================================
// 2. SMOOTH SCROLLING
// ========================================

/**
 * Smooth Scrolling für Anker-Links
 * Fügt sanftes Scrollen zu Sektionen hinzu
 */
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            
            // Ignoriere leere Anker
            if (href === '#' || href === '#!') return;
            
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                
                // Berechne Header-Höhe für Offset
                const header = document.querySelector('.header');
                const headerHeight = header ? header.offsetHeight : 0;
                
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ========================================
// 3. FORMULARVALIDIERUNG
// ========================================

/**
 * Validierungs-Regeln
 */
const validationRules = {
    name: {
        required: true,
        minLength: 2,
        errorMessage: 'Bitte geben Sie einen Namen mit mindestens 2 Zeichen ein.'
    },
    email: {
        required: true,
        pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        errorMessage: 'Bitte geben Sie eine gültige E-Mail-Adresse ein.'
    },
    message: {
        required: true,
        minLength: 10,
        errorMessage: 'Bitte geben Sie eine Nachricht mit mindestens 10 Zeichen ein.'
    },
    privacy: {
        required: true,
        errorMessage: 'Bitte akzeptieren Sie die Datenschutzerklärung.'
    }
};

/**
 * Validiert ein einzelnes Feld
 * @param {HTMLElement} field - Das zu validierende Formularfeld
 * @returns {boolean} - true wenn valid, false wenn invalid
 */
function validateField(field) {
    const fieldName = field.name;
    const fieldValue = field.value.trim();
    const rules = validationRules[fieldName];
    
    if (!rules) return true;
    
    const errorElement = document.getElementById(`${fieldName}-error`);
    
    // Required Check
    if (rules.required && !fieldValue) {
        if (field.type === 'checkbox') {
            if (!field.checked) {
                showError(field, errorElement, rules.errorMessage);
                return false;
            }
        } else {
            showError(field, errorElement, rules.errorMessage);
            return false;
        }
    }
    
    // MinLength Check
    if (rules.minLength && fieldValue.length < rules.minLength) {
        showError(field, errorElement, rules.errorMessage);
        return false;
    }
    
    // Pattern Check (z.B. für E-Mail)
    if (rules.pattern && !rules.pattern.test(fieldValue)) {
        showError(field, errorElement, rules.errorMessage);
        return false;
    }
    
    // Feld ist valide
    clearError(field, errorElement);
    return true;
}

/**
 * Zeigt Fehlermeldung an
 */
function showError(field, errorElement, message) {
    field.classList.add('error');
    field.setAttribute('aria-invalid', 'true');
    
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.setAttribute('role', 'alert');
    }
}

/**
 * Entfernt Fehlermeldung
 */
function clearError(field, errorElement) {
    field.classList.remove('error');
    field.setAttribute('aria-invalid', 'false');
    
    if (errorElement) {
        errorElement.textContent = '';
        errorElement.removeAttribute('role');
    }
}

/**
 * Initialisiert Formularvalidierung
 */
function initFormValidation() {
    const form = document.getElementById('contactForm');
    if (!form) return;
    
    // Real-time Validierung bei Blur
    const fields = form.querySelectorAll('input, textarea, select');
    fields.forEach(field => {
        field.addEventListener('blur', () => {
            validateField(field);
        });
        
        // Entferne Fehler beim Tippen
        field.addEventListener('input', () => {
            if (field.classList.contains('error')) {
                validateField(field);
            }
        });
    });
    
    // Form Submit Handler
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validiere alle Felder
        let isValid = true;
        fields.forEach(field => {
            if (validationRules[field.name]) {
                const fieldValid = validateField(field);
                if (!fieldValid) isValid = false;
            }
        });
        
        if (!isValid) {
            // Scrolle zum ersten Fehler
            const firstError = form.querySelector('.error');
            if (firstError) {
                firstError.focus();
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            return;
        }
        
        // Formular ist valide - sende Daten
        await submitForm(form);
    });
}

/**
 * Sendet Formulardaten (Simulation)
 * In der Praxis würde hier ein echter API-Call stattfinden
 */
async function submitForm(form) {
    const submitButton = form.querySelector('button[type="submit"]');
    const messageElement = document.getElementById('formMessage');
    
    // Button deaktivieren während des Sendens
    submitButton.disabled = true;
    submitButton.textContent = 'Wird gesendet...';
    
    try {
        // Simuliere API-Call
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Formular-Daten sammeln
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        console.log('Formulardaten:', data);
        
        // Erfolgsmeldung anzeigen
        showFormMessage(messageElement, 'success', 
            '✅ Vielen Dank für Ihre Nachricht! Wir melden uns bald bei Ihnen.');
        
        // Formular zurücksetzen
        form.reset();
        
        // Scrolle zur Erfolgsmeldung
        messageElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
    } catch (error) {
        console.error('Fehler beim Senden:', error);
        
        showFormMessage(messageElement, 'error', 
            '❌ Es ist ein Fehler aufgetreten. Bitte versuchen Sie es später erneut.');
            
    } finally {
        // Button wieder aktivieren
        submitButton.disabled = false;
        submitButton.textContent = 'Nachricht senden';
    }
}

/**
 * Zeigt Formular-Nachricht an
 */
function showFormMessage(element, type, message) {
    element.className = `form-message ${type}`;
    element.textContent = message;
    
    // Auto-Hide nach 5 Sekunden
    setTimeout(() => {
        element.className = 'form-message';
        element.textContent = '';
    }, 5000);
}

// ========================================
// 4. SCROLL EFFECTS
// ========================================

/**
 * Header Scroll Effect
 * Fügt Schatten hinzu wenn gescrollt wird
 */
function initHeaderScrollEffect() {
    const header = document.querySelector('.header');
    if (!header) return;
    
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Füge Klasse hinzu wenn gescrollt
        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
}

// ========================================
// 5. INTERSECTION OBSERVER (Animate on Scroll)
// ========================================

/**
 * Fade-In Animation beim Scrollen
 */
function initScrollAnimations() {
    // Prüfe ob Reduced Motion bevorzugt wird
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Beobachte Elemente die animiert werden sollen
    const animateElements = document.querySelectorAll(
        '.feature-card, .project-card, .service-card, .team-member'
    );
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });
}

// CSS Klasse für Animation hinzufügen
const style = document.createElement('style');
style.textContent = `
    .fade-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
    
    .header.scrolled {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
`;
document.head.appendChild(style);

// ========================================
// 6. LAZY LOADING IMAGES
// ========================================

/**
 * Lazy Loading für Bilder (Fallback für ältere Browser)
 */
function initLazyLoading() {
    // Browser mit nativer lazy loading Unterstützung
    if ('loading' in HTMLImageElement.prototype) {
        return;
    }
    
    // Fallback für ältere Browser
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// ========================================
// 7. ACCESSIBILITY HELPERS
// ========================================

/**
 * Tastatur-Navigation für Mobile Menu
 */
function initKeyboardNav() {
    const nav = document.getElementById('mainNav');
    const navToggle = document.getElementById('navToggle');
    
    if (!nav || !navToggle) return;
    
    // Escape-Taste schließt das Menü
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && nav.classList.contains('active')) {
            navToggle.classList.remove('active');
            nav.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false');
            navToggle.focus();
        }
    });
}

/**
 * Skip to Main Content Link
 */
function initSkipLink() {
    // Erstelle Skip-Link wenn nicht vorhanden
    if (!document.querySelector('.skip-link')) {
        const skipLink = document.createElement('a');
        skipLink.href = '#main';
        skipLink.className = 'skip-link';
        skipLink.textContent = 'Zum Hauptinhalt springen';
        
        // Füge CSS hinzu
        const style = document.createElement('style');
        style.textContent = `
            .skip-link {
                position: absolute;
                top: -40px;
                left: 0;
                background: var(--color-primary);
                color: white;
                padding: 8px 16px;
                text-decoration: none;
                z-index: 1000;
            }
            
            .skip-link:focus {
                top: 0;
            }
        `;
        
        document.head.appendChild(style);
        document.body.insertBefore(skipLink, document.body.firstChild);
        
        // Füge ID zum Main-Element hinzu falls nicht vorhanden
        const main = document.querySelector('main');
        if (main && !main.id) {
            main.id = 'main';
        }
    }
}

// ========================================
// 8. PERFORMANCE MONITORING
// ========================================

/**
 * Performance Logging (nur in Development)
 */
function logPerformance() {
    if (!window.performance || window.location.hostname === 'localhost') return;
    
    window.addEventListener('load', () => {
        setTimeout(() => {
            const perfData = window.performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            const connectTime = perfData.responseEnd - perfData.requestStart;
            
            console.log('📊 Performance Metrics:');
            console.log(`Page Load Time: ${pageLoadTime}ms`);
            console.log(`Server Response Time: ${connectTime}ms`);
        }, 0);
    });
}

// ========================================
// 9. INITIALISIERUNG
// ========================================

/**
 * Hauptinitialisierung
 * Wird aufgerufen wenn DOM geladen ist
 */
function init() {
    console.log('🚀 MiFa Website initialisiert');
    
    // Navigation
    initMobileNav();
    initSmoothScrolling();
    initKeyboardNav();
    
    // Formular
    initFormValidation();
    
    // Scroll Effects
    initHeaderScrollEffect();
    initScrollAnimations();
    
    // Performance
    initLazyLoading();
    initSkipLink();
    logPerformance();
    adjustHeroBackgroundForViewport();
    
    console.log('✅ Alle Features geladen');
}

// Event Listener für DOM Ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// ========================================
// 10. GLOBALE ERROR HANDLER
// ========================================

/**
 * Globaler Error Handler für unerwartete Fehler
 */
window.addEventListener('error', (e) => {
    console.error('❌ JavaScript Error:', e.error);
    
    // In Production: Error an Monitoring-Service senden
    // In Development: Nur loggen
    if (window.location.hostname !== 'localhost') {
        // Hier würde normalerweise ein Error-Tracking Service aufgerufen werden
        // z.B. Sentry, LogRocket, etc.
    }
});

/**
 * Handler für unhandled Promise Rejections
 */
window.addEventListener('unhandledrejection', (e) => {
    console.error('❌ Unhandled Promise Rejection:', e.reason);
});

// ========================================
// 10. HINTERGRUND-ANPASSUNG HERO
// ========================================

/**
 * Prüft, ob das Hero-Hintergrundbild für den aktuellen Viewport geeignet ist.
 * Wenn das Bild im Verhältnis zur Fensterhöhe zu hoch ist, wird der
 * Hintergrund deaktiviert (Klasse .hero--no-bg).
 */
function adjustHeroBackgroundForViewport() {
    const hero = document.querySelector('.hero');
    const heroImg = document.querySelector('.hero-bg img');
    
    if (!hero || !heroImg) return;

    const evaluate = () => {
        const vw = window.innerWidth || document.documentElement.clientWidth;
        const vh = window.innerHeight || document.documentElement.clientHeight;

        // Warte bis Bild geladen ist
        if (!heroImg.naturalWidth || !heroImg.naturalHeight) {
            return;
        }

        // Aspect Ratio Vergleich: Bild vs Viewport
        const imageAR = heroImg.naturalWidth / heroImg.naturalHeight;
        const viewportAR = vw / vh;

        // Regel: Wenn Bild "höher" als Viewport ist (vertikaler)
        // UND die natürliche Höhe den Viewport deutlich überschreitet
        const aspectTooTall = imageAR < viewportAR * 0.9; // 10% Toleranz
        const absoluteTooTall = heroImg.naturalHeight > vh * 1.5; // 150% Viewport-Höhe
        
        const isTooTall = aspectTooTall && absoluteTooTall;

        if (isTooTall) {
            hero.classList.add('hero--no-bg');
            console.log('🖼️ Hero-Hintergrund deaktiviert (Bild zu hoch für Viewport)');
        } else {
            hero.classList.remove('hero--no-bg');
        }
    };

    // Initial evaluation
    if (heroImg.complete && heroImg.naturalWidth) {
        evaluate();
    } else {
        heroImg.addEventListener('load', evaluate);
        heroImg.addEventListener('error', () => {
            // Bei Fehler: BG anzeigen (Fallback-Farbe wird verwendet)
            hero.classList.remove('hero--no-bg');
        });
    }

    // Neu evaluieren bei Resize (mit Debounce)
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(evaluate, 150);
    });
}

// ========================================
// EXPORT FÜR MODULE (Optional)
// ========================================

// Wenn du später Module verwenden möchtest:
// export { initMobileNav, initFormValidation, validateField };
