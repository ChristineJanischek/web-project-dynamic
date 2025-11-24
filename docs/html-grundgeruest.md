# HTML Grundgerüst

Ein minimales HTML5-Dokument:
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Meine erste Seite</title>
</head>
<body>
  <h1>Hallo Welt</h1>
  <p>Mein erster Absatz.</p>
</body>
</html>
```

## Zeile für Zeile erklärt

### `<!DOCTYPE html>`
- **Pflicht** an erster Stelle!
- Sagt dem Browser: "Dies ist ein HTML5-Dokument"
- Ohne DOCTYPE: Browser nutzt veraltete Rendering-Modi

### `<html lang="de">`
- Das **Wurzelelement** - umschließt alles
- `lang="de"` = Sprache ist Deutsch
  - Hilft Screenreadern (Vorleseprogramme)
  - Hilft Suchmaschinen
  - Andere Sprachen: `en` (Englisch), `fr` (Französisch)...

### `<head>` - Metadaten (nicht sichtbar)

Enthält Informationen **über** die Seite:

#### `<meta charset="UTF-8">`
- Zeichensatz festlegen
- UTF-8 = Universeller Standard (Umlaute, Emojis, alle Sprachen)
- **Wichtig:** Immer als erstes im `<head>`!

#### `<meta name="viewport" ...>`
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
- **Unverzichtbar für Responsive Design!**
- `width=device-width` → Breite = Gerätbreite
- `initial-scale=1.0` → Keine Zoom beim Laden
- Ohne dies: Mobile Geräte zeigen Desktop-Version verkleinert

#### `<title>`
- Erscheint im **Browser-Tab**
- Wichtig für **Suchmaschinen** (SEO)
- Sollte beschreibend sein (nicht nur "Startseite")

### `<body>` - Der sichtbare Inhalt

Alles was im Browser angezeigt wird, kommt hierhin!

```html
<body>
  <h1>Hauptüberschrift</h1>
  <p>Ein Absatz Text.</p>
  <img src="bild.jpg" alt="Beschreibung">
</body>
```

---

## Wichtige Tags im Überblick

### Überschriften (6 Ebenen)
```html
<h1>Wichtigste Überschrift (nur 1x pro Seite!)</h1>
<h2>Unterüberschrift</h2>
<h3>Unter-Unterüberschrift</h3>
<h4>Ebene 4</h4>
<h5>Ebene 5</h5>
<h6>Kleinste Überschrift</h6>
```

**Regel:** Hierarchie einhalten! Nicht von `<h1>` zu `<h3>` springen.

### Absätze und Text
```html
<p>Ein normaler Absatz.</p>
<strong>Fettgedruckt (wichtig)</strong>
<em>Kursiv (betont)</em>
<br>  <!-- Zeilenumbruch -->
```

### Links
```html
<a href="https://example.com">Externer Link</a>
<a href="#kontakt">Interner Ankerlink</a>
<a href="about.html">Link zu anderer Seite</a>
```

### Bilder
```html
<img src="pfad/zum/bild.jpg" alt="Beschreibung für Screenreader">
```

### Listen
```html
<!-- Ungeordnete Liste -->
<ul>
  <li>Punkt 1</li>
  <li>Punkt 2</li>
</ul>

<!-- Geordnete Liste -->
<ol>
  <li>Erster Punkt</li>
  <li>Zweiter Punkt</li>
</ol>
```

---

## Vollständiges Beispiel

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Meine erste Webseite über Webentwicklung">
  <meta name="author" content="Max Mustermann">
  <title>Webentwicklung lernen | Meine erste Seite</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h1>Willkommen zur Webentwicklung</h1>
  
  <p>
    Dies ist meine <strong>erste Webseite</strong>. 
    Ich lerne gerade HTML und bin begeistert!
  </p>
  
  <h2>Was ich lerne:</h2>
  <ul>
    <li>HTML Grundlagen</li>
    <li>CSS Styling</li>
    <li>Responsive Design</li>
  </ul>
  
  <p>
    Mehr Infos: <a href="https://developer.mozilla.org">MDN Web Docs</a>
  </p>
</body>
</html>
```

---

## Best Practices

✅ **Immer einrücken** für Lesbarkeit:
```html
<body>
  <header>
    <h1>Titel</h1>
  </header>
</body>
```

✅ **Kleinschreibung** für Tags (Konvention):
```html
<body>  <!-- Gut -->
<BODY>  <!-- Funktioniert, aber nicht schön -->
```

✅ **Tags schließen**:
```html
<p>Text</p>  <!-- Gut -->
<p>Text      <!-- Schlecht -->
```

✅ **Alt-Texte** bei Bildern:
```html
<img src="logo.png" alt="Firmenlogo">
```

---

## Häufige Anfängerfehler

❌ **Falsch:** DOCTYPE fehlt
```html
<html>...</html>
```

✅ **Richtig:**
```html
<!DOCTYPE html>
<html>...</html>
```

❌ **Falsch:** Meta-Tags im Body
```html
<body>
  <meta charset="UTF-8">
</body>
```

✅ **Richtig:** Meta-Tags gehören in den Head
```html
<head>
  <meta charset="UTF-8">
</head>
```

❌ **Falsch:** Mehrere `<h1>` Tags
```html
<h1>Titel 1</h1>
<h1>Titel 2</h1>
```

✅ **Richtig:** Nur eine `<h1>` pro Seite
```html
<h1>Haupttitel</h1>
<h2>Untertitel</h2>
```

---

## Validierung

Überprüfe dein HTML auf Fehler:
1. Öffne [validator.w3.org](https://validator.w3.org/)
2. HTML-Code einfügen oder URL eingeben
3. Fehler beheben!

Oder nutze die Browser-DevTools:
- F12 drücken → Console → Fehler werden rot angezeigt

---

## Nächste Schritte

- `seitenstrukturelemente.md` → Semantische Struktur
- `css-einbinden.md` → Style hinzufügen
- Experimentiere! HTML ist verzeihend - probiere einfach aus!
