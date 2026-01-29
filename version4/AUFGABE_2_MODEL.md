# 🧮 Aufgabe 2: Die Geschäftslogik (Model) implementieren

**Schwierigkeitsgrad:** ⭐⭐⭐ (PHP-Klassen schreiben)

**Ziel dieser Aufgabe:**  
Ihr programmiert die **BMI-Berechnung**! Die Logik gehört ins Model. Das ist das Fachkonzept. 📐

**Voraussetzung:** [Aufgabe 1](AUFGABE_1_VIEW.md) (Formular) muss fertig sein.

---

## 📋 Aufgabe: Die BmiRechner-Klasse programmieren

Ihr werdet die Datei `models/RechnerModel.php` umbauen. Statt die alte `RechnerModel`-Klasse zu nutzen, schreiben wir eine spezialisierte **`BmiRechner`-Klasse**.

### ✅ Das muss die `BmiRechner`-Klasse können:

1. **Speichern:** Gewicht und Größe speichern
2. **Berechnen:** BMI nach der Formel: `BMI = Gewicht / (Größe in Metern)²`
3. **Kategorie:** Die Gewichtskategorie bestimmen
4. **Abrufen:** Alle Werte zurückgeben

---

## 🎯 Die BMI-Formel

```
BMI = Gewicht (kg) / (Größe in Metern)²
```

**WICHTIG:** Die Größe kommt vom Formular in **Zentimetern** (cm)!

Also müsst ihr umrechnen: **Meter = cm / 100**

**Beispiel:**

```
Gewicht: 70 kg
Größe: 175 cm = 1,75 m

BMI = 70 / (1,75 × 1,75)
BMI = 70 / 3,0625
BMI ≈ 22,86
```

---

## 📊 Die Gewichtskategorien

Nutzt diese Tabelle:

| BMI             | Kategorie     |
| --------------- | ------------- |
| BMI < 18,5      | Untergewicht  |
| 18,5 ≤ BMI < 25 | Normalgewicht |
| 25 ≤ BMI < 30   | Übergewicht   |
| BMI ≥ 30        | Adipositas    |

---

## 💻 Die Vorlage für eure `BmiRechner`-Klasse

Ersetzt den Inhalt von `models/RechnerModel.php` mit diesem Code:

```php
<?php

class BmiRechner {

    // Private Eigenschaften (nur diese Klasse kann sie ändern)
    private $gewicht;      // in Kilogramm (kg)
    private $groesse;      // in Zentimetern (cm)
    private $bmi;          // Das Ergebnis
    private $kategorie;    // z.B. "Normalgewicht"

    /**
     * Konstruktor - wird aufgerufen, wenn die Klasse erstellt wird
     * z.B.: $rechner = new BmiRechner(70, 175);
     */
    public function __construct($gewicht = null, $groesse = null) {
        $this->gewicht = $gewicht;
        $this->groesse = $groesse;
        if ($gewicht && $groesse) {
            $this->berechne();
        }
    }

    /**
     * Speichert Gewicht und Größe
     */
    public function setWerte($gewicht, $groesse) {
        $this->gewicht = $gewicht;
        $this->groesse = $groesse;
        $this->berechne();
    }

    /**
     * Gibt Gewicht zurück
     */
    public function getGewicht() {
        return $this->gewicht;
    }

    /**
     * Gibt Größe zurück
     */
    public function getGroesse() {
        return $this->groesse;
    }

    /**
     * Gibt den berechneten BMI zurück
     */
    public function getBmi() {
        return round($this->bmi, 2);  // Runden auf 2 Dezimalen
    }

    /**
     * Gibt die Gewichtskategorie zurück
     */
    public function getKategorie() {
        return $this->kategorie;
    }

    /**
     * DIESE METHODE MÜSST IHR SCHREIBEN!
     *
     * Berechnet den BMI und die Kategorie.
     *
     * Schritte:
     * 1. Größe von cm zu Metern umrechnen (cm / 100)
     * 2. BMI berechnen: Gewicht / (Größe in Metern)²
     * 3. Kategorie bestimmen
     */
    private function berechne() {
        // TODO: Hier kommt euer Code!
        // Hinweis: pow($zahl, 2) berechnet das Quadrat

        // Beispiel (löschen):
        // $groesseInMetern = $this->groesse / 100;
        // $this->bmi = $this->gewicht / pow($groesseInMetern, 2);
        // ...
    }

    /**
     * DIESE METHODE MÜSST IHR AUCH SCHREIBEN!
     *
     * Bestimmt die Kategorie basierend auf BMI:
     * - BMI < 18,5: "Untergewicht"
     * - 18,5 ≤ BMI < 25: "Normalgewicht"
     * - 25 ≤ BMI < 30: "Übergewicht"
     * - BMI ≥ 30: "Adipositas"
     */
    private function bestimmeKategorie() {
        // TODO: Hier kommt euer Code mit if-else oder switch!
    }
}
```

