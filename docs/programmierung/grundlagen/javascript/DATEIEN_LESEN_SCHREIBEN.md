````markdown
# Persistentes Schreiben in und Lesen aus Dateien in JavaScript

## Lernziele

- Grundidee von persistenter Speicherung verstehen
- Unterschied zwischen Browser-Speicher und Dateisystem kennen
- Einfache Dateioperationen mit Node.js einordnen

## Theorie kompakt

JavaScript läuft in unterschiedlichen Umgebungen:

- Im Browser: kein direkter Dateisystemzugriff; stattdessen z. B. `localStorage`
- In Node.js: Zugriff auf Dateien über das Modul `fs`

## Deklaration & Implementierung

Beispiel in Node.js mit `fs`:

```javascript
const fs = require("fs");

const text = "Hallo Datei";
fs.writeFileSync("notiz.txt", text, "utf8");

const inhalt = fs.readFileSync("notiz.txt", "utf8");
console.log(inhalt);
```

## Best Practices

- Kodierung (`utf8`) explizit angeben
- Fehlerfälle berücksichtigen (Datei fehlt, Rechte fehlen)
- Für Browserprojekte passende Speicherstrategien wählen

## Häufige Fehler

- Browser-Code und Node.js-Code verwechseln
- Pfade falsch angeben
````
