# Konzeption im Webdesign

Die **Konzeption** ist die Planungsphase vor der eigentlichen Umsetzung einer Website. Hier werden Ziele definiert, Inhalte strukturiert und die User Experience geplant.

**Merksatz:** Wer nicht plant, plant zu scheitern.

---

## Warum ist Konzeption wichtig?

Siehe auch: [Einführung ins Web](../statisch/intro.md) für grundlegende Konzepte.

✅ **Klare Ziele** - Wissen, was erreicht werden soll  
✅ **Strukturierte Inhalte** - Übersichtliche Navigation  
✅ **Bessere UX** - Nutzer finden schnell, was sie suchen  
✅ **Zeit sparen** - Weniger Änderungen während der Entwicklung  
✅ **Kosteneffizienz** - Fehler früh erkennen ist günstiger

---

## Die 7 Phasen der Webdesign-Konzeption

### Phase 1: Briefing & Zielsetzung

**Was soll die Website erreichen?**

#### Fragen klären

- **Zweck:** Informieren, Verkaufen, Kontakte generieren?
- **Zielgruppe:** Wen möchten wir erreichen?
- **Alleinstellungsmerkmal:** Was macht uns einzigartig?
- **Budget & Timeline:** Welche Ressourcen stehen zur Verfügung?
- **Erfolgsmetriken:** Woran messen wir den Erfolg?

#### Beispiel: Schülerfirma MiFa (Mission Future Academy)

```
Zweck:
- Vorstellung der Schülerfirma
- Präsentation nachhaltiger Software-Lösungen
- Kontaktaufnahme für Projekte

Zielgruppe:
- Schulen und Bildungseinrichtungen
- Umweltorganisationen
- Gleichgesinnte Schüler:innen
- Potenzielle Partner

Alleinstellungsmerkmal:
- Von Schülern für Bildung & Ökologie
- Nachhaltige Software-Entwicklung
- Junge, frische Perspektive

Ziele:
- Mindestens 100 Besucher/Monat im ersten Jahr
- 10 Kontaktanfragen pro Quartal
- Sichtbarkeit bei lokalen Schulen
```

---

### Phase 2: Zielgruppenanalyse

📖 **Vertiefung:** [`docs/zielgruppenanalyse.md`](zielgruppenanalyse.md)

**Verstehe deine Nutzer!**

#### Personas erstellen

Eine **Persona** ist eine fiktive Person, die eine Nutzergruppe repräsentiert.

**Beispiel-Persona 1: Laura (Lehrerin)**

```
Name: Laura Schneider
Alter: 32 Jahre
Beruf: Lehrerin für Informatik & Ethik
Technik-Level: Fortgeschritten

Ziele:
- Nachhaltige Lernmaterialien finden
- Schüler für IT & Umwelt begeistern
- Kooperationsprojekte initiieren

Bedürfnisse:
- Übersichtliche Projektübersicht
- Kontakt zu Schülerfirma
- Einfache Buchung von Workshops

Frustrationen:
- Komplizierte Websites
- Fehlende Informationen zu Preisen
- Lange Wartezeiten bei Anfragen
```

**Beispiel-Persona 2: Tim (Schüler)**

```
Name: Tim Weber
Alter: 16 Jahre
Beruf: Schüler, interessiert an Programmierung
Technik-Level: Mittel bis fortgeschritten

Ziele:
- Praktische Erfahrung sammeln
- Bei Projekten mitarbeiten
- Gleichgesinnte finden

Bedürfnisse:
- Einfache Bewerbungsmöglichkeit
- Infos zu aktuellen Projekten
- Social-Media-Verlinkungen

Frustrationen:
- Zu viel Text
- Unübersichtliche Navigation
- Keine mobilen Ansichten
```

#### User Stories ableiten

**Format:** Als [Nutzer] möchte ich [Funktion], um [Ziel] zu erreichen.

```
✅ Als Lehrerin möchte ich Projektbeispiele sehen, um einschätzen zu können, ob die Schülerfirma zu uns passt.

✅ Als Schüler möchte ich ein Kontaktformular nutzen, um mich schnell bewerben zu können.

✅ Als Umweltorganisation möchte ich Referenzen sehen, um Vertrauen aufzubauen.

✅ Als mobiler Nutzer möchte ich die Website auf dem Smartphone nutzen, um auch unterwegs Infos zu finden.
```

