# Version 4: Didaktischer Leitfaden für Lehrende

## 🎯 Pädagogisches Konzept

Diese Version folgt dem **Constructivist Learning Approach** mit **Scaffolding**:

1. **Aufgabe 0 (Erkundung):** Verständnis OHNE Programmierung
2. **Aufgabe 1 (View):** Erste sichtbare Erfolge (Formular sehen)
3. **Aufgabe 2 (Model):** Isolierte Geschäftslogik testen
4. **Aufgabe 3 (Controller):** Alles zusammenbauen

### Warum dieser Aufbau?

- **Progression:** Vom Verständnis zur Implementierung
- **Separated Concerns:** Model/View/Controller getrennt üben
- **Realismus:** Echte Architektur, die in der Industrie verwendet wird
- **Motivation:** Nach jeder Aufgabe funktionierende Features

---

## 📋 Aufgabenverteilung

### Aufgabe 0: Erkundungsauftrag (30-45 Min)

**Ziel:** Verstehen, wie die MVC-Architektur funktioniert

- Keine Programmierung nötig!
- Schüler lesen Code
- Beantwortung von Verständnisfragen
- Zeichnen von Ablauf-Diagrammen

**Bewertung:**

- ✅ Alle Fragen beantwortet (100%)
- ⚠️ Die meisten Fragen beantwortet (75%)
- ❌ Wenige Antworten (50%)

**Tipp für Lehrende:**

- Lest die Antworten durch - zeigen sie echtes Verständnis?
- Ungenaue Antworten korrigieren und zurückgeben
- Group Discussion: "Was ist ein Controller?" - laut diskutieren

---

### Aufgabe 1: View (Formular erstellen) (60-90 Min)

**Ziel:** HTML-Formular mit Gewicht & Größe

**Inhalte:**

- [ ] `<input type="number">` für Gewicht
- [ ] `<input type="number">` für Größe
- [ ] `<button type="submit">` für Senden
- [ ] `name`-Attribute korrekt
- [ ] `method="post"` im Formular

**Checkpoints:**

1. Formular wird angezeigt (PHP -S localhost:8000)
2. Felder sind sichtbar und beschriftet
3. Button funktioniert (sendet Daten, auch wenn noch keine Verarbeitung)

**Bewertung:**

- ✅ Formular vollständig & funktionstüchtig (100%)
- ⚠️ Formular funktioniert, aber kleine Fehler (80%)
- ❌ Formular unvollständig oder kaputt (50%)

**Tipps für Lehrende:**

- Zeigt den `name`-Attribut-Fehler häufig auf ("Wir brauchen die Namen später!")
- CSS-Styling ist optional, aber ermutigt es!
- Formular testen lassen mit echtem Browser

---

### Aufgabe 2: Model (Geschäftslogik) (90-120 Min)

**Ziel:** BMI berechnen und Kategorie bestimmen

**Inhalte:**

- [ ] `BmiRechner`-Klasse mit Konstruktor
- [ ] `setWerte($gewicht, $groesse)`
- [ ] `getBmi()` mit korrekter Formel
- [ ] `getKategorie()` mit if-else Logik
- [ ] Umrechnung cm → Meter
- [ ] Alle 4 Kategorien implementiert

**Math Check:**

```
Test: 70 kg, 175 cm
Erwartet: BMI ≈ 22.86, "Normalgewicht"

Test: 50 kg, 170 cm
Erwartet: BMI ≈ 17.30, "Untergewicht"

Test: 90 kg, 175 cm
Erwartet: BMI ≈ 29.39, "Übergewicht"

Test: 110 kg, 175 cm
Erwartet: BMI ≈ 35.92, "Adipositas"
```

**Checkpoints:**

1. Test-Datei `test_bmi.php` funktioniert
2. Alle 4 Test-Cases grün
3. Mathematik korrekt

**Bewertung:**

