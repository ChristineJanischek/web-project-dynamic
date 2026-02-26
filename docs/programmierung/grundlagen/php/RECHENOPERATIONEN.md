# Rechenoperationen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Vergleichsoperatoren und logische Operatoren](VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md)

## Lernziele

- Grundrechenarten in PHP anwenden
- Operatoren sicher einsetzen
- Rechenergebnisse in Programmlogik nutzen

## Theorie kompakt

Wichtige Operatoren:

- `+` Addition
- `-` Subtraktion
- `*` Multiplikation
- `/` Division
- `%` Modulo (Rest)

Kombinierte Zuweisung:

- `$x += 2` entspricht `$x = $x + 2`

## Deklaration & Implementierung

```php
<?php
$a = 12;
$b = 5;

echo $a + $b; // 17
echo $a - $b; // 7
echo $a * $b; // 60
echo $a / $b; // 2.4
echo $a % $b; // 2
```

Praktisches Beispiel:

```php
<?php
$netto = 100;
$mwstSatz = 0.19;
$brutto = $netto + ($netto * $mwstSatz);

echo "Bruttopreis: " . $brutto;
```

## Best Practices

- Mit Klammern Prioritäten klar machen
- Zwischenergebnisse in gut benannten Variablen speichern
- Bei Geldwerten auf Rundung achten (`round`)

## Häufige Fehler

- Ganzzahl-/Kommazahl-Verwechslung
- Rechenlogik ohne Klammern missverständlich schreiben
- Divisionsfälle mit `0` nicht berücksichtigen
