# Grundlagen der Programmierung - Exam Kontrollstrukturen (SPRACHE)

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

- A Fallunterscheidungen mit if-else: 5.0 Punkte
- B Mehrfach-Verzweigung mit switch/case: 7.5 Punkte
- C Schleifen (for, while): 6.0 Punkte
- D Verschachtelte Kontrollstrukturen: 6.5 Punkte

**Bewertungsschlüssel (linear)**

Punkte werden linear in Prozent umgerechnet: $prozent = (punkte / 25) * 100$.
Teilpunkte sind zulässig (Rundung in 0.5-Schritten).

---

## Aufgabe A - if-else (5.0 Punkte)

Schreibe eine Funktion `CHECK_AGE(age)`, die:

- `"underage"` zurückgibt, wenn `age < 18`
- `"adult"` zurückgibt, wenn `age >= 18`

**Beispiele:**

- `CHECK_AGE(16)` -> `"underage"`
- `CHECK_AGE(25)` -> `"adult"`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe B - switch/case Struktur (7.5 Punkte)

Schreibe eine Funktion `GRADE_DESCRIPTION(grade)`, die für Noten (1-5) eine Beschreibung gibt:

- 1 -> `"sehr gut"`
- 2 -> `"gut"`
- 3 -> `"befriedigend"`
- 4 -> `"ausreichend"`
- 5 -> `"mangelhaft"`
- sonstig -> `"ungueltige Note"`

**Beispiele:**

- `GRADE_DESCRIPTION(1)` -> `"sehr gut"`
- `GRADE_DESCRIPTION(6)` -> `"ungueltige Note"`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe C - Schleifen (6.0 Punkte)

Schreibe zwei kleine Funktionen:

1. `SUM_TO_N(n)` berechnet die Summe 1+2+3+...+n. (3.0)
2. `COUNT_EVENS(limit)` zählt alle geraden Zahlen von 1 bis `limit`. (3.0)

**Beispiele:**

- `SUM_TO_N(5)` -> `15`
- `COUNT_EVENS(10)` -> `5` (2, 4, 6, 8, 10)

**Antwortbereich:**

```SPRACHE

```

## Aufgabe D - Verschachtelte Strukturen (6.5 Punkte)

Schreibe eine Funktion `MULTIPLICATION_TABLE(rows)`, die eine kleine Multiplikationstabelle ausgibt:

- Schleife für Zeilen: 1 bis `rows`
- Innenschleife für Spalten: 1 bis `rows`
- Format: `Zeile nacheinander ausgeben` oder `als Array sameln`

**Beispiel** (rows=3):

```
Zeile 1: 1 2 3
Zeile 2: 2 4 6
Zeile 3: 3 6 9
```

**Antwortbereich:**

```SPRACHE

```
