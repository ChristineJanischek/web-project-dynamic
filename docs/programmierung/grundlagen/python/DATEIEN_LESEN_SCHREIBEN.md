# Persistentes Schreiben in und Lesen aus Dateien in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Sprachvergleich](../VERGLEICH_JS_PY_PHP_OPERATOR_DATEI_IO.md)

## Lernziele

- Textdateien, CSV-Dateien und Log-Dateien in Python lesen/schreiben
- Dateioperationen in Funktionen kapseln
- Praxisnahe Abläufe robust und testbar aufbauen

## Theorie kompakt

Für Datei-I/O wird in Python `open(...)` mit `with` genutzt. CSV-Dateien werden mit dem Modul `csv` verarbeitet.

- CSV ist geeignet für strukturierte Tabellenwerte
- Log-Dateien halten technische Ereignisse nachvollziehbar fest
- Kapselung in Funktionen verbessert Wartbarkeit und Erweiterbarkeit

## Deklaration & Implementierung

### Einfaches Beispiel: Notiz speichern und lesen

```python
def speichere_notiz(datei_pfad, text):
    with open(datei_pfad, "w", encoding="utf-8") as datei:
        datei.write(text + "\n")


def lese_notiz(datei_pfad):
    with open(datei_pfad, "r", encoding="utf-8") as datei:
        return datei.read().strip()


speichere_notiz("notiz.txt", "Projektstart erfolgreich")
print("Test Notiz:", lese_notiz("notiz.txt"))
```

### Komplexeres Beispiel: CSV-Export und Ereignis-Logging

```python
import csv
from datetime import datetime


def schreibe_bestellungen_csv(datei_pfad, bestellungen):
    feldnamen = ["id", "kunde", "betrag", "status"]
    with open(datei_pfad, "w", newline="", encoding="utf-8") as datei:
        writer = csv.DictWriter(datei, fieldnames=feldnamen)
        writer.writeheader()
        writer.writerows(bestellungen)


def lese_bestellungen_csv(datei_pfad):
    with open(datei_pfad, "r", newline="", encoding="utf-8") as datei:
        reader = csv.DictReader(datei)
        ergebnis = []
        for zeile in reader:
            ergebnis.append(
                {
                    "id": int(zeile["id"]),
                    "kunde": zeile["kunde"],
                    "betrag": float(zeile["betrag"]),
                    "status": zeile["status"],
                }
            )
        return ergebnis


def schreibe_logeintrag(log_pfad, level, nachricht):
    zeit = datetime.now().isoformat(timespec="seconds")
    with open(log_pfad, "a", encoding="utf-8") as log_datei:
        log_datei.write(f"{zeit} [{level}] {nachricht}\n")


beispiel_bestellungen = [
    {"id": 1, "kunde": "Mia", "betrag": 129.9, "status": "offen"},
    {"id": 2, "kunde": "Noah", "betrag": 59.5, "status": "bezahlt"},
]

schreibe_bestellungen_csv("bestellungen.csv", beispiel_bestellungen)
geladen = lese_bestellungen_csv("bestellungen.csv")
print("Test CSV:", geladen)

schreibe_logeintrag("app.log", "INFO", "CSV-Datei wurde erfolgreich erstellt")
schreibe_logeintrag("app.log", "INFO", f"Anzahl Datensätze: {len(geladen)}")
print("Test Log: app.log wurde erweitert")
```

## Best Practices

- Immer `with open(...)` nutzen
- `utf-8` explizit setzen
- CSV-Datentypen beim Einlesen gezielt konvertieren
- Logeinträge mit Zeitstempel und Level versehen

## Häufige Fehler

- Datei im falschen Modus öffnen (`w` statt `a`)
- CSV-Werte als Strings weiterverarbeiten
- Relative Pfade ohne klares Arbeitsverzeichnis nutzen
