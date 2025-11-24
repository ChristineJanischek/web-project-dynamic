# Responsive Design

Responsive Design bedeutet, dass eine Webseite auf allen Geräten (Desktop, Tablet, Smartphone) gut aussieht und funktioniert.

## Viewport Meta-Tag
**Wichtig!** Immer im `<head>` einfügen:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```
Dies sorgt dafür, dass die Seite auf mobilen Geräten richtig skaliert wird.

## Media Queries
CSS kann auf Bildschirmgröße reagieren:
```css
/* Standard (Desktop) */
.container { width: 1200px; }

/* Tablet */
@media (max-width: 1024px) {
  .container { width: 100%; }
}

/* Mobile */
@media (max-width: 768px) {
  .container { padding: 10px; }
}
```

## Flexbox & Grid
Moderne Layout-Techniken passen sich automatisch an:
```css
/* Flexbox */
.nav { display: flex; flex-wrap: wrap; }

/* Grid - automatische Spalten */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

## Mobile Navigation (Hamburger-Menü)
Auf kleinen Bildschirmen wird das Menü ausgeblendet und per Button (☰) geöffnet:
```html
<button class="nav-toggle">☰</button>
<nav class="hidden-mobile">...</nav>
```
JavaScript zeigt/versteckt das Menü bei Klick.

## Breakpoints (Richtwerte)
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## Best Practices
- **Mobile First**: Erst für kleine Bildschirme designen, dann erweitern.
- **Touch-Friendly**: Buttons mind. 44x44px (Finger!).
- **Bilder**: `max-width: 100%; height: auto;` für Flexibilität.
- **Testen**: Browser DevTools Device-Modus nutzen.

Siehe `shared-examples/` für ein vollständiges Beispiel mit Toggle-Menü.
