// Mobile Navigation Toggle
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

navToggle.addEventListener('click', () => {
  mainNav.classList.toggle('active');
  
  // Animation für Hamburger Icon
  const hamburgers = navToggle.querySelectorAll('.hamburger');
  hamburgers.forEach((bar, index) => {
    if (mainNav.classList.contains('active')) {
      if (index === 0) bar.style.transform = 'rotate(45deg) translateY(10px)';
      if (index === 1) bar.style.opacity = '0';
      if (index === 2) bar.style.transform = 'rotate(-45deg) translateY(-10px)';
    } else {
      bar.style.transform = '';
      bar.style.opacity = '';
    }
  });
});

// Menü schließen beim Klick auf Link (Mobile)
const navLinks = mainNav.querySelectorAll('a');
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      mainNav.classList.remove('active');
      const hamburgers = navToggle.querySelectorAll('.hamburger');
      hamburgers.forEach(bar => {
        bar.style.transform = '';
        bar.style.opacity = '';
      });
    }
  });
});

// Beispiel Button Interaktion
document.getElementById('klick').addEventListener('click', () => {
  alert('🚀 Super! Du bist bereit für deine Webentwicklungs-Reise!\n\nSchaue dir die Dokumentation im docs/ Ordner an und beginne mit den Grundlagen.');
});

// Smooth Scroll für Ankerlinks
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
