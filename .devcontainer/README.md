# DevContainer Konfiguration

Diese Konfiguration sorgt dafür, dass **alle Codespaces** automatisch mit den benötigten Tools und Extensions ausgestattet werden.

## 🎯 Was wird automatisch installiert?

### Extensions

#### Core Web Development

- ✅ **Live Server** - Lokaler Webserver mit Auto-Reload
- ✅ **Prettier** - Code-Formatierung
- ✅ **ESLint** - JavaScript Linting
- ✅ **HTML CSS Support** - IntelliSense für HTML/CSS
- ✅ **Auto Rename Tag** - HTML-Tags automatisch umbenennen

#### Python Development

- ✅ **Python** - Volle Python-Unterstützung
- ✅ **Pylance** - Python Language Server
- ✅ **Python Debugger** - Debugging-Unterstützung

#### PHP Development

- ✅ **PHP Intelephense** - PHP IntelliSense & Code-Intelligence
- ✅ **PHP Debug** - Xdebug-Integration
- ✅ **PHP DocBlocker** - Automatische Dokumentation
- ✅ **PHP Namespace Resolver** - Import von Klassen
- ✅ **PHP CS Fixer** - Code-Formatierung nach PSR-Standards

#### Git & Collaboration

- ✅ **GitLens** - Erweiterte Git-Features
- ✅ **GitHub Pull Requests** - PR-Management in VS Code

#### Zusätzliche Tools

- ✅ **Path Intellisense** - Pfad-Autovervollständigung
- ✅ **HTML CSS Class Completion** - CSS-Klassen-Vorschläge

### Vorkonfigurierte Settings

- ⚡ **Auto Save** nach 1 Sekunde
- 🎨 **Format on Save** aktiviert
- 📏 **Tab Size** = 2 Spaces
- 🌈 **Bracket Pair Colorization** aktiviert
- 🔧 **Python Linting** mit Pylint
- 🐘 **PHP Validation** aktiviert

### Automatisch verfügbare Ports

| Port | Verwendung            | Verhalten                     |
| ---- | --------------------- | ----------------------------- |
| 5500 | Live Server           | Öffnet automatisch im Browser |
| 8000 | PHP/Python Dev Server | Benachrichtigung              |
| 3000 | React Dev Server      | Öffnet automatisch im Browser |
| 8001 | Zusätzlicher Port     | Manuell                       |

### Installierte Tools

- 📦 **Node.js** (LTS)
- 🐘 **PHP** (Latest)
- 🐍 **Python 3.11**
- 📚 **Git** (Latest)

## 🚀 Wie funktioniert es?

### Für Schüler (neuer Codespace)

1. **Codespace erstellen** über GitHub
2. ⏳ Warten (~2-3 Minuten) während alles installiert wird
3. ✅ **Fertig!** Alle Extensions sind da, keine manuelle Installation nötig

### Für Lehrkräfte (bestehendes Classroom)

Diese Konfiguration wird automatisch aktiv, sobald sie im Repository ist:

```bash
# Änderungen committen
git add .devcontainer/
git commit -m "chore: Add automatic devcontainer configuration"
git push
```

**Wichtig:** Schüler müssen danach ihre Codespaces **neu erstellen** oder rebuilden:

- Bestehende Codespaces: `Cmd/Ctrl+Shift+P` → "Codespaces: Rebuild Container"
- Neue Codespaces: Automatisch aktiv ✅

## 🔧 Anpassungen

### Weitere Extensions hinzufügen

Bearbeite `.devcontainer/devcontainer.json`:

```json
"extensions": [
  "ritwickdey.liveserver",
  "deine-neue-extension"
]
```

### Settings ändern

```json
"settings": {
  "editor.fontSize": 14,
  "deine-setting-key": "dein-wert"
}
```

### Ports hinzufügen

```json
"forwardPorts": [5500, 8000, 9000],
"portsAttributes": {
  "9000": {
    "label": "Mein Service",
    "onAutoForward": "openBrowser"
  }
}
```

## 📚 Weiterführende Dokumentation

- [VS Code DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Codespaces](https://docs.github.com/en/codespaces)
- [DevContainer Features](https://containers.dev/features)

## 🐛 Troubleshooting

### Extensions werden nicht installiert

**Lösung:**

1. `Cmd/Ctrl+Shift+P`
2. "Codespaces: Rebuild Container"
3. Warten, bis Rebuild abgeschlossen ist

### Port nicht verfügbar

**Lösung:**

1. Terminal öffnen: `Ports` Tab unten
2. Port manuell hinzufügen: `+` Klicken
3. Port-Nummer eingeben

### Settings werden nicht übernommen

**Lösung:**

- Settings in `devcontainer.json` haben Vorrang
- User-Settings werden überschrieben
- Check: "Workspace Settings" vs. "User Settings"

## ✨ Vorteile

- 🎯 **Konsistenz**: Alle arbeiten mit gleichen Tools
- ⚡ **Zero Setup**: Schüler können sofort loslegen
- 🔄 **Versionskontrolle**: Settings im Git-Repo
- 🎓 **Best Practices**: Vorkonfigurierte Qualitäts-Tools
- 🚀 **Schneller Start**: Kein "Bei mir funktioniert es nicht"

## 🎓 Für GitHub Classroom

Diese Konfiguration ist **perfekt für GitHub Classroom**:

1. Template-Repository wird mit DevContainer gepusht
2. Schüler erstellen Assignment-Repository
3. Codespace startet automatisch mit allen Tools
4. Schüler können sofort programmieren ✅

**Keine IT-Support-Anfragen mehr wegen fehlender Extensions!** 🎉
