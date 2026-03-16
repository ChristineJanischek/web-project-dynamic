# Grundlagen der Programmierung - Basics (Python) - Variante 2

**Dokumenttyp:** Musterlösung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `produkt` und `preis` einliest (oder setzt) und eine Produktinformation ausgibt.

**Beispiel-Ausgabe:** `Artikel: Laptop, Preis: 899 Euro`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```python
produkt = "Laptop"
preis = 899

print(f"Artikel: {produkt}, Preis: {preis} Euro")
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

1. Schreibe eine Funktion `calc_circle_circumference(radius)`, die den Kreisumfang berechnet (Formel: 2 \* π \* r). (4.0)
2. Schreibe eine Funktion `fahrenheit_to_celsius(f)`, die Fahrenheit in Celsius umrechnet (Formel: (f - 32) \* 5 / 9). (3.5)

**Beispiele:**

- `calc_circle_circumference(5)` -> `31.4159...` (ca. 31.42)
- `fahrenheit_to_celsius(32)` -> `0`

**Musterlösung**

```python
import math

def calc_circle_circumference(radius):
    return 2 * math.pi * radius

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
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

Schreibe eine Funktion `classify_age(age)`, die eine Altersgruppe als Text liefert:

- `age < 0` oder `age > 150` -> `ungueltig` (2.0)
- `age < 18` -> `minderjaehrig`
- `age >= 18` und `< 65` -> `erwachsen`
- `age >= 65` -> `senior` (4.0)

**Beispiele:**

- `classify_age(16)` -> `minderjaehrig`
- `classify_age(70)` -> `senior`

**Musterlösung**

```python
def classify_age(age):
    if age < 0 or age > 150:
        return "ungueltig"
    elif age < 18:
        return "minderjaehrig"
    elif age < 65:
        return "erwachsen"
    else:
        return "senior"
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

- die Anzahl ungerader Zahlen zählt (3.0)
- die Summe aller negativen Zahlen berechnet (3.5)

Rückgabeformat als Dictionary: `{"odd_count": X, "negative_sum": Y}`

**Beispiel:**

`analyze_numbers([3, -2, 5, 0, -4])` -> `{"odd_count": 2, "negative_sum": -6}`

**Musterlösung**

```python
def analyze_numbers(numbers):
    odd_count = 0
    negative_sum = 0

    for num in numbers:
        if num % 2 != 0:
            odd_count += 1
        if num < 0:
            negative_sum += num

    return {"odd_count": odd_count, "negative_sum": negative_sum}
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
