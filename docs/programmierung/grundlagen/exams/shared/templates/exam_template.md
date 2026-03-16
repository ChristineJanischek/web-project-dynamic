# Grundlagen der Programmierung - Basics (SPRACHE)

<!-- Konfigurierbare Werte (hier mit Standardwerten):
     SPRACHE: JavaScript, PHP, Python
     Bearbeitungszeit: 45 Minuten
     Gesamtpunkte: 25
     Aufgabe A: 5.0 Punkte
     Aufgabe B: 7.5 Punkte
     Aufgabe C: 6.0 Punkte
     Aufgabe D: 6.5 Punkte
-->

**Name:**

---

**Datum:** **\*\***\_\_\_\_**\*\*** **Klasse:** **\*\***\_\_\_\_**\*\***

**Sprache:** SPRACHE

**Bearbeitungszeit:** 45 Minuten

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

Schreibe ein kleines Programm, das `vorname` und `alter` einliest (oder setzt) und eine Begrüßung ausgibt.

**Beispiel-Ausgabe:** `Hallo Lena, du bist 16 Jahre alt.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Antwortbereich:**

```SPRACHE

```

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

1. Schreibe eine Funktion `FUNC_RECT`, die die Fläche berechnet. (4.0)
2. Schreibe eine Funktion `FUNC_TEMP`, die Celsius in Fahrenheit umrechnet. (3.5)

**Beispiele:**

- `FUNC_RECT(4, 3)` -> `12`
- `FUNC_TEMP(0)` -> `32`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

Schreibe eine Funktion `FUNC_SCORE`, die eine Note als Text liefert:

- `score < 0` oder `score > 100` -> `ungueltig` (2.0)
- `score < 50` -> `nicht bestanden`
- `score >= 50` und `< 90` -> `bestanden`
- `score >= 90` -> `sehr gut` (4.0)

**Beispiele:**

- `FUNC_SCORE(45)` -> `nicht bestanden`
- `FUNC_SCORE(90)` -> `sehr gut`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

Schreibe eine Funktion `FUNC_ANALYZE`, die:

- die Anzahl gerader Zahlen zählt (3.0)
- die Summe aller positiven Zahlen berechnet (3.5)

Rückgabeformat an Sprache anpassen.

**Beispiel:**

`FUNC_ANALYZE([2, -3, 4, 0, 5])` -> `(3, 11)`

**Antwortbereich:**

```SPRACHE

```
