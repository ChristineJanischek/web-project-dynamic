# Grundlagen der Programmierung - Basics (PHP) - Variante 5

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

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

### Haeufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

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
- 4.0 Punkte: Funktion 1 (Signatur, Berechnung, Rueckgabe) korrekt
- 3.5 Punkte: Funktion 2 (Signatur, Berechnung, Rueckgabe) korrekt

### Haeufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rueckgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

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
- 1.5 Punkte: Iteration ueber alle Elemente korrekt
- 3.0 Punkte: Kernlogik der ersten Kennzahl korrekt
- 1.5 Punkte: Kernlogik der zweiten Kennzahl korrekt
- 0.5 Punkte: Rueckgabeformat (Schluessel/Struktur) korrekt

### Haeufige Fehler
- Zaehler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung fuer Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rueckgabe enthaelt falsche Schluessel oder unvollstaendige Werte
