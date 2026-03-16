# Grundlagen der Programmierung - Basics (Python) - Variante 2

**Name:** ****\*\*\*\*****\_\_\_\_****\*\*\*\***** **Datum:** **\*\***\_\_\_\_**\*\*** **Klasse:** \***\*\_\_\_\_\*\***

**Sprache:** Python

**Bearbeitungszeit:** 45-60 Minuten

**Hinweise**

- Löse die Aufgaben so, dass der Code auch handschriftlich nachvollziehbar ist.
- Falls keine echte Eingabe möglich ist, simuliere Eingaben mit Variablen.
- Schreibe klar, kurz und ohne Redundanz. Keine externen Bibliotheken.

**Punkteübersicht (25 Punkte gesamt)**

- A Variablen + Ein/Ausgabe: 5.0 Punkte
- B Funktionen (kleine Berechnungen): 7.5 Punkte
- C Funktionen + Fallunterscheidungen: 6.0 Punkte
- D Funktionen + Schleifen + Datenstrukturen: 6.5 Punkte

**Bewertungsschlüssel (linear)**

Punkte werden linear in Prozent umgerechnet: $prozent = (punkte / 25) * 100$.
Teilpunkte sind zulässig (Rundung in 0.5-Schritten).

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

Schreibe ein kleines Programm, das `produkt` und `preis` einliest (oder setzt) und eine Produktinformation ausgibt.

**Beispiel-Ausgabe:** `Artikel: Laptop, Preis: 899 Euro`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```python

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calc_circle_circumference(radius)`, die den Kreisumfang berechnet (Formel: 2 \* π \* r). (4.0)
2. Schreibe eine Funktion `fahrenheit_to_celsius(f)`, die Fahrenheit in Celsius umrechnet (Formel: (f - 32) \* 5 / 9). (3.5)

**Beispiele:**

- `calc_circle_circumference(5)` -> `31.4159...` (ca. 31.42)
- `fahrenheit_to_celsius(32)` -> `0`

**Antwortbereich:**

```python

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classify_age(age)`, die eine Altersgruppe als Text liefert:

- `age < 0` oder `age > 150` -> `ungueltig` (2.0)
- `age < 18` -> `minderjaehrig`
- `age >= 18` und `< 65` -> `erwachsen`
- `age >= 65` -> `senior` (4.0)

**Beispiele:**

- `classify_age(16)` -> `minderjaehrig`
- `classify_age(70)` -> `senior`

**Antwortbereich:**

```python

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyze_numbers(numbers)`, die:

- die Anzahl ungerader Zahlen zählt (3.0)
- die Summe aller negativen Zahlen berechnet (3.5)

Rückgabeformat als Dictionary: `{"odd_count": X, "negative_sum": Y}`

**Beispiel:**

`analyze_numbers([3, -2, 5, 0, -4])` -> `{"odd_count": 2, "negative_sum": -6}`

**Antwortbereich:**

```python

```
