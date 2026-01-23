// MiFa - Mission Future Academy | Musterlösung JavaScript
// ============================================================================

// DOM Elements
const navToggle = document.querySelector('.nav__toggle');
const navMenu = document.querySelector('.nav__menu');
const navLinks = document.querySelectorAll('.nav__link');
const contactForm = document.getElementById('contactForm');
const header = document.getElementById('header');

// ============================================================================
// 1. Mobile Navigation Toggle
// ============================================================================

function toggleNav() {
  const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
  
  navToggle.setAttribute('aria-expanded', !isExpanded);
  navMenu.classList.toggle('active');
  
  // Accessibility: Trap focus in menu when open
  if (!isExpanded) {
    navMenu.querySelector('a').focus();
  }
}

if (navToggle) {
  navToggle.addEventListener('click', toggleNav);
}

// Close menu when clicking on a link
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (navMenu.classList.contains('active')) {
      toggleNav();
    }
  });
});

// Close menu on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && navMenu.classList.contains('active')) {
    toggleNav();
  }
});

// ============================================================================
// 2. Active Navigation Link on Scroll
// ============================================================================

function updateActiveLink() {
  const sections = document.querySelectorAll('section[id]');
  const scrollY = window.pageYOffset;
  
  sections.forEach(section => {
    const sectionHeight = section.offsetHeight;
    const sectionTop = section.offsetTop - 100;
    const sectionId = section.getAttribute('id');
    const navLink = document.querySelector(`.nav__link[href="#${sectionId}"]`);
    
    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      navLinks.forEach(link => link.classList.remove('nav__link--active'));
      navLink?.classList.add('nav__link--active');
    }
  });
}

window.addEventListener('scroll', updateActiveLink);

// ============================================================================
// 3. Header Shadow on Scroll
// ============================================================================

function updateHeader() {
  if (window.scrollY > 50) {
    header.classList.add('header--scrolled');
  } else {
    header.classList.remove('header--scrolled');
  }
}

window.addEventListener('scroll', updateHeader);

// ============================================================================
// 4. Form Validation & Submit
// ============================================================================

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

function showError(inputId, message) {
  const errorElement = document.getElementById(`${inputId}-error`);
  const inputElement = document.getElementById(inputId);
  
  if (errorElement && inputElement) {
    errorElement.textContent = message;
    inputElement.setAttribute('aria-invalid', 'true');
    inputElement.style.borderColor = 'var(--color-error)';
  }
}

function clearError(inputId) {
  const errorElement = document.getElementById(`${inputId}-error`);
  const inputElement = document.getElementById(inputId);
  
  if (errorElement && inputElement) {
    errorElement.textContent = '';
    inputElement.setAttribute('aria-invalid', 'false');
    inputElement.style.borderColor = 'var(--color-border)';
  }
}

function validateForm(formData) {
  let isValid = true;
  
  // Name validation
  const name = formData.get('name');
  if (!name || name.trim().length < 2) {
    showError('name', 'Bitte gib einen gültigen Namen ein (mindestens 2 Zeichen)');
    isValid = false;
  } else {
    clearError('name');
  }
  
  // Email validation
  const email = formData.get('email');
  if (!email || !validateEmail(email)) {
    showError('email', 'Bitte gib eine gültige E-Mail-Adresse ein');
    isValid = false;
  } else {
    clearError('email');
  }
  
  // Message validation
  const message = formData.get('message');
  if (!message || message.trim().length < 10) {
    showError('message', 'Bitte schreibe eine Nachricht (mindestens 10 Zeichen)');
    isValid = false;
  } else {
    clearError('message');
  }
  
  return isValid;
}

function handleFormSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(contactForm);
  
  if (!validateForm(formData)) {
    return;
  }
  
  // Simulate successful submission
  const successMessage = document.getElementById('form-success');
  successMessage.hidden = false;
  successMessage.setAttribute('role', 'alert');
  
  // Reset form
  contactForm.reset();
  
  // Hide success message after 5 seconds
  setTimeout(() => {
    successMessage.hidden = true;
  }, 5000);
  
  // In production: Send data to server
  // fetch('/api/contact', { method: 'POST', body: formData })
  //   .then(response => response.json())
  //   .then(data => console.log(data));
}

if (contactForm) {
  contactForm.addEventListener('submit', handleFormSubmit);
  
  // Real-time validation on blur
  const inputs = contactForm.querySelectorAll('input, textarea');
  inputs.forEach(input => {
    input.addEventListener('blur', () => {
      const formData = new FormData(contactForm);
      validateForm(formData);
    });
  });
}

// ============================================================================
// 5. Smooth Scroll Enhancement (fallback for older browsers)
// ============================================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    
    if (href === '#') return;
    
    const target = document.querySelector(href);
    
    if (target) {
      e.preventDefault();
      
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
      
      // Update URL without jumping
      history.pushState(null, null, href);
    }
  });
});

// ============================================================================
// 6. Accessibility: Focus Management
// ============================================================================

// Ensure keyboard users can see focus
document.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    document.body.classList.add('keyboard-user');
  }
});

document.addEventListener('mousedown', () => {
  document.body.classList.remove('keyboard-user');
});

// ============================================================================
// 7. Initialize on DOM Ready
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  console.log('🌱 MiFa Website geladen - Mission Future Academy');
  
  // Set initial active link
  updateActiveLink();
  
  // Set initial header state
  updateHeader();
});

// ============================================================================
// 8. Performance: Lazy Loading Images (if not using native loading="lazy")
// ============================================================================

if ('IntersectionObserver' in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        observer.unobserve(img);
      }
    });
  });
  
  document.querySelectorAll('img.lazy').forEach(img => {
    imageObserver.observe(img);
  });
}