- ✅ Alles korrekt implementiert (100%)
- ⚠️ Logik funktioniert, aber kleine Fehler (80%)
- ⚠️ Nur 3 von 4 Kategorien (70%)
- ❌ Große Fehler (50%)

**Tipps für Lehrende:**

- **Fehler 1:** Größe wird nicht zu Metern umgerechnet → `$groesse * 0.01` zeigen
- **Fehler 2:** `pow()` nicht bekannt → Dokumentation zeigen
- **Fehler 3:** if-else Bedingungen falsch → Grenzwerte durchsprechen (18.5, 25, 30)
- **Trick:** Lest die Formeln laut vor ("Untergewicht ist kleiner als 18.5")

---

### Aufgabe 3: Controller (Ablauf verbinden) (90-120 Min)

**Ziel:** Formular verarbeiten + Model aufrufen + Ergebnis zeigen

**Inhalte:**

- [ ] `BmiRechnerController`-Klasse
- [ ] `handleRequest()` als Einstiegspunkt
- [ ] POST-Check mit `$_SERVER['REQUEST_METHOD']`
- [ ] Daten aus `$_POST['gewicht']` und `$_POST['groesse']`
- [ ] Model aufrufen: `setWerte()`
- [ ] Ergebnisse abrufen: `getBmi()`, `getKategorie()`
- [ ] View aufrufen: `renderErgebnis()`
- [ ] `index.php` aktualisiert mit require & neue Controller-Aufrufe

**Checkpoints:**

1. Seite lädt ohne Fehler
2. Formular wird angezeigt
3. Nach Eingabe und Senden: Ergebnis wird angezeigt
4. Nach jeder Berechnung: Formular bleibt sichtbar (zum nochmal berechnen)

**Bewertung:**

- ✅ Alles funktioniert end-to-end (100%)
- ⚠️ Berechnung funktioniert, aber Formular bleibt nicht (80%)
- ⚠️ Fehler beim Validieren von Eingaben (70%)
- ❌ App lädt nicht (50%)

**Tipps für Lehrende:**

- **Häufiger Fehler:** Formular wird nach Berechnung nicht erneut gezeigt
  - Lösung: `zeigeFormular()` am Ende von `verarbeiteBmi()` aufrufen
- **Häufiger Fehler:** `require` vergessen → Zeigt "Class not found"
  - Lösung: Oben in `index.php` die drei `require`-Zeilen einfügen
- **Häufiger Fehler:** `$_POST` ist leer
  - Lösung: Form `method="post"` und richtige `name`-Attribute checken
- **Bug-Tipp:** Mit `var_dump($_POST)` debuggen lassen

---

## 📊 Zeitbudget für Schulstunde (45 Min)

**Szenarien:**

### Szenario 1: Vier Stunden Programmierung (180 Min)

```
Woche 1:
- Tag 1 (45 Min): Aufgabe 0 Erkundung + 25% Aufgabe 1
- Tag 2 (45 Min): Aufgabe 1 fertig + 50% Aufgabe 2
- Tag 3 (45 Min): Aufgabe 2 fertig + 50% Aufgabe 3
- Tag 4 (45 Min): Aufgabe 3 fertig + Zeit zum Debuggen
```

### Szenario 2: Drei Stunden Programmierung (135 Min)

```
- Tag 1: Aufgabe 0 + Aufgabe 1 (2 Stunden Hausaufgabe)
- Tag 2: Aufgabe 2 (1,5 Stunden, Teil in HA)
- Tag 3: Aufgabe 3 + Fehlerbehebung
```

---

## 🧪 Automatisches Testen

**Für Lehrende:** So prüft ihr die Schüler-Arbeit schnell:

```bash
# Test Model
cd /path/to/version4
php test_bmi.php

# Ergebnis sollte so aussehen:
# Test 1 - Normalgewicht:
# Gewicht: 70 kg
# Größe: 175 cm
# BMI: 22.86
# Kategorie: Normalgewicht
```

---

## 🚀 Erweiterungen & Bonus-Aufgaben

Wenn Schüler früh fertig sind:

