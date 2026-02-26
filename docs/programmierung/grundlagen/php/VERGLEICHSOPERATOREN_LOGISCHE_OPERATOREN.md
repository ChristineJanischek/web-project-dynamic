# Vergleichsoperatoren und logische Operatoren in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Funktionen und Methoden](FUNKTIONEN_METHODEN.md)

## Lernziele

- Vergleichsoperatoren sicher einsetzen (`===`, `!==`, `>`, `<`, `>=`, `<=`)
- Logische Operatoren kombinieren (`&&`, `||`, `!`)
- Bedingungen in Funktionen kapseln und testbar machen

## Theorie kompakt

Vergleichsoperatoren liefern in PHP boolesche Werte (`true`/`false`). Logische Operatoren verknüpfen mehrere Bedingungen.

- `&&`: beide Bedingungen müssen wahr sein
- `||`: mindestens eine Bedingung muss wahr sein
- `!`: kehrt den Wahrheitswert um

Best Practice: Für Vergleiche möglichst `===` und `!==` nutzen, um ungewollte Typumwandlungen zu vermeiden.

## Deklaration & Implementierung

### Einfaches Beispiel: Volljährigkeit prüfen

```php
<?php
function istVolljaehrig(int $alter): bool
{
    return $alter >= 18;
}

echo "Test 1: " . (istVolljaehrig(16) ? "true" : "false") . PHP_EOL;
echo "Test 2: " . (istVolljaehrig(18) ? "true" : "false") . PHP_EOL;
```

### Komplexeres Beispiel: Freigabe für Rabattaktion

Regel: Eine Bestellung ist rabattberechtigt, wenn

- der Warenkorb mindestens 100 € hat **und**
- der Kunde entweder Premium ist **oder** einen Gutschein hat **und**
- das Konto nicht gesperrt ist.

```php
<?php
function istRabattFreigegeben(
    float $bestellwert,
    bool $istPremium,
    bool $hatGutschein,
    bool $kontoGesperrt
): bool {
    $mindestwertErreicht = $bestellwert >= 100;
    $kundeQualifiziert = $istPremium || $hatGutschein;
    $kontoIstAktiv = !$kontoGesperrt;

    return $mindestwertErreicht && $kundeQualifiziert && $kontoIstAktiv;
}

echo "Test A: " . (istRabattFreigegeben(80, true, false, false) ? "true" : "false") . PHP_EOL;
echo "Test B: " . (istRabattFreigegeben(120, false, true, false) ? "true" : "false") . PHP_EOL;
echo "Test C: " . (istRabattFreigegeben(200, true, false, true) ? "true" : "false") . PHP_EOL;
```

## Best Practices

- Teilbedingungen in sprechende Variablen aufteilen
- Komplexe Bedingungen in eigene Funktionen auslagern
- Grenzwerte und Negativfälle immer mit Testaufrufen prüfen

## Häufige Fehler

- `==` statt `===` verwenden
- Bedingungen ohne klare Struktur verketten
- Negation (`!`) auf den falschen Teilausdruck anwenden
