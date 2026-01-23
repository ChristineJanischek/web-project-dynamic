# CSS Box-Modell

Das **Box-Modell** ist eines der wichtigsten Konzepte in CSS. Jedes HTML-Element ist eine rechteckige Box mit vier Bereichen.

## Die vier Bereiche

```
┌─────────────────────────────────────┐
│         MARGIN (außen)              │
│  ┌───────────────────────────────┐  │
│  │      BORDER (Rahmen)          │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │   PADDING (innen)       │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │   CONTENT         │  │  │  │
│  │  │  │  (Inhalt/Text)    │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### 1. **Content** (Inhalt)
- Der eigentliche Inhalt: Text, Bilder, etc.
- Gesteuert durch `width` und `height`

### 2. **Padding** (Innenabstand)
- Abstand zwischen Content und Border
- Transparent, nimmt Hintergrundfarbe an

### 3. **Border** (Rahmen)
- Umrandung der Box
- Hat Farbe, Breite und Stil

### 4. **Margin** (Außenabstand)
- Abstand zu anderen Elementen
- Immer transparent

---

## Praktisches Beispiel

### HTML
```html
<div class="box">
  Ich bin eine Box!
</div>
```

### CSS
```css
.box {
  /* Content */
  width: 200px;
  height: 100px;
  
  /* Padding (Innenabstand) */
  padding: 20px;
  
  /* Border (Rahmen) */
  border: 3px solid #e74c3c;
  
  /* Margin (Außenabstand) */
  margin: 30px;
  
  /* Styling */
  background-color: #ecf0f1;
  color: #2c3e50;
}
```

**Ergebnis:**
- Content-Breite: 200px
- + Padding links/rechts: 40px (20px × 2)
- + Border links/rechts: 6px (3px × 2)
- = **Gesamtbreite: 246px**

---

## Einzelne Seiten steuern

Statt alle Seiten gleich, kannst du jede Seite individuell setzen:

```css
.box {
  /* Alle Seiten gleich */
  margin: 20px;
  
  /* Vertikal | Horizontal */
  margin: 10px 20px;
  
  /* Oben | Horizontal | Unten */
  margin: 10px 20px 30px;
  
  /* Oben | Rechts | Unten | Links (im Uhrzeigersinn!) */
  margin: 10px 20px 30px 40px;
  
  /* Einzeln */
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 30px;
  margin-left: 40px;
}
```

**Gilt auch für:** `padding`, `border-width`, etc.

---

## Border Eigenschaften

```css
.box {
  /* Kurzform */
  border: 2px solid red;
  
  /* Ausführlich */
  border-width: 2px;
  border-style: solid;  /* solid, dashed, dotted, double, none */
  border-color: red;
  
  /* Nur eine Seite */
  border-top: 3px dashed blue;
  border-bottom: 1px solid gray;
  
  /* Abgerundete Ecken */
  border-radius: 10px;
}
```

### Border-Styles

```css
.solid { border: 3px solid black; }      /* ──── */
.dashed { border: 3px dashed black; }    /* ---- */
.dotted { border: 3px dotted black; }    /* ···· */
.double { border: 3px double black; }    /* ════ */
.groove { border: 3px groove gray; }     /* 3D effekt */
```

---

## box-sizing Eigenschaft

Standardmäßig wird `width` nur auf den **Content** angewendet. Mit `box-sizing` änderst du das!

### Standard (`content-box`)
```css
.box {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
}
/* Gesamtbreite = 200 + 40 + 10 = 250px */
```

### Besser: `border-box`
```css
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 5px solid black;
}
/* Gesamtbreite = 200px (Padding + Border inbegriffen!) */
```

**Best Practice:** Setze `border-box` global!
```css
* {
  box-sizing: border-box;
}
```

---

## Vollständiges Beispiel

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Box-Modell Demo</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <div class="box box-1">Box 1</div>
    <div class="box box-2">Box 2</div>
    <div class="box box-3">Box 3</div>
  </div>
</body>
</html>
```

