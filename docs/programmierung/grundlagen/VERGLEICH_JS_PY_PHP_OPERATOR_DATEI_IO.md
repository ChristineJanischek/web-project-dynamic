# Sprachvergleich: JavaScript, Python, PHP

[← Zurück zur Grundlagen-Übersicht](README.md)

Dieses Blatt bündelt die wichtigsten Unterschiede und Gemeinsamkeiten zu:

1. Vergleichsoperatoren und logische Operatoren
2. Lesen und Schreiben von Dateien (CSV, Log)

## Lernziele

- Operatoren und Dateizugriffe sprachübergreifend vergleichen
- Wiedererkennbare Muster für funktionales Arbeiten nutzen
- Unterschiede bewusst einordnen, ohne Konzepte doppelt zu lernen

## 1) Vergleichsoperatoren und logische Operatoren

### Operatoren im direkten Vergleich

| Konzept                  | JavaScript           | Python               | PHP                  |
| ------------------------ | -------------------- | -------------------- | -------------------- |
| Gleichheit (empfohlen)   | `===`                | `==`                 | `===`                |
| Ungleichheit (empfohlen) | `!==`                | `!=`                 | `!==`                |
| Größer / kleiner         | `>`, `<`, `>=`, `<=` | `>`, `<`, `>=`, `<=` | `>`, `<`, `>=`, `<=` |
| Logisches UND            | `&&`                 | `and`                | `&&`                 |
| Logisches ODER           | `\|\|`               | `or`                 | `\|\|`               |
| Logisches NICHT          | `!`                  | `not`                | `!`                  |

Hinweis:

- In JavaScript und PHP möglichst strikt vergleichen (`===`, `!==`).
- In Python gibt es keinen getrennten strikten Gleichheitsoperator.

### Gemeinsames Funktionsmuster (Rabattfreigabe)

Regel: Rabatt nur bei Mindestwert, qualifiziertem Kunden und aktivem Konto.

```text
funktion istRabattFreigegeben(bestellwert, istPremium, hatGutschein, kontoGesperrt):
    mindestwertErreicht = bestellwert >= 100
    kundeQualifiziert = istPremium ODER hatGutschein
    kontoIstAktiv = NICHT kontoGesperrt
    gib mindestwertErreicht UND kundeQualifiziert UND kontoIstAktiv zurück
```

Empfohlene Detailkapitel:

- JavaScript: [javascript/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md](javascript/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md)
- Python: [python/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md](python/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md)
- PHP: [php/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md](php/VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md)

## 2) Dateien lesen und schreiben (CSV + Log)

### API-Vergleich

| Aufgabe        | JavaScript (Node.js)               | Python           | PHP                                   |
| -------------- | ---------------------------------- | ---------------- | ------------------------------------- |
| Text schreiben | `fs.writeFileSync(...)`            | `open(..., "w")` | `file_put_contents(...)`              |
| Text lesen     | `fs.readFileSync(...)`             | `open(..., "r")` | `file_get_contents(...)`              |
| CSV schreiben  | manuell/Library (`fs` + Mapping)   | `csv.DictWriter` | `fputcsv`                             |
| CSV lesen      | manuell/Library (`split`, Mapping) | `csv.DictReader` | `fgetcsv`                             |
| Log anhängen   | `fs.appendFileSync(...)`           | `open(..., "a")` | `file_put_contents(..., FILE_APPEND)` |

### Gemeinsames Funktionsmuster

```text
funktion exportiereBestellungen(bestellungen):
    schreibe CSV mit Header
    lese CSV wieder ein
    konvertiere Datentypen (id, betrag)
    schreibe Logeintrag mit Zeitstempel und Anzahl Datensätze
```

Empfohlene Detailkapitel:

- JavaScript: [javascript/DATEIEN_LESEN_SCHREIBEN.md](javascript/DATEIEN_LESEN_SCHREIBEN.md)
- Python: [python/DATEIEN_LESEN_SCHREIBEN.md](python/DATEIEN_LESEN_SCHREIBEN.md)
- PHP: [php/DATEIEN_LESEN_SCHREIBEN.md](php/DATEIEN_LESEN_SCHREIBEN.md)

## Best Practices (sprachübergreifend)

- Funktionen pro Verantwortlichkeit klein und eindeutig halten
- Ein- und Ausgabeformat klar definieren (CSV-Header, Log-Struktur)
- Datentypen beim Einlesen konsequent prüfen/konvertieren
- UTF-8 und Dateipfade bewusst setzen
- Tests über konkrete Funktionsaufrufe mit Grenzfällen durchführen

## Häufige Fehler (sprachübergreifend)

- Operatoren mit impliziten Typumwandlungen einsetzen
- Dateioperationen direkt im Hauptablauf statt in Funktionen vermischen
- Log-Dateien versehentlich überschreiben statt anhängen
- CSV ohne Header speichern oder uneinheitlich parsen
