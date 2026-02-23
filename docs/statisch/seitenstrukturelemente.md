# Semantische Seitenstrukturelemente

Semantische Tags geben dem Inhalt **Bedeutung** und helfen:

- **Suchmaschinen** die Seite zu verstehen (SEO)
- **Screenreadern** bei der Navigation
- **Entwicklern** den Code schneller zu verstehen

## Warum semantisch?

Siehe auch: [HTML Grundgerüst](html-grundgeruest.md) für grundlegende Struktur.

❌ **Alte Methode** (alles `<div>`):

```html
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">...</div>
<div class="footer">...</div>
```

✅ **Moderne Methode** (semantisch):

```html
<header>
  <nav>...</nav>
</header>
<main>...</main>
<footer>...</footer>
```

**Vorteile:**

- Lesbarer Code
- Besseres SEO
- Barrierefreiheit

---

## Die wichtigsten semantischen Tags

| Tag         | Bedeutung               | Verwendung                    |
| ----------- | ----------------------- | ----------------------------- |
| `<header>`  | Kopfbereich             | Logo, Titel, Navigation       |
| `<nav>`     | Navigationslinks        | Menü, Hauptnavigation         |
| `<main>`    | Hauptinhalt             | Der zentrale Inhalt (nur 1x!) |
| `<section>` | Thematische Gruppierung | Ein zusammenhängender Bereich |
| `<article>` | Eigenständiger Inhalt   | Blogpost, News-Artikel        |
| `<aside>`   | Randinfo, Sidebar       | Zusatzinfos, Werbung          |
| `<footer>`  | Fußbereich              | Copyright, Links, Kontakt     |

---

## `<header>` - Kopfbereich

Enthält meist Logo, Titel und Navigation.

```html
<header>
  <h1>Meine Webseite</h1>
  <nav>
    <a href="#home">Home</a>
    <a href="#about">Über mich</a>
    <a href="#contact">Kontakt</a>
  </nav>
</header>
```

**Wichtig:** Kann mehrfach vorkommen (z.B. auch in `<article>`), aber meist nur 1x ganz oben.

---

## `<nav>` - Navigation

Für Hauptnavigationslinks.

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">Über uns</a></li>
    <li><a href="contact.html">Kontakt</a></li>
  </ul>
</nav>
```

**Tipp:** Nicht für jeden einzelnen Link! Nur für die Hauptnavigation.

---

## `<main>` - Hauptinhalt

Der zentrale, einzigartige Inhalt der Seite.

```html
<main>
  <h1>Willkommen</h1>
  <p>Dies ist der Hauptinhalt...</p>
</main>
```

**Regel:** Nur **einmal pro Seite**! Nicht in `<header>`, `<footer>` oder `<aside>` verschachteln.

---

## `<section>` - Thematische Gruppierung

Für zusammenhängende Inhaltsbereiche, meist mit eigener Überschrift.

```html
<main>
  <section id="about">
    <h2>Über mich</h2>
    <p>Ich bin...</p>
  </section>

  <section id="skills">
    <h2>Meine Fähigkeiten</h2>
    <ul>
      <li>HTML</li>
      <li>CSS</li>
    </ul>
  </section>
</main>
```

---

## `<article>` - Eigenständiger Inhalt

Für in sich abgeschlossene Inhalte (Blogposts, News, Kommentare).

```html
<article>
  <h2>Mein erster Blogpost</h2>
  <p>Veröffentlicht am 21.11.2025</p>
  <p>Heute habe ich gelernt...</p>
</article>
```

**Faustregel:** Könnte dieser Inhalt woanders wiederverwendet werden? → Dann `<article>`

---

## `<aside>` - Randinfo / Sidebar

Für Inhalte, die ergänzend sind (nicht zum Hauptinhalt gehören).

```html
<aside>
  <h3>Weitere Infos</h3>
  <p>Dies ist eine Sidebar...</p>
</aside>
```

**Beispiele:** Werbung, verwandte Artikel, Social-Media-Widgets

---

## `<footer>` - Fußbereich

Am Ende der Seite oder eines Artikels.

```html
<footer>
  <p>&copy; 2025 Meine Webseite</p>
  <nav>
    <a href="impressum.html">Impressum</a>
    <a href="datenschutz.html">Datenschutz</a>
  </nav>
