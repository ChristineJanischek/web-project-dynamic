# Persistentes Schreiben in und Lesen aus Dateien (PHP)

[← Zurück zur PHP-Übersicht](README.md) · [Weiter: Sprachvergleich](../VERGLEICH_JS_PY_PHP_OPERATOR_DATEI_IO.md)

## Lernziele

- Textdateien, CSV-Dateien und Log-Dateien in PHP lesen/schreiben
- Dateioperationen in Funktionen kapseln
- Praxisnahe Abläufe sauber und wartbar umsetzen

## Theorie kompakt

Für Datei-I/O in PHP sind diese Bausteine zentral:

- `fopen`, `fputcsv`, `fgetcsv` für CSV-Dateien
- `file_put_contents(..., FILE_APPEND)` für Log-Dateien
- Klare Funktionsgrenzen für Lesen, Schreiben und Protokollieren

## Deklaration & Implementierung

### Einfaches Beispiel: Notiz speichern und lesen

```php
<?php
function speichereNotiz(string $dateiPfad, string $text): void
{
    file_put_contents($dateiPfad, $text . PHP_EOL);
}

function leseNotiz(string $dateiPfad): string
{
    if (!file_exists($dateiPfad)) {
        return "";
    }
    return trim((string) file_get_contents($dateiPfad));
}

speichereNotiz("notiz.txt", "Projektstart erfolgreich");
echo "Test Notiz: " . leseNotiz("notiz.txt") . PHP_EOL;
```

### Komplexeres Beispiel: CSV-Export und Ereignis-Logging

```php
<?php
function schreibeBestellungenCsv(string $dateiPfad, array $bestellungen): void
{
    $datei = fopen($dateiPfad, "w");
    fputcsv($datei, ["id", "kunde", "betrag", "status"]);

    foreach ($bestellungen as $eintrag) {
        fputcsv($datei, [
            $eintrag["id"],
            $eintrag["kunde"],
            $eintrag["betrag"],
            $eintrag["status"],
        ]);
    }

    fclose($datei);
}

function leseBestellungenCsv(string $dateiPfad): array
{
    $ergebnis = [];
    if (!file_exists($dateiPfad)) {
        return $ergebnis;
    }

    $datei = fopen($dateiPfad, "r");
    $header = fgetcsv($datei);

    while (($zeile = fgetcsv($datei)) !== false) {
        $ergebnis[] = [
            "id" => (int) $zeile[0],
            "kunde" => $zeile[1],
            "betrag" => (float) $zeile[2],
            "status" => $zeile[3],
        ];
    }

    fclose($datei);
    return $ergebnis;
}

function schreibeLogeintrag(string $logPfad, string $level, string $nachricht): void
{
    $zeit = date("c");
    $zeile = sprintf("%s [%s] %s%s", $zeit, $level, $nachricht, PHP_EOL);
    file_put_contents($logPfad, $zeile, FILE_APPEND);
}

$beispielBestellungen = [
    ["id" => 1, "kunde" => "Mia", "betrag" => 129.9, "status" => "offen"],
    ["id" => 2, "kunde" => "Noah", "betrag" => 59.5, "status" => "bezahlt"],
];

schreibeBestellungenCsv("bestellungen.csv", $beispielBestellungen);
$geladen = leseBestellungenCsv("bestellungen.csv");
echo "Test CSV: " . print_r($geladen, true) . PHP_EOL;

schreibeLogeintrag("app.log", "INFO", "CSV-Datei wurde erfolgreich erstellt");
schreibeLogeintrag("app.log", "INFO", "Anzahl Datensätze: " . count($geladen));
echo "Test Log: app.log wurde erweitert" . PHP_EOL;
```

## Best Practices

- Lese-/Schreiblogik pro Aufgabe in eigene Funktion legen
- CSV-Werte beim Einlesen sauber typisieren
- Logs nur anhängen statt überschreiben
- Dateiexistenz vor dem Lesen prüfen

## Häufige Fehler

- Datei-Handles nicht schließen
- CSV ohne Header schreiben und später schwer zuordnen
- Log-Dateien bei jedem Lauf vollständig ersetzen
