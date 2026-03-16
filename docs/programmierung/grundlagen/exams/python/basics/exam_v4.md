# Grundlagen der Programmierung - Basics (Python) - Variante 4

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

Schreibe ein kleines Programm, das `buch` und `seiten` einliest (oder setzt) und eine Buchinformation ausgibt.

**Beispiel-Ausgabe:** `Das Buch "1984" hat 328 Seiten.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```python

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calc_triangle_area(base, height)`, die die Fläche eines Dreiecks berechnet (Formel: base \* height / 2). (4.0)
2. Schreibe eine Funktion `miles_to_km(miles)`, die Meilen in Kilometer umrechnet (Formel: miles \* 1.609). (3.5)

**Beispiele:**

- `calc_triangle_area(6, 4)` -> `12`
- `miles_to_km(10)` -> `16.09`

**Antwortbereich:**

```python

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classify_speed(kmh)`, die eine Geschwindigkeitsklassifizierung als Text liefert:

- `kmh < 0` -> `ungueltig` (2.0)
- `kmh <= 30` -> `langsam`
- `kmh > 30` und `<= 100` -> `normal`
- `kmh > 100` -> `schnell` (4.0)

**Beispiele:**

- `classify_speed(25)` -> `langsam`
- `classify_speed(120)` -> `schnell`

**Antwortbereich:**

```python

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyze_numbers(numbers)`, die:

- das Minimum der Zahlen findet (3.0)
- die Anzahl positiver Zahlen zählt (3.5)

Rückgabeformat als Dictionary: `{"minimum": X, "positive_count": Y}`

**Beispiel:**

`analyze_numbers([5, -3, 2, 0, -7])` -> `{"minimum": -7, "positive_count": 2}`

**Antwortbereich:**

```python

```
