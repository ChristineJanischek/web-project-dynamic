# 🔄 Template Sync Setup - Automatische Synchronisation

## ✅ Status

Die GitHub Action für automatisches Template-Sync ist **installiert und einsatzbereit**!

Datei: `.github/workflows/template-sync.yml`

---

## 📋 Konfigurationsschritte

### 1️⃣ Personal Access Token erstellen

1. Gehe zu **GitHub Settings** → [Personal Access Tokens (classic)](https://github.com/settings/tokens)
2. Klicke auf **Generate new token (classic)**
3. Gib dem Token einen Namen: `Template Sync Bot`
4. Wähle folgende Berechtigungen:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
5. Klicke **Generate token**
6. **Kopiere den Token sofort** (wird nur einmal angezeigt!)

---

### 2️⃣ Token als Secret hinzufügen

1. Gehe zu deinem Repository **web-project-dynamic**
2. Navigiere zu **Settings** → **Secrets and variables** → **Actions**
3. Klicke **New repository secret**
4. Name: `TEMPLATE_SYNC_TOKEN`
5. Value: *Füge deinen kopierten Token ein*
6. Klicke **Add secret**

---

### 3️⃣ Abhängige Repositories konfigurieren

Öffne `.github/workflows/template-sync.yml` und aktualisiere die Repository-Liste:

```yaml
env:
  DEPENDENT_REPOS: |
    ChristineJanischek/web-project-student-example
    ChristineJanischek/web-project-klasse-10a
    ChristineJanischek/web-project-klasse-10b
```

**Beispiel für GitHub Classroom:**

```yaml
env:
  DEPENDENT_REPOS: |
    github-classroom-org/web-project-max-mustermann
    github-classroom-org/web-project-anna-schmidt
    github-classroom-org/web-project-tom-weber
```

---

## 🚀 Verwendung

### Automatisch (Standard)

Die Action läuft automatisch bei jedem Push in `main`, wenn folgende Dateien geändert wurden:
- `docs/**` (Dokumentation)
- `version*/**` (Versionen)
- `templates/**` (Projekt-Templates)
- `scripts/**` (Hilfsskripte)
- `README.md`, `ARCHITECTURE.md`, etc.

### Manuell triggern

1. Gehe zu **Actions** Tab
2. Wähle **🔄 Template Sync to Dependent Repos**
3. Klicke **Run workflow**
4. Optional: Aktiviere "Force sync" um alle Repos zu synchronisieren

---

## 📊 Was passiert bei der Synchronisation?

1. **Änderungen erkennen:** Action prüft, welche Template-Dateien sich geändert haben
2. **Branch erstellen:** In jedem abhängigen Repo wird ein neuer Branch `template-sync-YYYYMMDD-HHMMSS` erstellt
3. **Dateien kopieren:** Nur Template-Dateien werden übernommen (Schülerarbeiten bleiben unberührt!)
4. **Pull Request erstellen:** Automatischer PR mit Beschreibung der Änderungen
5. **Review & Merge:** Lehrende können den PR prüfen und mergen

---

## 🔒 Geschützte Dateien (werden NICHT überschrieben)

Die Action schützt automatisch:
- ✅ `version*/aufgabe/index.html` (Schülerarbeiten)
- ✅ `version*/aufgabe/css/style.css`
- ✅ `version*/aufgabe/js/script.js`
- ✅ `version*/loesung/` (Musterlösungen - nur für Lehrende)
- ✅ `**/projects/*` (Schülerprojekte)
- ✅ `**/surveys/*/results` (Umfrageergebnisse)

---

## ⏭️ Sync für einzelnes Repo deaktivieren

Falls ein Repository keine Updates mehr erhalten soll:

```bash
# Im jeweiligen Repo:
touch .template-sync-ignore
git add .template-sync-ignore
git commit -m "Disable template sync"
git push
```

---

## 🧪 Test-Lauf

So testest du die Action:

1. Mache eine kleine Änderung in `docs/intro.md`
2. Committe und pushe nach `main`
3. Gehe zu **Actions** Tab → Schau den Workflow-Lauf an
4. Prüfe das abhängige Repository auf den neuen PR

---

## 🔍 Troubleshooting

### ❌ "TEMPLATE_SYNC_TOKEN not configured"

**Lösung:** Siehe Schritt 1 & 2 oben - Token muss erstellt und als Secret hinzugefügt werden.

### ❌ "Failed to clone [repo]"

**Mögliche Ursachen:**
- Token hat keine Berechtigung für das Ziel-Repository
- Repository existiert nicht oder ist falsch geschrieben
- Repository ist privat und Token hat keine `repo` Berechtigung

**Lösung:** Prüfe Token-Berechtigungen und Repository-Namen.

### ❌ "PR creation failed"

**Mögliche Ursachen:**
- GitHub CLI (`gh`) konnte nicht authentifizieren
- Branch existiert bereits
- Keine Änderungen zum Committen

**Lösung:** Prüfe GitHub Action Logs für Details.

---

## 📚 Weiterführende Dokumentation

- [TEMPLATE_SYNC.md](../../TEMPLATE_SYNC.md) - Manuelle Sync-Anleitung
- [TEMPLATE_UPDATE_STRATEGY.md](../../TEMPLATE_UPDATE_STRATEGY.md) - Update-Strategien
- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)

---

## 💡 Tipps für Lehrende

### Staged Rollout (schrittweise Verteilung)

Statt alle Repos auf einmal zu aktualisieren:

1. Teste zuerst mit einem Test-Repository:
   ```yaml
   DEPENDENT_REPOS: |
     ChristineJanischek/web-project-test
   ```

2. Bei Erfolg erweitere auf eine Klasse:
   ```yaml
   DEPENDENT_REPOS: |
     github-classroom/web-project-klasse-10a-*
   ```

3. Dann auf alle Klassen ausweiten

### Kommunikation mit Schülern

Erstelle ein Issue-Template für automatische PRs, damit Schüler wissen was zu tun ist:

```markdown
## 📢 Neues Template-Update verfügbar!

Euer Lehrer hat die Dokumentation aktualisiert.

**Was tun?**
1. Schau dir die Änderungen im "Files changed" Tab an
2. Wenn alles gut aussieht, klicke "Merge pull request"
3. Bei Fragen: Schreibe einen Kommentar in diesem PR

**Keine Sorge:** Eure Arbeiten in `aufgabe/` bleiben unverändert! ✅
```

---

**Status:** ✅ Bereit zur Verwendung  
**Version:** 1.0  
**Zuletzt aktualisiert:** 4. Dezember 2025
