# Version 3: MiFa – Mission Future Academy Website

**Status:** ✅ Bereit zum Lernen!

## 🎯 Projektübersicht

In dieser Version entwickelst du die Website für **MiFa - Mission Future Academy**, eine Schülerfirma, die sich auf nachhaltige Software im Bereich Bildung und Ökologie spezialisiert.

**Besonderheit:** Anders als in Version 1 und 2 liegt der Fokus zu **60% auf der Konzeption** und nur zu **40% auf der technischen Umsetzung**. Du lernst, wie professionelle Webprojekte entstehen – vom ersten Briefing bis zum fertigen Produkt.

## 🎯 Lernziele

Nach Abschluss dieser Version kannst du:
- ✅ Zielgruppenanalysen für Webprojekte durchführen
- ✅ Corporate Design Richtlinien entwickeln und anwenden
- ✅ Sitemaps und Wireframes erstellen
- ✅ Responsive Websites mit modernem Design umsetzen
- ✅ Formulare mit JavaScript-Validierung implementieren
- ✅ Bilder responsive und performant einbinden
- ✅ Ein professionelles Web-Projekt von A-Z durchführen

## 📋 Voraussetzungen

- Abgeschlossene **Version 1** (HTML-Grundgerüst & CSS-Basics)
- Abgeschlossene **Version 2** (Box-Modell & Responsive Design)
- Grundkenntnisse in JavaScript (DOM-Manipulation)
- Verständnis von CSS Grid und Flexbox
- Git installiert (für Versionsverwaltung)

---

## 🚀 Quick Start - So startest du!

### 1. Repository klonen & Branch erstellen

```bash
# Repository klonen (falls noch nicht geschehen)
git clone <deine-repository-url>
cd web-project-dynamic

# Eigenen Feature-Branch erstellen
git checkout -b version3-mifa-website

# In den Version 3 Ordner wechseln
cd version3/aufgabe/
```

**📖 Mehr zu Git:** Lies [`docs/git-versionsmanagement.md`](../docs/konzeption/git-versionsmanagement.md) für detaillierte Git-Anleitung!

### 2. Starter-Dateien aktivieren

```bash
# Vorlagen-Dateien zu Arbeits-Dateien umbenennen
cp index_neu.html index.html
cp css/style_neu.css css/style.css
cp js/script_neu.js js/script.js
```

### 3. Projekt im Browser öffnen

```bash
# Öffne index.html im Browser
# - Rechtsklick auf index.html → "Open with Live Server" (VS Code Extension)
# - ODER: Doppelklick auf index.html im Datei-Explorer
```

**✅ Checkpoint:** Browser zeigt MiFa-Website mit Navigation, Hero-Bereich, Projekten und Kontaktformular?

### 4. Erste Git-Commits

```bash
# Änderungen stagen
git add index.html css/style.css js/script.js

# Ersten Commit erstellen
git commit -m "feat: Starter-Dateien für MiFa-Website aktiviert"

# Zum Remote Repository pushen
git push origin version3-mifa-website
```

**💡 Tipp:** Committe regelmäßig nach jedem abgeschlossenen Schritt! Nutze aussagekräftige Commit-Messages:
- `feat: Hero-Sektion mit Corporate Design angepasst`
- `style: Logo als background-image eingebunden`
- `docs: Persona für Lehrkraft erstellt`

---

## 📚 Wichtige Dokumentation (ZUERST lesen!)

### 🎨 Phase 1: Konzeption (60% der Arbeitszeit)

Diese Phase ist entscheidend! Professionelle Webprojekte beginnen immer mit sorgfältiger Planung:

#### 1. Zielgruppenanalyse (90 Min)
📖 **Dokumentation:** [`docs/zielgruppenanalyse.md`](../docs/konzeption/zielgruppenanalyse.md)

**Lernziele:**
- Zielgruppen identifizieren (Lehrkräfte, Schüler:innen, NGOs)
- User Personas erstellen
- Customer Journey Map entwickeln
- Nutzerbedürfnisse analysieren

**Aufgaben:**
1. Erstelle 2-3 detaillierte Personas für MiFa
2. Definiere Hauptzielgruppe und Nebenzielgruppen
3. Entwickle eine Customer Journey Map
4. Dokumentiere Erkenntnisse im `concept/` Ordner

#### 2. Corporate Design (120 Min)
📖 **Dokumentation:** [`docs/corporate-design.md`](../docs/konzeption/corporate-design.md)

**Lernziele:**
- Logo-Verwendung und Schutzraum verstehen
- Farbpsychologie für Nachhaltigkeit anwenden
- Typografie-System entwickeln
- CSS Custom Properties für Design-Tokens nutzen

**Aufgaben:**
1. Analysiere das MiFa-Logo (`images/Logo_farbig.jpg`)
2. Definiere Farbpalette (Primär: Grün, Sekundär: Blau, Akzent: Orange)
3. Wähle passende Google Fonts aus
4. Erstelle CSS Custom Properties für alle Design-Tokens

**Verfügbare Assets:**
- `images/Logo_farbig.jpg` - Hauptlogo
- `images/Startbild.png` - Hero-Bild (Desktop)
- `images/Startbild_klein.png` - Hero-Bild (Mobile)
- `images/ic_launcher.png` - Favicon

#### 3. Konzeption & Webdesign (90 Min)
📖 **Dokumentation:** [`docs/konzeption-webdesign.md`](../docs/konzeption/konzeption-webdesign.md)

**Lernziele:**
- Briefing analysieren und verstehen
- Sitemap-Struktur entwickeln
- Wireframes für Desktop und Mobile erstellen
- Mockups interpretieren

**Aufgaben:**
1. Analysiere das Mockup in `concept/Mockups_MiFa.odp`
2. Erstelle eine Sitemap für die Website-Struktur
3. Zeichne Low-Fidelity Wireframes (Papier oder Tool)
4. Plane Content-Bereiche für alle Seiten

**Mindest-Seiten:**
- Startseite (Hero, Über uns, Call-to-Action)
- Projekte (Grid mit 3+ Projekten)
- Services (Was bietet MiFa an?)
- Kontakt (Formular, Kontaktdaten)

**✅ CHECKPOINT - Phase 1 abgeschlossen?**

