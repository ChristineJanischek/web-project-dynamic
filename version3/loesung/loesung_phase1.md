# Phase 1 Musterlösung: Konzeption & Design

## Übersicht
Diese Musterlösung zeigt eine vollständige Konzeption für die **MiFa - Mission Future Academy** Website mit Fokus auf Nachhaltigkeit, Bildung und Innovation.

---

## 1. Zielgruppenanalyse

### Zielgruppe 1: Schüler:innen (14-18 Jahre)
**Bedürfnisse:**
- Inspiration für eigene nachhaltige Projekte
- Einfacher Einstieg in Coding & digitale Tools
- Peer-to-Peer Austausch

**Verhalten:**
- Mobile-first (90% Smartphone-Nutzung)
- Visuelle Inhalte (Videos, Infografiken)
- Social Media affin

### Zielgruppe 2: Lehrkräfte & Schulen
**Bedürfnisse:**
- Unterrichtsmaterialien & Workshops
- Kooperationsmöglichkeiten
- Erfolgsgeschichten & Best Practices

**Verhalten:**
- Desktop-Nutzung während Arbeitszeit
- Suche nach vertrauenswürdigen Partnern
- Langfristige Planungshorizonte

### Zielgruppe 3: Eltern & Förderer
**Bedürfnisse:**
- Transparenz über Projekte & Wirkung
- Kontaktmöglichkeiten
- Finanzielle Förderoptionen

**Verhalten:**
- Tablet/Desktop bevorzugt
- Vertrauen durch professionelles Auftreten
- Interesse an messbaren Erfolgen

---

## 2. Personas

### Persona 1: Emma (16 Jahre) - Schülerin & Umweltaktivistin

**Profil:**
- Gymnasium, 10. Klasse
- Aktiv bei Fridays for Future
- Bloggt über Nachhaltigkeit

**Ziele:**
- Eigene nachhaltige App-Idee umsetzen
- Gleichgesinnte finden
- Digitale Skills ausbauen

**Frustrationen:**
- "Die meisten Coding-Kurse sind langweilig und nicht praxisnah"
- "Ich will etwas Sinnvolles entwickeln, nicht nur Übungen machen"

**User Story:**
*"Als umweltbewusste Schülerin möchte ich lernen, wie man Apps entwickelt, um meine Ideen für eine nachhaltige Zukunft umzusetzen."*

---

### Persona 2: Herr Schmidt (42 Jahre) - Informatiklehrer

**Profil:**
- Gymnasium, Fachbereichsleiter Informatik
- 15 Jahre Lehrerfahrung
- Sucht innovative Unterrichtsprojekte

**Ziele:**
- Schüler:innen für MINT begeistern
- Realitätsnahe Projekte im Unterricht
- Externe Partner für Workshops

**Frustrationen:**
- "Lehrpläne sind oft zu theoretisch"
- "Schwierig, echte Praxisprojekte zu finden"

**User Story:**
*"Als Informatiklehrer möchte ich mit externen Partnern zusammenarbeiten, um meinen Schüler:innen praxisnahe Programmierprojekte anzubieten."*

---

### Persona 3: Sandra (38 Jahre) - Mutter & Unternehmerin

**Profil:**
- Selbstständige Designerin
- Zwei Kinder (14 & 16 Jahre)
- Interesse an nachhaltigen Initiativen

**Ziele:**
- Förderung ihrer Kinder
- Lokale nachhaltige Projekte unterstützen
- Networking mit anderen Eltern

**Frustrationen:**
- "Ich weiß nicht, welche Initiativen wirklich seriös sind"
- "Zu wenig Transparenz über Projekterfolge"

**User Story:**
*"Als Mutter möchte ich vertrauenswürdige Bildungsinitiativen finden, die meine Kinder fördern und gleichzeitig Nachhaltigkeit vermitteln."*

---

## 3. Corporate Design

### Farbpalette

**Primärfarbe: Waldgrün `#2D6A4F`**
- Symbolisiert Nachhaltigkeit, Wachstum, Natur
- Beruhigend und vertrauenswürdig
- Assoziiert mit Umweltschutz

