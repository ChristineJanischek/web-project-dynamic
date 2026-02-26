# Funktionen und Methoden in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Kontrollstrukturen: Fallunterscheidungen](KONTROLLSTRUKTUREN_FALLUNTERSCHEIDUNGEN.md)

## Lernziele

- Funktionen definieren und aufrufen
- Parameter und Rückgabewerte verstehen
- Unterschied zwischen Funktion und Methode kennen

## Theorie kompakt

- **Funktion:** Eigenständiger, wiederverwendbarer Codeblock
- **Methode:** Funktion innerhalb einer Klasse (objektorientiert)

Für den Einstieg sind Funktionen zentral.

## Deklaration & Implementierung

Funktion mit Rückgabewert:

```php
<?php
function addiere(int $a, int $b): int
{
    return $a + $b;
}

$summe = addiere(4, 7);
echo $summe; // 11
```

Funktion ohne Rückgabewert:

```php
<?php
function begruessung(string $name): void
{
    echo "Hallo $name!";
}

begruessung("Nora");
```

## Best Practices

- Eine Funktion = eine klare Aufgabe
- Aussagekräftige Namen (`berechneMwst`, `istGueltig`)
- Parameter und Rückgabewerte typisieren
- Kleine Funktionen statt langer Monster-Funktionen

## Häufige Fehler

- Funktionsname doppelt vergeben
- `return` vergessen
- Zu viele Verantwortlichkeiten in einer Funktion bündeln
