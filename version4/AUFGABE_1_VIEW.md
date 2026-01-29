# 📝 Aufgabe 1: Das Formular (View) erstellen

**Schwierigkeitsgrad:** ⭐⭐ (Ein wenig HTML schreiben)

**Ziel dieser Aufgabe:**  
Ihr erstellt das Formular, das der Benutzer sieht. Keine Berechnung noch - aber die **erste sichtbare Erfolge**! ✨

**Voraussetzung:** Ihr solltet [Aufgabe 0](AUFGABE_0_ERKUNDUNG.md) (Erkundung) abgeschlossen haben.

---

## 📋 Aufgabe: Das HTML-Formular für den BMI-Rechner

### ✅ Das musst ihr tun:

1. Öffnet die Datei: `layouts/main.php`

2. Ersetzt den Platzhalter-Text durch ein HTML-Formular mit:
   - **Feld für Gewicht** (in kg) - `<input type="number">`
   - **Feld für Größe** (in cm) - `<input type="number">`
   - **Senden-Button** - `<button type="submit">`

3. Das Formular soll per `POST` an `index.php` senden

4. Speichert die Datei

---

## 💻 So sieht das Formular aus (visuell):

```
┌─────────────────────────────────┐
│  BMI-Rechner                    │
├─────────────────────────────────┤
│ Gewicht (kg):                   │
│ [________________]              │
│                                 │
│ Größe (cm):                     │
│ [________________]              │
│                                 │
│ [    Berechnen    ]             │
└─────────────────────────────────┘
```

---

## 🎯 HTML-Vorlage zum Anpassen

Hier ist eine Vorlage - ihr könnt sie anpassen und verschönern:

```html
<div class="formular-container">
  <h2>BMI-Rechner</h2>

  <form method="post" action="index.php">
    <div class="form-group">
      <label for="gewicht">Gewicht (kg):</label>
      <input
        type="number"
        id="gewicht"
        name="gewicht"
        placeholder="z.B. 70"
        step="0.1"
        required
      />
    </div>

    <div class="form-group">
      <label for="groesse">Größe (cm):</label>
      <input
        type="number"
        id="groesse"
        name="groesse"
        placeholder="z.B. 175"
        step="0.1"
        required
      />
    </div>

    <button type="submit">Berechnen</button>
  </form>
</div>
```

---

## 🤔 Erklärung der Attribute:

| Attribut         | Was macht es?             | Beispiel                  |
| ---------------- | ------------------------- | ------------------------- |
| `type="number"`  | Nur Zahlen erlauben       | `<input type="number">`   |
| `id="gewicht"`   | Eindeutige Kennung        | Mit Label verbinden       |
| `name="gewicht"` | Der Name im `$_POST`      | `$_POST['gewicht']`       |
| `placeholder`    | Grauer Hinweistext        | `70` → Hilfe für Benutzer |
| `step="0.1"`     | In 0,1er Schritten        | Auch 70,5 kg möglich      |
| `required`       | Feld muss ausgefüllt sein | Verhindert leere Eingaben |
| `method="post"`  | Daten per POST senden     | Sicherer als GET          |

---

## 🎨 Extra: Styling (optional)

Wenn euer CSS schlecht aussieht, könnt ihr diese Zeilen in `css/style.css` hinzufügen:

```css
.formular-container {
  max-width: 500px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}
```

---

## 🧪 So testet ihr euer Formular

1. Speichert `layouts/main.php`
2. Öffnet ein Terminal
3. Navigiert zu: `cd /workspaces/web-project-dynamic/version4`
4. Startet PHP: `php -S localhost:8000`
5. Öffnet im Browser: `http://localhost:8000`

**Sieht ihr das Formular?** ✅

---

## ❓ Häufige Fehler

| Problem                       | Lösung                                                         |
| ----------------------------- | -------------------------------------------------------------- |
| Formular ist nicht sichtbar   | Ihr habt es nicht in `main.php` eingefügt!                     |
| Formulare sieht komisch aus   | CSS-Problem - Schaut `css/style.css` an                        |
| "required" funktioniert nicht | Nutzt `required` ohne Wert: `required` nicht `required="true"` |
| Button funktioniert nicht     | Nutzt `type="submit"` im Button                                |

---

## 🎯 Anforderungen (Checkliste)

- [ ] Datei `layouts/main.php` wurde bearbeitet
- [ ] Das Formular hat ein Gewicht-Eingabefeld
- [ ] Das Formular hat ein Größe-Eingabefeld
- [ ] Das Formular hat einen Senden-Button
- [ ] Das Formular sendet per `POST` an `index.php`
- [ ] Das Formular sieht gut aus (HTML + CSS)
- [ ] Das Formular lädt im Browser

---

## 💡 Tipps

- **Zahlen mit Dezimalen:** Nutzt `type="number"` mit `step="0.1"`
- **Größe in cm:** Ein Mensch ist 160-200 cm groß, nicht 1,6-2,0!
- **Namen wichtig:** Die `name`-Attribute braucht ihr später im Controller!
- **Testen:** Nach jeder Änderung speichern und Browser aktualisieren (F5)

---

## 🚀 Nächste Schritte

Wenn das Formular funktioniert, seid ihr bereit für **[Aufgabe 2: Das Model (die Berechnung)](AUFGABE_2_MODEL.md)**!

Dort programmieren wir die **BMI-Berechnung**! 🧮

---

**Fragen oder Probleme?** Redet mit eurem Lehrer/eurer Lehrerin! 💬
