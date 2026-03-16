# Grundlagen der Programmierung - Basics (PHP) - Variante 6

**Name:** \***\*\*\*\*\*\*\***\_\_\_\_\***\*\*\*\*\*\*\*** **Datum:** **\*\***\_\_\_\_**\*\*** **Klasse:** \*\*\*\*\*\_\_\_\_\*\*\*

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

Schreibe ein kleines Programm, das `eventName` und `teilnehmerzahl` einliest (oder setzt) und eine Eventmeldung ausgibt.

**Beispiel-Ausgabe:** `Event: Hackathon, Teilnehmende: 42`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```php

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calcRemainingBudget($budget, $spent)`, die das Restbudget berechnet. (4.0)
2. Schreibe eine Funktion `metersToCentimeters($meters)`, die Meter in Zentimeter umrechnet. (3.5)

**Beispiele:**

- `calcRemainingBudget(1200, 450)` -> `750`
- `metersToCentimeters(1.75)` -> `175`

**Antwortbereich:**

```php

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classifyBattery($percent)`, die den Akkustand als Text klassifiziert:

- `$percent < 0` oder `$percent > 100` -> `ungueltig` (2.0)
- `$percent < 20` -> `niedrig`
- `$percent >= 20` und `< 80` -> `mittel`
- `$percent >= 80` -> `hoch` (4.0)

**Beispiele:**

- `classifyBattery(10)` -> `niedrig`
- `classifyBattery(85)` -> `hoch`

**Antwortbereich:**

```php

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyzeMeasurements($values)`, die:

- die Anzahl von Werten im Bereich `1` bis `9` (inklusive) zählt (3.0)
- die Summe der Absolutwerte aller Elemente berechnet (3.5)

Rückgabeformat als Array: `["singleDigitPositiveCount" => X, "absoluteSum" => Y]`

**Beispiel:**

`analyzeMeasurements([-3, 0, 4, 12, 9])` -> `["singleDigitPositiveCount" => 2, "absoluteSum" => 28]`

**Antwortbereich:**

```php

```
