````markdown
# Datenstrukturen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Algorithmen](ALGORITHMEN.md)

## Lernziele

- Arrays und Objekte unterscheiden
- Daten strukturiert speichern
- Sicher auf Werte zugreifen

## Theorie kompakt

Wichtige Einstiegsstrukturen:

- `Array`: geordnete Liste
- `Object`: Schlüssel-Wert-Paare
- Optional für später: `Map`, `Set`

## Deklaration & Implementierung

```javascript
const farben = ["rot", "blau", "gruen"];
const schueler = {
  name: "Lea",
  klasse: "11A",
  punkte: 82,
};

console.log(farben[1]);
console.log(schueler.name);
```

## Best Practices

- Für Listen Arrays, für Eigenschaften Objekte nutzen
- Schlüssel konsistent benennen
- Optional Chaining (`?.`) bei unsicheren Zugriffen erwägen

## Häufige Fehler

- Auf nicht vorhandene Eigenschaften zugreifen
- Objekt und Array semantisch verwechseln
````
