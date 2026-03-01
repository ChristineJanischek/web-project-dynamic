# Grundlagen der Programmierung - Basics (Python) - Variante 2

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```python
produkt = "Laptop"
preis = 899

print(f"Artikel: {produkt}, Preis: {preis} Euro")
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```python
import math

def calc_circle_circumference(radius):
    return 2 * math.pi * radius

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

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

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

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
