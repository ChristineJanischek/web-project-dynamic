# Grundlagen der Programmierung - Basics (Python) - Variante 3

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```python
stadt = "Stuttgart"
einwohner = 635911

print(f"In {stadt} leben {einwohner} Menschen.")
```

### Punktbewertung
- 2.0 Punkte: Variablen korrekt deklariert und initialisiert
- 1.0 Punkt: Eingabe korrekt eingelesen oder sauber simuliert
- 2.0 Punkte: Ausgabeformat entspricht der Vorgabe

### Haeufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```python
def calc_cube_volume(side):
    return side ** 3
    # Alternative: return side * side * side

def km_to_miles(km):
    return km / 1.609
```

### Punktbewertung
- 4.0 Punkte: Funktion 1 (Signatur, Berechnung, Rueckgabe) korrekt
- 3.5 Punkte: Funktion 2 (Signatur, Berechnung, Rueckgabe) korrekt

### Haeufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rueckgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

```python
def classify_temperature(temp):
    if temp < -273:
        return "ungueltig"
    elif temp < 0:
        return "gefroren"
    elif temp < 25:
        return "angenehm"
    else:
        return "heiss"
```

### Punktbewertung
- 2.0 Punkte: Ungueltige Werte werden korrekt erkannt
- 2.5 Punkte: Fallunterscheidungen vollstaendig und logisch korrekt
- 1.5 Punkte: Korrekte Rueckgabewerte gemaess Aufgabenstellung

### Haeufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungueltigkeitspruefung fehlt oder steht an falscher Stelle
- Ein oder mehrere Faelle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

```python
def analyze_numbers(numbers):
    maximum = numbers[0]
    total_sum = 0

    for num in numbers:
        if num > maximum:
            maximum = num
        total_sum += num

    return {"maximum": maximum, "sum": total_sum}
```

**Alternative Loesung (mit Builtin-Funktionen)**

```python
def analyze_numbers(numbers):
    return {"maximum": max(numbers), "sum": sum(numbers)}
```

### Punktbewertung
- 1.5 Punkte: Iteration ueber alle Elemente korrekt
- 3.0 Punkte: Kernlogik der ersten Kennzahl korrekt
- 1.5 Punkte: Kernlogik der zweiten Kennzahl korrekt
- 0.5 Punkte: Rueckgabeformat (Schluessel/Struktur) korrekt

### Haeufige Fehler
- Zaehler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung fuer Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rueckgabe enthaelt falsche Schluessel oder unvollstaendige Werte