Prüfe, ob du folgende Dateien erstellt hast:
- [ ] `concept/personas.md` - Mindestens 2 detaillierte User Personas
- [ ] `concept/customer-journey.md` - Customer Journey Map für Hauptnutzer
- [ ] `concept/corporate-design.md` - Farbpalette, Typografie, Logo-Usage definiert
- [ ] `concept/sitemap.md` - Website-Struktur skizziert
- [ ] `concept/wireframes.pdf` (oder .png) - Wireframes für Desktop & Mobile

**Git-Commit:**
```bash
git add concept/
git commit -m "docs: Konzeptionsphase abgeschlossen (Personas, Corporate Design, Wireframes)"
git push origin version3-mifa-website
```

---

### 💻 Phase 2: Technische Umsetzung (40% der Arbeitszeit)

Jetzt setzt du deine Konzeption in Code um!

#### 1. HTML-Struktur (60 Min)
📖 **Dokumentation:** [`docs/html-grundgeruest.md`](../docs/statisch/html-grundgeruest.md), [`docs/seitenstrukturelemente.md`](../docs/statisch/seitenstrukturelemente.md)

**Aufgaben:**
1. Nutze die bereitgestellte Vorlage `aufgabe/index_neu.html` als Startpunkt
2. Passe Texte und Inhalte an deine Konzeption an
3. Füge weitere Sektionen hinzu falls nötig
4. Stelle sicher, dass die HTML-Struktur semantisch korrekt ist

**Vorlagen-Features:**
- ✅ Sticky Header mit Navigation
- ✅ Hamburger-Menü für Mobile
- ✅ Hero-Section mit Background-Image
- ✅ Responsive Grid-Layouts
- ✅ Kontaktformular mit Validierung
- ✅ Footer mit mehreren Spalten

#### 2. CSS-Styling & Corporate Design (90 Min)
📖 **Dokumentation:** [`docs/css-basis.md`](../docs/statisch/css-basis.md), [`docs/corporate-design.md`](../docs/konzeption/corporate-design.md)

**Aufgaben:**
1. Nutze `aufgabe/css/style_neu.css` als Basis
2. Passe CSS Custom Properties an dein Corporate Design an
3. Ergänze weitere Komponenten nach Bedarf
4. Achte auf mobile-first Responsive Design

**CSS-Features in der Vorlage:**
- ✅ CSS Custom Properties für alle Design-Tokens
- ✅ Mobile-first Responsive Breakpoints (480px, 768px, 1400px)
- ✅ Flexbox und CSS Grid Layouts
- ✅ Hover- und Transition-Effekte
- ✅ Accessibility-Features (Focus States, Reduced Motion)

#### 3. Responsive Bilder (45 Min)
📖 **Dokumentation:** [`docs/bilder-grafiken.md`](../docs/statisch/bilder-grafiken.md)

**Aufgaben:**
1. Logo als `background-image` im CSS einbinden
2. Hero-Bild responsive einsetzen (Desktop: `Startbild.png`, Mobile: `Startbild_klein.png`)
3. Projekt-Bilder optimiert einbinden
4. Alt-Texte für Barrierefreiheit schreiben

#### 4. JavaScript-Interaktivität (75 Min)
📖 **Dokumentation:** [`docs/js.md`](../docs/dynamisch/js.md), [`docs/formulare.md`](../docs/statisch/formulare.md)

**Aufgaben:**
1. Nutze `aufgabe/js/script_neu.js` als Vorlage
2. Teste Mobile Navigation (Hamburger-Menü)
3. Implementiere Formularvalidierung
4. Füge Scroll-Animationen hinzu (optional)

**JavaScript-Features in der Vorlage:**
- ✅ Mobile Navigation Toggle
- ✅ Smooth Scrolling für Anker-Links
- ✅ Formularvalidierung (HTML5 + Custom)
- ✅ Intersection Observer für Scroll-Animationen
- ✅ Lazy Loading für Bilder
- ✅ Accessibility Features (Keyboard Navigation)

#### 5. Formulare & Validierung (60 Min)
📖 **Dokumentation:** [`docs/formulare.md`](../docs/statisch/formulare.md)

**Aufgaben:**
1. Kontaktformular ist bereits implementiert in der Vorlage
2. Passe Formularfelder an deine Anforderungen an
3. Teste HTML5-Validierung (required, email, minlength)
4. Teste JavaScript-Validierung bei Submit
5. Ergänze weitere Formularfelder falls nöig (z.B. Datei-Upload für Bewerbungen)

**✅ CHECKPOINT - Phase 2 abgeschlossen?**

Prüfe im Browser (F12 für DevTools):
- [ ] **HTML:** Alle Sektionen vorhanden (Hero, Über uns, Projekte, Services, Kontakt, Footer)
- [ ] **CSS:** Corporate Design umgesetzt (Farben, Fonts, Logo sichtbar)
- [ ] **Responsive:** Mobile Navigation (Hamburger) funktioniert bei < 768px
- [ ] **Bilder:** Logo & Hero-Bild responsive eingebunden
- [ ] **Formular:** Validierung funktioniert (leere Felder werden abgefangen)
- [ ] **Konsole:** Keine JavaScript-Fehler (rote Meldungen in F12)

**Test-Checkliste Responsive:**
```bash
# In Browser DevTools (F12):
# - Responsive Design Mode aktivieren (Strg+Shift+M)
# - Teste: 320px, 768px, 1024px, 1920px
# - Prüfe: Lesbarkeit, Navigation, Bilder, Formular
```

**Git-Commit:**
```bash
git add .
git commit -m "feat: MiFa-Website komplett implementiert (HTML/CSS/JS)"
git push origin version3-mifa-website
```

---

## 🛠️ Schritt-für-Schritt Anleitung

### Schritt 1: Starter-Vorlagen verstehen (30 Min)

1. **Dateien umbenennen:**
   ```bash
   cd version3/aufgabe/
   cp index_neu.html index.html
   cp css/style_neu.css css/style.css
   cp js/script_neu.js js/script.js
   ```

2. **Vorlage im Browser öffnen:**
   - Öffne `index.html` im Browser
   - Prüfe, dass alle Sektionen sichtbar sind
   - Teste mobile Navigation (Browser-Fenster verkleinern)

