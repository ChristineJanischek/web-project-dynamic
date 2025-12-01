# Corporate Design & Corporate Identity

**Corporate Design (CD)** ist das visuelle Erscheinungsbild eines Unternehmens oder einer Organisation. Es sorgt für Wiedererkennbarkeit und vermittelt die Werte und Persönlichkeit der Marke.

---

## Was ist Corporate Design?

Corporate Design umfasst alle **visuellen Elemente**, die ein Unternehmen nach außen präsentieren:

- **Logo** - Das zentrale Erkennungszeichen
- **Farben** - Primär- und Sekundärfarben
- **Typografie** - Schriftarten für Headlines und Fließtext
- **Bildsprache** - Stil der Fotografien und Illustrationen
- **Layout-Prinzipien** - Gestaltungsraster und Abstände
- **Icons & Grafiken** - Visuelle Elemente und Symbole

---

## Corporate Identity vs. Corporate Design

### Corporate Identity (CI)
Die **Gesamtheit** aller Merkmale, die ein Unternehmen charakterisieren:
- **Corporate Behavior** - Wie verhält sich das Unternehmen?
- **Corporate Communication** - Wie kommuniziert es?
- **Corporate Design** - Wie sieht es aus?

### Corporate Design (CD)
Der **visuelle Teil** der Corporate Identity - das, was man sieht.

**Merksatz:** CI ist die Persönlichkeit, CD ist das Aussehen.

---

## Warum ist Corporate Design wichtig?

✅ **Wiedererkennbarkeit** - Kunden erkennen dich sofort  
✅ **Professionalität** - Seriöses Auftreten  
✅ **Vertrauen** - Konsistenz schafft Glaubwürdigkeit  
✅ **Differenzierung** - Abhebung von Konkurrenten  
✅ **Markenbindung** - Emotionale Verbindung zu Kunden  

---

## Die wichtigsten Elemente

### 1. Logo

Das **Herzstück** des Corporate Designs.

**Anforderungen:**
- ✅ Einfach und einprägsam
- ✅ Skalierbar (von Visitenkarte bis Plakatwand)
- ✅ In Schwarz-Weiß funktionierend
- ✅ Zeitlos (nicht an Trends gebunden)

**Beispiel-Code für Logo-Einbindung:**
```html
<!-- Logo als SVG (empfohlen) -->
<div class="logo">
  <img src="images/logo.svg" alt="MiFa - Mission Future Academy">
</div>
```

```css
.logo img {
  max-width: 200px;
  height: auto;
}

/* Responsive */
@media (max-width: 768px) {
  .logo img {
    max-width: 150px;
  }
}
```

---

### 2. Farbschema

**Primärfarbe** - Die Hauptfarbe der Marke  
**Sekundärfarben** - Ergänzende Farben  
**Akzentfarbe** - Für Call-to-Actions und Highlights  
**Neutrale Farben** - Grau, Schwarz, Weiß für Text und Hintergründe

#### Beispiel: Nachhaltige Schülerfirma

```css
:root {
  /* Primärfarben - Natur & Nachhaltigkeit */
  --color-primary: #2D6A4F;      /* Waldgrün */
  --color-primary-light: #52B788; /* Helles Grün */
  --color-primary-dark: #1B4332;  /* Dunkelgrün */
  
  /* Sekundärfarben - Innovation & Technologie */
  --color-secondary: #0077B6;     /* Tech-Blau */
  --color-secondary-light: #48CAE4;
  
  /* Akzentfarbe - Energie & Aktion */
  --color-accent: #F4A261;        /* Warmes Orange */
  
  /* Neutrale Farben */
  --color-text: #2B2D42;          /* Dunkelgrau */
  --color-background: #F8F9FA;    /* Hellgrau */
  --color-white: #FFFFFF;
}

/* Anwendung */
body {
  background-color: var(--color-background);
  color: var(--color-text);
}

.button-primary {
  background-color: var(--color-primary);
  color: var(--color-white);
}

.button-secondary {
  background-color: var(--color-accent);
  color: var(--color-white);
}
```

#### Farbpsychologie

| Farbe | Wirkung | Einsatz |
|-------|---------|---------|
| **Grün** | Natur, Nachhaltigkeit, Wachstum | Umwelt, Bio, Gesundheit |
| **Blau** | Vertrauen, Technologie, Seriosität | IT, Finanzen, Bildung |
| **Orange** | Energie, Kreativität, Optimismus | Call-to-Actions, Highlights |
| **Grau** | Neutral, Modern, Professionell | Text, Hintergründe |

