````markdown
# Kontrollstrukturen – Fallunterscheidungen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Kontrollstrukturen – Wiederholungsstrukturen](KONTROLLSTRUKTUREN_WIEDERHOLUNGSSTRUKTUREN.md)

## Lernziele

- Bedingungen mit `if`, `else if`, `else` formulieren
- Vergleichsoperatoren sicher einsetzen
- Mehrfachfälle mit `switch` abbilden

## Theorie kompakt

Mit Fallunterscheidungen reagiert ein Programm auf unterschiedliche Eingaben oder Zustände.

## Deklaration & Implementierung

```javascript
const punkte = 78;

if (punkte >= 90) {
  console.log("Note 1");
} else if (punkte >= 75) {
  console.log("Note 2");
} else {
  console.log("Verbesserung nötig");
}

const tag = 2;
switch (tag) {
  case 1:
    console.log("Montag");
    break;
  case 2:
    console.log("Dienstag");
    break;
  default:
    console.log("Unbekannt");
}
```

## Best Practices

- Bedingungen möglichst klar und kurz halten
- Strikte Vergleiche mit `===` bevorzugen
- `switch` nur bei klaren diskreten Fällen einsetzen

## Häufige Fehler

- `=` statt `===` in Bedingungen
- `break` in `switch` vergessen
````