3. **Code-Struktur analysieren:**
   - Lies HTML-Kommentare für TODO-Markierungen
   - Finde CSS Custom Properties in `:root`
   - Verstehe JavaScript-Module-Struktur

### Schritt 2: Corporate Design anpassen (60 Min)

**In `css/style.css` (Zeilen 14-50):**

Passe die CSS Custom Properties an deine Konzeption an:

```css
:root {
    /* DEINE Farbpalette aus Corporate Design */
    --color-primary: #2D6A4F;        /* Grün für Nachhaltigkeit */
    --color-primary-light: #52B788;
    --color-primary-dark: #1B4332;
    
    --color-secondary: #0077B6;      /* Blau für Technologie */
    --color-secondary-light: #48CAE4;
    --color-secondary-dark: #023E8A;
    
    --color-accent: #F4A261;         /* Orange für Energie */
    
    /* DEINE Typografie */
    --font-primary: 'Inter', sans-serif;      /* Aus Google Fonts */
    --font-secondary: 'Merriweather', serif;  /* Aus Google Fonts */
    
    /* Spacing, Radius, Shadows bleiben meistens gleich */
}
```

**Google Fonts einbinden (in `index.html` `<head>`):**

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap" rel="stylesheet">
```

### Schritt 3: Logo & Bilder einbinden (45 Min)

**Logo im CSS (`css/style.css` Zeile ~230):**

```css
.logo {
    background-image: url('../images/Logo_farbig.jpg');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    width: 150px;
    height: 60px;
}

@media (max-width: 768px) {
    .logo {
        width: 120px;
        height: 50px;
    }
}
```

**Hero-Bild responsive (`css/style.css` Zeile ~300):**

```css
.hero {
    background-image: url('../images/Startbild.png');
    /* ... weitere Styles ... */
}

@media (max-width: 768px) {
    .hero {
        background-image: url('../images/Startbild_klein.png');
    }
}
```

**Projekt-Bilder im HTML ersetzen:**

Ersetze Platzhalter-URLs durch eigene Bilder oder erstelle Screenshots deiner Projekte:

```html
<div class="project-image">
    <img src="images/projekt-ecolearn.jpg" 
         alt="EcoLearn App Screenshot" 
         loading="lazy">
