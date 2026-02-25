# Version 5: Notenrechner mit MVC-Architektur (Transfer aus Version 4)

**Willkommen zur Version 5!** 🚀

Diese Version hat denselben Umfang und dieselben Schritte wie Version 4. Ihr übertragt das Gelernte vom BMI-Rechner auf einen neuen fachlichen Kontext: **Notendurchschnitt und Nachhilfe-Prüfung**.

## 📋 Aufgabenstruktur (wie in Version 4)

### [📘 Aufgabe 0: Reflexion & Erkundung](AUFGABE_0_ERKUNDUNG.md)

**Ziel:** Version 4 reflektieren und die neue Aufgabenstellung analysieren.

### [📝 Aufgabe 1: Das Formular (View) erstellen](AUFGABE_1_VIEW.md)

**Ziel:** Formular für die Hauptfächer `bwl`, `mathe`, `deutsch`, `englisch` erstellen.

### [🧮 Aufgabe 2: Die Geschäftslogik (Model) implementieren](AUFGABE_2_MODEL.md)

**Ziel:** Notendurchschnitt berechnen und Methode `pruefeNachhilfe()` mit Verzweigungen umsetzen.

### [🎮 Aufgabe 3: Den Controller verbinden](AUFGABE_3_CONTROLLER.md)

**Ziel:** POST-Daten verarbeiten, Model aufrufen, Ergebnisse und Nachhilfe-Hinweise anzeigen.

---

## 🧠 Transferziel (Version 4 → Version 5)

Ihr sollt bewusst erkennen, was gleich bleibt und was sich fachlich ändert:

- **Gleich:** MVC-Struktur, Klassenaufbau, POST-Verarbeitung, View-Ausgabe
- **Neu:** Fachlogik für Noten statt BMI
- **Vertiefung:** Methode `pruefeNachhilfe()` als zusätzliche Entscheidungslogik

---

## 📐 Fachlogik: Notenrechner

- Notensystem: **1 bis 6** (`1 = sehr gut`, `6 = ungenügend`)
- Hauptfächer: **BWL, Mathe, Deutsch, Englisch**
- Durchschnitt:

```
durchschnitt = (bwl + mathe + deutsch + englisch) / 4
```

- Nachhilfe-Regel:

```
Nachhilfe ist erforderlich, wenn die Note in einem Fach > 4.0 ist.
```

---

## 🎯 Lernziele dieser Version

Nach Version 5 könnt ihr:

✅ Eine bekannte Architektur auf neue Problemstellungen übertragen  
✅ Fachlogik mit Funktionen/Methoden erweitern (`pruefeNachhilfe`)  
✅ Verzweigungen zielgerichtet einsetzen (`if/elseif`)  
✅ Benutzereingaben validieren und Ergebnisse verständlich ausgeben  
✅ Eure Architekturentscheidungen begründen (Transferleistung)

---

## 🧩 Musterlösungen in `src/`

Diese Stufen führen schrittweise in PHP und die Vorlage `src/dynamic_layout_projektvorlage` ein:

1. [src/01_PHP](../src/01_PHP/index.php) - Einfache Ausgabe
2. [src/02_PHP](../src/02_PHP/index.php) - Includes und Seitenstruktur
3. [src/03_PHP](../src/03_PHP/README.md) - MVC-Musterlösung BMI
4. [src/04_PHP](../src/04_PHP/README.md) - MVC-Musterlösung Notenrechner (Version 5)

---

## 🆘 Hilfreiche Ressourcen

- [PHP Fundamentals (modular)](../docs/programmierung/grundlagen/php/README.md)
- [PHP Basics](../docs/dynamisch/php.md)
- [PHP lokal testen](../docs/dynamisch/php-lokal-testen.md)
- [Version 4 (Vergleichsbasis)](../version4/README.md)

---

**Viel Erfolg beim Transfer! 🎉**
