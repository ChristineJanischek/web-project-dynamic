# Grundlagen der Programmierung - Basics (PHP) - Variante 5

**Name:** \***\*\*\*\*\*\*\***\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\***\*\*\*\*\*\*\*** **Datum:** **\*\***\_\_\_\_\_\_\_\_\_\_\_\_\_**\*\*** **Klasse:** \*\*\*\*\*\_\_\_\_\_\_\_\_\*\*\*

**Sprache:** PHP

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

Schreibe ein kleines Programm, das `film` und `dauerMinuten` einliest (oder setzt) und eine Filminformation ausgibt.

**Beispiel-Ausgabe:** `Film: Inception, Dauer: 148 Minuten`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```php

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calcAverageThree($a, $b, $c)`, die den Durchschnitt von drei Zahlen berechnet. (4.0)
2. Schreibe eine Funktion `minutesToSeconds($minutes)`, die Minuten in Sekunden umrechnet. (3.5)

**Beispiele:**

- `calcAverageThree(2, 4, 6)` -> `4`
- `minutesToSeconds(3)` -> `180`

**Antwortbereich:**

```php

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classifyHumidity($humidity)`, die Luftfeuchtigkeit als Text klassifiziert:

- `$humidity < 0` oder `$humidity > 100` -> `ungueltig` (2.0)
- `$humidity < 30` -> `trocken`
- `$humidity >= 30` und `< 60` -> `normal`
- `$humidity >= 60` -> `feucht` (4.0)

**Beispiele:**

- `classifyHumidity(25)` -> `trocken`
- `classifyHumidity(72)` -> `feucht`

**Antwortbereich:**

```php

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyzeValues($values)`, die:

- die Anzahl von Werten zählt, die durch 3 teilbar sind (3.0)
- den Durchschnitt aller nicht-negativen Werte berechnet (3.5)

Wenn es keine nicht-negativen Werte gibt, soll der Durchschnitt `0` sein.

Rückgabeformat als Array: `["divByThreeCount" => X, "nonNegativeAverage" => Y]`

**Beispiel:**

`analyzeValues([3, -4, 6, 1, -2])` -> `["divByThreeCount" => 2, "nonNegativeAverage" => 3.3333...]`

**Antwortbereich:**

```php

```
