# Galerien

Einfache Galerie mit CSS Grid:
```html
<div class="galerie">
  <img src="bilder/img1.jpg" alt="1">
  <img src="bilder/img2.jpg" alt="2">
  <img src="bilder/img3.jpg" alt="3">
</div>
```
```css
.galerie {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(150px,1fr));
  gap: 10px;
}
.galerie img { width: 100%; display: block; }
```
Weiter: `formulare.md`.
