# PHP Grundlagen

PHP führt Code auf dem Server aus und erzeugt HTML.

Beispiel `index.php`:
```php
<?php
$name = $_POST['name'] ?? 'Gast';
?>
<h1>Willkommen <?= htmlspecialchars($name) ?></h1>
```
Sicherheit: `htmlspecialchars` verhindert XSS.
Weiter: `datenbank.md`.
