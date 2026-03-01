# Shared Resources

Zentrale Ressourcen, die **sprach-übergreifend** verwendet werden.

## 📁 Verzeichnisstruktur

```
shared/
├── README.md (diese Datei)
├── rubrics.json           # Zentrale Bewertungsrubriken
├── templates/             # Vorlagen für neue Exams
└── structogramme/         # Allgemeine Standards
```

## 📊 rubrics.json

**Zentrale Bewertungsrubriken** für alle Sprachen und Themen.

### Struktur

```json
{
  "rubrics": {
    "aufgabe_a": { "punkte": 5.0, "beschreibung": "..." },
    "aufgabe_b": { "punkte": 7.5, "beschreibung": "..." },
    "aufgabe_c": { "punkte": 6.0, "beschreibung": "..." },
    "aufgabe_d": { "punkte": 6.5, "beschreibung": "..." }
  },
  "theme_adaptations": {
    "basics": {
      /* anpassungen */
    },
    "datenstrukturen": {
      /* anpassungen */
    }
  },
  "metadata_schema": {
    /* JSON-Schema */
  }
}
```

### Verwendung

- **Validierung:** `python3 scripts/validate_exams.py`
- **Neue Themen:** `theme_adaptations` erweitern
- **Export:** Für Online-Exams, PDF-Export, LMS-Integration

**⚠️ Wichtig:** Diese Datei ist die **Single Source of Truth** für alle Bewertungen. Änderungen wirken sich auf alle Exams aus.

## 📄 templates/

Vorlagen für neue Exams:

| Template                                | Beschreibung                    | Status     |
| --------------------------------------- | ------------------------------- | ---------- |
| **exam_template.md**                    | Basis-Template (generisch)      | ✅ Ready   |
| **exam_datenstrukturen_template.md**    | Template für Datenstrukturen    | ⏳ Geplant |
| **exam_funktionen_template.md**         | Template für Funktionen         | ⏳ Geplant |
| **exam_kontrollstrukturen_template.md** | Template für Kontrollstrukturen | ⏳ Geplant |
| **exam_dateien_template.md**            | Template für Dateien            | ⏳ Geplant |
| **exam_datenbank_template.md**          | Template für Datenbank          | ⏳ Geplant |

### Template verwenden

```bash
# 1. Template kopieren
cp shared/templates/exam_template.md [sprache]/[thema]/exam.md

# 2. Anpassen:
#    - Kontext ändern (Aufgaben-Formulierung)
#    - Zahlen/Werte variieren
#    - Syntax an Sprache anpassen

# 3. Varianten erstellen (v2, v3, v4)
cp [sprache]/[thema]/exam.md [sprache]/[thema]/exam_v2.md
# ... anpassen ...

# 4. Lösungen schreiben
cp [sprache]/[thema]/exam.md [sprache]/[thema]/solutions.md
# ... Lösungen einfügen ...

# 5. Validierung
python3 scripts/validate_exams.py --language [sprache]
```

## 📐 structogramme/

Allgemeine Standards für **Struktogramme** (Nassi-Shneiderman-Diagramme).

**Inhalt:**

- Konventionen für Symbole
- Beispiele
- Best Practices

**Status:** ⏳ Geplant (zukünftige Phase)

## 🔄 Erweiterbarkeit

### Neue Rubrik hinzufügen

1. **rubrics.json** bearbeiten:

   ```json
   {
     "rubrics": {
       "aufgabe_e": {
         "punkte": 5.0,
         "beschreibung": "Neue Aufgabe",
         "bewertungsschritte": [...]
       }
     }
   }
   ```

2. **Validierung anpassen** (falls nötig):
   - `scripts/validate_exams.py` → Punktesumme aktualisieren

3. **Templates aktualisieren**:
   - Neue Aufgabe in Templates einfügen

### Neues Thema hinzufügen

1. **Template erstellen**:

   ```bash
   cp shared/templates/exam_template.md shared/templates/exam_[thema]_template.md
   # ... anpassen ...
   ```

2. **theme_adaptations** in rubrics.json ergänzen:

   ```json
   {
     "theme_adaptations": {
       "[thema]": {
         "aufgabe_a": { "beschreibung": "..." }
       }
     }
   }
   ```

3. **Dokumentation aktualisieren**:
   - README.md (Themen-Übersicht)
   - ARCHITECTURE.md (Roadmap)

## 📖 Dokumentation

- **[ARCHITECTURE.md](../ARCHITECTURE.md)** – Design-Prinzipien, Roadmap
- **[README.md](../README.md)** – Hauptdokumentation
- **[scripts/validate_exams.py](../../../../../../scripts/validate_exams.py)** – Validierungs-Script

---

**Zurück zu:** [Exam-System Übersicht](../)