---

### 3. Typografie

**Schriften transportieren Persönlichkeit!**

#### Schriftarten-Kategorien

**Serif (mit Serifen)**
- Traditionell, seriös, elegant
- Beispiele: Times New Roman, Georgia
- Einsatz: Print, längere Texte

**Sans-Serif (ohne Serifen)**
- Modern, klar, sachlich
- Beispiele: Arial, Helvetica, Open Sans
- Einsatz: Web, Headlines, UI

**Monospace (feste Breite)**
- Technisch, Code-ähnlich
- Beispiele: Courier, Roboto Mono
- Einsatz: Code-Blöcke, technische Inhalte

#### Beispiel: Schriftarten-System

```css
/* Schriften definieren */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap');

:root {
  /* Schriftfamilien */
  --font-primary: 'Inter', sans-serif;       /* Hauptschrift */
  --font-secondary: 'Merriweather', serif;   /* Headlines */
  --font-mono: 'Courier New', monospace;     /* Code */
  
  /* Schriftgrößen */
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.125rem;  /* 18px */
  --text-xl: 1.25rem;   /* 20px */
  --text-2xl: 1.5rem;   /* 24px */
  --text-3xl: 2rem;     /* 32px */
  --text-4xl: 2.5rem;   /* 40px */
}

/* Anwendung */
body {
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: 1.6;
}

h1, h2, h3 {
  font-family: var(--font-secondary);
  font-weight: 700;
}

h1 {
  font-size: var(--text-4xl);
}

code, pre {
  font-family: var(--font-mono);
}
```

#### Typografie-Regeln

✅ **Maximal 2-3 Schriftarten** verwenden  
✅ **Kontrast** zwischen Headlines und Text  
✅ **Lesbarkeit** vor Kreativität  
✅ **Zeilenlänge** 50-75 Zeichen optimal  
✅ **Zeilenabstand** (line-height) 1.4-1.6 für Fließtext  

---

### 4. Bildsprache

**Einheitliche Bildsprache** verstärkt den Markenauftritt.

#### Kriterien definieren

- **Stil:** Fotografisch, illustriert, minimalistisch?
- **Stimmung:** Professionell, locker, inspirierend?
- **Farben:** Pastelltöne, kräftige Farben, Schwarz-Weiß?
- **Motive:** Menschen, Natur, Technologie, Abstrakt?

#### Beispiel: Nachhaltige Tech-Firma

```
✅ Natürliche Lichtverhältnisse
✅ Echte Menschen in Aktion (nicht gestellt)
✅ Grün- und Blautöne dominant
✅ Technologie im Einklang mit Natur
✅ Authentizität vor Hochglanz
```

#### Bild-Optimierung für Web

```css
/* Responsive Bilder */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Bild mit Overlay (für Hero-Bereiche) */
.hero-image {
  position: relative;
  background-image: url('images/hero.jpg');
  background-size: cover;
  background-position: center;
  min-height: 400px;
}

.hero-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(45, 106, 79, 0.6); /* Primärfarbe mit Transparenz */
}
```

---

### 5. Layout-Prinzipien

#### Gestaltungsraster

**Grid-System** für konsistente Layouts:

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 12-Spalten-Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}

.col-6 {
  grid-column: span 6; /* 50% Breite */
}

.col-4 {
  grid-column: span 4; /* 33% Breite */
}
```

#### Weißraum (Whitespace)

**Nicht Platz verschwenden, sondern nutzen!**

```css
:root {
  /* Spacing-System */
  --space-xs: 0.25rem;  /* 4px */
  --space-sm: 0.5rem;   /* 8px */
  --space-md: 1rem;     /* 16px */
  --space-lg: 1.5rem;   /* 24px */
  --space-xl: 2rem;     /* 32px */
  --space-2xl: 3rem;    /* 48px */
  --space-3xl: 4rem;    /* 64px */
}

/* Konsistente Abstände */
section {
  padding: var(--space-3xl) 0;
}