---

### Phase 3: Inhaltsplanung (Content Strategy)

**Welche Inhalte braucht die Website?**

#### Seitenstruktur definieren

**Hauptnavigation:**

```
- Startseite
- Über uns
- Projekte / Portfolio
- Team
- Kontakt
```

**Footer-Navigation:**

```
- Impressum
- Datenschutz
- Social Media Links
```

#### Content-Inventar erstellen

| Seite          | Inhalt                                    | Priorität | Status |
| -------------- | ----------------------------------------- | --------- | ------ |
| **Startseite** | Hero-Bild, Mission-Statement, Highlights  | Hoch      | Todo   |
| **Über uns**   | Vision, Werte, Geschichte                 | Hoch      | Todo   |
| **Projekte**   | Portfolio mit Screenshots, Beschreibungen | Hoch      | Todo   |
| **Team**       | Fotos, Rollen, Kurzbiografien             | Mittel    | Todo   |
| **Kontakt**    | Formular, E-Mail, Social Media            | Hoch      | Todo   |

#### Texte schreiben: Die 3 K's

**Klar - Kurz - Konkret**

❌ **Schlecht:**

```
Unsere Schülerfirma beschäftigt sich mit der
Entwicklung von innovativen Softwarelösungen
im Bereich nachhaltiger Technologien für den
Bildungssektor und ökologische Organisationen.
```

✅ **Besser:**

```
Wir entwickeln nachhaltige Software für
Bildung und Umwelt. Von Schülern. Für die Zukunft.
```

---

### Phase 4: Informationsarchitektur

**Wie ist die Website strukturiert?**

#### Sitemap erstellen

```
Startseite
│
├── Über uns
│   ├── Vision & Mission
│   ├── Unser Team
│   └── Partner
│
├── Projekte
│   ├── Bildungs-Apps
│   ├── Öko-Tools
│   └── Alle Projekte
│
├── Services
│   ├── Workshops
│   ├── Beratung
│   └── Entwicklung
│
└── Kontakt
    ├── Kontaktformular
    └── Bewerbung
```

#### Navigation gestalten

**Flache Hierarchie bevorzugen:**

- ✅ Max. 3 Klick-Ebenen bis zum Ziel
- ✅ Hauptnavigation mit 5-7 Punkten
- ✅ Aussagekräftige Bezeichnungen

**Breadcrumbs nutzen:**

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/">Startseite</a></li>
    <li><a href="/projekte">Projekte</a></li>
    <li aria-current="page">Bildungs-Apps</li>
  </ol>
</nav>
```

---

### Phase 5: Wireframing

**Skizzen der Seitenlayouts**

#### Low-Fidelity Wireframes

**Einfache Skizzen** mit Kästen und Platzhaltern:

```
┌─────────────────────────────────────────┐
│  [LOGO]              [NAV] [NAV] [NAV] │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│                                         │
│         [HERO IMAGE]                    │
│    "Nachhaltige Software"               │
│         [Button]                        │
│                                         │
└─────────────────────────────────────────┘

┌──────────────┬──────────────┬──────────────┐
│   [Icon]     │   [Icon]     │   [Icon]     │
│  Feature 1   │  Feature 2   │  Feature 3   │
│  Beschreibung│  Beschreibung│  Beschreibung│
└──────────────┴──────────────┴──────────────┘
```

#### Tools für Wireframes

- **Stift & Papier** - Schnellste Methode
- **Excalidraw** - Kostenlos, Browser-basiert
- **Figma** - Professionell, gratis für Studenten
- **Balsamiq** - Spezialisiert auf Wireframes

#### Beispiel-Wireframe: Startseite MiFa

```html
<!-- Wireframe als HTML-Kommentar -->
<!--
HEADER
- Logo links
- Navigation rechts: Über uns | Projekte | Kontakt

HERO
- Vollbild-Bild (Natur + Technologie)
- Overlay mit Slogan
- CTA-Button

MISSION SECTION
- 3 Spalten (Icon + Text)
  1. Nachhaltig
  2. Innovativ
  3. Von Schülern

PROJEKTE-PREVIEW
- Grid mit 3 Projekten
- Bild, Titel, kurze Beschreibung
- "Alle Projekte" Button

