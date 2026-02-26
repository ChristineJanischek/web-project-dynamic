````markdown
# Algorithmen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Persistentes Schreiben in und Lesen aus Dateien](DATEIEN_LESEN_SCHREIBEN.md)

## Lernziele

- Den Begriff Algorithmus verstehen
- Probleme in klare Schritte zerlegen
- Einfache Algorithmen in JavaScript umsetzen

## Theorie kompakt

Ein Algorithmus ist eine eindeutige, endliche Folge von Schritten zur Lösung eines Problems.

Typischer Ablauf:

1. Eingabe festlegen
2. Verarbeitung in Einzelschritten beschreiben
3. Ausgabe definieren

## Deklaration & Implementierung

Beispiel: Größten Wert in einem Array finden.

```javascript
const zahlen = [4, 9, 2, 11, 7];
let maximum = zahlen[0];

for (const zahl of zahlen) {
  if (zahl > maximum) {
    maximum = zahl;
  }
}

console.log(`Maximum: ${maximum}`);
```

## Best Practices

- Zuerst als Pseudocode planen
- Mit kleinen Testdaten starten
- Sonderfälle prüfen (leeres Array, negative Zahlen)

## Häufige Fehler

- Startwert falsch initialisieren
- Randfälle nicht berücksichtigen
````
