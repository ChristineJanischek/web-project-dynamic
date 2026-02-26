# Einfache Ausgaben in PHP

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Variablen](VARIABLEN.md)

## Lernziele

- Verstehen, wie PHP Text ausgibt
- Unterschied zwischen `echo` und `print` kennen
- Variablen in Ausgaben sicher darstellen

## Theorie kompakt

PHP wird auf dem Server ausgeführt. Das Ergebnis (meist HTML/Text) wird an den Browser gesendet.

- `echo` gibt einen oder mehrere Strings aus
- `print` gibt einen String aus und liefert `1` zurück

In der Praxis wird meistens `echo` verwendet.

## Deklaration & Implementierung

```php
<?php
echo "Hallo Welt!";
print "Willkommen im PHP-Kurs";
```

Ausgabe mit Variablen:

```php
<?php
$name = "Mila";
echo "Hallo " . $name . "!";
echo "<p>Hallo $name!</p>";
```

## Best Practices

- Für Einsteiger möglichst durchgehend `echo` nutzen
- HTML-Ausgaben sauber strukturieren
- Nutzereingaben vor HTML-Ausgabe escapen (`htmlspecialchars`)

## Häufige Fehler

- Fehlendes Semikolon `;`
- Falsche Anführungszeichen-Kombination
- Vergessene Escapes bei Nutzereingaben
