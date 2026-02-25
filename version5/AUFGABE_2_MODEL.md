# 🧮 Aufgabe 2: Die Geschäftslogik (Model) implementieren

**Schwierigkeitsgrad:** ⭐⭐⭐

**Ziel:**
Ihr implementiert die Notenlogik im Model mit Durchschnittsberechnung und Nachhilfe-Prüfung.

---

## 📋 Aufgabe

Bearbeitet `models/RechnerModel.php` und implementiert eine Klasse `NotenRechner`.

Die Klasse soll können:

1. Noten speichern (`bwl`, `mathe`, `deutsch`, `englisch`)
2. Durchschnitt berechnen
3. Mit `pruefeNachhilfe()` prüfen, in welchen Fächern Nachhilfe nötig ist

---

## 🎯 Fachregeln

- Gültige Noten: `1.0` bis `6.0`
- Nachhilfe in einem Fach, wenn `note > 4.0`
- Durchschnitt:

```text
(bwl + mathe + deutsch + englisch) / 4
```

---

## 💻 Strukturvorschlag

```php
class NotenRechner {
    private $noten = [];
    private $durchschnitt = 0.0;

    public function setNoten($bwl, $mathe, $deutsch, $englisch) {
        // speichern + berechnen
    }

    public function getDurchschnitt() {
        return $this->durchschnitt;
    }

    public function pruefeNachhilfe() {
        // liefert Array mit Fächern zurück, die > 4.0 sind
    }
}
```

---

## ✅ Checkliste

- [ ] Klasse `NotenRechner` erstellt
- [ ] Noten werden gespeichert
- [ ] Durchschnitt korrekt berechnet
- [ ] Methode `pruefeNachhilfe()` implementiert
- [ ] Verzweigungen (`if/elseif` oder `if`) sinnvoll eingesetzt

---

## 🔁 Reflexion (Transfer)

Vergleicht mit Version 4:

- Welche Methodenidee wurde direkt übertragen?
- Welche Bedingungen sind neu (Branching/Nachhilfe)?

---

## 🚀 Nächster Schritt

Weiter mit **[Aufgabe 3: Controller verbinden](AUFGABE_3_CONTROLLER.md)**.
