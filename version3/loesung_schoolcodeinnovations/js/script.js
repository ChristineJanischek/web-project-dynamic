// SchoolCodeInnovations - JavaScript

// Mobile Navigation Toggle
const navToggle = document.querySelector('.nav__toggle');
const nav = document.querySelector('.nav');

if (navToggle) {
  navToggle.addEventListener('click', () => {
    nav.classList.toggle('nav--active');
  });
}

// Smooth Scrolling für Anchor-Links
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

// Form Validation
const contactForm = document.querySelector('.contact-form');

if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const kurs = document.getElementById('kurs').value;
    const message = document.getElementById('message').value.trim();
    
    // Einfache Validierung
    if (!name || !email) {
      alert('Bitte fülle alle Pflichtfelder aus!');
      return;
    }
    
    // Email-Validierung
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Bitte gib eine gültige E-Mail-Adresse ein!');
      return;
    }
    
    // Erfolgreiche Validierung
    alert('Vielen Dank für deine Nachricht! Wir melden uns bald bei dir.');
    contactForm.reset();
  });
}

// Scroll-Animation für Sections
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
    }
  });
}, observerOptions);

document.querySelectorAll('section').forEach(section => {
  observer.observe(section);
});
