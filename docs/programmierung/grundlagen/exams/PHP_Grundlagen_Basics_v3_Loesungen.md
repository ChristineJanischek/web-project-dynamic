# Grundlagen der Programmierung - Basics (PHP) - Variante 3

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```php
<?php
$stadt = "Stuttgart";
$einwohner = 635911;

echo "In {$stadt} leben {$einwohner} Menschen.";
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```php
<?php
function calcCubeVolume($side) {
    return $side * $side * $side;
    // Alternative: return pow($side, 3);
}

function kmToMiles($km) {
    return $km / 1.609;
}
```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

```php
<?php
function classifyTemperature($temp) {
    if ($temp < -273) {
        return "ungueltig";
    } elseif ($temp < 0) {
        return "gefroren";
    } elseif ($temp < 25) {
        return "angenehm";
    } else {
        return "heiss";
    }
}
```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

```php
<?php
function analyzeNumbers($numbers) {
    $maximum = $numbers[0];
    $sum = 0;

    foreach ($numbers as $num) {
        if ($num > $maximum) {
            $maximum = $num;
        }
        $sum += $num;
    }

    return ["maximum" => $maximum, "sum" => $sum];
}
```