**Sekundärfarbe: Ozeanblau `#0077B6`**
- Steht für Innovation, Technologie, Zukunft
- Kommuniziert Professionalität
- Ergänzt Grün harmonisch (Natur + Tech)

**Akzentfarbe: Sonnengelb `#FFB703`**
- Energie, Optimismus, Kreativität
- Hebt Call-to-Actions hervor
- Jugendlich und einladend

**Neutrale Farben:**
- Weiß `#FFFFFF` - Haupthintergrund
- Hellgrau `#F8F9FA` - Sektionshintergründe
- Dunkelgrau `#2B2D42` - Haupttext
- Mittelgrau `#6C757D` - Sekundärtext

**Begründung:**
Die Farbkombination vereint Natur (Grün) mit Technologie (Blau) und jugendlicher Energie (Gelb) - perfekt für eine Schülerfirma im Bereich nachhaltige Software.

### Typografie

**Headlines: Montserrat (Google Fonts)**
- Modern, geometrisch, gut lesbar
- Vermittelt Innovation und Zukunft
- Starke Präsenz in Headlines
- Weights: Bold (700) für H1/H2, SemiBold (600) für H3

**Body: Open Sans (Google Fonts)**
- Hervorragende Lesbarkeit
- Freundlich und zugänglich
- Optimiert für Bildschirme
- Weights: Regular (400), Medium (500)

**Code/Technisch: Fira Code (optional)**
- Für Code-Snippets in Blog/Projekten
- Ligatures für bessere Code-Darstellung

**Schriftgrößen-System:**
```css
--font-size-xs: 0.875rem;   /* 14px - Captions */
--font-size-sm: 1rem;        /* 16px - Body */
--font-size-md: 1.125rem;    /* 18px - Lead text */
--font-size-lg: 1.5rem;      /* 24px - H3 */
--font-size-xl: 2rem;        /* 32px - H2 */
--font-size-2xl: 3rem;       /* 48px - H1 */
```

**Begründung:**
Montserrat wirkt modern und zukunftsorientiert, während Open Sans maximale Lesbarkeit auch auf mobilen Geräten garantiert.

### Logo-Usage

**Vorhandenes Logo:** `../aufgabe/concept/images/Logo_farbig.jpg`

**Verwendungsregeln:**
- **Mindestgröße:** 120px Breite (Desktop), 80px (Mobile)
- **Schutzraum:** Mindestens 16px Abstand zu anderen Elementen
- **Platzierung:** 
  - Header: Links oben (Standard)
  - Footer: Zentriert mit Kontaktdaten
- **Varianten:**
  - Farbig auf hellem Hintergrund (Standard)
  - Weiß auf dunklen Hero-Backgrounds (mit leichtem Schatten für Kontrast)

**Don'ts:**
- Nicht verzerren (Aspect Ratio beibehalten)
- Nicht auf unruhigen Hintergründen
- Nicht kleiner als Mindestgröße

### Bildsprache

**Stil:**
- Authentische Fotos von echten Schüler:innen bei der Arbeit
- Helle, freundliche Atmosphäre
- Diverse Darstellung (Geschlecht, Herkunft)
- Mix aus Close-ups und Gruppenaufnahmen

**Farbbehandlung:**
- Leichter Grün-/Blau-Stich in Nachbearbeitung
- Hohe Helligkeit, mittlerer Kontrast
- Vermeidung von Überbelichtung

**Motive:**
- Coding-Sessions am Laptop
- Teamwork & Brainstorming
- Natur-Elemente (Pflanzen, Außenaufnahmen)
- Produkte/Apps in Verwendung

**Technische Specs:**
- Format: JPG für Fotos, PNG für Grafiken, SVG für Icons
- Hero-Bilder: Min. 1920x1080px
- Thumbnails: 800x600px
- Kompression: < 200KB (TinyPNG/Squoosh)

---

## 4. Sitemap & Content-Inventar

