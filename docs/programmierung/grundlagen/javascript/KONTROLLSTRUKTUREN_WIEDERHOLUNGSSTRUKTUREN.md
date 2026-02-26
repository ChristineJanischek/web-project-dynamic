````markdown
# Kontrollstrukturen – Wiederholungsstrukturen in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Datenstrukturen](DATENSTRUKTUREN.md)

## Lernziele

- Schleifen mit `for` und `while` einsetzen
- Arrays mit `for...of` durchlaufen
- Endlosschleifen vermeiden

## Theorie kompakt

Wiederholungsstrukturen führen Code mehrfach aus, solange eine Bedingung erfüllt ist oder Elemente vorhanden sind.

## Deklaration & Implementierung

```javascript
for (let i = 1; i <= 3; i++) {
  console.log(`Runde ${i}`);
}

const namen = ["Lea", "Mila", "Noah"];
for (const name of namen) {
  console.log(name);
}

let zaehler = 0;
while (zaehler < 2) {
  console.log("while-Schleife");
  zaehler++;
}
```

## Best Practices

- Abbruchbedingung immer klar definieren
- Bei Arrays `for...of` für Lesbarkeit bevorzugen
- Schleifenkörper klein halten

## Häufige Fehler

- Zähler nicht ändern (`i++` vergessen)
- Falsche Start-/Endwerte bei Schleifen
````
