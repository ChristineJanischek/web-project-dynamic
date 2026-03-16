# Grundlagen der Programmierung - Basics (PHP) - Variante 3

**Name:** ****\*\*\*\*****\_\_\_\_****\*\*\*\***** **Datum:** **\*\***\_\_\_\_**\*\*** **Klasse:** \***\*\_\_\_\_\*\***

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

Schreibe ein kleines Programm, das `stadt` und `einwohner` einliest (oder setzt) und eine Stadtinformation ausgibt.

**Beispiel-Ausgabe:** `In Stuttgart leben 635911 Menschen.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```php

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `calcCubeVolume($side)`, die das Volumen eines Würfels berechnet (Formel: $side³). (4.0)
2. Schreibe eine Funktion `kmToMiles($km)`, die Kilometer in Meilen umrechnet (Formel: $km / 1.609). (3.5)

**Beispiele:**

- `calcCubeVolume(3)` -> `27`
- `kmToMiles(16.09)` -> `10` (ca.)

**Antwortbereich:**

```php

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `classifyTemperature($temp)`, die eine Temperaturbewertung als Text liefert:

- `$temp < -273` -> `ungueltig` (absoluter Nullpunkt) (2.0)
- `$temp < 0` -> `gefroren`
- `$temp >= 0` und `< 25` -> `angenehm`
- `$temp >= 25` -> `heiss` (4.0)

**Beispiele:**

- `classifyTemperature(-5)` -> `gefroren`
- `classifyTemperature(30)` -> `heiss`

**Antwortbereich:**

```php

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `analyzeNumbers($numbers)`, die:

- das Maximum der Zahlen findet (3.0)
- die Summe aller Zahlen berechnet (3.5)

Rückgabeformat als Array: `["maximum" => X, "sum" => Y]`

**Beispiel:**

`analyzeNumbers([7, -2, 9, 3, -1])` -> `["maximum" => 9, "sum" => 16]`

**Antwortbereich:**

```php

```