### Sitemap
```
Home
├── Über uns
│   ├── Vision & Mission
│   ├── Team
│   └── Partner
├── Projekte
│   ├── MiFaRide (Mitfahrgelegenheiten-App)
│   ├── EduTrack (Lernfortschritts-Tracker)
│   └── GreenChallenge (Nachhaltigkeits-App)
├── Services
│   ├── Workshops
│   ├── App-Entwicklung
│   └── Beratung
├── Blog
└── Kontakt
    ├── Formular
    ├── Bewerbung
    └── Social Media
```

### Content-Inventar: Startseite

| Element | Priorität | Inhalt | CTA |
|---------|-----------|--------|-----|
| **Hero** | Must | Mission Statement, Hintergrundbild | "Projekte entdecken" |
| **Mission** | Must | Kurzer Text über Ziele | - |
| **Projekte-Preview** | Must | 3 Highlight-Projekte mit Bild | "Alle Projekte" |
| **Services** | Should | 3 Hauptservices (Icons + Text) | "Mehr erfahren" |
| **Team-Preview** | Should | 4-6 Team-Mitglieder | "Team kennenlernen" |
| **Partner/Testimonials** | Nice | Logos/Zitate | - |
| **CTA-Sektion** | Must | Bewerbung/Kontakt prominent | "Jetzt bewerben" |

---

## 5. Wireframes (Beschreibung)

### Desktop (> 1200px)

**Header:**
- Logo links (120px Höhe)
- Horizontale Navigation rechts (Home, Über uns, Projekte, Services, Blog, Kontakt)
- Sticky bei Scroll

**Hero:**
- Fullscreen Background Image (`Startbild.png`)
- Zentrierter Text: 
  - H1: "Mission Future Academy"
  - Tagline: "Von Schüler:innen für die Zukunft"
  - Button: "Projekte entdecken" (Gelb)
- Scroll-Indikator (Pfeil nach unten)

**Mission-Sektion:**
- Container 1200px max-width
- Zweispaltig: Text links, Bild rechts
- Padding: 80px vertikal

**Projekte-Grid:**
- 3-Spalten Grid
- Cards mit Bild, Titel, Kurzbeschreibung, "Mehr"-Link
- Hover-Effekt: Leichter Lift + Schatten

**Footer:**
- 3-Spalten: Über uns | Quick Links | Kontakt
- Logo zentriert oben
- Social Media Icons
- Copyright-Zeile

### Tablet (768px - 1200px)

**Änderungen:**
- Projekte-Grid: 2 Spalten
- Navigation: Bleibt horizontal (kleinere Schrift)
- Hero: Text bleibt zentriert, etwas kleinere Schrift

### Mobile (< 768px)

**Änderungen:**
- Hamburger-Menü statt horizontaler Navigation
- Projekte-Grid: 1 Spalte
- Hero: H1 kleiner (2rem statt 3rem)
- Footer: 1 Spalte, gestapelt
- Touch-Ziele: Min. 44px Höhe

---

## 6. Navigationskonzept

### Hauptnavigation
- **Desktop:** Horizontale Leiste, max. 6 Punkte
- **Mobile:** Hamburger-Menü (rechts oben)
- **Aktiver Status:** Farbiger Underline (Akzentfarbe)
- **Hover:** Leichte Farbänderung

### Footer-Navigation
- Sitemap-Links
- Legal (Impressum, Datenschutz)
- Social Media

### Accessibility
- Keyboard-Navigation (`Tab`, `Enter`)
- Skip-Link zu Hauptinhalt
- ARIA-Labels für Menü-Toggle

---

## 7. User Stories & Priorisierung

### Must-Have (MVP)
1. Als Besucher möchte ich die Mission von MiFa verstehen, um zu entscheiden, ob ich mich engagieren will.
2. Als Schüler:in möchte ich Projektbeispiele sehen, um zu wissen, was ich lernen kann.
3. Als Lehrkraft möchte ich Kontaktmöglichkeiten finden, um eine Kooperation anzufragen.
4. Als mobiler Nutzer möchte ich die Seite auf dem Smartphone nutzen können.

