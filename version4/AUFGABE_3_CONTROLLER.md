# 🎮 Aufgabe 3: Den Controller verbinden (alles funktioniert!)

**Schwierigkeitsgrad:** ⭐⭐⭐⭐ (Das meiste zusammensetzen)

**Ziel dieser Aufgabe:**  
Der Controller verbindet Model und View! Wenn der Benutzer das Formular absende wird das Model berechnet und das Ergebnis angezeigt. **Die App funktioniert!** 🎉

**Voraussetzung:** [Aufgabe 2](AUFGABE_2_MODEL.md) (Model) muss fertig sein.

---

## 🎯 Überblick: Der Ablauf

```
1. Benutzer füllt Formular aus
   ↓
2. Klickt "Berechnen"
   ↓
3. Controller bekommt Daten vom Formular ($_POST['gewicht'], $_POST['groesse'])
   ↓
4. Controller ruft das Model auf: new BmiRechner($gewicht, $groesse)
   ↓
5. Model berechnet BMI
   ↓
6. Controller ruft View auf: $view->zeigeErgebnis($bmi, $kategorie)
   ↓
7. View zeigt das Ergebnis an (HTML)
```

---

## 📋 Aufgabe: Den Controller programmieren

Öffnet die Datei: `controllers/RechnerController.php`

Ihr werdet diese Klasse umbauen, damit sie:

1. Das Formular zeigt
2. Formular-Eingaben verarbeitet
3. Das Model aufruft
4. Das Ergebnis mit der View anzeigt

---

## 💻 Die neue BmiRechnerController-Klasse

Ersetzt den Inhalt von `controllers/RechnerController.php`:

```php
<?php

class BmiRechnerController {

    private $model;
    private $view;

    /**
     * Konstruktor
     * Wird aufgerufen: $controller = new BmiRechnerController($model, $view);
     */
    public function __construct($model, $view) {
        $this->model = $model;
        $this->view = $view;
    }

    /**
     * HAUPTMETHODE: Verarbeitet die Anfrage
     *
     * 1. Wenn der Benutzer das Formular absendet (POST), berechne
     * 2. Ansonsten zeige nur das Formular
     */
    public function handleRequest() {
        // TODO: Ist es ein POST-Request? (Formular wurde abgesendet?)
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // TODO: Das Formular wurde abgesendet!
            // Hole die Werte aus $_POST
            // Rufe das Model auf
            // Zeige das Ergebnis
            $this->verarbeiteBmi();
        } else {
            // TODO: Erstes Laden - Zeige nur das Formular
            $this->zeigeFormular();
        }
    }

    /**
     * PRIVATE METHODE: Zeigt nur das Formular
     * Wird aufgerufen, wenn die Seite das erste Mal geladen wird
     */
    private function zeigeFormular() {
        // TODO: Ruft die View auf, um das Formular zu zeigen
        // Hinweis: Die View hat eine Methode renderForm()
    }

    /**
     * PRIVATE METHODE: Verarbeitet die BMI-Berechnung
     * Wird aufgerufen, wenn der Benutzer das Formular absendet
     *
     * Schritte:
     * 1. Gewicht und Größe aus $_POST holen
     * 2. Model setzen: $this->model->setWerte($gewicht, $groesse)
     * 3. Werte vom Model abrufen: getBmi(), getKategorie()
     * 4. View aufrufen: $this->view->renderErgebnis(...)
     */
    private function verarbeiteBmi() {
        // TODO: Hier kommt euer Code!

        // Beispiel (löschen):
        // $gewicht = $_POST['gewicht'] ?? null;
        // ...
    }
}
```

---

## 📝 Das müsst ihr programmieren:

### Schritt 1: Die `zeigeFormular()`-Methode

Diese Methode soll das Formular anzeigen. Die `RechnerView` hat dafür eine Methode:

```php
private function zeigeFormular() {
    // Die RechnerView hat die Methode renderForm()
    // Ihr müsst sie aufrufen mit: $this->view->...

    // Die Vorlage zeigt nur das Formular:
    // <h2>Rechner Formular</h2>
    // <form>...</form>
}
```

**Hinweis:** Schaut in `views/RechnerView.php`, welche Methoden es gibt!

### Schritt 2: Die `verarbeiteBmi()`-Methode

Diese Methode wird aufgerufen, wenn der Benutzer das Formular absendet:

```php
private function verarbeiteBmi() {
    // 1. Werte aus dem Formular holen
    $gewicht = $_POST['gewicht'] ?? null;
    $groesse = $_POST['groesse'] ?? null;

    // 2. Prüfe: Sind die Werte valid?
    if (!$gewicht || !$groesse) {
        echo "Fehler: Beide Felder sind erforderlich!";
        $this->zeigeFormular();
        return;
    }

    // 3. Model aufrufen (Werte speichern und berechnen)
    $this->model->setWerte($gewicht, $groesse);

    // 4. Ergebnisse abrufen
    $bmi = $this->model->getBmi();
    $kategorie = $this->model->getKategorie();

    // 5. View aufrufen - Ergebnis zeigen
    // TODO: Welche Methode hat die View?
    // Hinweis: Schaut in RechnerView.php!

    // 6. Formular erneut zeigen (zum nochmal berechnen)
    $this->zeigeFormular();
}
```

---

