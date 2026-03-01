# Grundlagen der Programmierung - Basics (PHP)

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

```php
<?php
$vorname = "Lena";
$alter = 16;

echo "Hallo {$vorname}, du bist {$alter} Jahre alt.";
```

**Bewertungsrubrik**

| Kriterium                                | Punkte  | Hinweise                                                   |
| ---------------------------------------- | ------- | ---------------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | `$` Praefix verwendet, Zuweisungsoperator korrekt          |
| Eingabe einlesen oder simulieren         | 1.0     | `$_GET`, `$_POST`, `readline()` oder direkte Wertzuweisung |
| Ausgabeformat exakt                      | 2.0     | String-Interpolation mit beiden Variablen, korrekte Syntax |
| **Summe Aufgabe A**                      | **5.0** |                                                            |

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcRectangleArea($width, $height)`, die die Flaeche berechnet.
2. Schreibe eine Funktion `celsiusToFahrenheit($c)`, die Celsius in Fahrenheit umrechnet.

**Musterloesung**

```php
<?php
function calcRectangleArea($width, $height) {
    return $width * $height;
}

function celsiusToFahrenheit($c) {
    return ($c * 9) / 5 + 32;
}
```

**Bewertungsrubrik**

| Kriterium                                     | Punkte  | Hinweise                                                            |
| --------------------------------------------- | ------- | ------------------------------------------------------------------- |
| `calcRectangleArea()` korrekt implementiert   | 4.0     | Parameter mit `$`, Multiplikation durchgefuehrt, `return` verwendet |
| `celsiusToFahrenheit()` korrekt implementiert | 3.5     | Formel $(c \times 9/5) + 32$ richtig umgesetzt, `return` korrekt    |
| **Summe Aufgabe B**                           | **7.5** |                                                                     |

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyScore($score)`, die eine Note als Text liefert.

**Musterloesung**

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

**Bewertungsrubrik**

| Kriterium                         | Punkte  | Hinweise                                                   |
| --------------------------------- | ------- | ---------------------------------------------------------- | --- | -------------- |
| Bereichs-Check (< 0 oder > 100)   | 2.0     | Ungueltige Werte werden mit `                              |     | ` (OR) erkannt |
| Fallunterscheidungen vollstaendig | 2.5     | Alle vier Faelle abgedeckt, `if-elseif` oder verschachtelt |
| Rueckgabewerte korrekt            | 1.5     | Strings entsprechen genau der Vorgabe                      |
| **Summe Aufgabe C**               | **6.0** |                                                            |

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers($numbers)`, die die Anzahl gerader Zahlen zaehlt und die Summe aller positiven Zahlen berechnet.

**Musterloesung**

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

**Bewertungsrubrik**

| Kriterium              | Punkte  | Hinweise                                                     |
| ---------------------- | ------- | ------------------------------------------------------------ |
| Schleife ueber Array   | 1.5     | `foreach` oder `for` mit Index, iteriert ueber alle Elemente |
| Gerade Zahlen zaehlen  | 3.0     | Modulo `%` oder `==` 0 korrekt, Counter wird erhoet          |
| Summe positiver Zahlen | 1.5     | Vergleich `> 0` korrekt, Summe wird nach += aktualisiert     |
| Rueckgabeformat        | 0.5     | Array mit korrekten Schluessel-Wert-Paaren                   |
| **Summe Aufgabe D**    | **6.5** |                                                              |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/PHP_Grundlagen_Basics_Aufgabe_D.svg)
