# Grundlagen der Programmierung - Basics (PHP) - Variante 6

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `eventName` und `teilnehmerzahl` einliest (oder setzt) und eine Eventmeldung ausgibt.

**Beispiel-Ausgabe:** `Event: Hackathon, Teilnehmende: 42`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```php
<?php
$eventName = "Hackathon";
$teilnehmerzahl = 42;

echo "Event: {$eventName}, Teilnehmende: {$teilnehmerzahl}";
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

1. Schreibe eine Funktion `calcRemainingBudget($budget, $spent)`, die das Restbudget berechnet. (4.0)
2. Schreibe eine Funktion `metersToCentimeters($meters)`, die Meter in Zentimeter umrechnet. (3.5)

**Beispiele:**

- `calcRemainingBudget(1200, 450)` -> `750`
- `metersToCentimeters(1.75)` -> `175`

**Musterlösung**

```php
<?php
function calcRemainingBudget($budget, $spent) {
    return $budget - $spent;
}

function metersToCentimeters($meters) {
    return $meters * 100;
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

Schreibe eine Funktion `classifyBattery($percent)`, die den Akkustand als Text klassifiziert:

- `$percent < 0` oder `$percent > 100` -> `ungueltig` (2.0)
- `$percent < 20` -> `niedrig`
- `$percent >= 20` und `< 80` -> `mittel`
- `$percent >= 80` -> `hoch` (4.0)

**Beispiele:**

- `classifyBattery(10)` -> `niedrig`
- `classifyBattery(85)` -> `hoch`

**Musterlösung**

```php
<?php
function classifyBattery($percent) {
    if ($percent < 0 || $percent > 100) {
        return "ungueltig";
    } elseif ($percent < 20) {
        return "niedrig";
    } elseif ($percent < 80) {
        return "mittel";
    } else {
        return "hoch";
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

Schreibe eine Funktion `analyzeMeasurements($values)`, die:

- die Anzahl von Werten im Bereich `1` bis `9` (inklusive) zählt (3.0)
- die Summe der Absolutwerte aller Elemente berechnet (3.5)

Rückgabeformat als Array: `["singleDigitPositiveCount" => X, "absoluteSum" => Y]`

**Beispiel:**

`analyzeMeasurements([-3, 0, 4, 12, 9])` -> `["singleDigitPositiveCount" => 2, "absoluteSum" => 28]`

**Musterlösung**

```php
<?php
function analyzeMeasurements($values) {
    $singleDigitPositiveCount = 0;
    $absoluteSum = 0;

    foreach ($values as $value) {
        if ($value >= 1 && $value <= 9) {
            $singleDigitPositiveCount++;
        }

        if ($value < 0) {
            $absoluteSum += -$value;
        } else {
            $absoluteSum += $value;
        }
    }

    return [
        "singleDigitPositiveCount" => $singleDigitPositiveCount,
        "absoluteSum" => $absoluteSum
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
