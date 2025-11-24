# Web Project Dynamic

Ein Ausbildungs-Template für den GitHub Classroom: Vom ersten HTML-Grundgerüst bis zu React, PHP, Python (Flask), JavaScript, CSS und MySQL-Datenbankanbindung. Alle Begriffe sind in verlinkten Info-Dateien erklärt. Ziel: Schüler ohne Vorkenntnisse schrittweise zur Erstellung einer vollständigen Webanwendung befähigen.

## Inhalt / Lernpfade

| Bereich | Datei / Link | Kurzbeschreibung |
|--------|---------------|------------------|
| Einstieg & Überblick | `docs/intro.md` | Was ist das Web? Rollen von Client/Server |
| HTML Grundgerüst | `docs/html-grundgeruest.md` | Aufbau von `<!DOCTYPE html>`, Grundtags, Validierung |
| Seitenstrukturelemente | `docs/seitenstrukturelemente.md` | Semantische Tags (`header`,`nav`,`main`,`section`,...) |
| CSS einbinden | `docs/css-einbinden.md` | Externe, interne & inline CSS, Best Practices |
| CSS Basis | `docs/css-basis.md` | Selektoren, Eigenschaften, erste Styles |
| CSS Formatierung | `docs/css-formatierung.md` | Text, Farben, Abstände, Schatten, Transitions |
| Box-Modell | `docs/box-modell.md` | `margin`, `border`, `padding`, `content` |
| Responsive Design | `docs/responsive-design.md` | Media Queries, Mobile Navigation, Breakpoints |
| Bilder & Grafiken | `docs/bilder-grafiken.md` | Formate, Einbindung, Responsivität |
| Galerien | `docs/galerien.md` | Einfache Bildgalerie, Grid/Flex |
| Formulare & Auswertung | `docs/formulare.md` | Formulare erstellen & validieren |
| JavaScript Grundlagen | `docs/js.md` | Variablen, Funktionen, DOM, Events |
| React Einstieg | `docs/react.md` | Komponenten, Props, State |
| Python (Flask) | `docs/python.md` | Minimales API Backend |
| PHP Grundlagen | `docs/php.md` | Serverseitige Skripte, Ausgabe, Verarbeitung |
| Datenbank (MySQL) | `docs/datenbank.md` | Tabellen, Abfragen, Verbindung |
| Algorithmen & Datenstrukturen | `docs/algorithmen-datenstrukturen.md` | Listen, Arrays, Sortieren, Suchen |
| Testen | `docs/testen.md` | Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit) |

Alle Dateien werden sukzessive erstellt. Falls ein Link ins Leere zeigt, steht der Abschnitt noch aus.

---

## 📚 Aufgaben & Lernversionen

### Version 1: HTML-Grundgerüst & CSS-Einbindung ✅
**Lernziele:** HTML5-Struktur, semantische Elemente, externe CSS-Datei, erste Formatierungen

- **Aufgabenstellung:** `version1/AUFGABE.md`
- **Musterlösung:** `version1/loesung/`
- **Arbeitsordner:** `version1/aufgabe/` (hier arbeitest du!)

**Themen:**
- ✅ HTML-Grundgerüst (DOCTYPE, head, body)
- ✅ Semantische Strukturelemente (header, nav, main, section, footer)
- ✅ CSS-Datei einbinden
- ✅ Grundlegende CSS-Formatierungen (Farben, Schriften, Abstände)

**Zeitaufwand:** Ca. 2-3 Stunden

---

### Version 2: Box-Modell & Layout (In Planung)
Coming soon...

### Version 3: Responsive Design & Mobile Menu (In Planung)
Coming soon...

### Version 4: Formulare & Validierung (In Planung)
Coming soon...

## Projektstruktur (geplant)

```
docs/                  # Lern- und Erklärdateien (Markdown)
shared-examples/       # Vollständiges responsive Beispiel mit React-Elementen
├── css/
│   └── style.css     # Moderne Styles mit Rot-Orange Farbschema
├── js/
│   └── script.js     # Interaktive Elemente
├── images/
│   └── schildkroete_echse.jpg
└── index.html        # Motivierendes Beispiel mit KI-Coach Motto

version1/              # Aufgabe 1: HTML-Grundgerüst & CSS
├── AUFGABE.md        # Detaillierte Aufgabenstellung
├── aufgabe/          # Hier arbeiten die Schüler
└── loesung/          # Musterlösung zur Selbstkontrolle
    ├── index.html
    └── css/style.css

frontend/              # React + JS/TS Beispiel (geplant)
backend-python/        # Flask Backend + Tests (geplant)
backend-php/           # PHP Beispiel + Tests (geplant)
db/                    # SQL Skripte / Migrationsgrundlagen (geplant)
docker-compose.yml     # Entwicklungsumgebung (geplant)
```

## Erste Schritte

1. Klone das Repository (Classroom verteilt es automatisch):
   ```bash
   git clone <REPO_URL>
   cd web-project-dynamic
   ```
