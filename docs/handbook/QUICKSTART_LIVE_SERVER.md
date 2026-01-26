# 🚀 Quick Start Guide - Live Server

**Für Schüler:** So testest du deine Website in Echtzeit!

---

## ✅ Schritt 1: Extensions installieren

Beim ersten Öffnen des Projekts erscheint diese Meldung:

```
┌─────────────────────────────────────────────────────┐
│  📦 Dieses Repository empfiehlt Extensions          │
│  [Details anzeigen] [Alle installieren] [Ignorieren] │
└─────────────────────────────────────────────────────┘
```

**➡️ Klicke auf "Alle installieren"**

Das installiert automatisch:
- ✅ Live Server (zum Testen)
- ✅ Prettier (Code-Formatierung)
- ✅ HTML/CSS Support
- ✅ Auto Rename Tag
- Und weitere hilfreiche Tools

**Falls die Meldung nicht erscheint:**
1. Drücke `Ctrl+Shift+P` (Windows) oder `Cmd+Shift+P` (Mac)
2. Tippe: `Show Recommended Extensions`
3. Klicke auf "Install Workspace Recommended Extensions"

---

## ✅ Schritt 2: HTML-Datei öffnen

Öffne deine Arbeits-HTML-Datei, z.B.:
- `version1/aufgabe/index.html` (für Version 1)
- `version2/aufgabe/index.html` (für Version 2)
- `version3/aufgabe/index.html` (für Version 3)

---

## ✅ Schritt 3: Live Server starten

### 🎯 Methode 1: Rechtsklick (am einfachsten!)

```
index.html (Tab ist aktiv)
   │
   ├─ [Rechtsklick in den Code-Editor]
   │
   └─ "Open with Live Server" ← Hier klicken!
```

**ODER:**

### 🎯 Methode 2: Status Bar Button

Schaue unten rechts in der blauen Status-Leiste:

```
VSCode Editor
┌─────────────────────────────────────────────┐
│ dein Code...                                 │
│                                              │
└─────────────────────────────────────────────┘
  [UTF-8] [HTML] [Ln 10, Col 5]  [Go Live] ← Hier klicken!
```

**ODER:**

### 🎯 Methode 3: Tastenkombination

- **Windows/Linux:** `Alt+L` dann `Alt+O`
- **Mac:** `Cmd+L` dann `Cmd+O`

---

## 🎉 Fertig! Browser öffnet sich automatisch

Deine Website läuft jetzt auf: `http://localhost:5500`

```
Chrome/Firefox
┌──────────────────────────────────────────────┐
│ ← → ↻  localhost:5500                        │
├──────────────────────────────────────────────┤
│                                               │
│  🎨 Deine Website wird hier angezeigt        │
│                                               │
│  Ändere HTML/CSS und speichere (Ctrl+S)      │
│  → Browser aktualisiert sich automatisch! ✨  │
│                                               │
└──────────────────────────────────────────────┘
```

---

## 🔄 Änderungen sehen (Auto-Reload!)

1. **Ändere** etwas in deiner HTML- oder CSS-Datei
2. **Speichere** mit `Ctrl+S` (Windows) / `Cmd+S` (Mac)
3. **Schaue** in den Browser → **Automatisch aktualisiert!** 🎉

**Beispiel:**
```html
<!-- Ändere dies: -->
<h1>Hallo Welt</h1>

<!-- In dies: -->
<h1>Meine tolle Website!</h1>
```

**Speichern** → Browser zeigt sofort die neue Überschrift!

---

## ❌ Server stoppen

Wenn du fertig bist:

1. **Klicke** unten rechts auf `Port: 5500`
2. **ODER** drücke `Alt+L` dann `Alt+C` (Windows) / `Cmd+L` dann `Cmd+C` (Mac)

```
Status Bar (unten rechts)
┌────────────────────────────────┐
│ [Port: 5500] ← Hier klicken    │  oder  [Rechtsklick] → "Stop Live Server"
└────────────────────────────────┘
```

---

## 🆘 Probleme?

