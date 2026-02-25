# 🎮 Aufgabe 3: Controller verbinden und Transfer abschließen

**Schwierigkeitsgrad:** ⭐⭐⭐⭐

**Ziel:**
Ihr verbindet Model und View zur vollständigen Notenrechner-App.

---

## 🎯 Ablauf

1. Formular absenden (`POST`)
2. Controller liest Noten
3. Eingaben validieren
4. Model berechnet Durchschnitt
5. Model prüft Nachhilfe (`pruefeNachhilfe()`)
6. View zeigt Ergebnis und Hinweise

---

## 📋 Aufgaben

Bearbeitet `controllers/RechnerController.php`:

1. `handleRequest()` mit GET/POST-Entscheidung
2. In der POST-Logik vier Noten lesen: `bwl`, `mathe`, `deutsch`, `englisch`
3. Validierung: numerisch und zwischen 1 und 6
4. Bei Fehlern sinnvolle Meldung ausgeben
5. Bei Erfolg `setNoten(...)`, Durchschnitt und Nachhilfefächer an View übergeben

---

## 💡 Beispielstruktur

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // POST lesen
    // validieren
    // model setzen
    // ergebnis rendern
} else {
    // formular rendern
}
```

---

## ✅ Checkliste

- [ ] Controller verarbeitet POST-Daten korrekt
- [ ] Validierung ist vorhanden
- [ ] Model wird mit vier Noten aufgerufen
- [ ] Durchschnitt wird angezeigt
- [ ] Nachhilfe-Hinweis je Fach wird angezeigt
- [ ] Formular bleibt nach Berechnung nutzbar

---

## 🔁 Abschluss-Reflexion

Beantwortet kurz:

1. Welche Teile aus Version 4 konntet ihr 1:1 wiederverwenden?
2. Wo musstet ihr wegen der neuen Fachlogik neu denken?
3. Warum gehört `pruefeNachhilfe()` ins Model und nicht in die View?

---

## 🧪 Test

```bash
cd /workspaces/web-project-dynamic/version5
php -S localhost:8000
```

Danach im Browser: `http://localhost:8000`

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
