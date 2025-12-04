# 🎯 Classroom Repos Finder - Anleitung

Dieses Skript hilft Ihnen, alle Repos aus Ihrer GitHub Classroom-Seite zu finden und automatisch in `DEPENDENT_REPOS` einzutragen.

## 🚀 Schnellstart

### Option 1: Mit GitHub CLI (Empfohlen)

```bash
# Wenn Sie die Organisation kennen:
python3 scripts/find_classroom_repos.py <ORGANISATION> [PATTERN]

# Beispiele:
python3 scripts/find_classroom_repos.py github-classroom-webentwicklung web-project
python3 scripts/find_classroom_repos.py ChristineJanischek web-project
```

### Option 2: Manuelle Methode (Browser-Konsole)

1. Öffne: https://classroom.github.com/classrooms/190190248-webentwicklung
2. Drücke `F12` (Browser-Konsole)
3. Gehe zum "Console" Tab
4. Kopiere und führe folgendes aus:

```javascript
// Finde alle Repository-Links
const repos = Array.from(
  document.querySelectorAll('a[href*="github.com"]')
)
.map(link => {
  const url = link.getAttribute('href');
  const match = url.match(/github\.com\/([\w-]+)\/([\w-]+)/);
  if (match) return `${match[1]}/${match[2]}`;
  return null;
})
.filter(Boolean)
.filter(repo => repo.includes('web-project'))
.sort();

// Ausgabe im YAML Format
console.log('env:\n  DEPENDENT_REPOS: |');
repos.forEach(repo => console.log(`    ${repo}`));
```

5. Kopiere den Output
6. Trage ihn in `.github/workflows/template-sync.yml` ein

## 📋 Häufige Organisationen

Versuchen Sie diese Organisationen in dieser Reihenfolge:

1. `ChristineJanischek` - Direkt unter Ihrem Benutzernamen
2. `github-classroom-webentwicklung` - Nach dem Klassenzimmer-Namen
3. `github-classroom-190190248` - Nach der Klassenzimmer-ID (aus URL)
4. `github-classroom-ws2024` - Nach Semester/Jahrgang

## 🔍 Script-Beispiele

```bash
# Zeige alle Repos einer Organisation
python3 scripts/find_classroom_repos.py github-classroom-webentwicklung

# Nur Repos mit "web" im Namen
python3 scripts/find_classroom_repos.py github-classroom-webentwicklung web

# Debugging: Zeige erste 10 Repos
gh repo list github-classroom-webentwicklung --limit 10
```

## 🛠️ Fehlerbehebung

### "Fehler beim Zugriff auf Organisation"

- Stelle sicher dass GitHub CLI installiert ist: `gh --version`
- Du bist authentifiziert: `gh auth status`
- Die Organisation existiert: `gh org list`
- Du hast Zugriff auf die Organisation

### "Keine Repos gefunden"

- Prüfe ob die Organisation korrekt ist
- Versuche eine andere Organisation aus der Liste oben
- Nutze die manuelle Browser-Methode

### "Pattern passt nicht"

Das Script filtert nach "web-project" standardmäßig.
Ändere das Pattern:

```bash
python3 scripts/find_classroom_repos.py <ORG> <PATTERN>

# Beispiele:
python3 scripts/find_classroom_repos.py github-classroom-webentwicklung webdev
python3 scripts/find_classroom_repos.py github-classroom-webentwicklung ""  # Alle Repos
```

## 📚 Was ist DEPENDENT_REPOS?

Das ist die Liste aller Schüler-Repositories, die bei jedem Push automatisch synchronisiert werden.

Format:
```yaml
env:
  DEPENDENT_REPOS: |
    owner/repository-1
    owner/repository-2
    owner/repository-3
```

**WICHTIG:** Alle Repos müssen tatsächlich existieren!

## ✅ Nächste Schritte

1. **Finde die Repos** mit diesem Script oder der Browser-Methode
2. **Kopiere den Output** im YAML Format
3. **Öffne** `.github/workflows/template-sync.yml`
4. **Ersetze** Zeile 31-45 mit dem Output
5. **Speichern** (Ctrl+S)
6. **Commit**: `git add -A && git commit -m "Configure DEPENDENT_REPOS"`
7. **Push**: `git push`
8. **Teste** im Actions Tab

---

**Benötigst Du Hilfe?** Sieh dir `.github/DEPENDENT_REPOS_ANLEITUNG.md` an!
