# Einführung ins Web

## Was ist das Web?

Das **World Wide Web** (WWW oder kurz Web) ist ein System von miteinander verlinkten Dokumenten und Ressourcen, die über das Internet zugänglich sind. Es wurde 1989 von Tim Berners-Lee erfunden und ermöglicht es uns heute, Webseiten zu besuchen, Videos anzuschauen, online einzukaufen und vieles mehr.

### Grundlegende Konzepte

- **Internet**: Das globale Netzwerk von Computern
- **Web**: Ein Dienst, der das Internet nutzt (neben E-Mail, FTP, etc.)
- **Browser**: Programme wie Chrome, Firefox, Safari, die Webseiten anzeigen
- **URL**: Die Adresse einer Webseite (z.B. `https://example.com`)

## Client-Server-Modell

Das Web funktioniert nach dem **Client-Server-Prinzip**:

```
┌─────────────┐                  ┌─────────────┐
│   CLIENT    │ ── Anfrage ───>  │   SERVER    │
│  (Browser)  │                  │ (Webserver) │
│             │ <── Antwort ───  │             │
└─────────────┘                  └─────────────┘
```

### Client (Browser)
- **Rolle**: Sendet Anfragen und zeigt Inhalte an
- **Beispiele**: Chrome, Firefox, Safari, Edge
- **Aufgaben**:
  - HTML interpretieren und darstellen
  - CSS für das Styling anwenden
  - JavaScript ausführen
  - Benutzerinteraktionen verarbeiten

### Server (Webserver)
- **Rolle**: Empfängt Anfragen und sendet Antworten
- **Beispiele**: Apache, Nginx, Node.js
- **Aufgaben**:
  - HTML-Dateien bereitstellen
  - Datenbankanfragen verarbeiten
  - Dynamische Inhalte generieren
  - Dateien (Bilder, Videos) ausliefern

## Die drei Säulen der Webentwicklung

### 1. HTML (HyperText Markup Language)
- **Zweck**: Struktur und Inhalt
- **Vergleich**: Das Skelett eines Hauses
- **Beispiel**: Überschriften, Absätze, Links, Bilder

### 2. CSS (Cascading Style Sheets)
- **Zweck**: Aussehen und Layout
- **Vergleich**: Die Farbe, Tapeten und Dekoration
- **Beispiel**: Farben, Schriftarten, Abstände, Animationen

### 3. JavaScript
- **Zweck**: Interaktivität und Dynamik
- **Vergleich**: Die Elektrik und smarte Funktionen
- **Beispiel**: Formularvalidierung, Animationen, API-Aufrufe

## Einfaches Beispiel: Eine erste Webseite

### HTML-Datei (`index.html`)
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine erste Webseite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Willkommen!</h1>
    </header>
    
    <main>
        <p>Das ist meine erste Webseite.</p>
        <button id="clickMe">Klick mich!</button>
    </main>
    
    <script src="script.js"></script>
</body>
</html>
```

### CSS-Datei (`style.css`)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

header {
    background-color: #ff6347;
    color: white;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #45a049;
}
```

### JavaScript-Datei (`script.js`)
```javascript
// Interaktivität hinzufügen
document.getElementById('clickMe').addEventListener('click', function() {
    alert('Hallo! Du hast den Button geklickt!');
});
```

## Wie läuft eine Webanfrage ab?

1. **URL eingeben**: Du gibst `https://example.com` im Browser ein
2. **DNS-Auflösung**: Browser findet die IP-Adresse des Servers
3. **HTTP-Anfrage**: Browser sendet eine Anfrage an den Server
4. **Server verarbeitet**: Server findet die angeforderte Datei
5. **HTTP-Antwort**: Server sendet HTML, CSS, JS, Bilder zurück
6. **Browser rendert**: Browser stellt die Webseite dar
7. **JavaScript ausführen**: Interaktive Elemente werden aktiviert

## Wichtige Begriffe

| Begriff | Bedeutung |
|---------|-----------|
| **HTML** | Struktursprache für Webseiten |
| **CSS** | Stylesheet-Sprache für Design |
| **JavaScript** | Programmiersprache für Interaktivität |
| **HTTP/HTTPS** | Protokoll für Datenübertragung (HTTPS = verschlüsselt) |
| **DOM** | Document Object Model - Baum-Struktur des HTML |
| **Frontend** | Was im Browser läuft (HTML, CSS, JS) |
| **Backend** | Was auf dem Server läuft (PHP, Python, Node.js) |
| **API** | Schnittstelle zwischen Frontend und Backend |

## Nächste Schritte

1. **HTML-Grundgerüst** verstehen und erstellen → `html-grundgeruest.md`
2. **Seitenstrukturelemente** semantisch einsetzen → `seitenstrukturelemente.md`
3. **CSS einbinden** und erste Styles anwenden → `css-einbinden.md`
4. **Responsive Design** für verschiedene Bildschirmgrößen → `responsive-design.md`

---

**Tipp**: Öffne die Browser-Entwicklertools (F12), um die Struktur jeder Webseite zu untersuchen!
