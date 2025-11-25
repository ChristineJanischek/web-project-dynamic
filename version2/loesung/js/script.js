/**
 * Mobile Navigation Toggle
 * Implementiert Hamburger-Menü Funktionalität
 */

// 1. DOM-Elemente auswählen
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

// 2. Event Listener für Toggle-Button
navToggle.addEventListener('click', function() {
    // Toggle 'active' Klasse für Navigation (öffnen/schließen)
    mainNav.classList.toggle('active');
    // Toggle 'active' Klasse für Button-Animation (Hamburger zu X)
    navToggle.classList.toggle('active');
});

// 3. Menü schließen beim Klick auf einen Navigationslink
const navLinks = mainNav.querySelectorAll('a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        // Navigation schließen
        mainNav.classList.remove('active');
        navToggle.classList.remove('active');
    });
});

// 4. Optional: Menü schließen bei Klick außerhalb
document.addEventListener('click', function(event) {
    // Prüfen ob Klick außerhalb von Navigation und Toggle-Button
    const isClickInsideNav = mainNav.contains(event.target);
    const isClickOnToggle = navToggle.contains(event.target);
    
    if (!isClickInsideNav && !isClickOnToggle && mainNav.classList.contains('active')) {
        mainNav.classList.remove('active');
        navToggle.classList.remove('active');
    });
});
