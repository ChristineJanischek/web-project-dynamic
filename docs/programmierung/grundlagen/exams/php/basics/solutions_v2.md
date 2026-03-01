# Grundlagen der Programmierung - Basics (PHP) - Variante 2

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```php
<?php
$produkt = "Laptop";
$preis = 899;

echo "Artikel: {$produkt}, Preis: {$preis} Euro";
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```php
<?php
function calcCircleCircumference($radius) {
    return 2 * M_PI * $radius;
}

function fahrenheitToCelsius($f) {
    return ($f - 32) * 5 / 9;
}
```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

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

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

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
