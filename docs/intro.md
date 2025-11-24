# Einstieg: Was ist das Web?

Das **World Wide Web** verbindet Clients (Browser) mit Servern über das HTTP-Protokoll.

## Grundbegriffe
- **Client**: Dein Browser, stellt Seiten dar.
- **Server**: Programm das Anfragen beantwortet (z.B. Apache, Flask, PHP-FPM).
- **Request**: Anfrage (z.B. GET eine Seite abrufen, POST Formular senden).
- **Response**: Antwort mit Statuscode (200 OK, 404 Nicht gefunden...).
- **HTML**: Struktur der Seite.
- **CSS**: Aussehen und Layout.
- **JavaScript**: Interaktivität und Logik im Browser.
- **Backend**: Code der auf dem Server läuft (PHP, Python, Node.js).
- **Datenbank**: Speichert Daten dauerhaft (MySQL).

## Ablauf einer Seitenanfrage
1. Browser sendet HTTP Request an Server.
2. Server verarbeitet (ggf. Datenbankzugriff).
3. Server sendet HTML/CSS/JS zurück.
4. Browser rendert die Seite und führt JS aus.

Weiter: Lies `html-grundgeruest.md`.
