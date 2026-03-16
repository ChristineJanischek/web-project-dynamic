# Grundlagen der Programmierung - Basics (JavaScript) - Variante 3

**Dokumenttyp:** Aufgabenstellung + Musterlösung

**Punkte gesamt:** 25

**Hinweis für Lehrkräfte**

- Teilpunkte in 0.5-Schritten vergeben.
- Lösungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `stadt` und `einwohner` einliest (oder setzt) und eine Stadtinformation ausgibt.

**Beispiel-Ausgabe:** `In Stuttgart leben 635911 Menschen.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```javascript
const stadt = "Stuttgart";
const einwohner = 635911;

console.log(`In ${stadt} leben ${einwohner} Menschen.`);
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

1. Schreibe eine Funktion `calcCubeVolume(side)`, die das Volumen eines Würfels berechnet (Formel: side³). (4.0)
2. Schreibe eine Funktion `kmToMiles(km)`, die Kilometer in Meilen umrechnet (Formel: km / 1.609). (3.5)

**Beispiele:**

- `calcCubeVolume(3)` -> `27`
- `kmToMiles(16.09)` -> `10` (ca.)

**Musterlösung**

```javascript
function calcCubeVolume(side) {
  return side * side * side;
  // Alternative: return Math.pow(side, 3);
}

function kmToMiles(km) {
  return km / 1.609;
}
```

### Punktbewertung

| Kriterium             | Punkte  | Hinweise                                                     |
| --------------------- | ------- | ------------------------------------------------------------ |
| Funktion 1 Signatur   | 1.0     | Name, Parameter korrekt                                      |
| Funktion 1 Berechnung | 3.0     | `side * side * side` oder `Math.pow(side, 3)` oder `side**3` |
| Funktion 2 Signatur   | 0.5     | Name, Parameter korrekt                                      |
| Funktion 2 Berechnung | 3.0     | Formel `km / 1.609` korrekt                                  |
| **Summe Aufgabe B**   | **7.5** |                                                              |

### Häufige Fehler

- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyTemperature(temp)`, die eine Temperaturbewertung als Text liefert:

- `temp < -273` -> `ungueltig` (absoluter Nullpunkt) (2.0)
- `temp < 0` -> `gefroren`
- `temp >= 0` und `< 25` -> `angenehm`
- `temp >= 25` -> `heiss` (4.0)

**Beispiele:**

- `classifyTemperature(-5)` -> `gefroren`
- `classifyTemperature(30)` -> `heiss`

**Musterlösung**

```javascript
function classifyTemperature(temp) {
  if (temp < -273) {
    return "ungueltig";
  } else if (temp < 0) {
    return "gefroren";
  } else if (temp < 25) {
    return "angenehm";
  } else {
    return "heiss";
  }
}
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                    |
| ---------------------- | ------- | ------------------------------------------- |
| Funktion Signatur      | 0.5     | Name und Parameter korrekt                  |
| Validierung (ungültig) | 2.0     | `temp < -273` richtig abgefangen            |
| Fallunterscheidungen   | 3.0     | Alle drei Fälle (gefroren, angenehm, heiss) |
| Rückgabewerte korrekt  | 0.5     | Strings exakt wie verlangt                  |
| **Summe Aufgabe C**    | **6.0** |                                             |

### Häufige Fehler

- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers(numbers)`, die:

- das Maximum der Zahlen findet (3.0)
- die Summe aller Zahlen berechnet (3.5)

Rückgabeformat als Objekt: `{ maximum: X, sum: Y }`

**Beispiel:**

`analyzeNumbers([7, -2, 9, 3, -1])` -> `{ maximum: 9, sum: 16 }`

**Musterlösung**

```javascript
function analyzeNumbers(numbers) {
  let maximum = numbers[0];
  let sum = 0;

  for (let num of numbers) {
    if (num > maximum) {
      maximum = num;
    }
    sum += num;
  }

  return { maximum: maximum, sum: sum };
}
```

**Alternative Lösung (mit Math.max)**

```javascript
function analyzeNumbers(numbers) {
  const maximum = Math.max(...numbers);
  const sum = numbers.reduce((acc, num) => acc + num, 0);

  return { maximum: maximum, sum: sum };
}
```

### Punktbewertung

| Kriterium           | Punkte  | Hinweise                                                           |
| ------------------- | ------- | ------------------------------------------------------------------ |
| Funktion Signatur   | 0.5     | Name und Parameter korrekt                                         |
| Schleife            | 1.0     | `for...of`, `forEach`, oder klassische `for`-Schleife              |
| Maximum finden      | 3.0     | Vergleich mit Initialisierung (z.B. `numbers[0]` oder `-Infinity`) |
| Summe berechnen     | 1.5     | Akkumulation mit `sum += num`                                      |
| Rückgabeformat      | 0.5     | Objekt mit korrekten Feldnamen/Werten                              |
| **Summe Aufgabe D** | **6.5** |                                                                    |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/JavaScript_Grundlagen_Basics_v3_Aufgabe_D.svg)

### Häufige Fehler

- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
