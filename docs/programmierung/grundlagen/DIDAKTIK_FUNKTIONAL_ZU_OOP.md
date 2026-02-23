# Didaktikpfad: Funktional starten, OOP sicher aufbauen

Dieses Kapitel beschreibt einen sprachübergreifenden Unterrichtspfad für **PHP, Python und JavaScript**:

1. **Jahr 1:** funktional-pragmatisches Denken (Funktionen, Datenfluss, Tests)
2. **Brücke:** Grenzen funktionaler Einheiten in größeren Systemen erkennen
3. **Jahr 2:** OOP gezielt einführen (Klassen, Verantwortlichkeiten, Modellierung)

So lernen Schülerinnen und Schüler zuerst stabile Grundlagen und verstehen OOP später als sinnvolle Antwort auf wachsende Systeme.

## Warum funktional zuerst?

- Weniger Einstiegskomplexität: Kein früher Overhead durch Klassenhierarchien
- Bessere Nachvollziehbarkeit: Input → Verarbeitung → Output ist direkt sichtbar
- Leichter testbar: Kleine, reine Funktionen sind schnell überprüfbar
- Bessere Fehlersuche: Nebenwirkungen und Zustand werden bewusst behandelt

## Lernziele über zwei Jahre

### Jahr 1 (funktional-pragmatisch)

- Daten sinnvoll strukturieren (Listen, Arrays, Dictionaries/Objekte)
- Funktionen sauber schneiden (ein Zweck pro Funktion)
- Kontrollstrukturen und Algorithmen sicher anwenden
- Ein- und Ausgabe sowie einfache Persistenz kontrolliert nutzen
- Ergebnisse dokumentieren und testen

### Brückenphase

- Wachsende Codebasen analysieren: Wo entstehen Doppelungen?
- Zustand und Verantwortlichkeiten identifizieren
- Modulare Grenzen ziehen (z. B. Berechnung, Validierung, Darstellung)

### Jahr 2 (OOP)

- Klassen als Bündel aus **Eigenschaften** (Daten) und **Verhalten** (Methoden)
- Kapselung, Komposition und klare Schnittstellen
- Trennung von Zuständigkeiten (z. B. Model, Service, Controller)
- Wartbarkeit und Erweiterbarkeit für größere Systeme

## Unterrichtssequenz (sprachübergreifend)

## Phase A: Funktionale Grundlagen

### Kernprinzipien

- Funktionen klein halten
- Klare Parameter statt globale Zustände
- Rückgabewerte statt versteckter Seiteneffekte

### Praxisaufgaben

#### PHP (3 Aufgaben)

1. **Notenrechner:** Funktion für Durchschnitt und verbale Bewertung
2. **Preisrechner:** Netto/Brutto, Rabatt, Mehrwertsteuer als getrennte Funktionen
3. **Listen-Filter:** Produkte nach Preisgrenze filtern und sortieren

#### Python (3 Aufgaben)

1. **Temperatur-Toolkit:** Umrechnung und Grenzwertprüfung in getrennten Funktionen
2. **Textanalyse:** Wortanzahl, häufigstes Wort, Stopwörter filtern
3. **CSV-Auswertung:** Einlesen, aggregieren, Ergebnisse als Tabelle ausgeben

#### JavaScript (3 Aufgaben)

1. **Formularprüfung:** Eingaben validieren (Pflichtfelder, Bereiche, Format)
2. **Warenkorb-Funktionen:** Zwischensumme, Rabatt, Gesamtsumme
3. **DOM-Mapper:** Datenliste in HTML-Karten transformieren und rendern

## Phase B: Brücke zu OOP

### Leitfragen

- Welche Funktionsgruppen arbeiten dauerhaft zusammen?
- Wo wird derselbe Zustand in mehreren Funktionen bearbeitet?
- Welche Teile ändern sich häufig, welche bleiben stabil?

### Praxisaufgaben

#### PHP (3 Aufgaben)

1. **Funktionssammlung clustern:** Preis-/Steuerlogik, Ausgabe, Validierung trennen
2. **Zustandsobjekt vorbereiten:** Warenkorb als Datenstruktur zentralisieren
3. **API-ähnliche Schnittstelle:** Einheitliche Funktionssignaturen für Erweiterbarkeit

#### Python (3 Aufgaben)

1. **Modulgrenzen ziehen:** `io.py`, `logic.py`, `report.py` aufbauen
2. **Zustandsübergänge modellieren:** Workflow-Schritte als klaren Prozess definieren
3. **Testfälle gruppieren:** Pro Funktionsblock eigene Testlisten anlegen

#### JavaScript (3 Aufgaben)

1. **State zentralisieren:** UI-Zustand in einem Objekt bündeln
2. **Renderer trennen:** Datenlogik und DOM-Ausgabe entkoppeln
3. **Event-Fluss dokumentieren:** Eingabe → Verarbeitung → Anzeige nachvollziehbar machen

## Phase C: OOP-Einstieg (Jahr 2)

### Kernprinzipien

- Klasse = zusammengehörige Daten + Verhalten
- Komposition vor Vererbung
- Öffentliche Schnittstelle klein halten

### Praxisaufgaben

#### PHP (3 Aufgaben)

1. **`CartItem` und `Cart`:** Positionen verwalten, Summen berechnen
2. **`BmiModel` + `BmiController`:** Anknüpfung an MVC-Themen
3. **`InvoiceService`:** Rechnungslogik aus proceduralem Code herauslösen

#### Python (3 Aufgaben)

1. **`Student` und `Course`:** Einschreibung und Notenverwaltung
2. **`SurveyAnalyzer`:** Daten laden, auswerten, Bericht erzeugen
3. **`Repository`-Pattern (einfach):** Datenzugriff kapseln

#### JavaScript (3 Aufgaben)

1. **`TodoStore`:** Zustand und CRUD-Methoden kapseln
2. **`Validator`:** Regeln als wiederverwendbare Methoden strukturieren
3. **`ViewModel`-Ansatz:** UI-Daten und Darstellungslogik organisieren

## Bewertungsraster (kurz)

- **Fachlich korrekt:** Ergebnisse stimmen, Randfälle bedacht
- **Strukturiert:** klare Namen, geringe Verschachtelung, kleine Einheiten
- **Begründet:** Wahl von funktional oder OOP wird argumentiert
- **Dokumentiert:** Quellen, Testfälle, ggf. KI-Einsatz transparent gemacht

## Verbindung zu bestehenden Kapiteln

- Zuerst die sprachspezifischen Fundamentals durcharbeiten:
  - [PHP Fundamentals](php/README.md)
  - [Python Fundamentals](python/README.md)
  - [JavaScript Fundamentals](javascript/README.md)
- Danach diesen Didaktikpfad als Planungs- und Reflexionsrahmen nutzen.
- Für OOP-nahe Projektarbeit die MVC-Inhalte in `version4/` ergänzend einsetzen.

## Praktischer Einsatz im Unterricht

- **Einstieg:** Ein Problem in allen drei Sprachen funktional lösen
- **Reflexion:** Unterschiede und Gemeinsamkeiten sichtbar machen
- **Transfer:** Lösung schrittweise in Klassenmodell überführen
- **Abschluss:** Architekturentscheidung begründen (Warum hier OOP?)

Hinweis: Der Pfad ist bewusst praxisorientiert; Reihenfolge und Tiefe können je Lerngruppe angepasst werden.
