# Version 5: Didaktischer Leitfaden für Lehrende

## 🎯 Pädagogischer Fokus

Version 5 setzt bewusst auf **Transferleistung**:

- gleicher Ablauf wie Version 4 (Aufgabe 0–3)
- gleicher Architekturrahmen (MVC)
- neue Fachlogik (Notenrechner statt BMI)

Ziel ist, dass Lernende Strukturwissen wiederverwenden und fachliche Änderungen eigenständig modellieren.

## 🧱 Scaffolding in vier Schritten

1. **Aufgabe 0 (Reflexion):** Version 4 analysieren, Unterschiede benennen
2. **Aufgabe 1 (View):** Formular mit vier Fächern erstellen
3. **Aufgabe 2 (Model):** Durchschnitt + `pruefeNachhilfe()` implementieren
4. **Aufgabe 3 (Controller):** End-to-End verbinden, validieren, ausgeben

## ✅ Kompetenzziele

- MVC-Rollen sicher anwenden
- fachliche Anforderungen in Methoden übersetzen
- Verzweigungen begründet einsetzen
- Eingabedaten validieren
- Architekturentscheidungen reflektieren

## 📋 Erwartungshorizont je Aufgabe

### Aufgabe 0 (30–45 Min)

- MVC aus Version 4 korrekt erklärt
- Transfer auf Notenrechner logisch skizziert

### Aufgabe 1 (45–75 Min)

- Formularfelder: `bwl`, `mathe`, `deutsch`, `englisch`
- `POST`, `required`, Zahlenbereich 1–6

### Aufgabe 2 (75–105 Min)

- Klasse `NotenRechner`
- Durchschnitt korrekt
- `pruefeNachhilfe()` liefert Fächer mit Note > 4.0

### Aufgabe 3 (75–105 Min)

- Controller verarbeitet `$_POST`
- validiert Eingaben
- ruft Model + View korrekt auf
- Ergebnis + Nachhilfe-Hinweise sichtbar

## 🧪 Schnelltests für Lehrkräfte

- Werden ungültige Werte abgefangen?
- Ist der Durchschnitt rechnerisch korrekt?
- Werden genau die Fächer mit Note > 4.0 markiert?
- Bleibt das Formular nach dem Submit nutzbar?

## 🧩 Differenzierung

- **Schneller fertig:** Fachgewichtung (z. B. Mathe doppelt) ergänzen
- **Unterstützung nötig:** Validierung gemeinsam als Klasse entwickeln

## 🔗 Verweise

- Aufgabenübersicht: [README.md](README.md)
- PHP-Grundlagen: [../docs/programmierung/grundlagen/php/README.md](../docs/programmierung/grundlagen/php/README.md)
- Musterlösung: [../src/04_PHP/README.md](../src/04_PHP/README.md)