### ❌ "Go Live" Button erscheint nicht

**Lösung:**
1. Stelle sicher, dass du eine `.html`-Datei geöffnet hast
2. Prüfe, ob Live Server installiert ist: Extensions-Tab (`Ctrl+Shift+X`)
3. Suche nach "Live Server" von Ritwick Dey
4. Falls nicht installiert: Klicke "Install"

### ❌ Browser öffnet sich nicht

**Lösung:**
- Öffne manuell deinen Browser
- Gehe zu: `http://localhost:5500`
- Falls Port 5500 belegt ist, probiere: `http://localhost:5501`

### ❌ Änderungen werden nicht angezeigt

**Lösung:**
1. **Hard Refresh** im Browser: `Ctrl+Shift+R` (Windows) / `Cmd+Shift+R` (Mac)
2. Stelle sicher, dass die Datei gespeichert wurde (kein weißer Punkt am Tab)
3. Prüfe die Browser-Konsole: Drücke `F12` → Suche nach Fehlern

### ❌ CSS wird nicht geladen

**Prüfe:**
1. Ist der CSS-Link in der HTML-Datei korrekt?
   ```html
   <link rel="stylesheet" href="css/style.css">
   ```
2. Pfad korrekt? Prüfe ob `css/style.css` wirklich existiert
3. Browser-Konsole (F12) → Fehler bei "Failed to load resource"?

### ❌ Port 5500 bereits verwendet

**Lösung:**
- Stoppe andere Live Server Instanzen
- Oder ändere Port in `.vscode/settings.json`:
  ```json
  "liveServer.settings.port": 5501
  ```

---

## 💡 Profi-Tipps

### 🔥 Auto-Save aktivieren

Damit du nicht ständig `Ctrl+S` drücken musst:

1. `File` → `Preferences` → `Settings`
2. Suche: `Auto Save`
3. Wähle: `afterDelay`
4. ✅ Speichert jetzt automatisch alle 1 Sekunde!

### 🔍 Browser DevTools nutzen

Drücke `F12` im Browser:

- **Console:** JavaScript-Fehler sehen
- **Elements:** HTML/CSS live bearbeiten (temporär zum Testen!)
- **Network:** Lädt CSS/JS korrekt?
- **Mobile View:** `Ctrl+Shift+M` - Teste responsive Design!

### 🎨 Live-Editing im Browser

1. Öffne DevTools (`F12`)
2. Klicke auf "Elements"
3. Klicke auf ein Element
4. Ändere im "Styles"-Panel CSS-Werte
5. **Achtung:** Änderungen gehen verloren beim Reload!
6. Kopiere gute Änderungen zurück in deine CSS-Datei

### 📱 Mobile-Ansicht testen

1. Öffne deine Website im Live Server
2. Drücke `Ctrl+Shift+M` (Windows) / `Cmd+Shift+M` (Mac)
3. Wähle verschiedene Geräte: iPhone, iPad, Android, etc.
4. Teste ob deine Media Queries funktionieren!

---

## ✅ Checkliste vor dem Committen

Bevor du `git commit` machst:

- ✅ Website im Live Server getestet?
- ✅ In verschiedenen Browsern getestet? (Chrome, Firefox, Safari)
- ✅ Mobile-Ansicht geprüft? (`Ctrl+Shift+M`)
- ✅ Keine Fehler in der Browser-Konsole? (F12)
- ✅ HTML validiert? → GitHub Actions läuft automatisch!
- ✅ Code sauber formatiert? → Prettier macht das automatisch (`Shift+Alt+F`)

---

## 📚 Weiterführende Links

- [Live Server Dokumentation](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [Chrome DevTools Guide](https://developer.chrome.com/docs/devtools/)
- [Responsive Design Testen](https://developers.google.com/web/tools/chrome-devtools/device-mode)

---

**Du bist startklar! Viel Erfolg beim Entwickeln!** 🚀

Bei Fragen: Frage deinen Lehrer oder schaue in die [`docs/`](../docs/) Dokumentation.
