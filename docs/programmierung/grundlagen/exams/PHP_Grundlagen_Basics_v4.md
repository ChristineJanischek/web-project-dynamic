# Grundlagen der Programmierung - Basics (PHP) - Variante 4

**Name:** ****\*\*\*\*****\_\_\_\_****\*\*\*\***** **Datum:** **\*\***\_\_\_\_**\*\*** **Klasse:** \***\*\_\_\_\_\*\***

**Sprache:** PHP

**Bearbeitungszeit:** 45-60 Minuten

**Hinweise**

- Loese die Aufgaben so, dass der Code auch handschriftlich nachvollziehbar ist.
- Falls keine echte Eingabe moeglich ist, simuliere Eingaben mit Variablen.
- Schreibe klar, kurz und ohne Redundanz. Keine externen Bibliotheken.

**Punkteuebersicht (25 Punkte gesamt)**

- A Variablen + Ein/Ausgabe: 5.0 Punkte
- B Funktionen (kleine Berechnungen): 7.5 Punkte
- C Funktionen + Fallunterscheidungen: 6.0 Punkte
- D Funktionen + Schleifen + Datenstrukturen: 6.5 Punkte

**Bewertungsschluessel (linear)**

Punkte werden linear in Prozent umgerechnet: $prozent = (punkte / 25) * 100$.
Teilpunkte sind zulaessig (Rundung in 0.5-Schritten).

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

Schreibe ein kleines Programm, das `buch` und `seiten` einliest (oder setzt) und eine Buchinformation ausgibt.

**Beispiel-Ausgabe:** `Das Buch "1984" hat 328 Seiten.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```php

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calcTriangleArea($base, $height)`, die die Flaeche eines Dreiecks berechnet (Formel: $base \* $height / 2). (4.0)
2. Schreibe eine Funktion `milesToKm($miles)`, die Meilen in Kilometer umrechnet (Formel: $miles \* 1.609). (3.5)

**Beispiele:**

- `calcTriangleArea(6, 4)` -> `12`
- `milesToKm(10)` -> `16.09`

**Antwortbereich:**

```php

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classifySpeed($kmh)`, die eine Geschwindigkeitsklassifizierung als Text liefert:

- `$kmh < 0` -> `ungueltig` (2.0)
- `$kmh <= 30` -> `langsam`
- `$kmh > 30` und `<= 100` -> `normal`
- `$kmh > 100` -> `schnell` (4.0)

**Beispiele:**

- `classifySpeed(25)` -> `langsam`
- `classifySpeed(120)` -> `schnell`

**Antwortbereich:**

```php

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyzeNumbers($numbers)`, die:

- das Minimum der Zahlen findet (3.0)
- die Anzahl positiver Zahlen zaehlt (3.5)

Rueckgabeformat als Array: `["minimum" => X, "positiveCount" => Y]`

**Beispiel:**

`analyzeNumbers([5, -3, 2, 0, -7])` -> `["minimum" => -7, "positiveCount" => 2]`

**Antwortbereich:**

```php

```
