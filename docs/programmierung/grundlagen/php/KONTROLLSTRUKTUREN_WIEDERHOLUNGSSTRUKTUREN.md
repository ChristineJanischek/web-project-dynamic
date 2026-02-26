# Kontrollstrukturen: Wiederholungsstrukturen in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Datenstrukturen](DATENSTRUKTUREN.md)

## Lernziele

- Schleifen mit `for`, `while`, `foreach` einsetzen
- Wiederholungen kontrolliert beenden
- Endlosschleifen vermeiden

## Theorie kompakt

Wiederholungsstrukturen führen Code mehrfach aus.

- `for`: bekannte Anzahl von Durchläufen
- `while`: solange Bedingung wahr ist
- `foreach`: über Arrays/Listen iterieren

## Deklaration & Implementierung

`for`-Schleife:

```php
<?php
for ($i = 1; $i <= 5; $i++) {
    echo "Runde $i <br>";
}
```

`while`-Schleife:

```php
<?php
$zaehler = 3;

while ($zaehler > 0) {
    echo "Noch $zaehler <br>";
    $zaehler--;
}
```

`foreach`-Schleife:

```php
<?php
$namen = ["Ali", "Mina", "Luca"];

foreach ($namen as $name) {
    echo "Hallo $name <br>";
}
```

## Best Practices

- Schleifenbedingung einfach und klar halten
- Bei `while` immer Änderung der Bedingungsvariable sicherstellen
- Für Arrays bevorzugt `foreach` nutzen

## Häufige Fehler

- Endlosschleifen durch fehlende Aktualisierung
- Falsche Start-/Endwerte in `for`
- Array-Indizes außerhalb des gültigen Bereichs
