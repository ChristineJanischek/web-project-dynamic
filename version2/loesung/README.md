# Musterlösung - Version 2: Box-Modell & Responsive Layout

Diese Musterlösung demonstriert alle Anforderungen aus der Version 2 Aufgabenstellung.

## Implementierte Features

### ✅ Teil 1: Box-Modell
- Drei unterschiedliche Boxen mit verschiedenen:
  - Padding-Werten
  - Border-Stilen
  - Margin-Abständen
- Demonstration von `content-box` vs. `border-box`
- Schatten und Border-Radius

### ✅ Teil 2: Responsive Layout
- **Desktop** (> 1024px): 3-spaltiges Grid
- **Tablet** (768px - 1024px): 2-spaltiges Grid
- **Mobile** (< 768px): 1-spaltiges Layout

### ✅ Teil 3: Mobile Navigation
- Hamburger-Menü für Mobile
- Slide-in Animation
- JavaScript Toggle-Funktionalität
- Schließen beim Klick auf Links

## Verwendete Techniken

### CSS
- CSS Box-Modell mit `box-sizing: border-box`
- Flexbox für flexible Layouts
- Media Queries für Responsive Design
- CSS-Variablen für konsistente Farben
- Transitions für sanfte Animationen

### JavaScript
- DOM-Manipulation
- Event Listeners
- classList Toggle

## Testen

Öffne `index.html` im Browser und teste:
1. Verändere die Browsergröße → Grid passt sich an
2. Mobile-Ansicht (< 768px) → Hamburger-Menü erscheint
3. Klicke auf Hamburger-Button → Navigation öffnet/schließt
4. DevTools (F12) → Box-Modell in "Computed" Tab prüfen

## Lernpunkte

- Das Box-Modell ist fundamental für CSS-Layout
- `border-box` macht Berechnungen einfacher
- Mobile-First Ansatz ist oft effizienter
- Media Queries ermöglichen flexible Designs
- JavaScript erweitert CSS um Interaktivität

---

**Erstellt:** 2025-11-25  
**Lernziel:** Box-Modell & Responsive Design beherrschen