## 🤔 Das müsst ihr wissen: `$_SERVER['REQUEST_METHOD']`

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Das Formular wurde abgesendet (Button gedrückt)
} else {
    // Erste Anfrage - Seite geladen
}
```

---

## 🤔 Das müsst ihr wissen: `$_POST`

Wenn das Formular so aussieht:

```html
<input type="text" name="gewicht" /> <input type="text" name="groesse" />
```

Dann bekommt ihr die Werte mit:

```php
$_POST['gewicht']  // Der eingegebene Wert
$_POST['groesse']  // Der eingegebene Wert
```

---

## ⚠️ Das musst ihr auch ändern: `index.php`

Öffnet `index.php` und findet diese Zeilen:

```php
<?php include 'layouts/main.php';?>
```

Ihr müsst die **main.php** durch euren Controller ersetzen:

```php
<?php
    require 'models/RechnerModel.php';
    require 'controllers/RechnerController.php';
    require 'views/RechnerView.php';

    // Objekte erstellen
    $model = new BmiRechner();
    $view = new RechnerView();
    $controller = new BmiRechnerController($model, $view);

    // Controller aufrufen
    $controller->handleRequest();
?>
```

**WICHTIG:** Das geht in den `<main>`-Tag, nicht in `<head>`!

```php
<main>
    <?php
        require 'models/RechnerModel.php';
        require 'controllers/RechnerController.php';
        require 'views/RechnerView.php';

        // Controller aufrufen
        ...
    ?>
</main>
```

---

## ⚠️ Das musst du auch ändern: Die View verbessern

Die aktuelle `RechnerView` hat nicht alle Methoden, die wir brauchen. Öffnet `views/RechnerView.php` und verbessert es:

```php
<?php

class RechnerView {

    /**
     * Zeigt nur das Formular
     */
    public function renderForm() {
        echo <<<HTML
<h2>BMI-Rechner</h2>
<form method="post" action="index.php">
    <div class="form-group">
        <label for="gewicht">Gewicht (kg):</label>
        <input type="number" id="gewicht" name="gewicht"
               placeholder="z.B. 70" step="0.1" required>
    </div>
    <div class="form-group">
        <label for="groesse">Größe (cm):</label>
        <input type="number" id="groesse" name="groesse"
               placeholder="z.B. 175" step="0.1" required>
    </div>
    <button type="submit">Berechnen</button>
</form>
HTML;
    }

    /**
     * Zeigt das Ergebnis an
     */
    public function renderErgebnis($bmi, $kategorie) {
        echo <<<HTML
<div class="ergebnis">
    <h3>Ergebnis:</h3>
    <p><strong>BMI:</strong> $bmi</p>
    <p><strong>Kategorie:</strong> $kategorie</p>
</div>
<hr>
HTML;
    }
}
```

---

## 🧪 So testet ihr die ganze App

1. Speichert alle Dateien:
   - `controllers/RechnerController.php`
   - `models/RechnerModel.php`
   - `views/RechnerView.php`
   - `index.php`
   - `layouts/main.php`

2. Im Terminal:

```bash
cd /workspaces/web-project-dynamic/version4
php -S localhost:8000
```

3. Im Browser öffnet: `http://localhost:8000`

4. **Das Formular sollte angezeigt werden!** ✅
5. **Gebt Werte ein und klickt "Berechnen"** ✅
6. **Das Ergebnis sollte angezeigt werden!** ✅

---

## ❓ Häufige Fehler

| Problem                                       | Lösung                                                             |
| --------------------------------------------- | ------------------------------------------------------------------ |
| Formular wird nicht angezeigt                 | Check: `zeigeFormular()` Methode aufgerufen?                       |
| "Class not found" Error                       | Check: `require` am Anfang von `index.php`?                        |
| Ergebnis wird nicht angezeigt                 | Check: `renderErgebnis()` aufgerufen?                              |
| Formular wird nach Berechnung nicht angezeigt | Check: `zeigeFormular()` am Ende der `verarbeiteBmi()` aufgerufen? |
| $\_POST-Werte sind null                       | Check: `name`-Attribute im Formular korrekt?                       |

---

## ✅ Checkliste

- [ ] `BmiRechnerController` ist programmiert
- [ ] `zeigeFormular()` ruft die View auf
- [ ] `verarbeiteBmi()` holt Werte aus $\_POST
- [ ] `verarbeiteBmi()` validiert die Eingaben
- [ ] `verarbeiteBmi()` ruft das Model auf
- [ ] `verarbeiteBmi()` zeigt das Ergebnis
- [ ] `index.php` wurde aktualisiert
- [ ] `RechnerView` hat `renderErgebnis()`-Methode
- [ ] Das Formular wird angezeigt
- [ ] Die Berechnung funktioniert
- [ ] Das Ergebnis wird angezeigt

---

## 🎉 Herzlichen Glückwunsch!

**Die App funktioniert!** Ihr habt gerade euer erstes richtiges PHP-Projekt mit MVC-Architektur gebaut!

Das ist genau das, was echte Entwickler machen! 🚀

---

## 💡 Ideen für Erweiterungen

Wenn alles funktioniert, könnt ihr erweitern:

- [ ] **Validierung:** Nur realistische Werte akzeptieren (z.B. 0 < Gewicht < 500)
- [ ] **Fehlerbehandlung:** Schöne Fehlermeldungen zeigen
- [ ] **Geschichte:** Alle bisherigen Berechnungen speichern und anzeigen
- [ ] **Styling:** Das Ergebnis je nach Kategorie anders färben (Normalgewicht = grün, Übergewicht = orange, etc.)
- [ ] **CSV-Export:** Die Ergebnisse in eine Datei speichern

---

**Fragen?** Fragt euren Lehrer/eure Lehrerin! 💬
