# CSS einbinden

Es gibt 3 Möglichkeiten, CSS in HTML einzubinden.

## 1. Externe CSS-Datei (✅ EMPFOHLEN)

Die beste Methode für echte Projekte!

**Vorteile:**
- Wiederverwendbar für mehrere HTML-Seiten
- Übersichtlich und wartbar
- Browser kann CSS cachen (schneller)

**So geht's:**

1. Erstelle einen Ordner `css/` in deinem Projekt
2. Erstelle darin eine Datei `style.css`
3. Verlinke sie im `<head>`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="css/style.css">
  <title>Meine Seite</title>
</head>
<body>
  <h1>Hallo Welt</h1>
</body>
</html>
```

**Wichtig:** Der Pfad muss stimmen!
- `href="css/style.css"` → wenn CSS-Datei im Unterordner `css/`
- `href="style.css"` → wenn CSS-Datei im gleichen Ordner wie HTML

---

## 2. Internes CSS (im `<style>`-Tag)

Für kleine Seiten oder Tests geeignet.

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Meine Seite</title>
  <style>
    body { background-color: lightblue; }
    h1 { color: navy; }
  </style>
</head>
<body>
  <h1>Hallo Welt</h1>
</body>
</html>
```

**Nachteil:** Nicht wiederverwendbar, wird unübersichtlich.

---

## 3. Inline CSS (im `style`-Attribut)

Direkt am Element - **NICHT EMPFOHLEN!**

```html
<h1 style="color: red; font-size: 2rem;">Hallo Welt</h1>
```

**Nachteile:**
- Schwer wartbar
- Nicht wiederverwendbar
- Vermischt Inhalt und Design

**Wann nutzen?** Nur für schnelle Tests oder dynamisches JavaScript-Styling.

---

## Beste Praxis

✅ **Nutze externe CSS-Dateien** für alle Projekte!

**Typische Struktur:**
```
mein-projekt/
├── index.html
├── about.html
└── css/
    └── style.css
```

**In jeder HTML-Datei:**
```html
<link rel="stylesheet" href="css/style.css">
```

---

## Fehlersuche

**CSS wird nicht geladen?**

1. **F12 drücken** → Tab "Network" → Seite neu laden
2. Steht `style.css` in der Liste? 
   - ❌ Nein → Pfad falsch!
   - ✅ Ja, aber rot (404) → Datei existiert nicht oder Pfad falsch
   - ✅ Ja, grün (200) → Alles ok!

3. **Console** checken: Gibt es Fehlermeldungen?

4. Pfad prüfen:
   ```html
   <!-- HTML liegt in: projekt/index.html -->
   <!-- CSS liegt in: projekt/css/style.css -->
   <!-- Dann: -->
   <link rel="stylesheet" href="css/style.css">
   ```

5. Dateinamen prüfen: `style.css` ≠ `Style.css` (Linux beachtet Groß-/Kleinschreibung!)

---

## Mehrere CSS-Dateien einbinden

Für größere Projekte kannst du CSS aufteilen:

```html
<head>
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/style.css">
</head>
```

Die Reihenfolge ist wichtig! Spätere Regeln überschreiben frühere.

---

## Weiter geht's

Jetzt weißt du, wie CSS eingebunden wird! 

Nächste Schritte:
- `css-basis.md` → Selektoren und Eigenschaften
- `css-formatierung.md` → Konkrete Styling-Beispiele
