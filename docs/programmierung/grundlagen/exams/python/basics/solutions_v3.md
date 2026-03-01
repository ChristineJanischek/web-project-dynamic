# Grundlagen der Programmierung - Basics (Python) - Variante 3

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```python
stadt = "Stuttgart"
einwohner = 635911

print(f"In {stadt} leben {einwohner} Menschen.")
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```python
def calc_cube_volume(side):
    return side ** 3
    # Alternative: return side * side * side

def km_to_miles(km):
    return km / 1.609
```

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
