# Grundlagen der Programmierung

Diese Doku ist als **sprachübergreifendes Nachschlagewerk** aufgebaut. Ziel ist, dass Lernende die gleichen Kernkonzepte zuerst in PHP verstehen und später strukturgleich in weiteren Sprachen (z. B. Python, JavaScript) wiederfinden.

## Ziele

- Einheitliche Struktur für alle Programmiersprachen
- Weniger Redundanz durch zentrale Leitlinien
- Schrittweise Erweiterbarkeit für zukünftige Entwicklungsschritte
- Verständliche Beispiele für Einsteigerinnen und Einsteiger

## Didaktischer Pfad (empfohlen)

- [Didaktikpfad: Funktional starten, OOP sicher aufbauen](DIDAKTIK_FUNKTIONAL_ZU_OOP.md)
- Fokus: Jahr 1 funktional-pragmatisch, Brückenphase, Jahr 2 OOP
- Mit konkreten Praxisaufgaben für PHP, Python und JavaScript

## Architektur der Dokumentation

```text
docs/programmierung/grundlagen/
├── README.md                       # Sprachübergreifende Leitlinien
├── UMSETZUNGSPLAN.md               # Schritt-für-Schritt-Roadmap
├── VERGLEICH_JS_PY_PHP_OPERATOR_DATEI_IO.md # Sprachvergleich Operatoren + Datei-I/O
├── php/
    ├── README.md
    ├── AUSGABEN.md
    ├── VARIABLEN.md
    ├── RECHENOPERATIONEN.md
    ├── VERGLEICHSOPERATOREN_LOGISCHE_OPERATOREN.md
    ├── FUNKTIONEN_METHODEN.md
    ├── KONTROLLSTRUKTUREN_FALLUNTERSCHEIDUNGEN.md
    ├── KONTROLLSTRUKTUREN_WIEDERHOLUNGSSTRUKTUREN.md
    ├── DATENSTRUKTUREN.md
    ├── ALGORITHMEN.md
│   └── DATEIEN_LESEN_SCHREIBEN.md
├── python/
│   └── ... identische Kapitelstruktur wie php/
└── javascript/
    └── ... identische Kapitelstruktur wie php/
```

## Einheitlicher Aufbau pro Themenblatt

Jede Datei folgt demselben Muster:

1. **Lernziele**
2. **Theorie kompakt**
3. **Deklaration & Implementierung**
4. **Beispiel(e)**
5. **Best Practices**
6. **Häufige Fehler**

Dadurch bleibt die Orientierung stabil, auch wenn später neue Sprachen ergänzt werden.

## Redundanzen vermeiden

- Sprachneutrale Erklärungen bleiben hier in der übergeordneten Struktur.
- Sprachspezifika stehen nur im jeweiligen Sprachordner.
- Beispiele sind kurz und fokussiert auf genau ein Konzept.
- Querverweise statt doppelter Inhalte.

## Nächste Erweiterungen

- Gemeinsame Aufgabenblätter, die pro Sprache Varianten verlinken
- Sprachvergleichstabellen je Kapitel (PHP/Python/JavaScript)
- Kurze Self-Exams mit Musterlösungen pro Fundamentals-Thema

Weiter mit der konkreten PHP-Reihe: [PHP Fundamentals](php/README.md)

Weitere Reihen:

- [Python Fundamentals](python/README.md)
- [JavaScript Fundamentals](javascript/README.md)

Vertiefung zur Unterrichtsplanung:

- [Didaktikpfad Funktional → OOP](DIDAKTIK_FUNKTIONAL_ZU_OOP.md)

Sprachübergreifender Schnellvergleich:

- [Vergleich JavaScript, Python, PHP (Operatoren + Datei-I/O)](VERGLEICH_JS_PY_PHP_OPERATOR_DATEI_IO.md)
