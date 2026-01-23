# 🎯 DEPENDENT_REPOS - Konfigurationsanleitung

## Was ist DEPENDENT_REPOS?

Die Liste aller **Schüler-Repositories**, die bei jedem Push automatisch aktualisiert werden sollen.

---

## 📝 Wie trage ich meine Repos ein?

### **Schritt 1: Finde deine Schüler-Repos**

**Option A: Manuell (im Browser)**

1. Gehe zu: `https://github.com/ChristineJanischek?tab=repositories`
2. Suche nach "web-project"
3. Notiere alle gefundenen Repos

**Option B: Mit GitHub CLI (schneller!)**

```bash
gh repo list ChristineJanischek --limit 1000 | grep "web-project"
```

Output:
```
ChristineJanischek/web-project-student-1
ChristineJanischek/web-project-student-2
ChristineJanischek/web-project-student-3
```

**Option C: GitHub Classroom (am einfachsten!)**

1. Gehe zu deiner Classroom: `https://classroom.github.com`
2. Wähle dein Assignment
3. Alle Schüler-Repos sind dort gelistet

---

## ✏️ Beispiel-Konfigurationen

### Beispiel 1: 3 Schüler (Manuelle Repos)

```yaml
env:
  DEPENDENT_REPOS: |
    ChristineJanischek/web-project-max
    ChristineJanischek/web-project-anna
    ChristineJanischek/web-project-tom
```

**So funktioniert's:**
- ✅ Zeile 1: `ChristineJanischek/web-project-max`
- ✅ Zeile 2: `ChristineJanischek/web-project-anna`
- ✅ Zeile 3: `ChristineJanischek/web-project-tom`
- Bei jedem Push werden ALLE 3 Repos synchronisiert!

---

### Beispiel 2: GitHub Classroom (2 Klassen)

```yaml
env:
  DEPENDENT_REPOS: |
    # Klasse 10a
    github-classroom-org/web-project-max-mustermann
    github-classroom-org/web-project-anna-schmidt
    github-classroom-org/web-project-tom-weber
    
    # Klasse 10b
    github-classroom-org/web-project-lisa-mueller
    github-classroom-org/web-project-peter-schneider
```

**So funktioniert's:**
- ✅ Kommentare mit `#` sind erlaubt
- ✅ Leerzeilen zur Struktur sind OK
- ✅ Jeder Repo in einer Zeile
- ✅ Format: `owner/repository-name`

---

### Beispiel 3: Viele Schüler (20+)

```yaml
env:
  DEPENDENT_REPOS: |
    # 2024 Webentwicklung Klasse A
    github-classroom/web-project-student-01-max
    github-classroom/web-project-student-02-anna
    github-classroom/web-project-student-03-tom
    github-classroom/web-project-student-04-lisa
    github-classroom/web-project-student-05-peter
    # ... weitere Schüler ...
    github-classroom/web-project-student-20-marie
```

---

## ⚙️ Format-Regeln

### ✅ RICHTIG:

```yaml
env:
  DEPENDENT_REPOS: |
    owner/repo-name
    owner/repo-name
    owner/repo-name
```

### ❌ FALSCH (keine Pipe):

```yaml
env:
  DEPENDENT_REPOS:
    owner/repo-name
```

### ❌ FALSCH (Bindestriche):

```yaml
env:
  DEPENDENT_REPOS: |
    - owner/repo-name
    - owner/repo-name
```

### ❌ FALSCH (Keine Einrückung):

```yaml
env:
  DEPENDENT_REPOS: |
  owner/repo-name
  owner/repo-name
```

---

## 🎯 Häufige Fragen

### **F: Muss ich ALLE Schüler-Repos auflisten?**

**A:** Ja! Nur aufgelistete Repos werden synchronisiert.

Beispiel:
- ✅ `web-project-max` in Liste → bekommt Updates
- ❌ `web-project-anna` NICHT in Liste → bekommt KEINE Updates

---

### **F: Was wenn ich einen Schüler vergesse?**

**A:** Kein Problem! Sie können jederzeit neue Repos hinzufügen:

1. Bearbeite `.github/workflows/template-sync.yml`
2. Füge die neuen Repos hinzu
3. Commit & Push
4. Beim nächsten Push werden sie synchronisiert!

---

### **F: Kann ich Schüler-Repos entfernen?**

**A:** Ja, einfach aus der Liste entfernen und committen. Dann erhält dieser Repo keine Updates mehr.

---

### **F: Was ist der richtige Format für Repo-Namen?**

**A:** Format: `owner/repository-name`

Beispiele:
- ✅ `ChristineJanischek/web-project-max`
- ✅ `github-classroom-org/web-project-anna-schmidt`
- ✅ `my-org/my-project`

**NICHT:**
- ❌ `web-project-max` (fehlt owner!)
- ❌ `ChristineJanischek-web-project-max` (falsches Trennzeichen!)
- ❌ `https://github.com/ChristineJanischek/web-project-max` (keine URL!)

---

### **F: Wie finde ich owner/repo Namen?**

**A:** Schau auf die GitHub URL:

```
https://github.com/ChristineJanischek/web-project-max
                    └─────────────────────────────────┘
                              ↓
                      owner/repository-name
```

---

## 🚀 Nächste Schritte

1. **Finde deine Repos** (siehe Optionen oben)
2. **Trage sie in die Liste ein**
3. **Formatiere korrekt** (owner/repo Format)
4. **Commit & Push**
5. **Teste!** (Actions Tab → "Run workflow")

---

## 📚 Datei zum Bearbeiten

Öffne diese Datei:
```
.github/workflows/template-sync.yml
```

Finde diese Zeile (ca. Zeile 31-35):
```yaml
env:
  DEPENDENT_REPOS: |
    # Deine Repos kommen hier hin!
```

Und trage dort alle Repos ein!

---

## ✅ Prüfliste

Bevor Sie testen:

- ✅ Alle Schüler-Repos eingetragen?
- ✅ Format richtig? (owner/repo)
- ✅ Pipe (`|`) nach `DEPENDENT_REPOS:` vorhanden?
- ✅ Keine Bindestriche (`-`) am Anfang der Zeilen?
- ✅ File gespeichert und gepusht?

Dann sollte das Sync-System funktionieren! 🚀
