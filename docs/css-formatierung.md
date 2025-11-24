# CSS Formatierung - Praktische Beispiele

Hier lernst du die wichtigsten CSS-Eigenschaften für die Formatierung deiner Webseite.

## Textformatierung

### Schriftart
```css
body {
  font-family: Arial, Helvetica, sans-serif;
}
```
**Tipp:** Gib mehrere Schriften an als Fallback!

### Schriftgröße
```css
h1 { font-size: 2rem; }      /* relativ zur Wurzelgröße */
p { font-size: 16px; }        /* absolut in Pixel */
small { font-size: 0.9em; }   /* relativ zum Eltern-Element */
```

### Schriftgewicht
```css
h1 { font-weight: bold; }     /* oder: 700 */
p { font-weight: normal; }    /* oder: 400 */
strong { font-weight: 600; }
```

### Textfarbe
```css
h1 { color: #e74c3c; }        /* Hexadezimal */
p { color: rgb(51, 51, 51); } /* RGB */
a { color: blue; }            /* Farbname */
```

### Text ausrichten
```css
h1 { text-align: center; }
p { text-align: left; }       /* Standard */
footer { text-align: right; }
```

### Zeilenhöhe (wichtig für Lesbarkeit!)
```css
p {
  line-height: 1.6;  /* 1.6 = 160% der Schriftgröße */
}
```

### Text-Dekoration
```css
a { text-decoration: none; }           /* Unterstrich weg */
a:hover { text-decoration: underline; } /* Beim Hover zeigen */
```

---

## Farben und Hintergründe

### Hintergrundfarbe
```css
body { background-color: #f5f5f5; }
header { background-color: #2c3e50; }
```

### Hintergrundbilder
```css
body {
  background-image: url('../images/bg.jpg');
  background-size: cover;
  background-repeat: no-repeat;
}
```

---

## Abstände (Box-Modell)

### Margin (Außenabstand)
```css
section {
  margin-top: 2rem;
  margin-bottom: 2rem;
  /* Oder kurz: */
  margin: 2rem 0;  /* oben/unten links/rechts */
}
```

### Padding (Innenabstand)
```css
header {
  padding: 2rem 1rem;  /* oben/unten links/rechts */
}

div {
  padding: 10px;  /* alle Seiten gleich */
}
```

### Kombinationen
```css
.box {
  margin: 1rem;      /* Außenabstand */
  padding: 2rem;     /* Innenabstand */
  border: 2px solid #ccc;  /* Rahmen */
}
```

---

## Rahmen (Borders)

```css
.card {
  border: 1px solid #ddd;        /* Durchgehend */
  border-radius: 8px;            /* Abgerundete Ecken */
  border-left: 4px solid red;    /* Nur links, dicker */
}
```

---

## Schatten

### Box-Shadow (Elementen-Schatten)
```css
.card {
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  /* x-offset y-offset blur-radius color */
}
```

### Text-Shadow
```css
h1 {
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
```

---

## Layout-Eigenschaften

### Breite und Höhe
```css
.container {
  width: 100%;
  max-width: 900px;  /* Nicht breiter als 900px */
  height: auto;
}
```

### Zentrieren (horizontal)
```css
.container {
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  /* Oder kurz: */
  margin: 0 auto;
}
```

---

## Links formatieren

```css
/* Standard-Zustand */
a {
  color: #3498db;
  text-decoration: none;
}

/* Beim Drüberfahren */
a:hover {
  color: #e74c3c;
  text-decoration: underline;
}

/* Besuchte Links */
a:visited {
  color: purple;
}

/* Beim Klicken */
a:active {
  color: red;
}
```

---

## Übergänge (Transitions)

Sanfte Animationen bei Änderungen:

```css
a {
  color: blue;
  transition: color 0.3s ease;
}

a:hover {
  color: red;  /* Farbwechsel dauert 0.3 Sekunden */
}

button {
  background: #3498db;
  transition: all 0.3s ease;
}

button:hover {
  background: #2980b9;
  transform: translateY(-2px);
}
```

---

## Praktisches Beispiel: Card-Design

```css
.card {
  /* Layout */
  max-width: 400px;
  margin: 2rem auto;
  padding: 1.5rem;
  
  /* Farben */
  background-color: white;
  color: #333;
  
  /* Rahmen & Schatten */
  border-radius: 8px;
  border-left: 4px solid #e74c3c;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  
  /* Animation */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.card h3 {
  color: #e74c3c;
  margin-top: 0;
}

.card p {
  line-height: 1.6;
}
```

---

## Häufige Fehler vermeiden

❌ **Falsch:**
```css
/* Zu viele Pixel-Angaben */
h1 { font-size: 32px; }
p { font-size: 16px; }
```

✅ **Besser:**
```css
/* Relative Einheiten */
h1 { font-size: 2rem; }
p { font-size: 1rem; }
```

❌ **Falsch:**
```css
/* Farben ohne Kontrast */
p { color: #ccc; background: #ddd; }
```

✅ **Besser:**
```css
/* Guter Kontrast */
p { color: #333; background: #fff; }
```

---

## Einheiten im Überblick

| Einheit | Bedeutung | Wann nutzen? |
|---------|-----------|--------------|
| `px` | Pixel | Feste Größen (Rahmen) |
| `%` | Prozent | Flexible Breiten |
| `rem` | Relativ zur Wurzel | Schriftgrößen |
| `em` | Relativ zum Eltern | Abstände |
| `vh/vw` | Viewport-Höhe/Breite | Vollbild-Elemente |

---

## Farbsysteme

### Hexadezimal
```css
color: #e74c3c;  /* Rot */
color: #3498db;  /* Blau */
```

### RGB
```css
color: rgb(231, 76, 60);      /* Rot */
color: rgba(52, 152, 219, 0.5); /* Blau, 50% transparent */
```

### Farbnamen
```css
color: red;
color: lightblue;
color: navy;
```

**Tipp:** Nutze [coolors.co](https://coolors.co) für Farbpaletten!

---

## Weiterführend

- `box-modell.md` → Verstehe Margin, Padding, Border
- `responsive-design.md` → Mobile Anpassungen
- Probiere die Beispiele selbst aus und experimentiere!