</div>
```

### Schritt 4: Inhalte anpassen (90 Min)

**In `index.html`:**

1. **Hero-Section personalisieren:**
   ```html
   <h1 class="hero-title">Mission Future Academy</h1>
   <p class="hero-subtitle">Nachhaltige Software für Bildung & Ökologie</p>
   <p class="hero-tagline">Von Schüler:innen entwickelt. Für die Zukunft gestaltet.</p>
   ```

2. **Über-uns-Texte schreiben:**
   - Füge dein Mission-Statement ein
   - Beschreibe MiFas Werte
   - Ergänze Features der Schülerfirma

3. **Projekte hinzufügen:**
   - Mindestens 3 Projekte (EcoLearn, CO2-Tracker, GreenDashboard)
   - Für jedes Projekt: Titel, Beschreibung, verwendete Technologien
   - Bilder oder Platzhalter

4. **Services definieren:**
   - Software-Entwicklung
   - Workshops
   - Beratung

5. **Kontaktformular anpassen:**
   - Bereits vollständig implementiert
   - Optional: Betreff-Optionen erweitern

### Schritt 5: Mobile Navigation testen (30 Min)

**Test-Checkliste:**
- [ ] Browser-Fenster auf < 768px verkleinern
- [ ] Hamburger-Icon erscheint
- [ ] Klick auf Hamburger öffnet Menü von rechts
- [ ] Klick auf Navigation-Link schließt Menü
- [ ] Klick außerhalb des Menüs schließt es
- [ ] ESC-Taste schließt Menü

**Falls etwas nicht funktioniert:**
- Prüfe Browser-Konsole auf Fehler (F12)
- Stelle sicher, dass IDs in HTML und JavaScript übereinstimmen
- Überprüfe, dass `script.js` am Ende von `<body>` geladen wird

### Schritt 6: Formularvalidierung testen (45 Min)

**Test-Szenarios:**

1. **Leeres Formular absenden:**
   - Erwartung: Fehlermeldungen bei allen Pflichtfeldern

2. **Ungültige E-Mail:**
   - Eingabe: "test@test"
   - Erwartung: "Bitte geben Sie eine gültige E-Mail-Adresse ein."

3. **Nachricht zu kurz:**
   - Eingabe: "Hallo"
   - Erwartung: "Bitte geben Sie eine Nachricht mit mindestens 10 Zeichen ein."

4. **Datenschutz nicht akzeptiert:**
   - Erwartung: Formular kann nicht abgesendet werden

5. **Erfolgreiches Absenden:**
   - Alle Felder korrekt ausgefüllt
   - Erwartung: Grüne Erfolgsmeldung, Formular wird zurückgesetzt

**JavaScript-Konsole beobachten:**
```javascript
// Im Browser-Konsole (F12):
// Bei erfolgreichem Submit sollte erscheinen:
// "Formulardaten: {name: '...', email: '...', ...}"
```

**✅ CHECKPOINT - Formular validiert?**

Alle 5 Test-Szenarios erfolgreich durchlaufen?
- [ ] Leeres Formular zeigt Fehlermeldungen
- [ ] Ungültige E-Mail wird abgefangen
- [ ] Zu kurze Nachricht wird abgefangen  
- [ ] Datenschutz-Checkbox ist Pflicht
- [ ] Erfolgreiches Submit zeigt grüne Meldung + Reset

**Falls Fehler auftreten:**
1. Browser-Konsole (F12) auf Fehlermeldungen prüfen
2. In `js/script.js` Zeile 45-80 nach Tippfehlern suchen
3. Prüfen, dass IDs in HTML und JavaScript übereinstimmen

### Schritt 7: Scroll-Animationen aktivieren (Optional, 30 Min)

Die Vorlage enthält bereits Intersection Observer für Fade-In-Animationen.

**Test:**
1. Scroll langsam durch die Seite
2. Karten sollten beim Erscheinen einblenden und nach oben sliden
3. Falls nicht: Prüfe Browser-Konsole

**Deaktivieren bei Motion Sensitivity:**
Die Vorlage respektiert automatisch `prefers-reduced-motion`.

---

## 🧪 Testing & Qualitätssicherung

### Browser-Kompatibilität
Teste in mindestens 3 Browsern:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (falls verfügbar)

### Responsive Testing
Teste in DevTools (F12) bei:
- [ ] 320px (Mobile klein)
- [ ] 480px (Mobile groß)
- [ ] 768px (Tablet)
- [ ] 1024px (Laptop)
- [ ] 1920px (Desktop)

### Accessibility Testing
- [ ] Alle Bilder haben Alt-Texte
- [ ] Formular-Labels sind mit Inputs verknüpft
- [ ] Navigation mit Tab-Taste funktioniert
- [ ] Focus-States sind sichtbar
- [ ] Kontraste sind ausreichend (nutze Browser-Tools)

### Performance Testing
- [ ] Bilder sind optimiert (< 500KB pro Bild)
- [ ] Keine Konsolen-Errors (F12)
- [ ] Page Load < 3 Sekunden

---

## 📦 Abgabe & Dokumentation

### Pflicht-Dateien

```
version3/aufgabe/
├── concept/
│   ├── personas.md              (2-3 User Personas)
│   ├── customer-journey.md      (Customer Journey Map)
│   ├── sitemap.md               (Website-Struktur)
│   ├── wireframes.pdf           (oder .png)
│   └── corporate-design.md      (Farbschema, Typografie, Logo-Usage)
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── images/
│   ├── Logo_farbig.jpg
│   ├── Startbild.png
│   ├── Startbild_klein.png
│   └── (weitere Projekt-Bilder)
└── README.md                    (Projekt-Dokumentation)
```

### README.md erstellen

Erstelle eine `README.md` im `aufgabe/` Ordner mit:

1. **Projekt-Titel & Beschreibung**
2. **Konzeption:**
   - Zusammenfassung Zielgruppenanalyse
   - Corporate Design Entscheidungen
   - Sitemap-Übersicht
3. **Technische Umsetzung:**
   - Verwendete Technologien
   - Besondere Features
   - Bekannte Limitationen
4. **Setup-Anleitung:**
   - Wie startet man das Projekt lokal?
5. **Credits:**
   - Bildquellen
   - Verwendete Libraries/Fonts

### Bewertungskriterien

| Kategorie | Gewichtung | Kriterien |
|-----------|------------|-----------|
| **Konzeption** | 60% | Vollständigkeit der Personas, Qualität der Wireframes, Durchdachtheit des Corporate Designs |
| **HTML** | 15% | Semantik, Struktur, Validität |
| **CSS** | 15% | Corporate Design Umsetzung, Responsive Design, Code-Qualität |
| **JavaScript** | 10% | Funktionalität, Fehlerfreiheit, Code-Stil |

---

## 💡 Tipps & Best Practices

### Konzeption
- **Nimm dir Zeit!** 60% der Arbeitszeit = 60% der Bewertung
- Nutze echte Namen und Geschichten für Personas
- Wireframes müssen nicht perfekt sein - Skizzen reichen
- Corporate Design Guide ist deine Referenz während des Codings

### Technische Umsetzung
- **Mobile-first:** Starte mit Mobile-Styling, dann Desktop
- **CSS Custom Properties:** Nutze sie konsequent statt hardcodierte Werte
- **Kommentiere deinen Code:** Hilft dir und anderen
- **Teste früh, teste oft:** Nicht alles am Ende testen

### Zeitmanagement
Plane ca. **12-15 Stunden** für Version 3:
- **Tag 1 (4-5h):** Konzeption (Personas, Corporate Design, Wireframes)
- **Tag 2 (3-4h):** HTML/CSS Grundstruktur, Corporate Design umsetzen
- **Tag 3 (2-3h):** Inhalte, Bilder, Feinschliff
- **Tag 4 (2-3h):** JavaScript, Testing, Dokumentation

---

## 🚀 Weiterführende Challenges (Optional)

Wenn du fertig bist und mehr lernen möchtest:

### Level 1: Erweiterte Features
- [ ] Dark Mode Toggle
- [ ] Bildergalerie mit Lightbox
- [ ] Projekt-Detailseiten
- [ ] Blog-Sektion mit mehreren Artikeln

### Level 2: Backend Integration
- [ ] Formular-Daten an Server senden (PHP oder Node.js)
- [ ] E-Mail-Versand bei Kontaktanfrage
- [ ] Admin-Bereich für Content-Management

### Level 3: Progressive Web App
- [ ] Service Worker für Offline-Funktionalität
- [ ] Manifest.json für "Add to Homescreen"
- [ ] Push Notifications

### Level 4: Deployment
- [ ] Website auf GitHub Pages deployen
- [ ] Custom Domain einrichten
- [ ] SSL-Zertifikat konfigurieren

---

## 📖 Weiterführende Ressourcen

### Genutzte Dokumentationen in diesem Projekt

**Konzeption & Design:**
- [`docs/intro.md`](../docs/statisch/intro.md) - Einführung in Webentwicklung
- [`docs/zielgruppenanalyse.md`](../docs/konzeption/zielgruppenanalyse.md) - User Personas & Customer Journey
- [`docs/konzeption-webdesign.md`](../docs/konzeption/konzeption-webdesign.md) - Briefing, Sitemap, Wireframes
- [`docs/corporate-design.md`](../docs/konzeption/corporate-design.md) - Logo, Farben, Typografie

**HTML & Struktur:**
- [`docs/html-grundgeruest.md`](../docs/statisch/html-grundgeruest.md) - HTML5 Grundgerüst
- [`docs/seitenstrukturelemente.md`](../docs/statisch/seitenstrukturelemente.md) - Semantische HTML-Elemente

**CSS & Styling:**
- [`docs/css-basis.md`](../docs/statisch/css-basis.md) - CSS Grundlagen, Selektoren
- [`docs/css-einbinden.md`](../docs/statisch/css-einbinden.md) - CSS richtig einbinden
- [`docs/css-formatierung.md`](../docs/statisch/css-formatierung.md) - Best Practices für CSS
- [`docs/box-modell.md`](../docs/statisch/box-modell.md) - Margin, Padding, Border
- [`docs/flexible-layouts.md`](../docs/statisch/flexible-layouts.md) - Flexbox & CSS Grid
- [`docs/responsive-design.md`](../docs/statisch/responsive-design.md) - Media Queries, Mobile-first

**Bilder & Medien:**
- [`docs/bilder-grafiken.md`](../docs/statisch/bilder-grafiken.md) - Bildformate, responsive Bilder
- [`docs/galerien.md`](../docs/statisch/galerien.md) - Grid-Galerien, Lightbox

**Interaktivität:**
- [`docs/js.md`](../docs/dynamisch/js.md) - JavaScript Grundlagen, DOM-Manipulation
- [`docs/formulare.md`](../docs/statisch/formulare.md) - Formularvalidierung, Styling

**Versionsverwaltung:**
- [`docs/git-versionsmanagement.md`](../docs/konzeption/git-versionsmanagement.md) - Git & GitHub Workflow

**Qualitätssicherung:**
- [`docs/testen.md`](../docs/dynamisch/testen.md) - Testing-Strategien

**Weiterführend (für spätere Versionen):**
- [`docs/php.md`](../docs/dynamisch/php.md) - Backend mit PHP
- [`docs/python.md`](../docs/dynamisch/python.md) - Backend mit Python/Flask
- [`docs/datenbank.md`](../docs/dynamisch/datenbank.md) - MySQL-Integration
- [`docs/react.md`](../docs/dynamisch/react.md) - React Framework
- [`docs/algorithmen-datenstrukturen.md`](../docs/dynamisch/algorithmen-datenstrukturen.md) - CS Grundlagen

### Tools für Konzeption
- **Figma** (kostenlos): Wireframes & Mockups erstellen
- **Miro** (kostenlos): Customer Journey Maps, Brainstorming
- **Coolors.co**: Farbpaletten generieren
- **Google Fonts**: Schriftarten durchsuchen

### Design-Inspiration
- **Awwwards.com**: Preisgekrönte Webdesigns
- **Dribbble.com**: UI/UX Design-Inspirationen
- **SiteInspire**: Portfolio-Websites
- **csswinner.com**: CSS-Galerien

### Code-Optimierung
- **PageSpeed Insights**: Performance testen
- **WAVE**: Accessibility testen
- **W3C Validator**: HTML/CSS validieren

---

## ❓ FAQ

**F: Muss ich echte Projekte für MiFa erfinden?**  
A: Nein, du kannst fiktive Projekt-Ideen verwenden. Wichtig ist, dass sie zum Thema "Nachhaltige Software für Bildung & Ökologie" passen.

**F: Brauche ich professionelle Design-Tools?**  
A: Nein! Wireframes kannst du auf Papier zeichnen und fotografieren. Für Personas reicht ein simples Markdown-Dokument.

**F: Was wenn ich kein Mockup in LibreOffice öffnen kann?**  
A: Das Mockup ist nur als Inspiration gedacht. Du kannst auch eigene Ideen entwickeln oder ähnliche Layouts im Web suchen.

**F: Muss ich alle JavaScript-Features nutzen?**  
A: Die Vorlage enthält viele Features. Konzentriere dich zuerst auf: Mobile Nav, Formularvalidierung, Smooth Scrolling. Der Rest ist optional.

**F: Wie viele Seiten muss die Website haben?**  
A: Minimum: 4 Bereiche (Home, Über uns, Projekte, Kontakt) als One-Pager. Optional: Mehrere separate HTML-Seiten.

**F: Kann ich ein anderes CSS-Framework nutzen (Bootstrap, Tailwind)?**  
A: Für diese Übung sollst du Custom CSS schreiben, um die Grundlagen zu verstehen. Frameworks sind für spätere Projekte empfohlen.

---

## 🎓 Lernziel-Checkliste

Nach Abschluss solltest du "Ja" sagen können:

### Konzeption
- [ ] Ich kann Zielgruppen für Webprojekte analysieren
- [ ] Ich kann User Personas erstellen
- [ ] Ich verstehe, warum Corporate Design wichtig ist
- [ ] Ich kann Wireframes zeichnen
- [ ] Ich kann eine Sitemap erstellen

### Design
- [ ] Ich kann Farbpsychologie anwenden
- [ ] Ich weiß, wie man Typografie-Hierarchien aufbaut
- [ ] Ich kann CSS Custom Properties sinnvoll einsetzen
- [ ] Ich verstehe Mobile-first Design

### Entwicklung
- [ ] Ich kann semantisches HTML schreiben
- [ ] Ich kann responsive Layouts mit Grid/Flexbox erstellen
- [ ] Ich kann Formulare mit HTML5 + JS validieren
- [ ] Ich kann einfache JavaScript-Interaktionen programmieren
- [ ] Ich kann Bilder responsive einbinden

### Projektmanagement
- [ ] Ich kann ein Webprojekt von A-Z durchführen
- [ ] Ich kann meine Arbeit dokumentieren
- [ ] Ich kann Code-Qualität sicherstellen (Testing)

---

**Viel Erfolg! 🌱💻🚀**

Bei Fragen: Nutze die verlinkten Dokumentationen oder frage deine Lehrkraft.

---

## 🗳️ Partizipative Namensfindung & App‑Portfolio

Ziel: Die Schülerfirma und ihre App‑Projekte werden gemeinschaftlich benannt. Ihr bewertet KI‑Vorschläge und könnt eigene Ideen einreichen. Die Auswertung läuft automatisiert (Python).

### 1) Schülerfirma: Namensvorschläge bewerten und ergänzen

- KI generiert drei Start‑Vorschläge (Beispiel):
    - „Mission Future Academy“ (MiFa)
    - „EduEco Labs“
    - „GreenMind Tech“
- Zusätzlich: Eigene Vorschläge eintragen.

Durchführung (im Classroom):
- Öffne den Fragebogen: `version3/aufgabe/surveys/name_survey/form.html`
- Bewerte jeden KI‑Vorschlag (Skala 1–5) und gib optional eigene Ideen ein.
- Sende das Formular (es erzeugt eine lokale JSON‑Datei im Repo).

Automatische Auswertung (Python):
- Skript: `version3/aufgabe/surveys/name_survey/process.py`
- Aggregiert Stimmen, berechnet Mittelwerte, zeigt Rangliste und Gewinner an.

### 2) App‑Projekte definieren und benennen

Geplante erste drei Projekte (Platzhalternamen → werden ebenfalls bewertet):
- App 1: Mitfahrgelegenheits‑App (Arbeitsname: „RideShare@School“)
- App 2: LernApp MindLink (alias „Mini‑Lük digital“)
- App 3: CO2‑Tracker (Arbeitsname: „School Carbon Tracker“)

Bewertung & Namensfindung:
- Fragebogen: `version3/aufgabe/surveys/app_names/form.html`
- Bewertet die drei Arbeitsnamen und schlagt Alternativen vor.
- Python‑Auswertung: `version3/aufgabe/surveys/app_names/process.py`

### 3) Integration ins Web‑Layout

- Verlinkt die App‑Projekte in `index.html` unter „Unsere Projekte“.
- Nach der Auswertung: Ersetzt Platzhaltertitel/Beschreibungen durch Gewinnernamen.
- Optional: Erstellt eigene Projekt‑Detailseiten.

### Empfehlung: Sollen auch App‑Namen bewertet werden?
- Ja. Dadurch steigt Identifikation und Qualität der Namen (Kriterien: Verständlichkeit, Passung, Merkbarkeit, Einzigartigkeit).
- Bewertet zunächst die drei Arbeitsnamen, sammelt eigene Alternativen und wählt per Auswertung.

---

### Abgabestruktur (Ergänzung)

Fügt für die Befragung folgende Struktur hinzu:

```
version3/aufgabe/
└── surveys/
        ├── name_survey/
        │   ├── form.html
        │   ├── process.py
        │   └── data/
        │       └── responses.json
        └── app_names/
                ├── form.html
                ├── process.py
                └── data/
                        └── responses.json