2. **Starte mit Version 1:** Lies `version1/AUFGABE.md` und arbeite im Ordner `version1/aufgabe/`
3. **Hilfe benötigt?** Schaue in die `docs/` Dateien - dort ist alles erklärt!
4. **Beispiel ansehen:** Öffne `shared-examples/index.html` im Browser für Inspiration

## 🧪 Wie teste ich meine Webseite?

### Methode 1: Direkt im Browser öffnen (Einfachste Methode)
1. Öffne den Datei-Explorer deines Computers
2. Navigiere zu: `web-project-dynamic/shared-examples/`
3. **Rechtsklick** auf `index.html` 
4. Wähle "Öffnen mit" → Dein Browser (Chrome, Firefox, Edge, Safari)
5. Die Seite wird sofort angezeigt!

**Tipp**: Bei Änderungen am Code einfach die Browser-Seite **neu laden** (F5 oder Strg+R / Cmd+R).

### Methode 2: VS Code Live Server (Empfohlen für Entwicklung)
1. Installiere die Extension "Live Server" in VS Code:
   - Klicke auf das Extensions-Symbol (links in der Seitenleiste)
   - Suche nach "Live Server" (von Ritwick Dey)
   - Klicke auf "Install"
2. Öffne `shared-examples/index.html` in VS Code
3. **Rechtsklick** im Editor → "Open with Live Server"
4. Dein Browser öffnet sich automatisch mit der Seite
5. **Vorteil**: Änderungen werden automatisch im Browser aktualisiert!

### Methode 3: Python HTTP Server (Terminal)
Falls Python installiert ist:
```bash
cd shared-examples
python3 -m http.server 8000
```
Dann im Browser öffnen: `http://localhost:8000`

### Methode 4: VS Code Simple Browser (Integriert)
1. Öffne `shared-examples/index.html` in VS Code
2. Drücke `Strg+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (Mac)
3. Tippe: "Simple Browser: Show"
4. Gib ein: `file:///DEIN_PFAD/web-project-dynamic/shared-examples/index.html`

### 📱 Mobile-Ansicht testen (Responsive Design)
**Im Browser (Chrome/Firefox/Edge)**:
1. Öffne die Webseite
2. Drücke `F12` für Developer Tools
3. Klicke auf das **Smartphone-Symbol** (Toggle Device Toolbar)
4. Wähle verschiedene Geräte aus dem Dropdown (iPhone, iPad, Samsung...)
5. Teste das Hamburger-Menü (☰) und die Anpassung der Layouts

**Tastenkombinationen**:
- Chrome: `Strg+Shift+M` / `Cmd+Shift+M`
- Firefox: `Strg+Shift+M` / `Cmd+Shift+M`

### ✅ Was solltest du testen?
- [ ] Seite lädt ohne Fehler
- [ ] Alle Bilder werden angezeigt
- [ ] CSS wird korrekt angewendet (Farben, Layout)
- [ ] JavaScript funktioniert (Button-Klick zeigt Alert)
- [ ] Navigation funktioniert (Links springen zu Sektionen)
- [ ] **Mobile**: Hamburger-Menü öffnet/schließt Navigation
- [ ] **Mobile**: Cards stapeln sich untereinander
- [ ] **Tablet**: Cards zeigen sich in 2 Spalten
- [ ] **Desktop**: Cards zeigen sich in 3 Spalten

### 🐛 Fehlersuche (Debugging)
Wenn etwas nicht funktioniert:
1. Öffne Developer Tools (`F12`)
2. Schaue in die **Console** (zeigt JavaScript-Fehler)
3. Schaue in den **Network**-Tab (zeigt fehlende Dateien)
4. Prüfe Dateinamen und Pfade (Groß-/Kleinschreibung beachten!)

Häufige Fehler:
- CSS wird nicht geladen → Pfad in `<link href="css/style.css">` prüfen
- JS funktioniert nicht → Pfad in `<script src="js/script.js">` prüfen
- Bilder fehlen → URL oder Pfad prüfen

## 🔍 Testen & Ansehen der Webseite

Es gibt mehrere Möglichkeiten, deine Arbeit im Browser zu testen:

### **Methode 1: Live Preview in VS Code (Empfohlen für Anfänger)**

1. **Live Server Extension installieren:**
   - Klicke links auf das Extensions-Symbol (vier Quadrate) oder drücke `Strg+Shift+X`
   - Suche nach "Live Server" (von Ritwick Dey)
   - Klicke auf "Install"

2. **HTML-Datei öffnen:**
   - Navigiere im Explorer zu `shared-examples/index.html`
   - Rechtsklick auf die Datei → **"Open with Live Server"**

3. **Automatisches Neuladen:**
   - Der Browser öffnet sich automatisch
   - Änderungen in HTML/CSS/JS werden sofort sichtbar (Auto-Reload)
   - Die Seite läuft auf `http://127.0.0.1:5500` oder ähnlich

