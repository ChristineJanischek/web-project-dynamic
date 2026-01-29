# 📘 Aufgabe 0: Erkundungsauftrag - Die Vorlage verstehen

**Schwierigkeitsgrad:** ⭐ (Keine Programmierung nötig!)

**Ziel dieser Aufgabe:**  
Ihr werdet Detektive und erkundet die Projektstruktur. Ihr lest den Code, stellt Fragen und versteht, wie alles zusammenhängt. Das ist die Grundlage für alle weiteren Aufgaben!

---

## 🔍 Teil 1: Die Dateien erkunden

### 1.1 Schaut euch diese Dateien an:

**📋 Checklist:**

- [ ] Öffnet `index.php` in eurem Editor
- [ ] Lest den Code von oben bis unten
- [ ] Beantwortet: **Was sind die `include`-Befehle? Welche Dateien werden geladen?**

- [ ] Öffnet die Datei `layouts/main.php`
- [ ] Beantwortet: **Was steht hier? Wo kommt die Ausgabe hin?**

- [ ] Öffnet `models/RechnerModel.php`
- [ ] Beantwortet: **Was ist eine Klasse? Was machen `setWerte()` und `getWerte()`?**

- [ ] Öffnet `views/RechnerView.php`
- [ ] Beantwortet: **Welche Methoden gibt es hier? Was wird mit `echo` gemacht?**

- [ ] Öffnet `controllers/RechnerController.php`
- [ ] Beantwortet: **Welche Klassen werden hier verwendet? Was macht die `handleRequest()`-Methode?**

---

## 🧠 Teil 2: Verständnisfragen

Beantwortet diese Fragen auf einem Blatt Papier oder in einer Textdatei:

### Frage 1: Wer macht was?

```
Ergänzt die Sätze:

Das MODEL ist für __________ zuständig.
Das VIEW ist für __________ zuständig.
Der CONTROLLER ist für __________ zuständig.
```

**Hilfe:** Schaut euch die Klassennamen und Methodennamen an:

- Im Model: `setWerte()`, `getWerte()` - speichert und gibt Daten zurück
- Im View: `render...()` - zeigt HTML auf dem Bildschirm
- Im Controller: `handleRequest()`, `construct()` - verbindet Model und View

---

### Frage 2: Der Ablauf verstehen

Zeichnet ein Diagramm oder beschreibt: **Wie fließt die Information?**

```
Benutzer gibt Daten ein
        ↓
   ???????
        ↓
Ergebnis wird angezeigt
```

**Hilfe:** Welche Klasse bekommt die Daten zuerst? Welche speichert sie? Welche zeigt sie an?

---

### Frage 3: Die include-Befehle

Schaut auf `index.php`. Dort stehen Zeilen wie:

```php
<?php include 'layouts/head.php';?>
```

**Aufgabe:**

- [ ] Zählt: Wie viele `include`-Befehle gibt es?
- [ ] Listet auf: Welche Dateien werden eingebunden?
- [ ] Erklärt: Warum macht man das so?

---

### Frage 4: Der Weg des Formulars

Schaut euch die `RechnerView.php` an, Methode `renderForm()`:

```php
public function renderForm($action = '') {
    echo <<<HTML
<h2>Rechner Formular</h2>
<form method="post" action="{$action}">
    <label for="werte">Wert:</label>
    <input type="text" id="werte" name="werte" required>
    <button type="submit">Senden</button>
</form>
HTML;
}
```

**Aufgaben:**

- [ ] Was bedeutet `method="post"`?
- [ ] Was bedeutet `name="werte"`? Wo geht dieser Wert hin?
- [ ] Was macht `htmlspecialchars()`? (Sucht nach dieser Methode!)

---

### Frage 5: Die Klasse verstehen

Schauen wir uns `RechnerModel.php` genauer an:

```php
class RechnerModel {
    private $werte;

    public function setWerte($werte) {
        $this->werte = $werte;
    }

    public function getWerte() {
        return $this->werte;
    }
}
```

**Aufgaben:**

- [ ] Was ist `private`? Was ist `public`?
- [ ] Was ist `$this`?
- [ ] Wie funktioniert das Speichern und Abrufen?

---

## 🎯 Teil 3: Die große Frage

Nachdem ihr alles erforscht habt, beantwortet:

### "Was passiert, wenn ein Schüler auf den 'Senden'-Button klickt?"

Schreibt einen Absatz (5-8 Sätze) mit euren Worten:

```
Wenn der Benutzer auf "Senden" klickt...

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________
```

---

## ✅ Checkliste zum Abhaken

- [ ] Ich habe alle fünf Dateien gelesen
- [ ] Ich habe die Verständnisfragen beantwortet
- [ ] Ich kenne die Rollen von Model, View, Controller
- [ ] Ich verstehe, wie die `include`-Befehle funktionieren
- [ ] Ich habe erklärt, was mit einem Formular passiert
- [ ] Ich habe Fragen mitgeschrieben, die ich noch habe

---

## 💡 Tipps für die Erkundung

1. **Lest den Code laut vor** - So versteht ihr besser!
2. **Schreibt Kommentare** - Erklärt euch selbst, was jede Zeile tut
3. **Zeichnet Pfeile** - Welche Datei ruft welche auf?
4. **Fragt euch** - "Warum ist das so gemacht?"
5. **Vergleicht mit 01_PHP und 02_PHP** - Ist das anders?

---

## 🚀 Nächste Schritte

Wenn ihr diese Erkundung fertig habt, seid ihr bereit für **[Aufgabe 1: Das Formular erstellen](AUFGABE_1_VIEW.md)**!

Dort werden wir den ersten echten Code schreiben und ein HTML-Formular für den BMI-Rechner bauen. 🎉

---

**Fragen?** Redet mit eurem Lehrer oder einer Lehrerin!
