# Algorithmen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Persistentes Schreiben in und Lesen aus Dateien](DATEIEN_LESEN_SCHREIBEN.md)

## Lernziele

- Algorithmen als Schrittfolgen verstehen
- Einfache Such- und Verarbeitungsalgorithmen umsetzen
- Lesbare, testbare Abläufe formulieren

## Theorie kompakt

Ein Algorithmus ist eine endliche, eindeutige Schrittfolge zur Lösung eines Problems.

Gute Algorithmen sind:

- korrekt
- verständlich
- für den Zweck ausreichend effizient

## Deklaration & Implementierung

Beispiel: Größten Wert in einem Array finden

```php
<?php
$werte = [12, 7, 25, 19, 3];
$max = $werte[0];

foreach ($werte as $wert) {
    if ($wert > $max) {
        $max = $wert;
    }
}

echo "Maximum: $max";
```

Beispiel: Lineare Suche

```php
<?php
function enthaeltWert(array $liste, int $gesucht): bool
{
    foreach ($liste as $element) {
        if ($element === $gesucht) {
            return true;
        }
    }
    return false;
}
```

## Best Practices

- Problem zuerst in Klartext-Schritten notieren
- Mit kleinen Testdaten starten
- Sonderfälle mitdenken (leeres Array, doppelte Werte)

## Häufige Fehler

- Keine Abbruchbedingung
- Ungenaue Vergleichslogik
- Unklare Variablennamen im Ablauf