4. **Responsive testen:**
   - Im Browser: `F12` für DevTools
   - Klicke auf das Handy/Tablet-Symbol (Toggle Device Toolbar)
   - Wähle verschiedene Geräte aus (iPhone, iPad, etc.)

### **Methode 2: Simple Browser in VS Code**

1. **HTML-Datei öffnen** (`shared-examples/index.html`)
2. Drücke `Strg+Shift+P` (Command Palette)
3. Tippe: **"Simple Browser: Show"**
4. Gib die URL ein: `file:///workspaces/web-project-dynamic/shared-examples/index.html`

⚠️ **Nachteil:** Kein automatisches Neuladen bei Änderungen.

### **Methode 3: Direkt im Browser öffnen**

1. **Datei-Explorer öffnen:**
   - Navigiere zu deinem Projektordner
   - Finde `shared-examples/index.html`

2. **Im Browser öffnen:**
   - Rechtsklick → "Öffnen mit" → Wähle deinen Browser (Chrome, Firefox, Edge)
   - Oder ziehe die Datei direkt ins Browser-Fenster

3. **Neuladen nach Änderungen:**
   - Nach jeder Änderung im Code drücke `F5` oder `Strg+R` im Browser

### **Methode 4: Python SimpleHTTPServer (Fortgeschritten)**

Falls Python installiert ist:
```bash
cd shared-examples
python3 -m http.server 8000
```
Dann öffne `http://localhost:8000` im Browser.

---

## 📱 Mobile Ansicht testen

1. **Browser DevTools öffnen:** `F12`
2. **Device Toolbar aktivieren:** `Strg+Shift+M` (Chrome/Edge) oder Icon oben links
3. **Gerät wählen:** iPhone, iPad, oder benutzerdefinierte Größe
4. **Hamburger-Menü testen:** Bei Bildschirmbreite < 768px erscheint das ☰ Symbol
5. **Touch-Simulation:** Klicke auf Links und Buttons, um Navigation zu testen

### Was du testen solltest:
- ✅ Funktioniert das Toggle-Menü auf kleinen Bildschirmen?
- ✅ Sind alle Texte lesbar?
- ✅ Passen Bilder sich an die Breite an?
- ✅ Sind Buttons groß genug zum Tippen (min. 44x44px)?
- ✅ Scrollen alle Bereiche korrekt?

---

## 🐛 Debugging-Tipps

**Problem: CSS wird nicht geladen**
- Prüfe den Pfad in `index.html`: `<link rel="stylesheet" href="css/style.css">`
- Öffne DevTools (F12) → Tab "Network" → Suche nach `style.css` (rot = Fehler)

**Problem: JavaScript funktioniert nicht**
- Öffne DevTools → Tab "Console" → Suche nach Fehlermeldungen (rot)
- Prüfe den Pfad: `<script src="js/script.js"></script>`

**Problem: Seite lädt nicht (Live Server)**
- Stelle sicher, dass Live Server Extension aktiv ist (unten rechts in VS Code)
- Stoppe Server (Rechtsklick auf Port) und starte neu

**Problem: Mobile Ansicht zeigt Desktop-Version**
- Prüfe ob `<meta name="viewport" content="width=device-width, initial-scale=1.0">` im `<head>` steht

---

## 📂 Dateistruktur (shared-examples/)

```
shared-examples/
├── index.html          # Haupt-HTML-Datei
├── css/
│   └── style.css       # Alle Styles + Media Queries
└── js/
    └── script.js       # Mobile Navigation + Interaktionen
```

**Wichtig:** Achte immer auf korrekte Pfade beim Einbinden von Dateien!

## Nächste Schritte für Lernende

1. HTML Grundgerüst nachvollziehen.
2. CSS Box-Modell begreifen und mit Entwickler-Tools inspizieren.
3. Bilder einfügen und responsiv skalieren.
4. Formulare bauen und erste Validierung (HTML5 / JS) ausprobieren.
5. JavaScript: DOM manipulieren, kleine Interaktion (Button klick).
6. React: Eine kleine Komponentenstruktur erstellen.
7. Backend Python/PHP: Ein einfaches Formular serverseitig verarbeiten.
8. Datenbank anbinden: Werte speichern und auslesen.
9. Tests schreiben: Einfache Funktion testen (z.B. Sortier-Algorithmus).

## Tests (Überblick)

Geplant sind einfache Beispiele für:
- Jest (JavaScript / React)
- Pytest (Python Flask Funktionen)
- PHPUnit (PHP Formulardaten-Verarbeitung)

## Mitmachen / Beiträge

Verbesserungen willkommen (Lehrer / Mentoren). Bitte klare, einfache Sprache nutzen.

## Lizenz / Nutzung

Interner Unterrichtsgebrauch. Kein sensibler Code. Bei externer Nutzung bitte an Lehrkräfte wenden.

---
Diese README wächst mit dem Projekt. Bei Fragen: Lehrkraft / Mentor fragen.
