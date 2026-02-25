# 03_PHP: Vollständige Musterlösung zu Version 4 (BMI mit MVC)

Dieses Verzeichnis enthält eine **voll funktionsfähige Musterlösung** für die Aufgaben aus `version4/`.

Die Lösung basiert auf der Vorlage aus `src/dynamic_layout_projektvorlage/` und führt den vollständigen MVC-Ablauf in PHP ein.

## 🏗️ Projektstruktur

```
03_PHP/
├── index.php              # Einstiegspunkt
├── controllers/
│   └── RechnerController.php      # Controller: Request-Verarbeitung
├── models/
│   └── RechnerModel.php           # Model: BMI-Berechnung + Kategorie
├── views/
│   └── RechnerView.php            # View: Formular, Ergebnis, Fehler
├── layouts/
│   ├── head.php           # HTML Header & CSS
│   ├── header.php         # Website Header
│   ├── nav.php            # Navigation
│   ├── main.php           # Initialisiert MVC und ruft Controller auf
│   └── footer.php         # Footer
├── css/                   # Stylesheets inkl. bmi.css
└── images/                # Bilder
```

## 🎯 MVC erklärt

| Komponente     | Aufgabe             | Beispiel                                          |
| -------------- | ------------------- | ------------------------------------------------- |
| **Model**      | Daten & Logik       | BMI-Berechnung, Formularvalidierung               |
| **View**       | Präsentation (HTML) | Formular anzeigen, Ergebnis darstellen            |
| **Controller** | Ablaufsteuerung     | Anfrage verarbeiten, Model aufrufen, View rendern |

## 🚀 Starten & testen

1. Im Terminal in das Verzeichnis wechseln:

```bash
cd /workspaces/web-project-dynamic/src/03_PHP
```

2. Lokalen PHP-Server starten:

```bash
php -S localhost:8000
```

3. Browser öffnen: `http://localhost:8000`

4. Gewicht und Größe eingeben und Ergebnis prüfen.

## ✅ Implementierte Fachlogik

- BMI-Formel: `BMI = Gewicht (kg) / (Größe in m)^2`
- Umrechnung Größe: cm → m
- Kategorien:
  - `< 18.5`: Untergewicht
  - `18.5 - < 25`: Normalgewicht
  - `25 - < 30`: Übergewicht
  - `>= 30`: Adipositas
- Validierung: Nur numerische Werte größer 0 werden akzeptiert

## 💡 Tipps

- **Separiere Daten und Präsentation:** Model speichert Daten, View gibt sie aus
- **Controller = Vermittler:** Der Controller verbindet Model und View
- **Kommentiere deine Klassen:** Erkläre, was jede Methode tut
- **Teste isoliert:** Teste Model-Methoden separat mit `test_*.php`

## 🔗 Lernbezug im Repository

- [Version 4: BMI-Rechner mit MVC](../../version4/README.md)
- [PHP-Grundlagen modular](../../docs/programmierung/grundlagen/php/README.md)
- [PHP Grundlagen (dynamisch)](../../docs/dynamisch/php.md)
- [PHP lokal testen](../../docs/dynamisch/php-lokal-testen.md)

## 🧭 Stufenübersicht in `src/`

- [01_PHP](../01_PHP/index.php): erste einfache PHP-Ausgabe
- [02_PHP](../02_PHP/index.php): mehrteilige Includes und Seitenstruktur
- [03_PHP](./): vollständige MVC-Musterlösung mit Formular, Model und Controller

---

Diese Lösung dient als Referenz für den Übergang von prozeduralen Includes zu objektorientierter MVC-Struktur in PHP.
