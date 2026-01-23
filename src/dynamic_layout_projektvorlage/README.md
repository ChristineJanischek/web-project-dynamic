# Schritt-für-Schritt Anleitung zur Nutzung des BMI-Rechners

## 1. Projektstruktur
Das Projekt ist in ein MVC-Format strukturiert:
- **Model**: `RechnerModel` - verwaltet die Daten.
- **View**: `RechnerView` - zeigt die Ausgaben an.
- **Controller**: `RechnerController` - steuert den Ablauf der Anwendung.

## 2. Installation
- Klone das Repository oder lade die Dateien herunter.
- Stelle sicher, dass der Webserver (z.B. Apache) korrekt konfiguriert ist.

## 3. Nutzung
- Die Formular-Komponenten sollten in die entsprechende Form-Datei eingefügt werden.
- Die `lib.php`-Datei muss im `<head>`-Bereich der HTML-Datei inkludiert werden.
- Die Steuerung der Ereignisse erfolgt in der Controller-Datei.

## 4. BMI-Rechner Implementierung
- Füge die Eingabefelder für Gewicht und Größe in die Form-Datei ein.
- Nutze die `RechnerModel`-Klasse, um die Werte zu setzen und zu berechnen.
- Die Ergebnisse werden über die `RechnerView`-Klasse angezeigt.

## 5. Erweiterungen
- Das Template kann leicht erweitert werden, indem neue Controller, Modelle und Views hinzugefügt werden.