.card {
  padding: var(--space-lg);
  margin-bottom: var(--space-xl);
}
```

---

## Corporate Design Manual erstellen

Ein **Style Guide** dokumentiert alle Design-Entscheidungen:

### Inhalt eines CD-Manuals

1. **Logo-Verwendung**
   - Varianten (farbig, schwarz-weiß, invertiert)
   - Schutzraum
   - Verbotene Verwendungen

2. **Farbpalette**
   - Primär-, Sekundär-, Akzentfarben
   - RGB, HEX, CMYK-Werte
   - Verwendungsbeispiele

3. **Typografie**
   - Schriftarten mit Download-Links
   - Größenabstufungen
   - Anwendungsbeispiele

4. **Bildsprache**
   - Do's und Don'ts
   - Beispielbilder
   - Filter und Bearbeitung

5. **Layout-Elemente**
   - Buttons
   - Icons
   - Formulare
   - Navigation

### Beispiel: Style Guide als HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>MiFa Style Guide</title>
  <link rel="stylesheet" href="styleguide.css">
</head>
<body>
  <h1>MiFa Corporate Design Manual</h1>
  
  <section class="colors">
    <h2>Farbpalette</h2>
    <div class="color-grid">
      <div class="color-sample" style="background-color: #2D6A4F;">
        <h3>Primär</h3>
        <p>#2D6A4F</p>
      </div>
      <div class="color-sample" style="background-color: #0077B6;">
        <h3>Sekundär</h3>
        <p>#0077B6</p>
      </div>
      <!-- Weitere Farben -->
    </div>
  </section>
  
  <section class="typography">
    <h2>Typografie</h2>
    <h1>Headline 1 - Inter Bold</h1>
    <h2>Headline 2 - Inter Semibold</h2>
    <p>Fließtext - Inter Regular, 16px, line-height 1.6</p>
  </section>
</body>
</html>
```

---

## Konsistenz sicherstellen

### CSS Custom Properties nutzen

```css
/* Design-Tokens in CSS-Variablen */
:root {
  /* Farben */
  --color-primary: #2D6A4F;
  --color-accent: #F4A261;
  
  /* Schriften */
  --font-heading: 'Inter', sans-serif;
  --font-body: 'Merriweather', serif;
  
  /* Abstände */
  --space-section: 4rem;
  --space-card: 1.5rem;
  
  /* Schatten */
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 30px rgba(0,0,0,0.15);
  
  /* Border-Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

/* Wiederverwendbare Komponenten */
.card {
  background: var(--color-white);
  padding: var(--space-card);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.button {
  background-color: var(--color-primary);
  color: white;
  padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-sm);
  font-family: var(--font-heading);
}
```

---

## Checkliste: Corporate Design erstellen

### Schritt 1: Analyse
- [ ] Werte und Mission definieren
- [ ] Zielgruppe bestimmen
- [ ] Konkurrenz analysieren

### Schritt 2: Logo
- [ ] Skizzen erstellen
- [ ] Digital umsetzen
- [ ] Varianten entwickeln (farbig, s/w)

### Schritt 3: Farbpalette
- [ ] Primärfarbe wählen
- [ ] Sekundär- und Akzentfarben festlegen
- [ ] Farbpsychologie beachten

### Schritt 4: Typografie
- [ ] Schriftarten auswählen (max. 2-3)
- [ ] Größensystem definieren
- [ ] Lesbarkeit testen

### Schritt 5: Bildsprache
- [ ] Stil definieren
- [ ] Beispielbilder sammeln
- [ ] Do's und Don'ts festhalten

### Schritt 6: Dokumentation
- [ ] Style Guide erstellen
- [ ] Code-Snippets bereitstellen
- [ ] Beispiele zeigen

---

## Häufige Fehler vermeiden

❌ **Zu viele Farben** → Max. 3-4 Hauptfarben  
❌ **Zu viele Schriften** → Max. 2-3 Schriftarten  
❌ **Inkonsistenz** → Immer gleiche Abstände und Größen  
❌ **Trends folgen** → Zeitlos statt trendy  
❌ **Unleserlich** → Funktion vor Form  

---

## Nächste Schritte

- **Konzeption** → `konzeption-webdesign.md` - Planung und Struktur
- **Zielgruppen** → `zielgruppenanalyse.md` - Nutzerbedürfnisse verstehen
- **Responsive Design** → `responsive-design.md` - Umsetzung für alle Geräte

---

## Ressourcen

- [Google Fonts](https://fonts.google.com/) - Kostenlose Web-Schriften
- [Coolors](https://coolors.co/) - Farbpaletten-Generator
- [Adobe Color](https://color.adobe.com/) - Farbharmonien finden
- [Canva](https://www.canva.com/) - Design-Vorlagen
- [Figma](https://www.figma.com/) - Interface-Design-Tool

---

**Tipp:** Ein gutes Corporate Design entwickelt sich. Starte einfach und verfeinere kontinuierlich!
