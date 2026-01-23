# CSS Basis

CSS (Cascading Style Sheets) beschreibt, wie HTML-Elemente auf der Webseite aussehen sollen – von Farben über Schriftarten bis hin zu komplexen Layouts.

## Was ist CSS?

CSS trennt **Inhalt** (HTML) von **Design** (CSS). Das macht Webseiten wartbar und flexibel.

### Syntax

```css
selektor {
  eigenschaft: wert;
  weitere-eigenschaft: wert;
}
```

**Beispiel:**
```css
h1 {
  color: blue;
  font-size: 32px;
  text-align: center;
}
```

---

## Selektoren

Selektoren bestimmen, **welche** Elemente gestylt werden.

### 1. Element-Selektor

Wählt **alle** Elemente eines Typs.

```css
p {
  color: #333;
  line-height: 1.6;
}
```

```html
<p>Dieser Absatz wird grau mit Zeilenhöhe 1.6</p>
<p>Dieser auch!</p>
```

### 2. Klassen-Selektor (`.`)

Wiederverwendbar für mehrere Elemente.

```css
.highlight {
  background-color: yellow;
  font-weight: bold;
}
```

```html
<p class="highlight">Dieser Text ist hervorgehoben</p>
<span class="highlight">Dieser auch!</span>
```

**Wichtig:** Ein Element kann mehrere Klassen haben:
```html
<p class="highlight wichtig">Mehrere Klassen</p>
```

### 3. ID-Selektor (`#`)

Für **einzigartige** Elemente (nur 1x pro Seite!).

```css
#haupttitel {
  color: #0b5cad;
  font-size: 48px;
}
```

```html
<h1 id="haupttitel">Einzigartiger Titel</h1>
```

**Regel:** IDs sollten sparsam verwendet werden. Nutze lieber Klassen!

### 4. Kombinationen

```css
/* Alle p innerhalb von main */
main p {
  color: darkgray;
}

/* Direktes Kind */
nav > ul {
  list-style: none;
}

/* Mehrere Selektoren */
h1, h2, h3 {
  font-family: 'Georgia', serif;
}
```

---

## Wichtige Eigenschaften

### Farben

```css
.element {
  color: red;                    /* Textfarbe */
  background-color: #f0f0f0;     /* Hintergrundfarbe */
  border-color: rgb(200, 50, 50); /* Rahmenfarbe */
}
```

**Farbformate:**
- **Namen**: `red`, `blue`, `lightgray`
- **HEX**: `#ff6347`, `#0b5cad`
- **RGB**: `rgb(255, 99, 71)`
- **RGBA**: `rgba(255, 99, 71, 0.5)` (mit Transparenz)

### Schriften

```css
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  font-weight: normal;  /* normal, bold, 100-900 */
  font-style: italic;
  text-align: center;   /* left, center, right, justify */
  text-decoration: underline;
  line-height: 1.5;
}
```

### Abstände

```css
.box {
  margin: 20px;        /* Außenabstand */
  padding: 15px;       /* Innenabstand */
}
```

Mehr dazu in `box-modell.md`!

---

## Praktisches Beispiel

### HTML (`index.html`)
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Basis Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1 id="haupttitel">Willkommen zu CSS!</h1>
  </header>
  
  <main>
    <p>Dies ist ein normaler Absatz.</p>
    <p class="highlight">Dieser Absatz ist hervorgehoben.</p>
    <p class="wichtig">Wichtiger Text!</p>
  </main>
  
  <footer>
    <p>&copy; 2025 Meine Webseite</p>
  </footer>
</body>
</html>
```

### CSS (`style.css`)
```css
/* Globale Styles */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
  color: #333;
  line-height: 1.6;
}

/* Header */
header {
  background-color: #0b5cad;
  color: white;
  padding: 20px;
  text-align: center;
}

#haupttitel {
  margin: 0;
  font-size: 2.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

/* Main Content */
main {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Klassen */
.highlight {
  background-color: #ffeb3b;
  padding: 10px;
  border-left: 4px solid #ffc107;
}

.wichtig {
  color: #d32f2f;
  font-weight: bold;
  border: 2px solid #d32f2f;
  padding: 10px;
  border-radius: 5px;
}

/* Footer */
footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 15px;
  margin-top: 40px;
}

footer p {
  margin: 0;
  font-size: 0.9rem;
}
```

---

## CSS Cascade & Spezifität

Wenn mehrere Regeln auf ein Element zutreffen, gewinnt die **spezifischste**:

```css
p { color: blue; }              /* Spezifität: 1 */
.highlight { color: yellow; }   /* Spezifität: 10 */
#haupttitel { color: red; }     /* Spezifität: 100 */
```

**Rangfolge:**
1. Inline-Styles (`style="..."`) → 1000
2. IDs (`#id`) → 100
3. Klassen (`.class`) → 10
4. Elemente (`p`, `div`) → 1

**Bei gleicher Spezifität:** Die **letzte** Regel gewinnt.

---

## Best Practices

✅ **Nutze Klassen** statt IDs für Styling
✅ **Vermeide Inline-Styles** (außer für dynamisches JS)
✅ **Nutze aussagekräftige Klassennamen**: `.button-primary` statt `.btn1`
✅ **Gruppiere verwandte Styles** zusammen
✅ **Kommentiere** komplexe Abschnitte

```css
/* ========================================
   Navigation Styles
   ======================================== */
nav {
  /* Styles hier */
}
```

❌ **Vermeide zu spezifische Selektoren**:
```css
/* Schlecht */
div#container main.content article.post p.text { ... }

/* Besser */
.post-text { ... }
```

---

## Häufige Anfängerfehler

❌ **Vergessener Doppelpunkt**
```css
color red;  /* Falsch! */
color: red; /* Richtig */
```

❌ **Vergessenes Semikolon**
```css
p {
  color: blue
  font-size: 16px  /* Zweite Regel wird ignoriert! */
}
```

✅ **Richtig:**
```css
p {
  color: blue;
  font-size: 16px;
}
```

❌ **Punkt vergessen bei Klasse**
```css
highlight { color: red; }  /* Falsch - sucht <highlight> Element */
.highlight { color: red; } /* Richtig - sucht class="highlight" */
```

---

## Nächste Schritte

1. **CSS Formatierung** → `css-formatierung.md` - Erweiterte Textformatierung
2. **Box-Modell** → `box-modell.md` - Margin, Padding, Border verstehen
3. **Responsive Design** → `responsive-design.md` - Mobile Anpassung

---

## Ressourcen

- [MDN CSS Reference](https://developer.mozilla.org/de/docs/Web/CSS)
- [CSS Tricks](https://css-tricks.com/)
- Browser DevTools (F12) → "Elements" Tab zum Experimentieren
