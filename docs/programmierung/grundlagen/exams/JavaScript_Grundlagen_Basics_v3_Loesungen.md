# Grundlagen der Programmierung - Basics (JavaScript) - Variante 3

**Dokumenttyp:** Aufgabenstellung + Musterloesung

**Punkte gesamt:** 25

**Hinweis fuer Lehrkraefte**

- Teilpunkte in 0.5-Schritten vergeben.
- Loesungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `stadt` und `einwohner` einliest (oder setzt) und eine Stadtinformation ausgibt.

**Musterloesung**

```javascript
const stadt = "Stuttgart";
const einwohner = 635911;

console.log(`In ${stadt} leben ${einwohner} Menschen.`);
```

**Bewertungsrubrik**

| Kriterium                                | Punkte  | Hinweise                                                         |
| ---------------------------------------- | ------- | ---------------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `const` oder `let` verwendet, Werte korrekt gesetzt              |
| Eingabe einlesen oder simulieren         | 1.0     | Eingabe ueber `prompt()`, `readline`, oder direkte Wertzuweisung |
| Ausgabeformat exakt                      | 2.0     | String-Format mit beiden Variablen interpoliert                  |
| **Summe Aufgabe A**                      | **5.0** |                                                                  |

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcCubeVolume(side)`, die das Volumen eines Wuerfels berechnet.
2. Schreibe eine Funktion `kmToMiles(km)`, die Kilometer in Meilen umrechnet.

**Musterloesung**

```javascript
function calcCubeVolume(side) {
  return side * side * side;
  // Alternative: return Math.pow(side, 3);
}

function kmToMiles(km) {
  return km / 1.609;
}
```

**Bewertungsrubrik**

| Kriterium             | Punkte  | Hinweise                                                     |
| --------------------- | ------- | ------------------------------------------------------------ |
| Funktion 1 Signatur   | 1.0     | Name, Parameter korrekt                                      |
| Funktion 1 Berechnung | 3.0     | `side * side * side` oder `Math.pow(side, 3)` oder `side**3` |
| Funktion 2 Signatur   | 0.5     | Name, Parameter korrekt                                      |
| Funktion 2 Berechnung | 3.0     | Formel `km / 1.609` korrekt                                  |
| **Summe Aufgabe B**   | **7.5** |                                                              |

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyTemperature(temp)`, die eine Temperaturbewertung als Text liefert.

**Musterloesung**

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

**Bewertungsrubrik**

| Kriterium               | Punkte  | Hinweise                                     |
| ----------------------- | ------- | -------------------------------------------- |
| Funktion Signatur       | 0.5     | Name und Parameter korrekt                   |
| Validierung (ungueltig) | 2.0     | `temp < -273` richtig abgefangen             |
| Fallunterscheidungen    | 3.0     | Alle drei Faelle (gefroren, angenehm, heiss) |
| Rueckgabewerte korrekt  | 0.5     | Strings exakt wie verlangt                   |
| **Summe Aufgabe C**     | **6.0** |                                              |

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers(numbers)`, die das Maximum und die Summe aller Zahlen berechnet.

**Musterloesung**

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

**Alternative Loesung (mit Math.max)**

```javascript
function analyzeNumbers(numbers) {
  const maximum = Math.max(...numbers);
  const sum = numbers.reduce((acc, num) => acc + num, 0);

  return { maximum: maximum, sum: sum };
}
```

**Bewertungsrubrik**

| Kriterium           | Punkte  | Hinweise                                                           |
| ------------------- | ------- | ------------------------------------------------------------------ |
| Funktion Signatur   | 0.5     | Name und Parameter korrekt                                         |
| Schleife            | 1.0     | `for...of`, `forEach`, oder klassische `for`-Schleife              |
| Maximum finden      | 3.0     | Vergleich mit Initialisierung (z.B. `numbers[0]` oder `-Infinity`) |
| Summe berechnen     | 1.5     | Akkumulation mit `sum += num`                                      |
| Rueckgabeformat     | 0.5     | Objekt mit korrekten Feldnamen/Werten                              |
| **Summe Aufgabe D** | **6.5** |                                                                    |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/JavaScript_Grundlagen_Basics_v3_Aufgabe_D.svg)
