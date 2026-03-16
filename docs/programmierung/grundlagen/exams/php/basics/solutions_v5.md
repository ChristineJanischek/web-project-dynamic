# Grundlagen der Programmierung - Basics (PHP) - Variante 5

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `film` und `dauerMinuten` einliest (oder setzt) und eine Filminformation ausgibt.

**Beispiel-Ausgabe:** `Film: Inception, Dauer: 148 Minuten`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```php
<?php
$film = "Inception";
$dauerMinuten = 148;

echo "Film: {$film}, Dauer: {$dauerMinuten} Minuten";
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

1. Schreibe eine Funktion `calcAverageThree($a, $b, $c)`, die den Durchschnitt von drei Zahlen berechnet. (4.0)
2. Schreibe eine Funktion `minutesToSeconds($minutes)`, die Minuten in Sekunden umrechnet. (3.5)

**Beispiele:**

- `calcAverageThree(2, 4, 6)` -> `4`
- `minutesToSeconds(3)` -> `180`

**Musterlösung**

```php
<?php
function calcAverageThree($a, $b, $c) {
    return ($a + $b + $c) / 3;
}

function minutesToSeconds($minutes) {
    return $minutes * 60;
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

Schreibe eine Funktion `classifyHumidity($humidity)`, die Luftfeuchtigkeit als Text klassifiziert:

- `$humidity < 0` oder `$humidity > 100` -> `ungueltig` (2.0)
- `$humidity < 30` -> `trocken`
- `$humidity >= 30` und `< 60` -> `normal`
- `$humidity >= 60` -> `feucht` (4.0)

**Beispiele:**

- `classifyHumidity(25)` -> `trocken`
- `classifyHumidity(72)` -> `feucht`

**Musterlösung**

```php
<?php
function classifyHumidity($humidity) {
    if ($humidity < 0 || $humidity > 100) {
        return "ungueltig";
    } elseif ($humidity < 30) {
        return "trocken";
    } elseif ($humidity < 60) {
        return "normal";
    } else {
        return "feucht";
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

Schreibe eine Funktion `analyzeValues($values)`, die:

- die Anzahl von Werten zählt, die durch 3 teilbar sind (3.0)
- den Durchschnitt aller nicht-negativen Werte berechnet (3.5)

Wenn es keine nicht-negativen Werte gibt, soll der Durchschnitt `0` sein.

Rückgabeformat als Array: `["divByThreeCount" => X, "nonNegativeAverage" => Y]`

**Beispiel:**

`analyzeValues([3, -4, 6, 1, -2])` -> `["divByThreeCount" => 2, "nonNegativeAverage" => 3.3333...]`

**Musterlösung**

```php
<?php
function analyzeValues($values) {
    $divByThreeCount = 0;
    $nonNegativeSum = 0;
    $nonNegativeCount = 0;

    foreach ($values as $value) {
        if ($value % 3 === 0) {
            $divByThreeCount++;
        }
        if ($value >= 0) {
            $nonNegativeSum += $value;
            $nonNegativeCount++;
        }
    }

    $nonNegativeAverage = 0;
    if ($nonNegativeCount > 0) {
        $nonNegativeAverage = $nonNegativeSum / $nonNegativeCount;
    }

    return [
        "divByThreeCount" => $divByThreeCount,
        "nonNegativeAverage" => $nonNegativeAverage
    ];
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