TEAM-PREVIEW
- Slider mit Teammitgliedern
- Fotos + Namen + Rollen

CTA SEKTION
- "Starte dein Projekt mit uns"
- Kontakt-Button

FOOTER
- Social Media Icons
- Impressum | Datenschutz
-->
```

---

### Phase 6: Mockups & Prototyping

**Visuelles Design** mit echten Farben, Schriften und Bildern.

#### High-Fidelity Mockups

**Detaillierte Designs** mit:

- Echten Farben aus dem Corporate Design
- Ausgewählten Schriftarten
- Beispielbildern
- Buttons und Icons

#### Tools für Mockups

- **Figma** - Industry-Standard, kostenlos
- **Adobe XD** - Professionell
- **Canva** - Einfach für Einsteiger
- **Sketch** - Mac only

#### Interaktive Prototypen

**Klickbare Mockups** zum Testen der Navigation:

```
[Startseite] → Klick auf "Projekte" → [Projekte-Seite]
                                      ↓
                      Klick auf Projekt → [Detail-Seite]
```

**In Figma:**

1. Frames für jede Seite erstellen
2. Buttons anklickbar machen
3. Transitions definieren
4. Prototyp teilen & testen

---

### Phase 7: Testing & Iteration

**Testen, Feedback sammeln, verbessern**

#### Usability-Tests durchführen

**5-Nutzer-Test:**

- 5 Personen aus der Zielgruppe
- Aufgaben vorgeben
- Beobachten (nicht helfen!)
- Probleme notieren

**Beispiel-Aufgaben:**

```
1. Finde heraus, welche Projekte die Schülerfirma bereits umgesetzt hat.
2. Bewirb dich als Teammitglied.
3. Kontaktiere die Firma für ein Kooperationsprojekt.
```

#### Feedback-Fragen

- War die Navigation verständlich?
- Hast du alle Informationen gefunden?
- Gab es frustrierende Momente?
- Was hat dir besonders gut gefallen?
- Würdest du die Seite weiterempfehlen?

#### A/B-Testing

**Zwei Varianten vergleichen:**

```html
<!-- Version A: Button grün -->
<button class="cta-button green">Projekt starten</button>

<!-- Version B: Button orange -->
<button class="cta-button orange">Projekt starten</button>
```

**Messung:** Welche Variante wird häufiger geklickt?

---

## Konzeptionsdokument erstellen

### Struktur eines Konzepts

**1. Executive Summary**

- Kurze Zusammenfassung (1 Seite)
- Ziele, Zielgruppe, Kernfunktionen

**2. Projektziele**

- Business-Ziele
- Nutzerziele
- Technische Ziele

**3. Zielgruppenanalyse**

- Personas
- User Stories
- Use Cases

**4. Inhaltskonzept**

- Sitemap
- Content-Inventar
- Textentwürfe

**5. Funktionskonzept**

- Features & Funktionen
- User Flows
- Interaktionen

**6. Designkonzept**

- Wireframes
- Mockups
- Style Guide

**7. Technisches Konzept**

- Technologie-Stack
- Hosting
- Performance-Anforderungen

**8. Zeitplan & Budget**

- Meilensteine
- Ressourcen
- Kosten

### Beispiel-Konzept (verkürzt)

```markdown
# Webkonzept: MiFa - Mission Future Academy

## 1. Executive Summary

MiFa ist eine Schülerfirma, die nachhaltige Software
für Bildung und Ökologie entwickelt. Die Website soll:

- Die Firma vorstellen
- Projekte präsentieren
- Kontakte generieren

Zielgruppe: Schulen, NGOs, Schüler:innen
Launch: Q2 2025

## 2. Zielgruppe

### Persona 1: Laura (Lehrerin, 32)

- Sucht nachhaltige Lernprojekte
- Benötigt schnelle Kontaktmöglichkeit

### Persona 2: Tim (Schüler, 16)

- Möchte mitarbeiten
- Nutzt primär mobil

## 3. Sitemap

- Startseite
- Über uns
- Projekte
- Kontakt

## 4. Wireframes

[Siehe Anhang]

## 5. Zeitplan

