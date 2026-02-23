# 🚀 Automatisches Setup für GitHub Codespaces

Dieses Repository ist vollständig konfiguriert für **Zero-Setup** in GitHub Codespaces!

## ✨ Was passiert automatisch?

Wenn du einen Codespace erstellst, werden automatisch installiert:

### 🛠️ Development Tools

| Tool    | Version | Zweck                        |
| ------- | ------- | ---------------------------- |
| Node.js | LTS     | JavaScript/React Development |
| PHP     | Latest  | Backend Development          |
| Python  | 3.11    | Flask/Django Backend         |
| Git     | Latest  | Versionskontrolle            |

### 📦 VS Code Extensions (25+)

#### Web Development (5 Extensions)

- ✅ Live Server
- ✅ Prettier (Formatierung)
- ✅ ESLint (JavaScript Linting)
- ✅ HTML CSS Support
- ✅ Auto Rename Tag

#### Python Development (3 Extensions)

- ✅ Python
- ✅ Pylance (Language Server)
- ✅ Python Debugger

#### PHP Development (5 Extensions)

- ✅ PHP Intelephense
- ✅ PHP Debug (Xdebug)
- ✅ PHP DocBlocker
- ✅ PHP Namespace Resolver
- ✅ PHP CS Fixer

#### Git & Tools (4+ Extensions)

- ✅ GitLens
- ✅ GitHub Pull Requests
- ✅ Path Intellisense
- ✅ HTML CSS Class Completion

### ⚙️ Vorkonfigurierte Settings

```json
{
  "files.autoSave": "afterDelay", // Auto-Save nach 1 Sekunde
  "editor.formatOnSave": true, // Automatische Formatierung
  "editor.tabSize": 2, // 2 Spaces Einrückung
  "liveServer.settings.port": 5500, // Live Server Port
  "python.linting.enabled": true, // Python Linting
  "php.validate.enable": true // PHP Validation
}
```

### 🌐 Automatische Port-Forwarding

| Port | Service               | Aktion                        |
| ---- | --------------------- | ----------------------------- |
| 5500 | Live Server           | Öffnet automatisch im Browser |
| 8000 | PHP/Python Dev Server | Notification                  |
| 3000 | React Dev Server      | Öffnet automatisch im Browser |
| 8001 | Custom                | Nach Bedarf                   |

## 🎯 Für Schüler: So nutzt du es

### Neuen Codespace erstellen

1. Gehe zu deinem GitHub Repository
2. Klicke auf **Code** → **Codespaces** → **Create codespace on main**
3. ⏳ Warte 2-3 Minuten
4. ✅ **Fertig!** Alle Tools sind installiert

### Prüfen, ob alles funktioniert

```bash
# Im Terminal eingeben:
node --version    # ✓ Node.js
php --version     # ✓ PHP
python3 --version # ✓ Python
git --version     # ✓ Git
```

### Extensions checken

1. Klicke auf Extensions-Symbol (links)
2. Scrolle durch die Liste
3. Alle sollten mit ✅ markiert sein

## 📖 Für Lehrkräfte: Setup & Wartung

### Initial Setup (bereits erledigt ✅)

Die Konfiguration ist bereits aktiv durch:

- `.devcontainer/devcontainer.json` - Hauptkonfiguration
- `.vscode/extensions.json` - Extension-Empfehlungen (Fallback für lokale Entwicklung)
- `.vscode/settings.json` - Workspace Settings

### Neue Extensions hinzufügen

1. Bearbeite `.devcontainer/devcontainer.json`
2. Füge Extension-ID unter `customizations.vscode.extensions` hinzu:

```json
"extensions": [
  "existierende.extension",
  "neue.extension-id"
]
```

3. Commit & Push
4. Schüler: Codespace neu erstellen oder rebuilden

### Settings anpassen

Bearbeite `.devcontainer/devcontainer.json` unter `customizations.vscode.settings`:

```json
"settings": {
  "editor.fontSize": 16,
  "dein-setting": "dein-wert"
}
```

### Bestehende Codespaces aktualisieren

Schüler müssen Container rebuilden:

1. `Cmd/Ctrl + Shift + P`
2. "Codespaces: Rebuild Container"
3. ⏳ Warten (~2 Minuten)
4. ✅ Alle neuen Extensions sind da

## 🔄 Update-Workflow

```bash
# 1. Lokale Änderungen
vim .devcontainer/devcontainer.json

# 2. Testen in eigenem Codespace
# Rebuild Container & Prüfen

# 3. Committen
git add .devcontainer/
git commit -m "chore: Update devcontainer config"
git push

# 4. Schüler informieren
# "Bitte Codespace neu erstellen oder rebuilden"
```

## 🎓 Für GitHub Classroom

### Vorteile

- ✅ **Einheitliche Umgebung**: Alle haben die gleichen Tools
- ✅ **Zero Setup Time**: Schüler können sofort loslegen
- ✅ **Keine IT-Probleme**: "Bei mir geht's nicht" gehört der Vergangenheit an
- ✅ **Best Practices**: Automatische Code-Formatierung & Linting
- ✅ **Skalierbar**: Funktioniert für 1 oder 100 Schüler

### Template-Repository Setup

1. Repository als **Template** markieren (GitHub Settings)
2. DevContainer-Konfiguration ist bereits drin ✅
3. GitHub Classroom Assignment erstellen
4. Schüler akzeptieren Assignment
5. Codespace erstellen → Automatisch konfiguriert! 🎉

## 🐛 Troubleshooting

### Problem: Extensions fehlen

**Ursache:** Container wurde nicht neu gebaut

**Lösung:**

```
Cmd/Ctrl + Shift + P → "Codespaces: Rebuild Container"
```

### Problem: Port nicht erreichbar

**Lösung:**

1. Terminal → "Ports" Tab
2. Klick auf Port → "Port Visibility" → "Public"

### Problem: Settings werden ignoriert

**Ursache:** User Settings überschreiben Workspace Settings

**Lösung:**

- DevContainer Settings haben höchste Priorität
- Falls nicht: Rebuild Container

### Problem: Zu langsamer Build

**Optimierung:**

- Pre-built Container nutzen (Advanced)
- Unnötige Extensions entfernen
- `postCreateCommand` optimieren

## 📚 Dokumentation

- **DevContainer Konfiguration:** [README.md](README.md)
- **VS Code DevContainers:** https://code.visualstudio.com/docs/devcontainers/containers
- **GitHub Codespaces:** https://docs.github.com/en/codespaces
- **Container Features:** https://containers.dev/features

## 🎉 Erfolgsgeschichten

### Vorher

- ❌ Schüler: "Meine Extensions funktionieren nicht"
- ❌ Lehrer: 30 Minuten Support pro Schüler
- ❌ Unterschiedliche Setups → Debugging schwierig

### Nachher

- ✅ Schüler: Codespace starten → Sofort loslegen!
- ✅ Lehrer: Kein Setup-Support mehr nötig
- ✅ Einheitliche Umgebung → Fokus auf Code, nicht auf Config

---

**🚀 Bereit für den Unterricht? Einfach Codespace erstellen und loslegen!**
