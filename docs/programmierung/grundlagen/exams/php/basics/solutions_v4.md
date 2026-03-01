# Grundlagen der Programmierung - Basics (PHP) - Variante 4

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```php
<?php
$buch = "1984";
$seiten = 328;

echo "Das Buch \"{$buch}\" hat {$seiten} Seiten.";
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```php
<?php
function calcTriangleArea($base, $height) {
    return $base * $height / 2;
}

function milesToKm($miles) {
    return $miles * 1.609;
}
```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

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

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

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
