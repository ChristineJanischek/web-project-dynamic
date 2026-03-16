# Grundlagen der Programmierung - Basics (JavaScript) - Variante 2

**Dokumenttyp:** Aufgabenstellung + Musterlösung

**Punkte gesamt:** 25

**Hinweis für Lehrkräfte**

- Teilpunkte in 0.5-Schritten vergeben.
- Lösungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `produkt` und `preis` einliest (oder setzt) und eine Produktinformation ausgibt.

**Beispiel-Ausgabe:** `Artikel: Laptop, Preis: 899 Euro`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```javascript
const produkt = "Laptop";
const preis = 899;

console.log(`Artikel: ${produkt}, Preis: ${preis} Euro`);
```

### Punktbewertung

| Kriterium                                | Punkte  | Hinweise                                                        |
| ---------------------------------------- | ------- | --------------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `const` oder `let` verwendet, Werte korrekt gesetzt             |
| Eingabe einlesen oder simulieren         | 1.0     | Eingabe über `prompt()`, `readline`, oder direkte Wertzuweisung |
| Ausgabeformat exakt                      | 2.0     | String-Format mit beiden Variablen interpoliert                 |
| **Summe Aufgabe A**                      | **5.0** |                                                                 |

### Häufige Fehler

- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcCircleCircumference(radius)`, die den Kreisumfang berechnet (Formel: 2 \* π \* r). (4.0)
2. Schreibe eine Funktion `fahrenheitToCelsius(f)`, die Fahrenheit in Celsius umrechnet (Formel: (f - 32) \* 5 / 9). (3.5)

**Beispiele:**

- `calcCircleCircumference(5)` -> `31.4159...` (ca. 31.42)
- `fahrenheitToCelsius(32)` -> `0`

**Musterlösung**

```javascript
function calcCircleCircumference(radius) {
  return 2 * Math.PI * radius;
}

function fahrenheitToCelsius(f) {
  return ((f - 32) * 5) / 9;
}
```

### Punktbewertung

| Kriterium             | Punkte  | Hinweise                                                |
| --------------------- | ------- | ------------------------------------------------------- |
| Funktion 1 Signatur   | 1.0     | Name, Parameter korrekt                                 |
| Funktion 1 Berechnung | 3.0     | `2 * Math.PI * radius` oder Konstante 3.14159           |
| Funktion 2 Signatur   | 0.5     | Name, Parameter korrekt                                 |
| Funktion 2 Berechnung | 3.0     | Formel `(f - 32) * 5 / 9` oder `(f - 32) / 1.8` korrekt |
| **Summe Aufgabe B**   | **7.5** |                                                         |

### Häufige Fehler

- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyAge(age)`, die eine Altersgruppe als Text liefert:

- `age < 0` oder `age > 150` -> `ungueltig` (2.0)
- `age < 18` -> `minderjaehrig`
- `age >= 18` und `< 65` -> `erwachsen`
- `age >= 65` -> `senior` (4.0)

**Beispiele:**

- `classifyAge(16)` -> `minderjaehrig`
- `classifyAge(70)` -> `senior`

**Musterlösung**

```javascript
function classifyAge(age) {
  if (age < 0 || age > 150) {
    return "ungueltig";
  } else if (age < 18) {
    return "minderjaehrig";
  } else if (age < 65) {
    return "erwachsen";
  } else {
    return "senior";
  }
}
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                          |
| ---------------------- | ------- | ------------------------------------------------- |
| Funktion Signatur      | 0.5     | Name und Parameter korrekt                        |
| Validierung (ungültig) | 2.0     | `age < 0` oder `age > 150` richtig abgefangen     |
| Fallunterscheidungen   | 3.0     | Alle drei Fälle (minderjährig, erwachsen, senior) |
| Rückgabewerte korrekt  | 0.5     | Strings exakt wie verlangt                        |
| **Summe Aufgabe C**    | **6.0** |                                                   |

### Häufige Fehler

- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers(numbers)`, die:

- die Anzahl ungerader Zahlen zählt (3.0)
- die Summe aller negativen Zahlen berechnet (3.5)

Rückgabeformat als Objekt: `{ oddCount: X, negativeSum: Y }`

**Beispiel:**

`analyzeNumbers([3, -2, 5, 0, -4])` -> `{ oddCount: 2, negativeSum: -6 }`

**Musterlösung**

```javascript
function analyzeNumbers(numbers) {
  let oddCount = 0;
  let negativeSum = 0;

  for (let num of numbers) {
    if (num % 2 !== 0) {
      oddCount++;
    }
    if (num < 0) {
      negativeSum += num;
    }
  }

  return { oddCount: oddCount, negativeSum: negativeSum };
}
```

### Punktbewertung

| Kriterium           | Punkte  | Hinweise                                              |
| ------------------- | ------- | ----------------------------------------------------- |
| Funktion Signatur   | 0.5     | Name und Parameter korrekt                            |
| Schleife            | 1.0     | `for...of`, `forEach`, oder klassische `for`-Schleife |
| Ungerade zählen     | 3.0     | Modulo-Check `num % 2 !== 0` oder `num % 2 === 1`     |
| Negative summieren  | 1.5     | `if (num < 0)` mit Summenbildung                      |
| Rückgabeformat      | 0.5     | Objekt oder Array mit korrekten Feldnamen/Werten      |
| **Summe Aufgabe D** | **6.5** |                                                       |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/JavaScript_Grundlagen_Basics_v2_Aufgabe_D.svg)

### Häufige Fehler

- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