- Woche 1-2: Design
- Woche 3-4: Entwicklung
- Woche 5: Testing
- Woche 6: Launch
```

---

## Checkliste: Konzeption

### Vorbereitung

- [ ] Briefing durchführen
- [ ] Ziele definieren
- [ ] Zielgruppe analysieren

### Planung

- [ ] Personas erstellen
- [ ] User Stories formulieren
- [ ] Sitemap skizzieren
- [ ] Content-Inventar anlegen

### Design

- [ ] Wireframes zeichnen
- [ ] Mockups erstellen
- [ ] Prototyp bauen

### Validierung

- [ ] Usability-Tests durchführen
- [ ] Feedback einholen
- [ ] Konzept anpassen

### Dokumentation

- [ ] Konzeptdokument schreiben
- [ ] Stakeholder-Freigabe einholen

---

## Häufige Fehler vermeiden

❌ **Sofort coden** → Erst planen, dann umsetzen  
❌ **Annahmen treffen** → Nutzer fragen, nicht vermuten  
❌ **Zu komplex** → Einfach starten, später erweitern  
❌ **Keine Tests** → Immer mit echten Nutzern testen  
❌ **Fehlendes Feedback** → Regelmäßig Rückmeldung einholen

---

## User Flows erstellen

**Visualisierung der Nutzerwege**

### Beispiel: Kontaktaufnahme

```
START
  ↓
Nutzer landet auf Startseite
  ↓
Klickt auf "Kontakt" in Navigation
  ↓
Füllt Kontaktformular aus
  ↓
Klickt "Absenden"
  ↓
Validierung OK? ──Nein→ Fehlermeldung → Zurück zum Formular
  ↓ Ja
Erfolgsmeldung anzeigen
  ↓
ENDE
```

### User Flow Notation

```
[Rechteck] = Aktion/Schritt
(Kreis) = Start/Ende
<Raute> = Entscheidung
→ = Fluss
```

---

## Card Sorting für Navigation

**Methode:** Nutzer gruppieren Inhalte selbst

### Durchführung

1. **Vorbereitung:** Alle Inhalte auf Karten schreiben
2. **Teilnehmer:** 5-10 Personen aus Zielgruppe
3. **Aufgabe:** "Gruppiere die Karten, wie es für dich Sinn macht"
4. **Analyse:** Häufigste Gruppierungen = Navigation

### Beispiel

**Karten:**

```
Vision, Team, Geschichte, Portfolio, Workshops,
Beratung, Kontaktformular, Bewerbung, E-Mail,
Social Media
```

**Ergebnis-Gruppierung:**

```
Gruppe 1 "Über uns": Vision, Team, Geschichte
Gruppe 2 "Services": Portfolio, Workshops, Beratung
Gruppe 3 "Kontakt": Formular, E-Mail, Bewerbung, Social Media
```

---

## Mobile First vs. Desktop First

### Mobile First (empfohlen)

**Vorteil:** Fokus auf das Wesentliche

```css
/* Base: Mobile */
.container {
  padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 20px;
  }
}

/* Desktop */
@media (min-width: 1200px) {
  .container {
    padding: 40px;
  }
}
```

### Desktop First

**Nachteil:** Oft zu viele Inhalte für Mobile

```css
/* Base: Desktop */
.navigation {
  display: flex;
  flex-direction: row;
}

/* Mobile */
@media (max-width: 768px) {
  .navigation {
    flex-direction: column;
  }
}
```

---

## Nächste Schritte

- **Zielgruppenanalyse** → `zielgruppenanalyse.md` - Nutzer verstehen
- **Corporate Design** → `corporate-design.md` - Visuelles Erscheinungsbild
- **Responsive Design** → `responsive-design.md` - Technische Umsetzung

---

## Tools & Ressourcen

- **Wireframing:** [Excalidraw](https://excalidraw.com/), [Figma](https://figma.com/)
- **Mind Mapping:** [MindMeister](https://www.mindmeister.com/), [Miro](https://miro.com/)
- **User Flows:** [Whimsical](https://whimsical.com/), [Draw.io](https://draw.io/)
- **Prototyping:** [Figma](https://figma.com/), [Adobe XD](https://www.adobe.com/de/products/xd.html)

---

**Tipp:** Plane mindestens 30% der Projektzeit für Konzeption ein. Es lohnt sich!
