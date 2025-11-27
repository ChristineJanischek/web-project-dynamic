# Version 3 - Musterlösung

## ✅ Vollständige Implementierung

Dies ist die **Musterlösung** für Version 3. Nutze sie zur Selbstkontrolle!

### 📂 Dateien

- **`index.html`** - Vollständige HTML-Struktur
- **`css/style.css`** - Komplette CSS-Styles
- **`js/script.js`** - JavaScript-Funktionalität
- **`images/`** - Platzhalter-Bilder (Picsum)

### 🎯 Implementierte Features

#### ✅ Hero Section
- Hintergrundbild mit Gradient-Overlay
- Parallax-Effekt (`background-attachment: fixed`)
- Responsive Typography

#### ✅ Bildgalerie
- CSS Grid mit `repeat(auto-fit, minmax(300px, 1fr))`
- 9 responsive Bilder
- Hover-Effekte (Scale & Shadow)
- `object-fit: cover` für einheitliche Größen

#### ✅ Lightbox
- Vollbild-Modal mit Overlay
- Navigation (Pfeile, Tastatur)
- Schließen (X, Escape, Außenklick)
- Caption zeigt Alt-Text
- Smooth Animations

#### ✅ Kontaktformular
- 4 Felder (Name, Email, Betreff, Nachricht)
- HTML5-Validierung (required, email, minlength)
- JavaScript-Validierung mit Regex
- Erfolgs-/Fehlermeldungen
- Modernes Styling mit Gradient-Button

#### ✅ Header & Navigation
- Sticky Header
- Smooth Scrolling zu Sektionen
- Gradient-Hintergrund

#### ✅ Responsive Design
- Desktop (> 1024px): 3-4 Bilder pro Zeile
- Tablet (768-1024px): 2-3 Bilder pro Zeile
- Mobile (< 768px): 1-2 Bilder pro Zeile
- Navigation stapelt vertikal auf Mobile

### 🧪 So testest du die Lösung

1. **Browser öffnen**
   ```bash
   # In VS Code: Rechtsklick auf index.html → "Open with Live Server"
   # Oder: Datei direkt im Browser öffnen
   ```

2. **Funktionen testen**
   - [ ] Hero-Bild lädt
   - [ ] Galerie zeigt 9 Bilder
   - [ ] Klick auf Bild → Lightbox öffnet
   - [ ] Pfeile/Tastatur navigieren zwischen Bildern
   - [ ] Escape/X schließt Lightbox
   - [ ] Formular validiert Eingaben
   - [ ] Submit zeigt Erfolgsmeldung

3. **Responsive testen**
   - DevTools (F12) → Toggle Device Toolbar
   - Teste verschiedene Viewports
   - Prüfe Mobile Navigation

### 📖 Vergleich mit deiner Lösung

**Tipps zum Vergleichen:**
1. Öffne deine Lösung (`../aufgabe/`) und diese Musterlösung nebeneinander
2. Vergleiche HTML-Struktur
3. Vergleiche CSS-Klassen und Styles
4. Vergleiche JavaScript-Logik

**Fragen zur Lösung:**
- Warum `box-sizing: border-box`?
- Was macht `repeat(auto-fit, minmax(...))`?
- Wie funktioniert der Modulo-Operator `%` bei der Bildnavigation?
- Warum `e.preventDefault()` bei Submit?

### 🎓 Lernpunkte

**HTML:**
- Semantische Struktur (header, main, section, footer)
- Formular mit Labels und Validierung
- Accessibility (Alt-Texte)

**CSS:**
- CSS Grid für responsive Layouts
- Transitions & Animations
- Flexbox für Navigation
- Media Queries
- Gradient Backgrounds

**JavaScript:**
- Event Listeners (click, keydown, submit)
- DOM-Manipulation (classList, textContent)
- Array-Methoden (forEach, querySelectorAll)
- Regex für E-Mail-Validierung
- Modulo für zyklische Navigation

### 🔍 Code-Highlights

**CSS Grid Auto-Responsive:**
```css
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```
→ Automatisch so viele Spalten wie möglich, mindestens 300px breit

**Zyklische Bildnavigation:**
```javascript
currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
```
→ Springt von letztem Bild zum ersten

**E-Mail Regex:**
```javascript
/^[^\s@]+@[^\s@]+\.[^\s@]+$/
```
→ Prüft grundlegendes E-Mail-Format

### 💡 Erweiterungsmöglichkeiten

- [ ] Lazy Loading für Bilder
- [ ] Swipe-Gesten für Mobile Lightbox
- [ ] Formular-Daten mit LocalStorage speichern
- [ ] Bildfilter mit CSS (`filter` Property)
- [ ] Backend-Integration (PHP/Node.js)

### 📚 Weitere Ressourcen

- [`../README.md`](../README.md) - Aufgabenstellung & Anleitung
- [`../../docs/`](../../docs/) - Theorie-Dokumentationen
- [MDN Web Docs](https://developer.mozilla.org) - HTML/CSS/JS Referenz

---

**Gut gemacht, wenn du so weit gekommen bist!** 🎉 Weiter zu Version 4!
