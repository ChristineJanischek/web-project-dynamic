# Grundlagen der Programmierung - Basics (Python) - Variante 3

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `stadt` und `einwohner` einliest (oder setzt) und eine Stadtinformation ausgibt.

**Beispiel-Ausgabe:** `In Stuttgart leben 635911 Menschen.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```python
stadt = "Stuttgart"
einwohner = 635911

print(f"In {stadt} leben {einwohner} Menschen.")
```

### Punktbewertung
- 2.0 Punkte: Variablen korrekt deklariert und initialisiert
- 1.0 Punkt: Eingabe korrekt eingelesen oder sauber simuliert
- 2.0 Punkte: Ausgabeformat entspricht der Vorgabe

### Häufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calc_cube_volume(side)`, die das Volumen eines Würfels berechnet (Formel: side³). (4.0)
2. Schreibe eine Funktion `km_to_miles(km)`, die Kilometer in Meilen umrechnet (Formel: km / 1.609). (3.5)

**Beispiele:**

- `calc_cube_volume(3)` -> `27`
- `km_to_miles(16.09)` -> `10` (ca.)

**Musterlösung**

```python
def calc_cube_volume(side):
    return side ** 3
    # Alternative: return side * side * side

def km_to_miles(km):
    return km / 1.609
```

### Punktbewertung
- 4.0 Punkte: Funktion 1 (Signatur, Berechnung, Rückgabe) korrekt
- 3.5 Punkte: Funktion 2 (Signatur, Berechnung, Rückgabe) korrekt

### Häufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classify_temperature(temp)`, die eine Temperaturbewertung als Text liefert:

- `temp < -273` -> `ungueltig` (absoluter Nullpunkt) (2.0)
- `temp < 0` -> `gefroren`
- `temp >= 0` und `< 25` -> `angenehm`
- `temp >= 25` -> `heiss` (4.0)

**Beispiele:**

- `classify_temperature(-5)` -> `gefroren`
- `classify_temperature(30)` -> `heiss`

**Musterlösung**

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
- 2.0 Punkte: Ungültige Werte werden korrekt erkannt
- 2.5 Punkte: Fallunterscheidungen vollständig und logisch korrekt
- 1.5 Punkte: Korrekte Rückgabewerte gemäß Aufgabenstellung

### Häufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyze_numbers(numbers)`, die:

- das Maximum der Zahlen findet (3.0)
- die Summe aller Zahlen berechnet (3.5)

Rückgabeformat als Dictionary: `{"maximum": X, "sum": Y}`

**Beispiel:**

`analyze_numbers([7, -2, 9, 3, -1])` -> `{"maximum": 9, "sum": 16}`

**Musterlösung**

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

**Alternative Lösung (mit Builtin-Funktionen)**

```python
def analyze_numbers(numbers):
    return {"maximum": max(numbers), "sum": sum(numbers)}
```

### Punktbewertung
- 1.5 Punkte: Iteration über alle Elemente korrekt
- 3.0 Punkte: Kernlogik der ersten Kennzahl korrekt
- 1.5 Punkte: Kernlogik der zweiten Kennzahl korrekt
- 0.5 Punkte: Rückgabeformat (Schlüssel/Struktur) korrekt

### Häufige Fehler
- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
