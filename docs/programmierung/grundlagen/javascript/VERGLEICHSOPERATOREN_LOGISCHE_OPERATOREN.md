# Vergleichsoperatoren und logische Operatoren in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Funktionen und Methoden](FUNKTIONEN_METHODEN.md)

## Lernziele

- Vergleichsoperatoren sicher einsetzen (`===`, `!==`, `>`, `<`, `>=`, `<=`)
- Logische Operatoren kombinieren (`&&`, `||`, `!`)
- Bedingungen in Funktionen kapseln und testbar machen

## Theorie kompakt

Vergleichsoperatoren liefern `true` oder `false` zurück. Mit logischen Operatoren werden mehrere Bedingungen kombiniert.

- `&&`: beide Bedingungen müssen wahr sein
- `||`: mindestens eine Bedingung muss wahr sein
- `!`: kehrt den Wahrheitswert um

Best Practice in JavaScript: für Vergleiche immer `===` und `!==` verwenden.

## Deklaration & Implementierung

### Einfaches Beispiel: Volljährigkeit prüfen

```javascript
function istVolljaehrig(alter) {
  return alter >= 18;
}

console.log("Test 1:", istVolljaehrig(16)); // false
console.log("Test 2:", istVolljaehrig(18)); // true
```

### Komplexeres Beispiel: Freigabe für Rabattaktion

Regel: Eine Bestellung ist rabattberechtigt, wenn

- der Warenkorb mindestens 100 € hat **und**
- der Kunde entweder Premium ist **oder** einen Gutschein hat **und**
- das Konto nicht gesperrt ist.

```javascript
function istRabattFreigegeben(
  bestellwert,
  istPremium,
  hatGutschein,
  kontoGesperrt,
) {
  const mindestwertErreicht = bestellwert >= 100;
  const kundeQualifiziert = istPremium || hatGutschein;
  const kontoIstAktiv = !kontoGesperrt;

  return mindestwertErreicht && kundeQualifiziert && kontoIstAktiv;
}

console.log("Test A:", istRabattFreigegeben(80, true, false, false)); // false
console.log("Test B:", istRabattFreigegeben(120, false, true, false)); // true
console.log("Test C:", istRabattFreigegeben(200, true, false, true)); // false
```

## Best Practices

- Teilausdrücke in sprechende Variablen auslagern
- Komplexe Bedingungen in Funktionen kapseln
- Randfälle (Grenzwerte) mit Testaufrufen prüfen

## Häufige Fehler

- `==` statt `===` verwenden
- Zu viele Bedingungen ohne Klammern in einer Zeile mischen
- Negationen (`!`) unklar platzieren
