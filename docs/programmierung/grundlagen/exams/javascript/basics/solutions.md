# Grundlagen der Programmierung - Basics (JavaScript)

**Dokumenttyp:** Aufgabenstellung + Musterloesung

**Punkte gesamt:** 25

**Hinweis fuer Lehrkraefte**

- Teilpunkte in 0.5-Schritten vergeben.
- Loesungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `vorname` und `alter` einliest (oder setzt) und eine Begruessung ausgibt.

**Musterloesung**

```javascript
const vorname = "Lena";
const alter = 16;

console.log(`Hallo ${vorname}, du bist ${alter} Jahre alt.`);
```

### Punktbewertung

| Kriterium                                | Punkte  | Hinweise                                                         |
| ---------------------------------------- | ------- | ---------------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `const` oder `let` verwendet, Werte korrekt gesetzt              |
| Eingabe einlesen oder simulieren         | 1.0     | Eingabe ueber `prompt()`, `readline`, oder direkte Wertzuweisung |
| Ausgabeformat exakt                      | 2.0     | String-Format mit beiden Variablen interpoliert                  |
| **Summe Aufgabe A**                      | **5.0** |                                                                  |

### Haeufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcRectangleArea(width, height)`, die die Flaeche berechnet.
2. Schreibe eine Funktion `celsiusToFahrenheit(c)`, die Celsius in Fahrenheit umrechnet.

**Musterloesung**

```javascript
function calcRectangleArea(width, height) {
  return width * height;
}

function celsiusToFahrenheit(c) {
  return (c * 9) / 5 + 32;
}
```

### Punktbewertung

| Kriterium                                     | Punkte  | Hinweise                                                             |
| --------------------------------------------- | ------- | -------------------------------------------------------------------- |
| `calcRectangleArea()` korrekt implementiert   | 4.0     | Parameter entgegen, Multiplikation durchgefuehrt, korrekte Rueckgabe |
| `celsiusToFahrenheit()` korrekt implementiert | 3.5     | Formel $(c \times 9/5) + 32$ richtig umgesetzt, Rueckgabe korrekt    |
| **Summe Aufgabe B**                           | **7.5** |                                                                      |

### Haeufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rueckgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyScore(score)`, die eine Note als Text liefert.

**Musterloesung**

```javascript
function classifyScore(score) {
  if (score < 0 || score > 100) {
    return "ungueltig";
  }
  if (score < 50) {
    return "nicht bestanden";
  }
  if (score < 90) {
    return "bestanden";
  }
  return "sehr gut";
}
```

### Punktbewertung

| Kriterium                         | Punkte  | Hinweise                                                                     |
| --------------------------------- | ------- | ---------------------------------------------------------------------------- |
| Bereichs-Check (< 0 oder > 100)   | 2.0     | Ungueltige Werte werden korrekt erkannt                                      |
| Fallunterscheidungen vollstaendig | 2.5     | Alle vier Faelle (ungueltig, nicht bestanden, bestanden, sehr gut) abgedeckt |
| Rueckgabewerte korrekt            | 1.5     | Strings entsprechen genau der Vorgabe                                        |
| **Summe Aufgabe C**               | **6.0** |                                                                              |

### Haeufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungueltigkeitspruefung fehlt oder steht an falscher Stelle
- Ein oder mehrere Faelle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers(numbers)`, die die Anzahl gerader Zahlen zaehlt und die Summe aller positiven Zahlen berechnet.

**Musterloesung**

```javascript
function analyzeNumbers(numbers) {
  let evenCount = 0;
  let positiveSum = 0;

  for (const value of numbers) {
    if (value % 2 === 0) {
      evenCount += 1;
    }
    if (value > 0) {
      positiveSum += value;
    }
  }

  return { evenCount, positiveSum };
}
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                                     |
| ---------------------- | ------- | ------------------------------------------------------------ |
| Schleife ueber Array   | 1.5     | `for`, `forEach` oder aehnlich, iteriert ueber alle Elemente |
| Gerade Zahlen zaehlen  | 3.0     | Modulo-Operator korrekt verwendet, Counter wird erhoet       |
| Summe positiver Zahlen | 1.5     | Vergleich `> 0` korrekt, Summe wird aktualisiert             |
| Rueckgabeformat        | 0.5     | Objekt oder Array mit korrekten Feldnamen/Werten             |
| **Summe Aufgabe D**    | **6.5** |                                                              |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/JavaScript_Grundlagen_Basics_Aufgabe_D.svg)

### Haeufige Fehler
- Zaehler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung fuer Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rueckgabe enthaelt falsche Schluessel oder unvollstaendige Werte
