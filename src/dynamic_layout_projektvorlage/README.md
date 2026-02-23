# Projektvorlage: MVC-Architektur in PHP

Diese Vorlage zeigt die professionelle **Model-View-Controller (MVC)** Architektur für PHP-Projekte.

## 🏗️ Projektstruktur

```
dynamic_layout_projektvorlage/
├── index.php              # Einstiegspunkt
├── controllers/
│   └── RechnerController.php      # Controller: Ablaufsteuerung
├── models/
│   └── RechnerModel.php           # Model: Geschäftslogik
├── views/
│   └── RechnerView.php            # View: Präsentation
├── layouts/
│   ├── head.php           # HTML Header & CSS
│   ├── header.php         # Website Header
│   ├── nav.php            # Navigation
│   ├── main.php           # Hauptinhalt
│   └── footer.php         # Footer
├── css/                   # Stylesheets
└── images/                # Bilder
```

## 🎯 MVC erklärt

| Komponente     | Aufgabe             | Beispiel                                          |
| -------------- | ------------------- | ------------------------------------------------- |
| **Model**      | Daten & Logik       | BMI-Berechnung, Formularvalidierung               |
| **View**       | Präsentation (HTML) | Formular anzeigen, Ergebnis darstellen            |
| **Controller** | Ablaufsteuerung     | Anfrage verarbeiten, Model aufrufen, View rendern |

## 🚀 Schnelleinstieg

1. **Folie kopieren** aus `src/` in euer Projektverzeichnis
2. **index.php** ausführen: `php -S localhost:8000`
3. **Browser öffnen:** `http://localhost:8000`

## 📝 Wie ihr die Vorlage nutzt

### Schritt 1: Das Formular gestalten (View)

Bearbeitet `layouts/main.php` und fügt HTML für euer Formular ein.

### Schritt 2: Die Geschäftslogik programmieren (Model)

Erweitert `models/RechnerModel.php` mit euren Berechnungen.

### Schritt 3: Alles verbinden (Controller)

Programmiert `controllers/RechnerController.php` für die Ablaufsteuerung.

## 💡 Tipps

- **Separiere Daten und Präsentation:** Model speichert Daten, View gibt sie aus
- **Controller = Vermittler:** Der Controller verbindet Model und View
- **Kommentiere deine Klassen:** Erkläre, was jede Methode tut
- **Teste isoliert:** Teste Model-Methoden separat mit `test_*.php`

## 🔗 Weiterführende Links

- [Version 4: BMI-Rechner mit MVC](../../version4/README.md) - Komplette Aufgabenstellung
- [PHP Grundlagen](../../docs/dynamisch/php.md) - PHP-Dokumentation
- [PHP lokal testen](../../docs/dynamisch/php-lokal-testen.md) - Anleitung zum Testen

---

**Diese Vorlage wird verwendet für:**

- Version 4 - BMI-Rechner mit MVC
- Weitere PHP-Projekte mit Geschäftslogik
