# Grundlagen der Programmierung - Basics (Python)

**Dokumenttyp:** Aufgabenstellung + Musterlösung

**Punkte gesamt:** 25

**Hinweis für Lehrkräfte**

- Teilpunkte in 0.5-Schritten vergeben.
- Lösungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `vorname` und `alter` einliest (oder setzt) und eine Begrüßung ausgibt.

**Beispiel-Ausgabe:** `Hallo Lena, du bist 16 Jahre alt.`

Anforderungen:

- Variablen korrekt deklarieren und initialisieren (2.0)
- Eingabe einlesen oder simulieren (1.0)
- Ausgabeformat exakt wie oben (2.0)

**Musterlösung**

```python
vorname = "Lena"
alter = 16

print(f"Hallo {vorname}, du bist {alter} Jahre alt.")
```

### Punktbewertung

| Kriterium                                | Punkte  | Hinweise                                            |
| ---------------------------------------- | ------- | --------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | Zuweisungsoperator verwendet, Werte korrekt gesetzt |
| Eingabe einlesen oder simulieren         | 1.0     | `input()` oder direkte Wertzuweisung                |
| Ausgabeformat exakt                      | 2.0     | F-String oder `.format()` mit beiden Variablen      |
| **Summe Aufgabe A**                      | **5.0** |                                                     |

### Häufige Fehler
- Variablenname in Ausgabe passt nicht zum deklarierten Namen
- Werte werden gesetzt, aber nicht ausgegeben
- Ausgabeformat weicht von der geforderten Struktur ab


## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calc_rectangle_area(width, height)`, die die Fläche berechnet. (4.0)
2. Schreibe eine Funktion `celsius_to_fahrenheit(c)`, die Celsius in Fahrenheit umrechnet. (3.5)

**Beispiele:**

- `calc_rectangle_area(4, 3)` -> `12`
- `celsius_to_fahrenheit(0)` -> `32`

**Musterlösung**

```python
def calc_rectangle_area(width, height):
    return width * height


def celsius_to_fahrenheit(c):
    return (c * 9) / 5 + 32
```

### Punktbewertung

| Kriterium                                       | Punkte  | Hinweise                                                               |
| ----------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `calc_rectangle_area()` korrekt implementiert   | 4.0     | `def` Syntax korrekt, Parameter entgegen, Multiplikation durchgeführt |
| `celsius_to_fahrenheit()` korrekt implementiert | 3.5     | Formel $(c \times 9/5) + 32$ richtig umgesetzt, `return` korrekt       |
| **Summe Aufgabe B**                             | **7.5** |                                                                        |

### Häufige Fehler
- Formel falsch umgesetzt (Operatorreihenfolge oder Konstante fehlt)
- Funktion ohne `return` bzw. Rückgabe in falschem Format
- Parameter werden nicht verwendet oder vertauscht


## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classify_score(score)`, die eine Note als Text liefert:

- `score < 0` oder `score > 100` -> `ungueltig` (2.0)
- `score < 50` -> `nicht bestanden`
- `score >= 50` und `< 90` -> `bestanden`
- `score >= 90` -> `sehr gut` (4.0)

**Beispiele:**

- `classify_score(45)` -> `nicht bestanden`
- `classify_score(90)` -> `sehr gut`

**Musterlösung**

```python
def classify_score(score):
    if score < 0 or score > 100:
        return "ungueltig"
    if score < 50:
        return "nicht bestanden"
    if score < 90:
        return "bestanden"
    return "sehr gut"
```

### Punktbewertung

| Kriterium                         | Punkte  | Hinweise                                                 |
| --------------------------------- | ------- | -------------------------------------------------------- |
| Bereichs-Check (< 0 oder > 100)   | 2.0     | Ungültige Werte werden mit `or` erkannt                 |
| Fallunterscheidungen vollständig | 2.5     | Alle vier Fälle abgedeckt, `if-elif` oder verschachtelt |
| Rückgabewerte korrekt            | 1.5     | Strings entsprechen genau der Vorgabe                    |
| **Summe Aufgabe C**               | **6.0** |                                                          |

### Häufige Fehler
- Grenzwerte falsch gesetzt (z. B. `<` statt `<=`)
- Ungültigkeitsprüfung fehlt oder steht an falscher Stelle
- Ein oder mehrere Fälle werden nicht abgedeckt


## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyze_numbers(numbers)`, die:

- die Anzahl gerader Zahlen zählt (3.0)
- die Summe aller positiven Zahlen berechnet (3.5)

Rückgabeformat als Tuple: `(even_count, positive_sum)`

**Beispiel:**

`analyze_numbers([2, -3, 4, 0, 5])` -> `(3, 11)`

**Musterlösung**

```python
def analyze_numbers(numbers):
    even_count = 0
    positive_sum = 0

    for value in numbers:
        if value % 2 == 0:
            even_count += 1
        if value > 0:
            positive_sum += value

    return even_count, positive_sum
```

### Punktbewertung

| Kriterium              | Punkte  | Hinweise                                                  |
| ---------------------- | ------- | --------------------------------------------------------- |
| Schleife über Liste   | 1.5     | `for ... in` Syntax korrekt, iteriert über alle Elemente |
| Gerade Zahlen zählen  | 3.0     | Modulo `%` 2 == 0 korrekt, Counter wird mit `+=` erhöht   |
| Summe positiver Zahlen | 1.5     | Vergleich `> 0` korrekt, Summe wird mit `+=` aktualisiert |
| Rückgabeformat        | 0.5     | Tupel mit korrekten Werten                                |
| **Summe Aufgabe D**    | **6.5** |                                                           |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/Python_Grundlagen_Basics_Aufgabe_D.svg)

### Häufige Fehler
- Zähler/Summe wird nicht initialisiert oder falsch aktualisiert
- Bedingung für Filterung (z. B. gerade/positiv) ist fehlerhaft
- Rückgabe enthält falsche Schlüssel oder unvollständige Werte
