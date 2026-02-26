````markdown
# Einfache Ausgaben in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Variablen](VARIABLEN.md)

## Lernziele

- Text und Variablen im Browser ausgeben
- `console.log()` für Entwicklung und Fehlersuche nutzen
- Template Literals für lesbare Ausgaben verwenden

## Theorie kompakt

In JavaScript wird für Entwicklungszwecke meist in die Konsole ausgegeben. Auf Webseiten wird Ausgabe häufig im DOM angezeigt.

## Deklaration & Implementierung

```javascript
console.log("Hallo Welt!");

const name = "Mila";
console.log(`Hallo ${name}!`);
```

## Best Practices

- Für Debugging konsequent `console.log()` verwenden
- Aussagekräftige Ausgaben mit Labels schreiben
- Template Literals statt unübersichtlicher Verkettung nutzen

## Häufige Fehler

- Tippfehler in Variablennamen
- Falsche Anführungszeichen bei Template Literals
````
