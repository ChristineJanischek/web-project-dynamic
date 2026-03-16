# Grundlagen der Programmierung - Basics (JavaScript) - Variante 4

**Dokumenttyp:** Aufgabenstellung + Musterlösung

**Punkte gesamt:** 25

**Hinweis für Lehrkräfte**

- Teilpunkte in 0.5-Schritten vergeben.
- Lösungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `buch` und `seiten` einliest (oder setzt) und eine Buchinformation ausgibt.

**Beispiel-Ausgabe:** `Das Buch "1984" hat 328 Seiten.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```javascript
const buch = "1984";
const seiten = 328;

console.log(`Das Buch "${buch}" hat ${seiten} Seiten.`);
```

### Punktbewertung

| Kriterium                                | Punkte  | Hinweise                                                                        |
| ---------------------------------------- | ------- | ------------------------------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `const` oder `let` verwendet, Werte korrekt gesetzt                             |
| Eingabe einlesen oder simulieren         | 1.0     | Eingabe über `prompt()`, `readline`, oder direkte Wertzuweisung                 |
| Ausgabeformat exakt                      | 2.0     | String-Format mit beiden Variablen interpoliert, Anführungszeichen um Buchtitel |
| **Summe Aufgabe A**                      | **5.0** |                                                                                 |

### Häufige Fehler

- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcTriangleArea(base, height)`, die die Fläche eines Dreiecks berechnet (Formel: base \* height / 2). (4.0)
2. Schreibe eine Funktion `milesToKm(miles)`, die Meilen in Kilometer umrechnet (Formel: miles \* 1.609). (3.5)

**Beispiele:**

- `calcTriangleArea(6, 4)` -> `12`
- `milesToKm(10)` -> `16.09`

**Musterlösung**

```javascript
function calcTriangleArea(base, height) {
  return (base * height) / 2;
}

function milesToKm(miles) {
  return miles * 1.609;
}
```

### Punktbewertung

| Kriterium             | Punkte  | Hinweise                                       |
| --------------------- | ------- | ---------------------------------------------- |
| Funktion 1 Signatur   | 1.0     | Name, Parameter korrekt                        |
| Funktion 1 Berechnung | 3.0     | `base * height / 2` oder `(base * height) / 2` |
| Funktion 2 Signatur   | 0.5     | Name, Parameter korrekt                        |
| Funktion 2 Berechnung | 3.0     | Formel `miles * 1.609` korrekt                 |
| **Summe Aufgabe B**   | **7.5** |                                                |

### Häufige Fehler

- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifySpeed(kmh)`, die eine Geschwindigkeitsklassifizierung als Text liefert:

- `kmh < 0` -> `ungueltig` (2.0)
- `kmh <= 30` -> `langsam`
- `kmh > 30` und `<= 100` -> `normal`
- `kmh > 100` -> `schnell` (4.0)

**Beispiele:**

- `classifySpeed(25)` -> `langsam`
- `classifySpeed(120)` -> `schnell`

**Musterlösung**

```javascript
function classifySpeed(kmh) {
  if (kmh < 0) {
    return "ungueltig";
  } else if (kmh <= 30) {
    return "langsam";
  } else if (kmh <= 100) {
    return "normal";
  } else {
    return "schnell";
  }
}
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                   |
| ---------------------- | ------- | ------------------------------------------ |
| Funktion Signatur      | 0.5     | Name und Parameter korrekt                 |
| Validierung (ungültig) | 2.0     | `kmh < 0` richtig abgefangen               |
| Fallunterscheidungen   | 3.0     | Alle drei Fälle (langsam, normal, schnell) |
| Rückgabewerte korrekt  | 0.5     | Strings exakt wie verlangt                 |
| **Summe Aufgabe C**    | **6.0** |                                            |

### Häufige Fehler

- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers(numbers)`, die:

- das Minimum der Zahlen findet (3.0)
- die Anzahl positiver Zahlen zählt (3.5)

Rückgabeformat als Objekt: `{ minimum: X, positiveCount: Y }`

**Beispiel:**

`analyzeNumbers([5, -3, 2, 0, -7])` -> `{ minimum: -7, positiveCount: 2 }`

**Musterlösung**

```javascript
function analyzeNumbers(numbers) {
  let minimum = numbers[0];
  let positiveCount = 0;

  for (let num of numbers) {
    if (num < minimum) {
      minimum = num;
    }
    if (num > 0) {
      positiveCount++;
    }
  }

  return { minimum: minimum, positiveCount: positiveCount };
}
```

**Alternative Lösung (mit Math.min)**

```javascript
function analyzeNumbers(numbers) {
  const minimum = Math.min(...numbers);
  const positiveCount = numbers.filter((num) => num > 0).length;

  return { minimum: minimum, positiveCount: positiveCount };
}
```

### Punktbewertung

| Kriterium           | Punkte  | Hinweise                                                          |
| ------------------- | ------- | ----------------------------------------------------------------- |
| Funktion Signatur   | 0.5     | Name und Parameter korrekt                                        |
| Schleife            | 1.0     | `for...of`, `forEach`, oder klassische `for`-Schleife             |
| Minimum finden      | 3.0     | Vergleich mit Initialisierung (z.B. `numbers[0]` oder `Infinity`) |
| Positive zählen     | 1.5     | `if (num > 0)` mit Zähler-Inkrement                               |
| Rückgabeformat      | 0.5     | Objekt mit korrekten Feldnamen/Werten                             |
| **Summe Aufgabe D** | **6.5** |                                                                   |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/JavaScript_Grundlagen_Basics_v4_Aufgabe_D.svg)

### Häufige Fehler

- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