</footer>
```

---

## Vollständiges Beispiel

```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Semantische Struktur Beispiel</title>
  </head>
  <body>
    <!-- Kopfbereich -->
    <header>
      <h1>🌐 Meine Lern-Webseite</h1>
      <nav>
        <a href="#home">Home</a>
        <a href="#about">Über mich</a>
        <a href="#blog">Blog</a>
        <a href="#contact">Kontakt</a>
      </nav>
    </header>

    <!-- Hauptinhalt -->
    <main>
      <!-- Begrüßungsbereich -->
      <section id="home">
        <h2>Willkommen!</h2>
        <p>Schön, dass du hier bist.</p>
      </section>

      <!-- Über mich Bereich -->
      <section id="about">
        <h2>Über mich</h2>
        <p>Ich lerne Webentwicklung...</p>
      </section>

      <!-- Blog-Artikel -->
      <section id="blog">
        <h2>Mein Blog</h2>

        <article>
          <h3>Mein erster Blogpost</h3>
          <p><time datetime="2025-11-21">21. November 2025</time></p>
          <p>Heute habe ich HTML gelernt...</p>
        </article>

        <article>
          <h3>CSS macht Spaß!</h3>
          <p><time datetime="2025-11-22">22. November 2025</time></p>
          <p>Farben und Layouts sind toll...</p>
        </article>
      </section>
    </main>

    <!-- Sidebar (optional) -->
    <aside>
      <h3>📌 Hinweis</h3>
      <p>Diese Seite ist ein Lernprojekt.</p>
    </aside>

    <!-- Fußbereich -->
    <footer>
      <p>&copy; 2025 Meine Webseite - Alle Rechte vorbehalten</p>
      <nav>
        <a href="#impressum">Impressum</a>
        <a href="#datenschutz">Datenschutz</a>
      </nav>
    </footer>
  </body>
</html>
```

---

## Verschachtelung verstehen

```
<body>
├── <header>
│   ├── <h1>
│   └── <nav>
├── <main>
│   ├── <section>
│   │   ├── <h2>
│   │   └── <p>
│   └── <article>
│       ├── <h3>
│       └── <p>
├── <aside>
│   └── <p>
└── <footer>
    └── <p>
```

---

## Wann welches Element?

**Header:**

- Seitenkopf mit Logo/Titel
- Navigation
- Meist ganz oben

**Nav:**

- Hauptmenü
- Breadcrumbs
- Interne Links-Sammlung

**Main:**

- Der eigentliche Seiteninhalt
- Nur 1x pro Seite!

**Section:**

- Thematisch zusammenhängender Bereich
- Hat meist eine Überschrift

**Article:**

- Eigenständiger, wiederverwendbarer Inhalt
- Blogposts, News, Kommentare

**Aside:**

- Sidebar
- Zusatzinfos
- Werbung

**Footer:**

- Seitenfuß
- Copyright, Links
- Meist ganz unten

---

## Häufige Fehler

❌ **Zu viele `<main>`**

```html
<main>...</main>
<main>...</main>
<!-- Falsch! -->
```

✅ **Nur ein `<main>`**

```html
<main>
  <section>...</section>
  <section>...</section>
</main>
```

❌ **`<section>` ohne Überschrift**

```html
<section>
  <p>Nur Text...</p>
  <!-- Besser: <div> -->
</section>
```

✅ **`<section>` mit Überschrift**

```html
<section>
  <h2>Überschrift</h2>
  <p>Text...</p>
</section>
```

---

## Zusätzliche nützliche Tags

### `<figure>` und `<figcaption>`

Für Bilder mit Beschriftung:

```html
<figure>
  <img src="bild.jpg" alt="Beschreibung" />
  <figcaption>Bildbeschreibung hier</figcaption>
</figure>
```

### `<time>`

Für Datumsangaben:

```html
<time datetime="2025-11-21">21. November 2025</time>
```

### `<mark>`

Für hervorgehobenen Text:

```html
<p>Dies ist <mark>wichtig</mark>!</p>
```

---

## Vorher / Nachher Vergleich

**Ohne Semantik:**

```html
<div class="header">
  <div class="logo">Logo</div>
  <div class="menu">
    <div><a href="#">Link</a></div>
  </div>
</div>
<div class="content">Inhalt</div>
<div class="footer">Footer</div>
```

**Mit Semantik:**

```html
<header>
  <h1>Logo</h1>
  <nav>
    <a href="#">Link</a>
  </nav>
</header>
<main>Inhalt</main>
<footer>Footer</footer>
```

Viel klarer, oder? 🎯

---

## Weiterführend

- `css-basis.md` → Jetzt diese Elemente stylen!
- `responsive-design.md` → Mobile Navigation
- Übung: Erstelle eine Seite mit allen semantischen Elementen!