```
    justify-content: center;
    text-align: center;
    color: white;
}

.hero-content h2 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-content p {
    font-size: 1.5rem;
}

/* Responsive Bilder */
img {
    max-width: 100%;
    height: auto;
    display: block;
}
```

**✅ Testen:**
- Hero-Section sollte Hintergrundbild zeigen
- Bei Fehlendem Bild: Platzhalter `https://picsum.photos/1920/1080` nutzen
- Bilder sollten nicht über Container hinausragen

**📖 Hinweis:** Lies [`docs/bilder-grafiken.md`](../docs/statisch/bilder-grafiken.md) für mehr zu Bildformaten und `object-fit`

---

### Schritt 3: Grid-Galerie (45 Min)

**Ziel:** Responsive Bildgalerie mit automatischem Layout

#### Zu implementieren in `css/style.css`:

```css
/* Galerie-Sektion */
.gallery-section {
    padding: 60px 0;
}

.gallery-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 40px;
    color: #2c3e50;
}

/* Grid-Galerie */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.gallery-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-img:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Responsive Anpassungen */
@media (max-width: 768px) {
    .gallery {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }
    
    .gallery-img {
        height: 200px;
    }
}
```

**✅ Testen:**
- DevTools → Responsive Mode
- **Desktop**: Mehrere Bilder nebeneinander
- **Mobile**: 1-2 Bilder pro Zeile
- **Hover**: Bild vergrößert sich und bekommt Schatten