### CSS
```css
/* Global: border-box */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  padding: 20px;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

.box {
  /* Content */
  width: 100%;
  padding: 20px;
  margin-bottom: 20px;
  
  /* Styling */
  background-color: white;
  border: 3px solid #3498db;
  border-radius: 8px;
  
  /* Text */
  font-size: 18px;
  color: #2c3e50;
}

.box-1 {
  border-color: #e74c3c;
  border-left-width: 10px;
}

.box-2 {
  border-color: #2ecc71;
  border-style: dashed;
  padding: 30px;
}

.box-3 {
  border-color: #f39c12;
  border-radius: 20px;
  margin-bottom: 0;
}
```

---

## Margin Collapsing

**Achtung:** Vertikale Margins (oben/unten) von benachbarten Elementen **verschmelzen**!

```html
<div style="margin-bottom: 30px;">Box 1</div>
<div style="margin-top: 20px;">Box 2</div>
```

**Erwartung:** 50px Abstand  
**Realität:** 30px Abstand (der größere gewinnt!)

**Lösung:**
- Nutze nur `margin-bottom` ODER `margin-top` (nicht beide)
- Oder verwende Padding stattdessen
- Oder nutze Flexbox/Grid (kein Collapsing!)

---

## Negative Margins

Du kannst auch **negative** Werte verwenden!

```css
.box {
  margin-top: -20px;  /* Schiebt Element 20px nach oben */
}
```

**Vorsicht:** Kann Elemente überlappen lassen!

---

## Debugging mit DevTools

1. **Öffne DevTools** (F12)
2. **Wähle ein Element** (Elements Tab)
3. **Scrolle nach unten** → Siehst du die Box-Modell-Visualisierung!

```
┌─────────────────┐
│ margin          │  blau/orange
│ ┌─────────────┐ │
│ │ border      │ │  gelb
│ │ ┌─────────┐ │ │
│ │ │ padding │ │ │  grün
│ │ │ ┌─────┐ │ │ │
│ │ │ │conte│ │ │ │  blau
│ │ │ │nt   │ │ │ │
```

**Tipp:** Klicke auf Werte, um sie live zu ändern!

---

## Häufige Anfängerfehler

❌ **Vergessen, box-sizing zu setzen**
```css
.box {
  width: 200px;
  padding: 50px;  /* Jetzt ist die Box 300px breit! */
}
```

✅ **Richtig:**
```css
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 50px;  /* Bleibt 200px breit */
}
```

❌ **Margin auf inline Elemente**
```css
span {
  margin-top: 20px;  /* Wirkt NICHT! */
}
```

✅ **Mach es zu Block oder Inline-Block:**
```css
span {
  display: inline-block;
  margin-top: 20px;  /* Jetzt funktioniert's! */
}
```

---

## Praktische Übung

Experimentiere mit diesem Code:

```html
<div class="playground">
  <div class="inner">
    Ändere Padding, Margin und Border in den DevTools!
  </div>
</div>
```

```css
.playground {
  background-color: #ecf0f1;
  padding: 40px;
}

.inner {
  background-color: #3498db;
  color: white;
  padding: 20px;
  border: 5px solid #2c3e50;
  margin: 20px;
}
```

**Aufgabe:**
1. Öffne DevTools (F12)
2. Wähle `.inner` aus
3. Ändere im "Styles" Panel die Werte
4. Beobachte, wie sich die Box verändert!

---

## Nächste Schritte

- **Responsive Design** → `responsive-design.md` - Box-Modell für verschiedene Bildschirmgrößen
- **Bilder & Grafiken** → `bilder-grafiken.md` - Bilder in Boxen einfügen
- **CSS Formatierung** → `css-formatierung.md` - Weitere Styling-Optionen

---

**Merke:** Das Box-Modell ist fundamental! Verstehst du es, verstehst du 50% von CSS!