### 🌟 Einfach (15-30 Min)

- [ ] **Validierung:** Nur realistische Werte akzeptieren (0 < Gewicht < 500)
- [ ] **Schöner:** CSS mit Farben je nach Kategorie (Normalgewicht = grün)
- [ ] **Fehlerbehandlung:** Schöne Fehlermeldungen anzeigen

### 🌟🌟 Mittel (30-60 Min)

- [ ] **Geschichte:** Alle Berechnungen speichern und anzeigen
- [ ] **Einheiten:** Umschaltung zwischen kg/lbs und cm/inch
- [ ] **API:** JSON-API statt nur HTML

### 🌟🌟🌟 Komplex (60+ Min)

- [ ] **Datenbank:** Alle Berechnungen in SQLite speichern
- [ ] **Statistik:** Durchschnitts-BMI ausrechnen
- [ ] **Grafik:** Chart.js für BMI-Verteilung

---

## 🆘 Häufige Schüler-Probleme

| Problem                       | Diagnose                            | Lösung                                                 |
| ----------------------------- | ----------------------------------- | ------------------------------------------------------ |
| "Class not found"             | `require` vergessen                 | Zeige die 3 `require` Zeilen am Anfang von `index.php` |
| Formular wird nicht angezeigt | `zeigeFormular()` nicht aufgerufen  | Ruft die Methode in `handleRequest()` auf              |
| Ergebnis wird nicht angezeigt | `renderErgebnis()` nicht aufgerufen | Ruft die View-Methode in Controller auf                |
| BMI ist falsch                | Höhenumrechnung vergessen           | `$groesseInMetern = $groesse / 100`                    |
| $\_POST ist leer              | Formular-Namen falsch               | Checkt `name="gewicht"` und `name="groesse"`           |
| Server lädt ewig              | Endlosschleife in Controller        | Prüft die Logik in `handleRequest()`                   |

---

## 📖 Diskussionsfragen für den Unterricht

### Nach Aufgabe 0:

1. "Warum trennen wir Model, View und Controller?"
2. "Was würde passieren, wenn alles in einer Datei wäre?"
3. "Wo ist der Controller in eurem Browser?"

### Nach Aufgabe 1:

1. "Warum ist das `name`-Attribut wichtig?"
2. "Was passiert, wenn wir `POST` zu `GET` ändern?"

### Nach Aufgabe 2:

1. "Warum ist die Geschäftslogik nicht in HTML/PHP vermischt?"
2. "Wie würdet ihr einen anderen Rechner (z.B. Kalorienrechner) bauen?"

### Nach Aufgabe 3:

1. "Was macht der Controller wirklich?"
2. "Könnten wir ein anderes View nehmen (z.B. JSON statt HTML)?"
3. "Warum ist das besser als alles in einer index.php zu haben?"

---

## 💾 Bewertungsmatrix

| Kriterium                  | Punkte | Aufgabe    |
| -------------------------- | ------ | ---------- |
| Aufgabe 0 beantwortet      | 20     | Alle       |
| Aufgabe 1 funktioniert     | 20     | View       |
| Aufgabe 2 Mathematik       | 20     | Model      |
| Aufgabe 3 Ablauf           | 20     | Controller |
| Code-Qualität (Kommentare) | 10     | Alle       |
| **Gesamt**                 | **90** |            |
| Bonus: Extra-Feature       | +10    | Jede       |

---

## 📚 Bezug zu Lehrplan

Diese Version deckt ab:

✅ **Funktionales Programmieren:** Klassen mit Methoden  
✅ **Problemlösung:** BMI-Formel in Code übersetzen  
✅ **Architekturdenkweise:** Separation of Concerns  
✅ **Web-Grundlagen:** POST-Formulare, PHP-Basics  
✅ **Best Practices:** MVC, Code-Reuse, Testbarkeit

---

**Viel Erfolg beim Unterrichten!** 🎉

Fragen? Christine.Janischek@...
