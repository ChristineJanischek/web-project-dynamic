````markdown
# Funktionen und Methoden in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Kontrollstrukturen – Fallunterscheidungen](KONTROLLSTRUKTUREN_FALLUNTERSCHEIDUNGEN.md)

## Lernziele

- Funktionen definieren und aufrufen
- Parameter und Rückgabewerte nutzen
- Methoden als Funktionen an Objekten verstehen

## Theorie kompakt

Funktionen bündeln wiederverwendbare Logik. Methoden sind Funktionen, die zu einem Objekt gehören.

## Deklaration & Implementierung

```javascript
function addiere(a, b) {
  return a + b;
}

const summe = addiere(4, 7);
console.log(summe);

const text = "javascript";
console.log(text.toUpperCase()); // Methode auf String
```

## Best Practices

- Eine Funktion sollte eine klar abgegrenzte Aufgabe haben
- Parameter sprechend benennen
- Rückgabewerte statt globaler Variablen bevorzugen

## Häufige Fehler

- `return` vergessen
- Zu viele Aufgaben in einer Funktion mischen
````
