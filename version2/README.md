# Version 2: Box-Modell & Responsive Layout

**Status:** 🚧 In Planung

## Lernziele

Nach Abschluss dieser Version kannst du:
- ✅ Das CSS Box-Modell verstehen und anwenden
- ✅ Margin, Padding und Border gezielt einsetzen
- ✅ Responsive Layouts mit Media Queries erstellen
- ✅ Mobile Navigation (Hamburger-Menü) implementieren
- ✅ Flexbox für flexible Layouts nutzen

## Voraussetzungen

- Abgeschlossene **Version 1** (HTML-Grundgerüst & CSS-Basics)
- Grundkenntnisse in HTML und CSS
- Verständnis von Selektoren und Eigenschaften

## Aufgabenstellung

### Teil 1: Box-Modell verstehen

📖 **Theorie:** [`docs/box-modell.md`](../docs/box-modell.md)

1. **Erstelle drei verschiedene Boxen** mit unterschiedlichen:
   - Padding-Werten
   - Border-Stilen
   - Margin-Abständen

2. **Experimentiere mit `box-sizing`**:
   - Eine Box mit `content-box`
   - Eine Box mit `border-box`
   - Vergleiche die Unterschiede

**Implementierungsbeispiele:** Siehe Abschnitt "Praktisches Beispiel" in `box-modell.md`

### Teil 2: Responsive Layout

📖 **Theorie:** [`docs/responsive-design.md`](../docs/responsive-design.md) & [`docs/flexible-layouts.md`](../docs/flexible-layouts.md)

1. **Desktop-Layout** (> 1024px):
   - 3-spaltiges Grid
   - Breite Navigation oben
   
2. **Tablet-Layout** (768px - 1024px):
   - 2-spaltiges Grid
   - Kompaktere Navigation

3. **Mobile-Layout** (< 768px):
   - 1-spaltig
   - Hamburger-Menü

**Implementierungsbeispiele:** 
- Grid-Layouts: `flexible-layouts.md` → Beispiel 1-4
- Media Queries: `responsive-design.md` → Abschnitt 2

### Teil 3: Mobile Navigation

📖 **Theorie:** [`docs/responsive-design.md`](../docs/responsive-design.md) (Abschnitt 5) & [`docs/js.md`](../docs/js.md)

Implementiere ein funktionierendes Hamburger-Menü mit:
- Toggle-Button (☰)
- Slide-in Animation
- JavaScript für Interaktivität

**Implementierungsbeispiele:**
- Vollständiges HTML/CSS/JS: `responsive-design.md` → Abschnitt 5 "Mobile Navigation"
- JavaScript Toggle-Funktion: `js.md` → DOM-Manipulation

## Zeitaufwand

- **Teil 1**: 1-2 Stunden
- **Teil 2**: 2-3 Stunden
- **Teil 3**: 1-2 Stunden
- **Gesamt**: Ca. 4-7 Stunden

## Hilfsmittel & Dokumentation

### Theorie & Konzepte
- [`docs/box-modell.md`](../docs/box-modell.md) - **Box-Modell** verstehen: Content, Padding, Border, Margin
- [`docs/responsive-design.md`](../docs/responsive-design.md) - **Responsive Design**: Media Queries, Breakpoints, Mobile-First
- [`docs/flexible-layouts.md`](../docs/flexible-layouts.md) - **Flexbox & Grid**: Flexible Layouts mit praktischen Beispielen
- [`docs/css-basis.md`](../docs/css-basis.md) - CSS Grundlagen: Selektoren, Eigenschaften, Spezifität
- [`docs/css-einbinden.md`](../docs/css-einbinden.md) - CSS einbinden: Inline, Internal, External

### JavaScript & Interaktivität
- [`docs/js.md`](../docs/js.md) - JavaScript Grundlagen für interaktive Navigation

### Zusätzliche Ressourcen
- [`shared-examples/`](../shared-examples/) - Vollständiges Beispiel zum Vergleich
- **Browser DevTools (F12)** - Box-Modell visualisieren & Grid/Flexbox anzeigen
- **Responsive Design Checker** - Testen auf verschiedenen Geräten

## Bewertungskriterien

- [ ] Korrektes Verständnis des Box-Modells
- [ ] Saubere Media Queries ohne Überlappungen
- [ ] Funktionierendes Hamburger-Menü
- [ ] Responsive Bilder (max-width: 100%)
- [ ] Code-Qualität und Kommentare
- [ ] Browser-Kompatibilität

## Bonus-Aufgaben (Optional)

- Smooth Scroll-Verhalten
- Sticky Navigation
- Dark Mode mit Media Query
- CSS Grid statt Flexbox

---

## Weiterführende Themen

Nach Abschluss dieser Version kannst du mit folgenden Themen weitermachen:

- [`docs/bilder-grafiken.md`](../docs/bilder-grafiken.md) - Responsive Bilder & `object-fit`
- [`docs/galerien.md`](../docs/galerien.md) - Bildgalerien mit Grid
- [`docs/formulare.md`](../docs/formulare.md) - Responsive Formulare gestalten
- [`docs/css-formatierung.md`](../docs/css-formatierung.md) - Typografie & Farben

---

**Viel Erfolg!** Bei Fragen schaue in die `docs/` oder frage deinen Mentor.
