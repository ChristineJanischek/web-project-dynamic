````markdown
# Variablen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Rechenoperationen](RECHENOPERATIONEN.md)

## Lernziele

- Variablen mit `let` und `const` korrekt verwenden
- Grundlegende Datentypen erkennen
- Gute Variablennamen verwenden

## Theorie kompakt

Variablen speichern Werte unter Namen. In modernem JavaScript nutzt man hauptsächlich:

- `const` für Werte, die nicht neu zugewiesen werden
- `let` für Werte, die sich ändern

Typische Datentypen: `string`, `number`, `boolean`, `object`, `undefined`, `null`.

## Deklaration & Implementierung

```javascript
const vorname = "Lea";
let punkte = 10;
punkte = punkte + 5;

console.log(`${vorname} hat ${punkte} Punkte.`);
```

## Best Practices

- Standardmäßig `const` nutzen, nur bei Bedarf `let`
- Sprechende Namen verwenden (`gesamtPreis`)
- Einheitlich bei `camelCase` bleiben

## Häufige Fehler

- Versehentlich `const` neu zuweisen
- Variablen vor der Deklaration verwenden
````
