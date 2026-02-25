# Version 4: BMI-Rechner mit MVC-Architektur

**Willkommen zur Version 4!** 🚀

In dieser Version lernt ihr eine realistische, professionelle Projektstruktur kennen: das **Model-View-Controller (MVC)** Muster. Das ist der Standard für größere PHP-Projekte!

## 📋 Aufgabenstruktur

Wir bauen den BMI-Rechner schrittweise auf - jedes Arbeitsblatt baut auf dem vorherigen auf:

### [📘 Aufgabe 0: Erkundungsauftrag - Die Vorlage erkunden](AUFGABE_0_ERKUNDUNG.md)

**Ziel:** Die Projektstruktur verstehen, ohne zu programmieren

- Lest den Code
- Versteht die Rollen von Model, View, Controller
- Beantwortet Verständnisfragen

### [📝 Aufgabe 1: Das Formular (View) erstellen](AUFGABE_1_VIEW.md)

**Ziel:** Die Benutzeroberfläche für den BMI-Rechner

- HTML-Formular mit Eingabefeldern für Gewicht und Größe
- Erste sichtbare Erfolge!

### [🧮 Aufgabe 2: Die Geschäftslogik (Model) implementieren](AUFGABE_2_MODEL.md)

**Ziel:** Der BMI wird berechnet

- Methoden zum Speichern von Gewicht und Größe
- BMI-Formel implementieren: BMI = Gewicht (kg) / (Größe (m))²
- Gewichtskategorie bestimmen

### [🎮 Aufgabe 3: Den Controller verbinden](AUFGABE_3_CONTROLLER.md)

**Ziel:** Alles funktioniert zusammen!

- Formular-Eingaben verarbeiten
- Model-Logik aufrufen
- Ergebnisse mit View anzeigen

---

## 🏗️ Projektstruktur verstehen

```
version4/
├── index.php              # Einstiegspunkt (starte hier!)
├── controllers/
│   └── RechnerController.php      # Steuert den Ablauf
├── models/
│   └── RechnerModel.php           # Geschäftslogik (BMI-Berechnung)
├── views/
│   └── RechnerView.php            # Zeigt Ergebnisse an (HTML)
├── layouts/
│   ├── head.php           # HTML-Header
│   ├── header.php         # Website-Header
│   ├── nav.php            # Navigation
│   ├── main.php           # Hauptinhalt (hier kommt euer Code!)
│   └── footer.php         # Website-Footer
└── css/
    └── style.css          # Styling
```

---

## ✅ So arbeitet ihr mit dieser Vorlage

1. **Startet mit [Aufgabe 0](AUFGABE_0_ERKUNDUNG.md)** - Ohne zu coden, erst verstehen!
2. **Folgt den Aufgaben der Reihe nach** - Sie bauen aufeinander auf
3. **Jede Aufgabe hat klare Anforderungen** - Was genau müsst ihr tun?
4. **Testet nach jeder Aufgabe** - Funktioniert euer Code? (Siehe [PHP lokal testen](../docs/dynamisch/php-lokal-testen.md))

---

## 🎯 Lernziele dieser Version

Nach dieser Version könnt ihr:

✅ Die MVC-Architektur verstehen und anwenden  
✅ PHP-Klassen mit Methoden schreiben  
✅ HTML-Formulare mit PHP verarbeiten  
✅ Formeln und Logik in ein Model auslagern  
✅ Controller für die Ablaufsteuerung nutzen  
✅ Eine realistische Projektstruktur verstehen

---

## 💡 BMI-Rechner Basics

Der **Body Mass Index (BMI)** wird so berechnet:

```
BMI = Gewicht (kg) / (Größe in Metern)²
```

**Beispiel:** Jemand wiegt 70 kg und ist 1,75 m groß

- BMI = 70 / (1,75 × 1,75) = 70 / 3,0625 ≈ 22,86

**Kategorien:**

- BMI < 18,5 → Untergewicht
- 18,5 ≤ BMI < 25 → Normalgewicht
- 25 ≤ BMI < 30 → Übergewicht
- BMI ≥ 30 → Adipositas (Fettleibigkeit)

---

## 🆘 Hilfreiche Ressourcen

- [PHP lokal testen](../docs/dynamisch/php-lokal-testen.md) - So testet ihr eure Dateien
- [PHP Basics](../docs/dynamisch/php.md) - PHP-Grundlagen auffrischen
- [HTML-Formulare](../docs/statisch/formulare.md) - Wie Formulare funktionieren
- [PHP Fundamentals (modular)](../docs/programmierung/grundlagen/php/README.md) - Grundlagenpfad für Deklaration, Kontrollstrukturen, Datenstrukturen

## 🧩 Musterlösungen in `src/`

Diese Stufen führen schrittweise in PHP und die Nutzung der Vorlage `src/dynamic_layout_projektvorlage` ein:

1. [src/01_PHP](../src/01_PHP/index.php) - Einfache Ausgabe mit erstem PHP-Block
2. [src/02_PHP](../src/02_PHP/index.php) - Seitenaufbau mit Includes (`head`, `header`, `content`, `sidebar`, `footer`)
3. [src/03_PHP](../src/03_PHP/README.md) - Vollständige MVC-Musterlösung zum BMI-Rechner auf Basis der Projektvorlage

---

**Viel Erfolg! 🎉**
