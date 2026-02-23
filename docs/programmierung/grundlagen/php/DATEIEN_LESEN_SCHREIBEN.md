# Persistentes Schreiben in und Lesen aus Dateien (PHP)

## Lernziele

- Daten dauerhaft in Dateien speichern
- Gespeicherte Daten wieder einlesen
- Sichere Grundregeln beim Dateizugriff anwenden

## Theorie kompakt

"Persistent" bedeutet: Daten bleiben nach dem Programmende erhalten.

Einstieg in PHP:

- `file_put_contents()` zum Schreiben
- `file_get_contents()` zum Lesen

## Deklaration & Implementierung

Einfaches Schreiben:

```php
<?php
$datei = "daten/notizen.txt";
$inhalt = "Erster Eintrag\n";

file_put_contents($datei, $inhalt, FILE_APPEND);
echo "Gespeichert";
```

Lesen:

```php
<?php
$datei = "daten/notizen.txt";

if (file_exists($datei)) {
    $text = file_get_contents($datei);
    echo nl2br(htmlspecialchars($text));
} else {
    echo "Datei nicht gefunden";
}
```

## Best Practices

- Immer auf Existenz und Zugriffsrechte prüfen
- Nutzereingaben vor Ausgabe escapen (`htmlspecialchars`)
- Für strukturierte Daten frühzeitig JSON erwägen
- Dateipfade zentral und klar definieren

## Häufige Fehler

- Relativer Pfad zeigt ins falsche Verzeichnis
- Gleichzeitige Schreibzugriffe nicht bedacht
- Binär-/Textdaten vermischt gespeichert