### Should-Have
5. Als Interessent:in möchte ich das Team kennenlernen, um Vertrauen aufzubauen.
6. Als Schüler:in möchte ich mich online bewerben können.
7. Als Besucher möchte ich Social Media Kanäle finden, um Updates zu erhalten.

### Nice-to-Have
8. Als Schüler:in möchte ich Blog-Artikel lesen, um Tipps zu erhalten.
9. Als Elternteil möchte ich Testimonials sehen, um die Qualität einzuschätzen.
10. Als Besucher möchte ich eine interaktive Projektkarte sehen.

---

## 8. Customer Journey: Schülerin Emma

### Phase 1: Awareness
**Touchpoint:** Instagram-Post über nachhaltiges Coding
**Emotion:** 😊 Neugierig
**Gedanke:** "Klingt spannend, will mehr wissen"
**Aktion:** Klick auf Link → Landingpage

### Phase 2: Consideration
**Touchpoint:** MiFa Website - Hero & Projekte
**Emotion:** 🤔 Interessiert, leicht skeptisch
**Gedanke:** "Ist das wirklich praxisnah? Was haben andere gemacht?"
**Aktion:** Scrollt zu Projekten, klickt auf MiFaRide

### Phase 3: Evaluation
**Touchpoint:** Projektdetails & Team-Seite
**Emotion:** 😍 Begeistert
**Gedanke:** "Die haben echt coole Apps gebaut! Das Team wirkt sympathisch"
**Aktion:** Sucht Bewerbungsformular

### Phase 4: Conversion
**Touchpoint:** Kontaktformular
**Emotion:** 😰 Etwas nervös
**Gedanke:** "Hoffentlich werde ich genommen"
**Aktion:** Füllt Bewerbung aus, sendet ab

### Phase 5: Retention
**Touchpoint:** Willkommens-E-Mail, Social Media
**Emotion:** 🎉 Aufgeregt
**Gedanke:** "Ich bin dabei! Kann's kaum erwarten"
**Aktion:** Folgt auf Instagram, teilt mit Freund:innen

**Pain Points erkannt:**
- Projektdetails müssen überzeugend sein (Screenshots, Videos)
- Bewerbungsformular darf nicht zu lang/komplex sein
- Schnelle Reaktionszeit wichtig

---

## 9. Design-Entscheidungen & Begründungen

### Warum Mobile-First?
- 70% der Zielgruppe (Schüler:innen) nutzen primär Smartphones
- Zwingt zu Priorisierung der wichtigsten Inhalte
- Bessere Performance auf allen Geräten

### Warum große Hero-Sektion?
- Sofortige emotionale Ansprache
- Kommuniziert Mission auf einen Blick
- Moderne Webdesign-Konvention (erwartet von Nutzern)

### Warum Card-basiertes Layout?
- Scanbarkeit: Nutzer können schnell Inhalte erfassen
- Flexibilität: Funktioniert auf allen Bildschirmgrößen
- Skalierbarkeit: Neue Projekte einfach ergänzbar

### Warum begrenzte Farbpalette?
- Wiedererkennungswert
- Konsistenz über alle Seiten
- Accessibility: Einfacher, Kontraste einzuhalten

---

## 10. Next Steps → Phase 2

Mit dieser Konzeption kann Phase 2 starten:

1. **HTML-Grundstruktur** gemäß Wireframes
2. **CSS Custom Properties** aus Corporate Design
3. **Responsive Grid** für Projekte-Sektion
4. **JavaScript** für Navigation & Formular-Validierung
5. **Optimierung** gemäß Performance-Checkliste

**Hinweis für Umsetzung:**
Alle Entscheidungen in dieser Konzeption sind begründet und auf die Zielgruppen ausgerichtet. Bei Änderungen in Phase 2 sollte immer hinterfragt werden: "Dient das unseren Nutzer:innen?"

---

**Fertigstellung:** Phase 1 ✅  
**Geschätzter Aufwand für Konzeption:** 8-10 Stunden  
**Qualität:** Realistische Schülerarbeit mit professioneller Struktur
