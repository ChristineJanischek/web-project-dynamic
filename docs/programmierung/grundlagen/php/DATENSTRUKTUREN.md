# Datenstrukturen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Algorithmen](ALGORITHMEN.md)

## Lernziele

- Arrays als zentrale Datenstruktur in PHP verstehen
- Numerische und assoziative Arrays einsetzen
- Daten strukturiert durchlaufen und auslesen

## Theorie kompakt

Datenstrukturen organisieren Daten so, dass Verarbeitung effizient und verständlich bleibt.

In PHP sind für den Einstieg besonders wichtig:

- numerische Arrays (`["A", "B"]`)
- assoziative Arrays (`["name" => "Lea"]`)

## Deklaration & Implementierung

Numerisches Array:

```php
<?php
$farben = ["rot", "blau", "gruen"];
echo $farben[1]; // blau
```

Assoziatives Array:

```php
<?php
$schueler = [
    "name" => "Lea",
    "klasse" => "11A",
    "punkte" => 82
];

echo $schueler["name"];
```

Durchlauf:

```php
<?php
foreach ($schueler as $schluessel => $wert) {
    echo "$schluessel: $wert <br>";
}
```

## Best Practices

- Einheitliche Struktur für gleichartige Datensätze
- Verständliche Schlüsselnamen verwenden
- Vor Zugriff prüfen, ob Schlüssel existiert (`isset`)

## Häufige Fehler

- Zugriff auf nicht vorhandene Indizes/Schlüssel
- Vermischte Struktur ohne klare Konvention
- Datenstruktur zu komplex für den aktuellen Zweck