---

## 📝 Das müsst ihr programmieren:

### Schritt 1: Die `berechne()`-Methode

```php
private function berechne() {
    // Größe von cm zu Metern umrechnen
    // ...

    // BMI berechnen
    // ...

    // Kategorie bestimmen
    // ...
}
```

**Hilfe:**

- `pow($zahl, 2)` = `$zahl²`
- Beispiel: `pow(1.75, 2)` = `3.0625`
- `round($zahl, 2)` = Rundet auf 2 Dezimalen

### Schritt 2: Die `bestimmeKategorie()`-Methode

```php
private function bestimmeKategorie() {
    if ($this->bmi < 18.5) {
        $this->kategorie = "Untergewicht";
    } else if ($this->bmi < 25) {
        // TODO: Normalgewicht
    } else if ($this->bmi < 30) {
        // TODO: Übergewicht
    } else {
        // TODO: Adipositas
    }
}
```

---

## ✅ Checkliste für die Implementierung

- [ ] Ich habe `berechne()` programmiert
- [ ] Ich habe `bestimmeKategorie()` programmiert
- [ ] Die Größe wird von cm zu Metern umgerechnet
- [ ] Die BMI-Formel ist richtig
- [ ] Alle vier Kategorien sind implementiert
- [ ] `getBmi()` gibt das Ergebnis mit 2 Dezimalen zurück

---

## 🧪 So testet ihr die Klasse

Erstellt eine Test-Datei `test_bmi.php` im `version4`-Verzeichnis:

```php
<?php
require 'models/RechnerModel.php';

// Test 1: Normalgewicht
$rechner = new BmiRechner(70, 175);
echo "Test 1 - Normalgewicht:<br>";
echo "Gewicht: " . $rechner->getGewicht() . " kg<br>";
echo "Größe: " . $rechner->getGroesse() . " cm<br>";
echo "BMI: " . $rechner->getBmi() . "<br>";
echo "Kategorie: " . $rechner->getKategorie() . "<br><br>";

// Test 2: Untergewicht
$rechner2 = new BmiRechner(50, 170);
echo "Test 2 - Untergewicht:<br>";
echo "BMI: " . $rechner2->getBmi() . "<br>";
echo "Kategorie: " . $rechner2->getKategorie() . "<br><br>";

// Test 3: Übergewicht
$rechner3 = new BmiRechner(90, 175);
echo "Test 3 - Übergewicht:<br>";
echo "BMI: " . $rechner3->getBmi() . "<br>";
echo "Kategorie: " . $rechner3->getKategorie() . "<br><br>";

// Test 4: Adipositas
$rechner4 = new BmiRechner(110, 175);
echo "Test 4 - Adipositas:<br>";
echo "BMI: " . $rechner4->getBmi() . "<br>";
echo "Kategorie: " . $rechner4->getKategorie() . "<br>";
?>
```

**Dann im Terminal testen:**

```bash
cd /workspaces/web-project-dynamic/version4
php test_bmi.php
```

**Erwartete Ausgabe:**

```
Test 1 - Normalgewicht:
Gewicht: 70 kg
Größe: 175 cm
BMI: 22.86
Kategorie: Normalgewicht

Test 2 - Untergewicht:
BMI: 17.30
Kategorie: Untergewicht
...
```

---

## ❓ Häufige Fehler

| Problem                         | Lösung                                         |
| ------------------------------- | ---------------------------------------------- |
| `Undefined variable: kategorie` | Ihr habt `$this->kategorie` nicht gesetzt      |
| BMI ist negativ oder 0          | Größe wird nicht richtig zu Metern umgerechnet |
| Kategorien stimmen nicht        | Schaut die if-Bedingungen nochmal an           |
| `pow()` funktioniert nicht      | Nutzt `pow($zahl, 2)` oder `$zahl ** 2`        |

---

## 💡 Tipps

- **Öfter testen:** Nach jeder Methode die Test-Datei laufen lassen
- **Dezimalpunkte:** Nutzt `.` nicht `,` für Dezimalzahlen in PHP
- **Kommentare:** Schreibt Kommentare zu eurer Logik
- **Kopf rechnen:** BMI von 22-24 = Normal, 18-20 = Schlank, 28-30 = Dick

---

## 🚀 Nächste Schritte

Wenn das Model funktioniert, seid ihr bereit für **[Aufgabe 3: Den Controller](AUFGABE_3_CONTROLLER.md)**!

Dort verbindet ihr Model + View und die ganze App funktioniert! 🎉

---

**Fragen?** Fragt euren Lehrer/eure Lehrerin! 💬
