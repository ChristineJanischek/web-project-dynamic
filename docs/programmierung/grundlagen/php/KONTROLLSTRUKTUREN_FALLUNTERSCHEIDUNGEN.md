# Kontrollstrukturen: Fallunterscheidungen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Kontrollstrukturen: Wiederholungsstrukturen](KONTROLLSTRUKTUREN_WIEDERHOLUNGSSTRUKTUREN.md)

## Lernziele

- Entscheidungen mit `if`, `elseif`, `else` treffen
- `switch` für mehrere feste Fälle nutzen
- Bedingungen sauber und nachvollziehbar formulieren

## Theorie kompakt

Fallunterscheidungen steuern, **welcher Code** abhängig von einer Bedingung ausgeführt wird.

Vergleichsoperatoren:

- `==` gleich
- `===` identisch (Wert + Typ)
- `!=` ungleich
- `>` `<` `>=` `<=`

## Deklaration & Implementierung

Mit `if`:

```php
<?php
$punkte = 74;

if ($punkte >= 90) {
    echo "Note 1";
} elseif ($punkte >= 75) {
    echo "Note 2";
} elseif ($punkte >= 60) {
    echo "Note 3";
} else {
    echo "Verbesserungsbedarf";
}
```

Mit `switch`:

```php
<?php
$tag = "Mo";

switch ($tag) {
    case "Mo":
        echo "Wochenstart";
        break;
    case "Fr":
        echo "Bald Wochenende";
        break;
    default:
        echo "Regulärer Tag";
}
```

## Best Practices

- Für Wertbereichsprüfungen eher `if/elseif`
- Für feste Einzelwerte oft `switch`
- Bedingungen lesbar halten (ggf. Hilfsvariablen)
- Möglichst strikt vergleichen (`===`)

## Häufige Fehler

- `=` statt `==`/`===` in Bedingungen
- `break` in `switch` vergessen
- Zu tief verschachtelte Bedingungen
