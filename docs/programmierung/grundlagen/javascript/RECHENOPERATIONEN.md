````markdown
# Rechenoperationen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Vergleichsoperatoren und logische Operatoren](VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md)

## Lernziele

- Grundrechenarten in JavaScript anwenden
- Operatoren korrekt einsetzen
- Typumwandlung bei Berechnungen berücksichtigen

## Theorie kompakt

Wichtige Operatoren: `+`, `-`, `*`, `/`, `%`, `**`.

In JavaScript kann `+` sowohl addieren als auch Strings verketten. Daher sind Datentypen wichtig.

## Deklaration & Implementierung

```javascript
const a = 12;
const b = 5;

console.log(a + b); // 17
console.log(a % b); // 2
console.log(a ** 2); // 144

const eingabe = "10";
console.log(Number(eingabe) + 5); // 15
```

## Best Practices

- Datentypen vor Rechnungen prüfen
- Bei Eingaben bewusst in `Number` umwandeln
- Teilschritte in Variablen speichern

## Häufige Fehler

- Unerwartete String-Verkettung mit `+`
- Division durch `0` nicht beachten
````
