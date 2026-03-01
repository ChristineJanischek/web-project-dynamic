# Grundlagen der Programmierung - Basics (Python) - Variante 4

**Dokumenttyp:** Musterloesung | **Punkte gesamt:** 25

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

```python
buch = "1984"
seiten = 328

print(f'Das Buch "{buch}" hat {seiten} Seiten.')
```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

```python
def calc_triangle_area(base, height):
    return base * height / 2

def miles_to_km(miles):
    return miles * 1.609
```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

```python
def classify_speed(kmh):
    if kmh < 0:
        return "ungueltig"
    elif kmh <= 30:
        return "langsam"
    elif kmh <= 100:
        return "normal"
    else:
        return "schnell"
```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

```python
def analyze_numbers(numbers):
    minimum = numbers[0]
    positive_count = 0

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > 0:
            positive_count += 1

    return {"minimum": minimum, "positive_count": positive_count}
```

**Alternative Loesung (mit Builtin-Funktionen)**

```python
def analyze_numbers(numbers):
    minimum = min(numbers)
    positive_count = len([n for n in numbers if n > 0])
    return {"minimum": minimum, "positive_count": positive_count}
```
