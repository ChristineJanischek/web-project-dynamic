# PHP Grundlagen

PHP führt Code auf dem Server aus und erzeugt HTML.

Für den vollständigen Grundlagen-Lernpfad (Ausgaben, Variablen, Rechenoperationen, Funktionen/Methoden, Kontrollstrukturen, Datenstrukturen, Algorithmen, Dateien) siehe:

- [Programmier-Grundlagen Übersicht](../programmierung/grundlagen/README.md)
- [PHP Fundamentals (modular)](../programmierung/grundlagen/php/README.md)

Beispiel `index.php`:

```php
<?php
$name = $_POST['name'] ?? 'Gast';
?>
<h1>Willkommen <?= htmlspecialchars($name) ?></h1>
```

Sicherheit: `htmlspecialchars` verhindert XSS.
Weiter: `datenbank.md`.
