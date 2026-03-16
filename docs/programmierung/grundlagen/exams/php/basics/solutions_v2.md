# Grundlagen der Programmierung - Basics (PHP) - Variante 2

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

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

```php
<?php
$produkt = "Laptop";
$preis = 899;

echo "Artikel: {$produkt}, Preis: {$preis} Euro";
```

### Punktbewertung
- 2.0 Punkte: Variablen korrekt deklariert und initialisiert
- 1.0 Punkt: Eingabe korrekt eingelesen oder sauber simuliert
- 2.0 Punkte: Ausgabeformat entspricht der Vorgabe

### Häufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calcCircleCircumference($radius)`, die den Kreisumfang berechnet (Formel: 2 \* π \* r). (4.0)
2. Schreibe eine Funktion `fahrenheitToCelsius($f)`, die Fahrenheit in Celsius umrechnet (Formel: ($f - 32) \* 5 / 9). (3.5)

**Beispiele:**

- `calcCircleCircumference(5)` -> `31.4159...` (ca. 31.42)
- `fahrenheitToCelsius(32)` -> `0`

**Musterlösung**

```php
<?php
function calcCircleCircumference($radius) {
    return 2 * M_PI * $radius;
}

function fahrenheitToCelsius($f) {
    return ($f - 32) * 5 / 9;
}
```

### Punktbewertung
- 4.0 Punkte: Funktion 1 (Signatur, Berechnung, Rückgabe) korrekt
- 3.5 Punkte: Funktion 2 (Signatur, Berechnung, Rückgabe) korrekt

### Häufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classifyAge($age)`, die eine Altersgruppe als Text liefert:

- `$age < 0` oder `$age > 150` -> `ungueltig` (2.0)
- `$age < 18` -> `minderjaehrig`
- `$age >= 18` und `< 65` -> `erwachsen`
- `$age >= 65` -> `senior` (4.0)

**Beispiele:**

- `classifyAge(16)` -> `minderjaehrig`
- `classifyAge(70)` -> `senior`

**Musterlösung**

```php
<?php
function classifyAge($age) {
    if ($age < 0 || $age > 150) {
        return "ungueltig";
    } elseif ($age < 18) {
        return "minderjaehrig";
    } elseif ($age < 65) {
        return "erwachsen";
    } else {
        return "senior";
    }
}
```

### Punktbewertung
- 2.0 Punkte: Ungültige Werte werden korrekt erkannt
- 2.5 Punkte: Fallunterscheidungen vollständig und logisch korrekt
- 1.5 Punkte: Korrekte Rückgabewerte gemäß Aufgabenstellung

### Häufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyzeNumbers($numbers)`, die:

- die Anzahl ungerader Zahlen zählt (3.0)
- die Summe aller negativen Zahlen berechnet (3.5)

Rückgabeformat als Array: `["oddCount" => X, "negativeSum" => Y]`

**Beispiel:**

`analyzeNumbers([3, -2, 5, 0, -4])` -> `["oddCount" => 2, "negativeSum" => -6]`

**Musterlösung**

```php
<?php
function analyzeNumbers($numbers) {
    $oddCount = 0;
    $negativeSum = 0;

    foreach ($numbers as $num) {
        if ($num % 2 !== 0) {
            $oddCount++;
        }
        if ($num < 0) {
            $negativeSum += $num;
        }
    }

    return ["oddCount" => $oddCount, "negativeSum" => $negativeSum];
}
```

### Punktbewertung
- 1.5 Punkte: Iteration über alle Elemente korrekt
- 3.0 Punkte: Kernlogik der ersten Kennzahl korrekt
- 1.5 Punkte: Kernlogik der zweiten Kennzahl korrekt
- 0.5 Punkte: Rückgabeformat (Schlüssel/Struktur) korrekt

### Häufige Fehler
- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
