````markdown
# Persistentes Schreiben in und Lesen aus Dateien in Python

## Lernziele

- Dateien mit Python öffnen, lesen und schreiben
- Textdaten dauerhaft speichern
- Sicheren Umgang mit Dateipfaden und Fehlerfällen verstehen

## Theorie kompakt

Dateizugriffe erfolgen in Python mit `open()`. Typische Modi:

- `"r"` lesen
- `"w"` schreiben (überschreibt Datei)
- `"a"` anhängen

Mit `with` wird die Datei nach der Nutzung automatisch geschlossen.

## Deklaration & Implementierung

```python
text = "Hallo Datei"

with open("notiz.txt", "w", encoding="utf-8") as datei:
    datei.write(text)

with open("notiz.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()

print(inhalt)
```

## Best Practices

- Immer `with open(...)` verwenden
- Zeichencodierung (`utf-8`) explizit setzen
- Dateipfade klar und konsistent halten

## Häufige Fehler

- Falscher Modus (`r` statt `w`)
- Datei nicht gefunden (`FileNotFoundError`)
- Umlaute ohne `utf-8` falsch dargestellt
````
