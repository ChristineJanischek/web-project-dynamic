# Grundlagen der Programmierung - Basics (Python) - Variante 3

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

Schreibe ein kleines Programm, das `stadt` und `einwohner` einliest (oder setzt) und eine Stadtinformation ausgibt.

**Beispiel-Ausgabe:** `In Stuttgart leben 635911 Menschen.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```python

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calc_cube_volume(side)`, die das Volumen eines Würfels berechnet (Formel: side³). (4.0)
2. Schreibe eine Funktion `km_to_miles(km)`, die Kilometer in Meilen umrechnet (Formel: km / 1.609). (3.5)

**Beispiele:**

- `calc_cube_volume(3)` -> `27`
- `km_to_miles(16.09)` -> `10` (ca.)

**Antwortbereich:**

```python

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classify_temperature(temp)`, die eine Temperaturbewertung als Text liefert:

- `temp < -273` -> `ungueltig` (absoluter Nullpunkt) (2.0)
- `temp < 0` -> `gefroren`
- `temp >= 0` und `< 25` -> `angenehm`
- `temp >= 25` -> `heiss` (4.0)

**Beispiele:**

- `classify_temperature(-5)` -> `gefroren`
- `classify_temperature(30)` -> `heiss`

**Antwortbereich:**

```python

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyze_numbers(numbers)`, die:

- das Maximum der Zahlen findet (3.0)
- die Summe aller Zahlen berechnet (3.5)

Rückgabeformat als Dictionary: `{"maximum": X, "sum": Y}`

**Beispiel:**

`analyze_numbers([7, -2, 9, 3, -1])` -> `{"maximum": 9, "sum": 16}`

**Antwortbereich:**

```python

```
