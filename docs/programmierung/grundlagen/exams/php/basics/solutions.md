# Grundlagen der Programmierung - Basics (PHP)

**Dokumenttyp:** Aufgabenstellung + Musterlösung

**Punkte gesamt:** 25

**Hinweis für Lehrkräfte**

- Teilpunkte in 0.5-Schritten vergeben.
- Lösungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `vorname` und `alter` einliest (oder setzt) und eine Begrüßung ausgibt.

**Beispiel-Ausgabe:** `Hallo Lena, du bist 16 Jahre alt.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```php
<?php
$vorname = "Lena";
$alter = 16;

echo "Hallo {$vorname}, du bist {$alter} Jahre alt.";
```

### Punktbewertung

| Kriterium                                | Punkte  | Hinweise                                                   |
| ---------------------------------------- | ------- | ---------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `$` Präfix verwendet, Zuweisungsoperator korrekt           |
| Eingabe einlesen oder simulieren         | 1.0     | `$_GET`, `$_POST`, `readline()` oder direkte Wertzuweisung |
| Ausgabeformat exakt                      | 2.0     | String-Interpolation mit beiden Variablen, korrekte Syntax |
| **Summe Aufgabe A**                      | **5.0** |                                                            |

### Häufige Fehler

- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcRectangleArea($width, $height)`, die die Fläche berechnet. (4.0)
2. Schreibe eine Funktion `celsiusToFahrenheit($c)`, die Celsius in Fahrenheit umrechnet. (3.5)

**Beispiele:**

- `calcRectangleArea(4, 3)` -> `12`
- `celsiusToFahrenheit(0)` -> `32`

**Musterlösung**

```php
<?php
function calcRectangleArea($width, $height) {
    return $width * $height;
}

function celsiusToFahrenheit($c) {
    return ($c * 9) / 5 + 32;
}
```

### Punktbewertung

| Kriterium                                     | Punkte  | Hinweise                                                           |
| --------------------------------------------- | ------- | ------------------------------------------------------------------ |
| `calcRectangleArea()` korrekt implementiert   | 4.0     | Parameter mit `$`, Multiplikation durchgeführt, `return` verwendet |
| `celsiusToFahrenheit()` korrekt implementiert | 3.5     | Formel $(c \times 9/5) + 32$ richtig umgesetzt, `return` korrekt   |
| **Summe Aufgabe B**                           | **7.5** |                                                                    |

### Häufige Fehler

- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyScore($score)`, die eine Note als Text liefert:

- `score < 0` oder `score > 100` -> `ungueltig` (2.0)
- `score < 50` -> `nicht bestanden`
- `score >= 50` und `< 90` -> `bestanden`
- `score >= 90` -> `sehr gut` (4.0)

**Beispiele:**

- `classifyScore(45)` -> `nicht bestanden`
- `classifyScore(90)` -> `sehr gut`

**Musterlösung**

```php
<?php
function classifyScore($score) {
    if ($score < 0 || $score > 100) {
        return "ungueltig";
    }
    if ($score < 50) {
        return "nicht bestanden";
    }
    if ($score < 90) {
        return "bestanden";
    }
    return "sehr gut";
}
```

### Punktbewertung

| Kriterium                        | Punkte  | Hinweise                                                  |
| -------------------------------- | ------- | --------------------------------------------------------- | --- | ---------------------- |
| Bereichs-Check (< 0 oder > 100)  | 2.0     | Ungültige Werte werden mit `                              |     | ` (OR) korrekt erkannt |
| Fallunterscheidungen vollständig | 2.5     | Alle vier Fälle abgedeckt, `if-elseif` oder verschachtelt |
| Rückgabewerte korrekt            | 1.5     | Strings entsprechen genau der Vorgabe                     |
| **Summe Aufgabe C**              | **6.0** |                                                           |

### Häufige Fehler

- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers($numbers)`, die:

- die Anzahl gerader Zahlen zählt (3.0)
- die Summe aller positiven Zahlen berechnet (3.5)

Rückgabeformat als Array: `['evenCount' => X, 'positiveSum' => Y]`

**Beispiel:**

`analyzeNumbers([2, -3, 4, 0, 5])` -> `['evenCount' => 3, 'positiveSum' => 11]`

**Musterlösung**

```php
<?php
function analyzeNumbers($numbers) {
    $evenCount = 0;
    $positiveSum = 0;

    foreach ($numbers as $value) {
        if ($value % 2 === 0) {
            $evenCount += 1;
        }
        if ($value > 0) {
            $positiveSum += $value;
        }
    }

    return ["evenCount" => $evenCount, "positiveSum" => $positiveSum];
}
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                                    |
| ---------------------- | ------- | ----------------------------------------------------------- |
| Schleife über Array    | 1.5     | `foreach` oder `for` mit Index, iteriert über alle Elemente |
| Gerade Zahlen zählen   | 3.0     | Modulo `%` oder `==` 0 korrekt, Counter wird erhöht         |
| Summe positiver Zahlen | 1.5     | Vergleich `> 0` korrekt, Summe wird nach += aktualisiert    |
| Rückgabeformat         | 0.5     | Array mit korrekten Schlüssel-Wert-Paaren                   |
| **Summe Aufgabe D**    | **6.5** |                                                             |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/PHP_Grundlagen_Basics_Aufgabe_D.svg)

### Häufige Fehler

- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
