# Contributing Guide für Studierende

## 🎯 Wie arbeite ich mit diesem Projekt?

### Schritt 1: Repository forken/klonen
```bash
git clone <DEINE_REPO_URL>
cd web-project-dynamic
```

### Schritt 2: Mit einer Version starten
```bash
cd version1/aufgabe
```

### Schritt 3: Dateien bearbeiten
- Öffne `index.html` in deinem Editor
- Bearbeite `css/style.css` für Styling
- Teste regelmäßig im Browser (F5 zum Neuladen)

### Schritt 4: Änderungen speichern (Git)
```bash
# Status prüfen
git status

# Dateien hinzufügen
git add version1/aufgabe/

# Commit erstellen
git commit -m "Version 1: HTML-Grundgerüst erstellt"

# Hochladen
git push origin main
```

## 📋 Workflow-Tipps

### Branch-Strategie (Optional für Fortgeschrittene)
```bash
# Neuen Branch für Version erstellen
git checkout -b version1-bearbeitung

# Arbeiten...
git add .
git commit -m "Fortschritt"

# Zurück zu main
git checkout main

# Branch mergen
git merge version1-bearbeitung
```

### Best Practices
- ✅ Committe oft und mit aussagekräftigen Messages
- ✅ Teste im Browser bevor du committest
- ✅ Nutze die `docs/` Ordner als Referenz
- ✅ Schaue in `shared-examples/` für Inspiration
- ✅ Erst selbst versuchen, dann `loesung/` anschauen

## 🆘 Hilfe benötigt?

1. **Lies die Dokumentation**: `docs/` Ordner
2. **Schaue Beispiele an**: `shared-examples/`
3. **Browser DevTools**: F12 drücken und inspizieren
4. **HTML Validator**: https://validator.w3.org/
5. **Frage deinen Lehrer/Mentor**

## 🎓 Lernpfad

1. **Version 1**: HTML-Grundgerüst + CSS-Basics
2. **Version 2**: Box-Modell + Responsive Design (geplant)
3. **Version 3**: Formulare + Validierung (geplant)
4. **Version 4**: JavaScript + Interaktivität (geplant)

## ⚠️ Wichtig

- Arbeite **nur** im `aufgabe/` Ordner deiner aktuellen Version
- Ändere **keine** Dateien in `docs/` oder `shared-examples/`
- Die `loesung/` Ordner sind zur Selbstkontrolle - erst selbst probieren!

Viel Erfolg! 🚀
