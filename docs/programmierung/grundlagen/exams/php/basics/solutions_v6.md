# Grundlagen der Programmierung - Basics (PHP) - Variante 6

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

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

### Haeufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

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
- 4.0 Punkte: Funktion 1 (Signatur, Berechnung, Rueckgabe) korrekt
- 3.5 Punkte: Funktion 2 (Signatur, Berechnung, Rueckgabe) korrekt

### Haeufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rueckgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

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
- 2.0 Punkte: Ungueltige Werte werden korrekt erkannt
- 2.5 Punkte: Fallunterscheidungen vollstaendig und logisch korrekt
- 1.5 Punkte: Korrekte Rueckgabewerte gemaess Aufgabenstellung

### Haeufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungueltigkeitspruefung fehlt oder steht an falscher Stelle
- Ein oder mehrere Faelle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

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
- 1.5 Punkte: Iteration ueber alle Elemente korrekt
- 3.0 Punkte: Kernlogik der ersten Kennzahl korrekt
- 1.5 Punkte: Kernlogik der zweiten Kennzahl korrekt
- 0.5 Punkte: Rueckgabeformat (Schluessel/Struktur) korrekt

### Haeufige Fehler
- Zaehler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung fuer Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rueckgabe enthaelt falsche Schluessel oder unvollstaendige Werte
