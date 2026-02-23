# PHP von der Console aus testen

Diese Anleitung zeigt dir, wie du PHP-Projekte (wie die `index.php` in `src/dynamic_layout_projektvorlage/`) direkt von der Kommandozeile aus testen kannst - ohne Webserver wie Apache oder nginx.

## 🎯 Voraussetzungen

Zunächst prüfen, ob PHP installiert ist:

```bash
php --version
```

**Erwartete Ausgabe:**

```
PHP 8.x.x (cli) ...
```

Falls PHP nicht installiert ist:

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install php php-cli
```

**macOS:**

```bash
brew install php
```

---

## 🚀 Methode 1: PHP Built-in Webserver (Empfohlen)

PHP hat seit Version 5.4 einen eingebauten Webserver für Entwicklungszwecke!

### Schritt 1: Terminal öffnen

In VS Code:

- **Keyboard Shortcut:** `` Ctrl+` `` (Windows/Linux) oder `` Cmd+` `` (Mac)
- **Oder:** `Terminal` → `New Terminal` im Menü

### Schritt 2: Ins Projektverzeichnis wechseln

```bash
cd /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage
```

**Tipp:** Mit der Tab-Taste kannst du Pfade automatisch vervollständigen!

### Schritt 3: PHP Webserver starten

```bash
php -S localhost:8000
```

**Ausgabe:**

```
PHP 8.x.x Development Server (http://localhost:8000) started
```

### Schritt 4: Im Browser öffnen

Der Server läuft jetzt! Öffne in deinem Browser:

```
http://localhost:8000
```

oder verwende in VS Code:

```bash
"$BROWSER" http://localhost:8000
```

### Schritt 5: Server stoppen

Wenn du fertig bist:

- Drücke `Ctrl+C` im Terminal
- Der Server wird beendet

---

## 🔧 Methode 2: PHP-Datei direkt ausführen

Für schnelle Tests ohne Browser kannst du PHP-Dateien direkt ausführen:

### Einfache PHP-Datei testen

```bash
php /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage/index.php
```

**Was passiert:**

- PHP verarbeitet die Datei
- Gibt den HTML-Output im Terminal aus
- **Nachteil:** Include-Pfade und relative URLs funktionieren möglicherweise nicht korrekt

### Mit korrektem Working Directory

```bash
cd /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage
php index.php
```

Dies ist besser, da alle relativen Pfade (wie `framework/head.php`) korrekt aufgelöst werden.

---

## 📊 Methode 3: PHP-Code interaktiv testen

### Schneller Test einzelner PHP-Befehle

```bash
php -r "echo 'Hello from PHP ' . phpversion();"
```

### Interaktive PHP-Shell starten

```bash
php -a
```

Jetzt kannst du PHP-Code direkt eingeben:

```php
php > $name = "Schüler";
php > echo "Hallo $name!";
Hallo Schüler!
php > exit
```

---

## 🐛 Fehlerbehebung und Debugging

### Syntax-Check ohne Ausführung

Prüfe eine PHP-Datei auf Syntaxfehler:

```bash
php -l /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage/index.php
```

**Erwartete Ausgabe bei korrektem Code:**

```
No syntax errors detected in index.php
```

### Detaillierte Fehleranzeige aktivieren

Im Terminal vor dem Start:

```bash
export XDEBUG_MODE=debug
php -S localhost:8000
```

Oder erstelle eine `php.ini` im Projektordner:

```ini
display_errors = On
error_reporting = E_ALL
```

Und starte den Server mit:

```bash
php -S localhost:8000 -c php.ini
```

### Häufige Probleme

#### Problem: "Address already in use"

Der Port 8000 wird bereits verwendet.

**Lösung 1 - Anderen Port verwenden:**

```bash
php -S localhost:8080
```

**Lösung 2 - Prozess beenden:**

```bash
# Prozess finden
lsof -i :8000

# Prozess beenden (ersetze PID mit der Prozess-ID)
kill -9 PID
```

#### Problem: Include-Dateien werden nicht gefunden

**Lösung:** Immer vom Projektverzeichnis aus starten:

```bash
cd /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage
php -S localhost:8000
```

#### Problem: CSS/JS-Dateien werden nicht geladen

**Lösung:** Verwende immer den Built-in Webserver (`php -S`), nicht die direkte Ausführung mit `php index.php`, da nur der Webserver statische Dateien (CSS, JS, Bilder) korrekt ausliefert.

---

## 💡 Best Practices für Schüler

### 1. Immer im richtigen Verzeichnis arbeiten

```bash
# Terminal-Tipp: Zeige aktuelles Verzeichnis an
pwd

# Sollte ausgeben: .../src/dynamic_layout_projektvorlage
```

### 2. Port-Nummer dokumentieren

Wenn du mehrere Projekte gleichzeitig testest, nutze unterschiedliche Ports:

- Projekt 1: `php -S localhost:8000`
- Projekt 2: `php -S localhost:8001`
- Projekt 3: `php -S localhost:8002`

### 3. Logs im Terminal beachten

Der PHP-Server zeigt dir alle Requests:

```
[Thu Jan 23 10:30:45 2026] 127.0.0.1:52534 [200]: GET /
[Thu Jan 23 10:30:45 2026] 127.0.0.1:52535 [200]: GET /css/style.css
[Thu Jan 23 10:30:46 2026] 127.0.0.1:52536 [404]: GET /images/logo.png - No such file or directory
```

- `[200]` = Erfolgreich ✅
- `[404]` = Datei nicht gefunden ❌

### 4. Automatisches Neuladen

Der PHP Built-in Server lädt Änderungen automatisch! Du musst nur:

1. Datei speichern (`Ctrl+S`)
2. Browser neu laden (`F5`)

---

## 🎓 Zusammenfassung - Quick Reference

```bash
# 1. Ins Verzeichnis wechseln
cd /workspaces/web-project-dynamic/src/dynamic_layout_projektvorlage

# 2. Server starten
php -S localhost:8000

# 3. Im Browser öffnen
# http://localhost:8000

# 4. Entwickeln & Testen:
#    - Datei bearbeiten
#    - Speichern (Ctrl+S)
#    - Browser neu laden (F5)

# 5. Server stoppen
# Ctrl+C im Terminal
```

---

## 📚 Weiterführende Themen

- **Datenbank-Integration:** Siehe [datenbank.md](datenbank.md)
- **PHP Grundlagen:** Siehe [php.md](php.md)
- **Debugging:** Siehe [testen.md](testen.md)

---

## ⚠️ Wichtiger Hinweis

Der PHP Built-in Webserver ist **nur für Entwicklung** gedacht! Für produktive Websites nutze:

- Apache mit mod_php
- nginx mit PHP-FPM
- Docker-Container mit PHP

Aber zum Lernen und Testen ist `php -S` perfekt! ✨
