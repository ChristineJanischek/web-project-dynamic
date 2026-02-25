# 📝 Aufgabe 1: Das Formular (View) erstellen

**Schwierigkeitsgrad:** ⭐⭐

**Ziel:**
Ihr erstellt die Oberfläche für den Notenrechner mit vier Eingabefeldern.

---

## 📋 Aufgabe

Bearbeitet `layouts/main.php` oder `views/RechnerView.php` (je nach eurem Stand) und erstellt ein Formular mit:

- `bwl`
- `mathe`
- `deutsch`
- `englisch`

Vorgaben:

- Eingabetyp: `number`
- Wertebereich: `min="1"`, `max="6"`, `step="0.1"`
- Versand: `method="post"` an `index.php`

---

## 🎯 HTML-Vorlage

```html
<form method="post" action="index.php">
  <label for="bwl">BWL</label>
  <input
    type="number"
    id="bwl"
    name="bwl"
    min="1"
    max="6"
    step="0.1"
    required
  />

  <label for="mathe">Mathe</label>
  <input
    type="number"
    id="mathe"
    name="mathe"
    min="1"
    max="6"
    step="0.1"
    required
  />

  <label for="deutsch">Deutsch</label>
  <input
    type="number"
    id="deutsch"
    name="deutsch"
    min="1"
    max="6"
    step="0.1"
    required
  />

  <label for="englisch">Englisch</label>
  <input
    type="number"
    id="englisch"
    name="englisch"
    min="1"
    max="6"
    step="0.1"
    required
  />

  <button type="submit">Notendurchschnitt berechnen</button>
</form>
```

---

## ✅ Checkliste

- [ ] Formular enthält alle vier Hauptfächer
- [ ] Alle Felder besitzen korrekte `name`-Attribute
- [ ] Wertebereich 1–6 ist gesetzt
- [ ] Formular sendet per POST

---

## 🔁 Reflexion (Transfer)

Vergleicht kurz mit Version 4:

- Was ist am Formular **gleich geblieben**?
- Was ist nur fachlich **umbenannt/erweitert**?

---

## 🚀 Nächster Schritt

Weiter mit **[Aufgabe 2: Model](AUFGABE_2_MODEL.md)**.
