# Grundlagen der Programmierung - Basics (PHP) - Variante 4

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

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

```php
<?php
$buch = "1984";
$seiten = 328;

echo "Das Buch \"{$buch}\" hat {$seiten} Seiten.";
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

1. Schreibe eine Funktion `calcTriangleArea($base, $height)`, die die Fläche eines Dreiecks berechnet (Formel: $base \* $height / 2). (4.0)
2. Schreibe eine Funktion `milesToKm($miles)`, die Meilen in Kilometer umrechnet (Formel: $miles \* 1.609). (3.5)

**Beispiele:**

- `calcTriangleArea(6, 4)` -> `12`
- `milesToKm(10)` -> `16.09`

**Musterlösung**

```php
<?php
function calcTriangleArea($base, $height) {
    return $base * $height / 2;
}

function milesToKm($miles) {
    return $miles * 1.609;
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

Schreibe eine Funktion `classifySpeed($kmh)`, die eine Geschwindigkeitsklassifizierung als Text liefert:

- `$kmh < 0` -> `ungueltig` (2.0)
- `$kmh <= 30` -> `langsam`
- `$kmh > 30` und `<= 100` -> `normal`
- `$kmh > 100` -> `schnell` (4.0)

**Beispiele:**

- `classifySpeed(25)` -> `langsam`
- `classifySpeed(120)` -> `schnell`

**Musterlösung**

```php
<?php
function classifySpeed($kmh) {
    if ($kmh < 0) {
        return "ungueltig";
    } elseif ($kmh <= 30) {
        return "langsam";
    } elseif ($kmh <= 100) {
        return "normal";
    } else {
        return "schnell";
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

- das Minimum der Zahlen findet (3.0)
- die Anzahl positiver Zahlen zählt (3.5)

Rückgabeformat als Array: `["minimum" => X, "positiveCount" => Y]`

**Beispiel:**

`analyzeNumbers([5, -3, 2, 0, -7])` -> `["minimum" => -7, "positiveCount" => 2]`

**Musterlösung**

```php
<?php
function analyzeNumbers($numbers) {
    $minimum = $numbers[0];
    $positiveCount = 0;

    foreach ($numbers as $num) {
        if ($num < $minimum) {
            $minimum = $num;
        }
        if ($num > 0) {
            $positiveCount++;
        }
    }

    return ["minimum" => $minimum, "positiveCount" => $positiveCount];
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
