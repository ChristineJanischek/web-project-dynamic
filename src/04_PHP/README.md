# 04_PHP: Vollständige Musterlösung zu Version 5 (Notenrechner mit MVC)

Dieses Verzeichnis enthält eine **voll funktionsfähige Musterlösung** für die Aufgaben aus `version5/`.

Die Lösung basiert auf der Vorlage aus `src/dynamic_layout_projektvorlage/` und führt den vollständigen MVC-Ablauf in PHP inklusive Transferleistung fort.

## 🏗️ Projektstruktur

```
04_PHP/
├── index.php              # Einstiegspunkt
├── controllers/
│   └── RechnerController.php      # Controller: POST-Verarbeitung und Validierung
├── models/
│   └── RechnerModel.php           # Model: Durchschnitt + pruefeNachhilfe()
├── views/
│   └── RechnerView.php            # View: Notenformular, Ergebnis, Hinweise
├── layouts/
│   ├── head.php           # HTML Header & CSS
│   ├── header.php         # Website Header
│   ├── nav.php            # Navigation
│   ├── main.php           # Initialisiert MVC und ruft Controller auf
│   └── footer.php         # Footer
├── css/                   # Stylesheets inkl. noten.css
└── images/                # Bilder
```

## 🎯 MVC erklärt

| Komponente     | Aufgabe             | Beispiel                                          |
| -------------- | ------------------- | ------------------------------------------------- |
| **Model**      | Daten & Logik       | Durchschnitt, Nachhilfe-Prüfung, Validierung      |
| **View**       | Präsentation (HTML) | Notenformular, Ergebnis und Hinweise anzeigen     |
| **Controller** | Ablaufsteuerung     | Anfrage verarbeiten, Model aufrufen, View rendern |

## 🚀 Starten & testen

1. Im Terminal in das Verzeichnis wechseln:

```bash
cd /workspaces/web-project-dynamic/src/04_PHP
```

2. Lokalen PHP-Server starten:

```bash
php -S localhost:8000
```

3. Browser öffnen: `http://localhost:8000`

4. Noten eingeben und Ergebnis prüfen.

## ✅ Implementierte Fachlogik

- Durchschnitt: `(bwl + mathe + deutsch + englisch) / 4`
- Validierung: Nur numerische Noten zwischen 1.0 und 6.0
- Verzweigung: `pruefeNachhilfe()` liefert alle Fächer mit `note > 4.0`
- Ausgabe: Durchschnitt plus konkrete Nachhilfeempfehlung je Fach

## 💡 Tipps

- **Separiere Daten und Präsentation:** Model speichert Daten, View gibt sie aus
- **Controller = Vermittler:** Der Controller verbindet Model und View
- **Kommentiere deine Klassen:** Erkläre, was jede Methode tut
- **Teste isoliert:** Teste Model-Methoden separat mit `test_*.php`

## 🔗 Lernbezug im Repository

- [Version 5: Notenrechner mit MVC](../../version5/README.md)
- [PHP-Grundlagen modular](../../docs/programmierung/grundlagen/php/README.md)
- [PHP Grundlagen (dynamisch)](../../docs/dynamisch/php.md)
- [PHP lokal testen](../../docs/dynamisch/php-lokal-testen.md)

## 🧭 Stufenübersicht in `src/`

- [01_PHP](../01_PHP/index.php): erste einfache PHP-Ausgabe
- [02_PHP](../02_PHP/index.php): mehrteilige Includes und Seitenstruktur
- [03_PHP](../03_PHP/README.md): vollständige MVC-Musterlösung BMI
- [04_PHP](./): vollständige MVC-Musterlösung Notenrechner mit Nachhilfe-Prüfung

---

Diese Lösung dient als Referenz für den Transfer von Version 4 auf ein neues Fachproblem mit erweiterter Verzweigungslogik.
