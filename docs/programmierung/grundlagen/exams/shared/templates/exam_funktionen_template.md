# Grundlagen der Programmierung - Exam Funktionen (SPRACHE)

<!-- Konfigurierbare Werte (hier mit Standardwerten):
     SPRACHE: JavaScript, PHP, Python
     Bearbeitungszeit: 60 Minuten
     Gesamtpunkte: 25
     Aufgabe A: 5.0 Punkte
     Aufgabe B: 7.5 Punkte
     Aufgabe C: 6.0 Punkte
     Aufgabe D: 6.5 Punkte
-->

**Name:**

---

**Datum:** ******\_\_\_\_****** **Klasse:** ******\_\_\_\_******

**Sprache:** SPRACHE

**Bearbeitungszeit:** 60 Minuten

**Hinweise**

- Löse die Aufgaben so, dass der Code auch handschriftlich nachvollziehbar ist.
- Falls keine echte Eingabe möglich ist, simuliere Eingaben mit Variablen.
- Schreibe klar, kurz und ohne Redundanz. Keine externen Bibliotheken.

**Punkteübersicht (25 Punkte gesamt)**

- A Basisfunktionen (Signatur, Parameter, Rückgabe): 5.0 Punkte
- B Lokale + globale Variablen: 7.5 Punkte
- C Funktionen mit Defaultwerten, optionalen Parametern: 6.0 Punkte
- D Rekursion: 6.5 Punkte

**Bewertungsschlüssel (linear)**

Punkte werden linear in Prozent umgerechnet: $prozent = (punkte / 25) * 100$.
Teilpunkte sind zulässig (Rundung in 0.5-Schritten).

---

## Aufgabe A - Basisfunktionen (5.0 Punkte)

Schreibe zwei einfache Funktionen:

1. `FUNC_GREET(name)` gibt eine persoenliche Begrüßung zurück.
2. `FUNC_ADD(a, b)` addiert zwei Zahlen.

**Beispiele:**

- `FUNC_GREET("Anna")` -> `"Hallo Anna!"`
- `FUNC_ADD(3, 5)` -> `8`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe B - Lokale + globale Variablen (7.5 Punkte)

Schreibe ein Programm, das:

1. Eine globale Variable `counter` mit Wert 0 deklariert. (2.0)
2. Eine Funktion `increment()` schreibt, die `counter` erhöht und den neuen Wert zurückgibt. (5.5)

**Beispiele nach zwei Aufrufen:**

- `increment()` -> `1`
- `increment()` -> `2`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe C - Defaultwerte + optionale Parameter (6.0 Punkte)

Schreibe eine Funktion `FUNC_POWER(base, exponent=2)`, die:

- `base` potenziert mit `exponent`
- Default-Exponent ist 2 (Quadrat)

**Beispiele:**

- `FUNC_POWER(3)` -> `9` (Standard: Quadrat)
- `FUNC_POWER(2, 3)` -> `8`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe D - Rekursion (6.5 Punkte)

Schreibe eine Funktion `FUNC_FACTORIAL(n)`, die die Fakultaet berechnet:

- Basis: $n = 0$ oder $n = 1$ -> 1
- Rekursion: $n! = n \\times (n-1)!$

**Beispiele:**

- `FUNC_FACTORIAL(0)` -> `1`
- `FUNC_FACTORIAL(5)` -> `120`

**Antwortbereich:**

```SPRACHE

```
