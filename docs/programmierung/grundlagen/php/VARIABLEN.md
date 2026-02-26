# Variablen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Rechenoperationen](RECHENOPERATIONEN.md)

## Lernziele

- Variablen korrekt deklarieren und verwenden
- Datentypen in PHP verstehen
- Gute Variablennamen nach Best Practice wählen

## Theorie kompakt

Eine Variable ist ein benannter Speicherplatz für Werte.

In PHP:

- Variablen beginnen mit `$`
- Der Name sollte beschreibend sein
- PHP ist dynamisch typisiert (Typ wird zur Laufzeit bestimmt)

Typische Datentypen:

- `string` (Text)
- `int` (Ganzzahl)
- `float` (Kommazahl)
- `bool` (`true`/`false`)
- `array` (Sammlung von Werten)

## Deklaration & Implementierung

```php
<?php
$vorname = "Lea";
$alter = 17;
$note = 1.7;
$istVolljaehrig = false;

echo "$vorname ist $alter Jahre alt.";
```

Variable ändern:

```php
<?php
$punkte = 10;
$punkte = $punkte + 5;

echo "Punkte: $punkte"; // 15
```

## Best Practices

- Verwende sprechende Namen wie `$gesamtPreis`, nicht `$x`
- Nutze konsistente Schreibweise (z. B. `camelCase`)
- Initialisiere Variablen möglichst direkt
- Vermeide "magische" Werte ohne Kontext

## Häufige Fehler

- `$` vergessen (`name` statt `$name`)
- Uneinheitliche Namensgebung (`$Name`, `$name`, `$NAME` gemischt)
- Variablen verwenden, bevor sie gesetzt wurden