**📖 Hinweis:** Lies [`docs/galerien.md`](../docs/statisch/galerien.md) für verschiedene Galerie-Layouts

---

### Schritt 4: Lightbox HTML & CSS (60 Min)

**Ziel:** Modal zum Vergrößern der Bilder

#### Zu implementieren in `index.html` (Lightbox-Bereich):

```html
<div id="lightbox" class="lightbox">
    <span class="lightbox-close">&times;</span>
    <span class="lightbox-prev">&#10094;</span>
    <span class="lightbox-next">&#10095;</span>
    <img src="" alt="" id="lightbox-img" class="lightbox-content">
    <div class="lightbox-caption"></div>
</div>
```

#### Zu implementieren in `css/style.css`:

```css
/* Lightbox */
.lightbox {
    display: none; /* Versteckt bis geöffnet */
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    align-items: center;
    justify-content: center;
}

.lightbox.active {
    display: flex;
}

.lightbox-content {
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
    border-radius: 8px;
}

/* Schließen-Button */
.lightbox-close {
    position: absolute;
    top: 20px;
    right: 40px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
    transition: color 0.3s ease;
}

.lightbox-close:hover {
    color: #ff6b6b;
}

/* Navigation */
.lightbox-prev,
.lightbox-next {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: white;
    font-size: 60px;
    font-weight: bold;
    cursor: pointer;
    user-select: none;
    padding: 20px;
    transition: background-color 0.3s ease;
}

.lightbox-prev {
    left: 20px;
}

.lightbox-next {
    right: 20px;
}

.lightbox-prev:hover,
.lightbox-next:hover {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
}

/* Caption */
.lightbox-caption {
    position: absolute;
    bottom: 30px;
    color: white;
    text-align: center;
    width: 100%;
    font-size: 1.2rem;
}
```

**✅ Testen:**
- DevTools → Füge `.active` Klasse zu `.lightbox` hinzu
- Lightbox sollte Vollbild-Overlay zeigen
- Schließen-Button (X) sollte oben rechts sein
- Pfeile sollten links/rechts sein

---

### Schritt 5: Lightbox JavaScript (60 Min)

**Ziel:** Interaktive Lightbox mit Bild-Navigation

#### Zu implementieren in `js/script.js`:

```javascript
// Lightbox Funktionalität
const galleryImages = document.querySelectorAll('.gallery-img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxCaption = document.querySelector('.lightbox-caption');
const closeBtn = document.querySelector('.lightbox-close');
const prevBtn = document.querySelector('.lightbox-prev');
const nextBtn = document.querySelector('.lightbox-next');

let currentImageIndex = 0;

// Bild in Lightbox öffnen
function openLightbox(index) {
    currentImageIndex = index;
    const img = galleryImages[index];
    lightboxImg.src = img.src;
    lightboxCaption.textContent = img.alt;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden'; // Scrollen verhindern
}

// Lightbox schließen
function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Nächstes Bild
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Vorheriges Bild
function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Event Listener für Galerie-Bilder
galleryImages.forEach((img, index) => {
    img.addEventListener('click', () => openLightbox(index));
});

// Event Listener für Lightbox-Controls
closeBtn.addEventListener('click', closeLightbox);
prevBtn.addEventListener('click', prevImage);
nextBtn.addEventListener('click', nextImage);

// Klick außerhalb des Bildes schließt Lightbox
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        closeLightbox();
    }
});

// Tastatur-Navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') nextImage();
    if (e.key === 'ArrowLeft') prevImage();
});
```

