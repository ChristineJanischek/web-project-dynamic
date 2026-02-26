# Funktionen und Methoden in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Kontrollstrukturen: Fallunterscheidungen](KONTROLLSTRUKTUREN_FALLUNTERSCHEIDUNGEN.md)

## Lernziele

- Funktionen definieren und aufrufen
- Parameter und Rückgabewerte verstehen
- Unterschied zwischen Funktion und Methode kennen

## Theorie kompakt

- **Funktion:** eigener, wiederverwendbarer Codeblock
- **Methode:** Funktion, die zu einem Objekt gehört

## Deklaration & Implementierung

```python
def addiere(a: int, b: int) -> int:
    return a + b

summe = addiere(4, 7)
print(summe)
```

Methodenbeispiel:

```python
name = "nora"
print(name.upper())
```

## Best Practices

- Eine Funktion mit klarer Aufgabe
- Aussagekräftige Funktionsnamen
- Type Hints schrittweise einsetzen

## Häufige Fehler

- Einrückungen inkonsistent
- `return` bei benötigtem Rückgabewert vergessen
