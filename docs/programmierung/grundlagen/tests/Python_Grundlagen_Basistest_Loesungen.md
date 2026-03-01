# Grundlagen der Programmierung - Basistest (Python)

**Dokumenttyp:** Aufgabenstellung + Musterloesung

**Punkte gesamt:** 25

**Hinweis fuer Lehrkraefte**

- Teilpunkte in 0.5-Schritten vergeben.
- Loesungen sind knapp gehalten und entsprechen dem erwarteten Niveau.

---

## Aufgabe A - Variablen + Ein/Ausgabe (5.0 Punkte)

**Aufgabenstellung**

Schreibe ein kleines Programm, das `vorname` und `alter` einliest (oder setzt) und eine Begruessung ausgibt.

**Musterloesung**

```python
vorname = "Lena"
alter = 16

print(f"Hallo {vorname}, du bist {alter} Jahre alt.")
```

**Bewertungsrubrik**

| Kriterium                                | Punkte  | Hinweise                                            |
| ---------------------------------------- | ------- | --------------------------------------------------- |
| Variablen deklarieren und initialisieren | 2.0     | Zuweisungsoperator verwendet, Werte korrekt gesetzt |
| Eingabe einlesen oder simulieren         | 1.0     | `input()` oder direkte Wertzuweisung                |
| Ausgabeformat exakt                      | 2.0     | F-String oder `.format()` mit beiden Variablen      |
| **Summe Aufgabe A**                      | **5.0** |                                                     |

## Aufgabe B - Funktionen mit kleinen Berechnungen (7.5 Punkte)

**Aufgabenstellung**

1. Schreibe eine Funktion `calc_rectangle_area(width, height)`, die die Flaeche berechnet.
2. Schreibe eine Funktion `celsius_to_fahrenheit(c)`, die Celsius in Fahrenheit umrechnet.

**Musterloesung**

```python
def calc_rectangle_area(width, height):
    return width * height


def celsius_to_fahrenheit(c):
    return (c * 9) / 5 + 32
```

**Bewertungsrubrik**

| Kriterium                                       | Punkte  | Hinweise                                                               |
| ----------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| `calc_rectangle_area()` korrekt implementiert   | 4.0     | `def` Syntax korrekt, Parameter entgegen, Multiplikation durchgefuehrt |
| `celsius_to_fahrenheit()` korrekt implementiert | 3.5     | Formel $(c \times 9/5) + 32$ richtig umgesetzt, `return` korrekt       |
| **Summe Aufgabe B**                             | **7.5** |                                                                        |

## Aufgabe C - Funktionen mit Fallunterscheidungen (6.0 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `classify_score(score)`, die eine Note als Text liefert.

**Musterloesung**

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

**Bewertungsrubrik**

| Kriterium                         | Punkte  | Hinweise                                                 |
| --------------------------------- | ------- | -------------------------------------------------------- |
| Bereichs-Check (< 0 oder > 100)   | 2.0     | Ungueltige Werte werden mit `or` erkannt                 |
| Fallunterscheidungen vollstaendig | 2.5     | Alle vier Faelle abgedeckt, `if-elif` oder verschachtelt |
| Rueckgabewerte korrekt            | 1.5     | Strings entsprechen genau der Vorgabe                    |
| **Summe Aufgabe C**               | **6.0** |                                                          |

## Aufgabe D - Funktionen mit Schleifen + Datenstrukturen (6.5 Punkte)

**Aufgabenstellung**

Schreibe eine Funktion `analyze_numbers(numbers)`, die die Anzahl gerader Zahlen zaehlt und die Summe aller positiven Zahlen berechnet.

**Musterloesung**

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

**Bewertungsrubrik**

| Kriterium              | Punkte  | Hinweise                                                  |
| ---------------------- | ------- | --------------------------------------------------------- |
| Schleife ueber Liste   | 1.5     | `for ... in` Syntax korrekt, iteriert ueber alle Elemente |
| Gerade Zahlen zaehlen  | 3.0     | Modulo `%` 2 == 0 korrekt, Counter wird mit `+=` erhoet   |
| Summe positiver Zahlen | 1.5     | Vergleich `> 0` korrekt, Summe wird mit `+=` aktualisiert |
| Rueckgabeformat        | 0.5     | Tupel mit korrekten Werten                                |
| **Summe Aufgabe D**    | **6.5** |                                                           |

**Struktogramm (Platzhalter)**

![Struktogramm Aufgabe D](structogramme/Python_Grundlagen_Basistest_Aufgabe_D.svg)