**✅ Testen:**
- Klicke auf ein Galerie-Bild → Lightbox öffnet sich
- Klicke auf X → Schließt
- Klicke auf Pfeile → Navigiert zwischen Bildern
- Tastatur:
  - **Escape** → Schließt Lightbox
  - **← →** → Navigiert zwischen Bildern
- Klick außerhalb des Bildes → Schließt Lightbox

**📖 Hinweis:** Lies [`docs/js.md`](../docs/dynamisch/js.md) für Event Handling und DOM-Manipulation

---

### Schritt 6: Kontaktformular HTML (30 Min)

**Ziel:** Formular mit allen wichtigen Feldern

#### Zu implementieren in `index.html` (Contact-Form):

```html
<form id="contactForm" class="contact-form">
    <div class="form-group">
        <label for="name">Name *</label>
        <input 
            type="text" 
            id="name" 
            name="name" 
            required 
            minlength="2"
            placeholder="Dein Name">
    </div>

    <div class="form-group">
        <label for="email">E-Mail *</label>
        <input 
            type="email" 
            id="email" 
            name="email" 
            required
            placeholder="deine@email.de">
    </div>

    <div class="form-group">
        <label for="subject">Betreff</label>
        <input 
            type="text" 
            id="subject" 
            name="subject"
            placeholder="Worum geht es?">
    </div>

    <div class="form-group">
        <label for="message">Nachricht *</label>
        <textarea 
            id="message" 
            name="message" 
            rows="5" 
            required
            minlength="10"
            placeholder="Deine Nachricht..."></textarea>
    </div>

    <button type="submit" class="btn-submit">Absenden</button>
</form>
<div id="formMessage" class="form-message"></div>
```

**✅ Testen:**
- Formular sollte 4 Felder zeigen
- `*` markiert Pflichtfelder

---

### Schritt 7: Formular-Styling (45 Min)

**Ziel:** Modernes, ansprechendes Formular-Design

#### Zu implementieren in `css/style.css`:

```css
/* Kontakt-Sektion */
.contact-section {
    padding: 60px 0;
    background-color: #f8f9fa;
}

.contact-section h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 40px;
    color: #2c3e50;
}

/* Formular */
.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #2c3e50;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #667eea;
}

.form-group textarea {
    resize: vertical;
}

/* Submit Button */
.btn-submit {
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.3s ease;
}

.btn-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-submit:active {
    transform: translateY(0);
}

/* Erfolgsmeldung */
.form-message {
    max-width: 600px;
    margin: 20px auto;
    padding: 15px;
    border-radius: 4px;
    text-align: center;
    display: none;
}

.form-message.success {
    display: block;
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.form-message.error {
    display: block;
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
```

**✅ Testen:**
- Formular sollte zentriert und mit weißem Hintergrund sein
- Fokus auf Input → Blauer Rand
- Button hat Gradient-Hintergrund
- Hover über Button → Hebt sich leicht an

**📖 Hinweis:** Lies [`docs/formulare.md`](../docs/statisch/formulare.md) für mehr zu Formular-Styling

---

### Schritt 8: JavaScript Formular-Validierung (60 Min)

**Ziel:** Custom Validierung und Feedback bei Submit

#### Zu implementieren in `js/script.js`:

```javascript
// Formular-Validierung
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Verhindert Standard-Submit
    
    // Formular-Daten auslesen
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        subject: document.getElementById('subject').value.trim(),
        message: document.getElementById('message').value.trim()
    };
    
    // Validierung
    if (!validateForm(formData)) {
        showMessage('Bitte fülle alle Pflichtfelder korrekt aus!', 'error');
        return;
    }
    
    // Simuliere erfolgreichen Versand
    showMessage('Danke für deine Nachricht! Ich melde mich bald.', 'success');
    contactForm.reset();
    
    // In Realität: Hier würde AJAX/Fetch zum Backend gehen
    // fetch('/api/contact', { method: 'POST', body: JSON.stringify(formData) })
});

// Validierungs-Funktion
function validateForm(data) {
    // Name mindestens 2 Zeichen
    if (data.name.length < 2) {
        return false;
    }
    
    // E-Mail Format prüfen
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(data.email)) {
        return false;
    }
    
    // Nachricht mindestens 10 Zeichen
    if (data.message.length < 10) {
        return false;
    }
    
    return true;
}

// Nachricht anzeigen
function showMessage(text, type) {
    formMessage.textContent = text;
    formMessage.className = `form-message ${type}`;
    
    // Nach 5 Sekunden ausblenden
    setTimeout(() => {
        formMessage.className = 'form-message';
    }, 5000);
}
```

**✅ Testen:**
- Formular leer absenden → Fehlermeldung (HTML5-Validierung)
- Ungültige Email → Fehlermeldung
- Name zu kurz (< 2 Zeichen) → Fehlermeldung
- Nachricht zu kurz (< 10 Zeichen) → Fehlermeldung
- Alle Felder korrekt → Erfolgsmeldung (grün)
- Formular wird zurückgesetzt

---

### Schritt 9: Header & Navigation (30 Min)

**Ziel:** Sticky Header mit Smooth Scrolling

#### Zu implementieren in `css/style.css`:

```css
/* Header */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 1.8rem;
}

/* Navigation */
.nav {
    display: flex;
    gap: 30px;
    list-style: none;
}

.nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.nav a:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}
```

**✅ Testen:**
- Header bleibt beim Scrollen oben (sticky)
- Navigation-Links haben Hover-Effekt
- Klick auf Link → Smooth Scroll zur Sektion

---

### Schritt 10: Footer & Mobile Optimierung (30 Min)

**Ziel:** Footer und responsive Anpassungen

#### Zu implementieren in `css/style.css`:

```css
/* Footer */
footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 30px 0;
    margin-top: 60px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    header .container {
        flex-direction: column;
        gap: 20px;
    }
    
    .nav {
        flex-direction: column;
        gap: 10px;
        text-align: center;
    }
    
    .hero-content h2 {
        font-size: 2rem;
    }
    
    .hero-content p {
        font-size: 1.2rem;
    }
    
    .contact-form {
        padding: 20px;
    }
}
```

