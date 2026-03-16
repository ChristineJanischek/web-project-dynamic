# Grundlagen der Programmierung - Exam Datenstrukturen (SPRACHE)

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

- A Arrays + Listen: Zugriff, Modifikation: 5.0 Punkte
- B Datenstruktur-Operationen (Laenge, Einfuegen, Loeschen): 7.5 Punkte
- C Objekte / Dictionaries: Zugriff und Modifikation: 6.0 Punkte
- D Komplexe Datenstrukturen (Arrays von Objekten): 6.5 Punkte

**Bewertungsschlüssel (linear)**

Punkte werden linear in Prozent umgerechnet: $prozent = (punkte / 25) * 100$.
Teilpunkte sind zulässig (Rundung in 0.5-Schritten).

---

## Aufgabe A - Arrays / Listen (5.0 Punkte)

Schreibe eine Funktion `PROCESS_LIST(items)`, die:

1. Das erste Element ausliest und zurückgibt. (2.0)
2. Das letzte Element ausliest und zurückgibt. (2.0)
3. Ein Element an Index 1 einfuegt. (1.0)

**Beispiel:**

```
items = [10, 20, 30]
first = 10, last = 30
Nach Einfuegen von 99 an Index 1: [10, 99, 20, 30]
```

**Antwortbereich:**

```SPRACHE

```

## Aufgabe B - Array-Operationen (7.5 Punkte)

Schreibe Funktionen für folgende Operationen:

1. `GET_LENGTH(arr)` gibt die Laenge zurück. (2.0)
2. `APPEND(arr, value)` haengt ein Element an und gibt das Array zurück. (2.5)
3. `REMOVE_AT(arr, index)` entfernt ein Element an `index`. (3.0)

**Beispiele:**

- `GET_LENGTH([1, 2, 3])` -> `3`
- `APPEND([1], 2)` -> `[1, 2]`
- `REMOVE_AT([1, 2, 3], 1)` -> `[1, 3]`

**Antwortbereich:**

```SPRACHE

```

## Aufgabe C - Objekte / Dictionaries (6.0 Punkte)

Schreibe eine Funktion `CREATE_PERSON(name, age, city)`, die:

1. Ein Objekt/Dictionary mit den Feldern erstellt und zurückgibt. (3.0)
2. Ein Feld ausliest (z. B. `person['name']`). (1.5)
3. Ein Feld aendert (z. B. `person['age'] = 20`). (1.5)

**Beispiel:**

```
person = CREATE_PERSON("Alice", 25, "Berlin")
person['age'] = 26  // Aendern
```

**Antwortbereich:**

```SPRACHE

```

## Aufgabe D - Komplexe Strukturen (6.5 Punkte)

Schreibe eine Funktion `CREATE_TEAM(members_list)`, die:

- Ein Array von Objekten/Dictionaries erstellt
- Jede Person hat: `name`, `role`, `salary`
- Rückgabe: Array mit allen Personen

Dann schreibe eine Funktion `GET_SALARIES(team)`, die:

- Alle Gehaelter aus dem Team-Array sammelt
- Eine Liste/Array aller Gehaelter zurückgibt

**Beispiel:**

```
members = [
  {name: "Bob", role: "Dev", salary: 3000},
  {name: "Carol", role: "Lead", salary: 4000}
]
team = CREATE_TEAM(members)
salaries = GET_SALARIES(team)  -> [3000, 4000]
```

**Antwortbereich:**

```SPRACHE

```
