# Datenstrukturen in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Algorithmen](ALGORITHMEN.md)

## Lernziele

- Listen, Tupel, Dictionaries und Mengen unterscheiden
- Geeignete Struktur für Daten auswählen
- Strukturen korrekt durchlaufen

## Theorie kompakt

Wichtige Einstiegsstrukturen:

- `list` geordnet, veränderbar
- `tuple` geordnet, unveränderbar
- `dict` Schlüssel-Wert-Paare
- `set` eindeutige Elemente

## Deklaration & Implementierung

```python
farben = ["rot", "blau", "gruen"]
schueler = {"name": "Lea", "klasse": "11A", "punkte": 82}

print(farben[1])
print(schueler["name"])
```

## Best Practices

- Datenstruktur passend zur Aufgabe wählen
- Schlüssel konsistent benennen
- Vor Zugriff auf Schlüssel Existenz prüfen

## Häufige Fehler

- Zugriff auf nicht vorhandene Schlüssel
- Falscher Datentyp für die Aufgabe