**✅ Finaler Test:**
- [ ] Alle Bilder laden korrekt
- [ ] Galerie ist responsive (1-4 Spalten)
- [ ] Lightbox funktioniert vollständig
- [ ] Formular validiert und zeigt Meldungen
- [ ] Smooth Scrolling zu Sektionen
- [ ] Mobile Ansicht optimiert
- [ ] Keine Fehler in der Console

---

## 🧪 Test-Checkliste

### Desktop (> 1024px)
- [ ] Hero-Bild wird angezeigt (Parallax-Effekt)
- [ ] Galerie zeigt 3-4 Bilder pro Zeile
- [ ] Lightbox öffnet beim Klick auf Bild
- [ ] Navigation zwischen Bildern (Pfeile, Tastatur)
- [ ] Formular ist zentriert und gut lesbar
- [ ] Header ist sticky

### Tablet (768px - 1024px)
- [ ] Galerie zeigt 2-3 Bilder pro Zeile
- [ ] Formular passt sich an
- [ ] Alle Funktionen verfügbar

### Mobile (< 768px)
- [ ] Galerie zeigt 1-2 Bilder pro Zeile
- [ ] Navigation untereinander
- [ ] Hero-Text skaliert herunter
- [ ] Formular ist gut bedienbar
- [ ] Lightbox nutzt vollen Bildschirm

### Bilder & Galerie
- [ ] Alle Bilder haben Alt-Texte
- [ ] `object-fit: cover` funktioniert
- [ ] Hover-Effekt auf Bildern (Scale, Shadow)
- [ ] Lightbox zeigt Bild in voller Auflösung
- [ ] Caption zeigt Alt-Text

### Formular
- [ ] HTML5-Validierung aktiv (required, email)
- [ ] JavaScript-Validierung funktioniert
- [ ] Erfolgsmeldung (grün) bei korrekter Eingabe
- [ ] Fehlermeldung (rot) bei Fehler
- [ ] Formular wird nach Submit zurückgesetzt
- [ ] Focus-State sichtbar (blauer Rand)

### Interaktivität
- [ ] Smooth Scrolling funktioniert
- [ ] Lightbox:
  - [ ] Öffnet bei Klick
  - [ ] Schließt bei X, Escape, Außenklick
  - [ ] Pfeile navigieren zwischen Bildern
  - [ ] Tastatur (← →) funktioniert
- [ ] Formular Submit verhindert Neuladen

---

## 💡 Debugging-Tipps

**Problem: Bilder werden nicht angezeigt**
- Prüfe Pfade in `src` Attribut
- DevTools → Network Tab → Rote Einträge = fehlende Dateien
- Groß-/Kleinschreibung beachten!

**Problem: Lightbox öffnet nicht**
- Console → JavaScript-Fehler?
- IDs korrekt? (`lightbox`, `lightbox-img`)
- `script.js` eingebunden?

**Problem: Formular sendet trotz Fehler**
- `e.preventDefault()` vorhanden?
- Validierungs-Funktion wird aufgerufen?

**Problem: Galerie nicht responsive**
- `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))` gesetzt?
- Media Queries aktiv?

---

## 📚 Hilfsmittel & Dokumentation

### Theorie & Konzepte
- [`docs/bilder-grafiken.md`](../docs/statisch/bilder-grafiken.md) - Bildformate, responsive Bilder, `object-fit`
- [`docs/galerien.md`](../docs/statisch/galerien.md) - Grid-Galerien, Lightbox, Masonry
- [`docs/formulare.md`](../docs/statisch/formulare.md) - Formular-Grundlagen, Validierung, Styling

### JavaScript & Interaktivität
- [`docs/js.md`](../docs/dynamisch/js.md) - DOM-Manipulation, Events, Validierung

### CSS & Layout
- [`docs/flexible-layouts.md`](../docs/statisch/flexible-layouts.md) - CSS Grid für Galerien
- [`docs/responsive-design.md`](../docs/statisch/responsive-design.md) - Media Queries

### Zusätzliche Ressourcen
- [`shared-examples/`](../shared-examples/) - Vollständiges Beispiel
- **Browser DevTools (F12)** - Element Inspector, Console, Network
- **[Unsplash](https://unsplash.com)** - Kostenlose Bilder
- **[Can I Use](https://caniuse.com)** - Browser-Kompatibilität

---

## 🎯 Bewertungskriterien

- [ ] Korrekte Verwendung von Bildformaten
- [ ] Responsive Bilder (max-width, srcset)
- [ ] Funktionale Grid-Galerie
- [ ] Vollständig funktionierende Lightbox
- [ ] Formular mit HTML5 & JS-Validierung
- [ ] Code-Qualität und Kommentare
- [ ] Mobile-Optimierung
- [ ] Barrierefreiheit (Alt-Texte, Labels)

---

## 🌟 Bonus-Aufgaben (Optional)

- [ ] Lazy Loading für Bilder implementieren
- [ ] Unterschiedliche Bildgrößen im Grid (Featured Images)
- [ ] Formular-Daten mit LocalStorage speichern
- [ ] Dark Mode Toggle
- [ ] Bildfilter mit CSS (`filter` Property)
- [ ] Masonry-Layout statt Grid
- [ ] Formular mit PHP/Node.js Backend verbinden

---

## ➡️ Weiterführende Themen

Nach Abschluss dieser Version kannst du mit folgenden Themen weitermachen:

- [`docs/js.md`](../docs/dynamisch/js.md) - Fortgeschrittenes JavaScript
- **Version 4**: JavaScript & Interaktivität (AJAX, Fetch API, Single Page App)
- **Version 5**: Backend Integration (PHP oder Python Flask)
- **Version 6**: Datenbank-Anbindung (MySQL)

---

## 📊 Zeitaufwand

- **Teil 1 (Bilder)**: 60 Min
- **Teil 2 (Galerie)**: 90 Min
- **Teil 3 (Lightbox)**: 60 Min
- **Teil 4 (Formular)**: 90 Min
- **Gesamt**: Ca. 5-6 Stunden

---

**Viel Erfolg!** 🚀 Bei Fragen schaue in die `docs/` oder frage deinen Mentor.
