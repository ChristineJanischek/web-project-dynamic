# Shared Resources

Zentrale Ressourcen, die **sprach-übergreifend** verwendet werden.

## 📁 Verzeichnisstruktur

```
shared/
├── README.md (diese Datei)
├── rubrics.json           # Zentrale Bewertungsrubriken
├── variation_knowledge_base.json # Aufgaben-Fingerprints
├── variation_knowledge_base_schema.json # Schema fuer Aufgaben-Fingerprints
├── solution_rubrics_knowledge_base.json # Maschinenlesbare Bewertungslogik
├── solution_rubrics_schema.json # Schema fuer Bewertungslogik
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

| Template                                | Beschreibung                      | Status     |
| --------------------------------------- | --------------------------------- | ---------- |
| **exam_template.md**                    | Basis-Template (generisch)        | ✅ Ready   |
| **solutions_template.md**               | Musterlösung mit Bewertungslogik | ✅ Ready   |
| **exam_datenstrukturen_template.md**    | Template für Datenstrukturen      | ⏳ Geplant |
| **exam_funktionen_template.md**         | Template für Funktionen           | ⏳ Geplant |
| **exam_kontrollstrukturen_template.md** | Template für Kontrollstrukturen   | ⏳ Geplant |
| **exam_dateien_template.md**            | Template für Dateien              | ⏳ Geplant |
| **exam_datenbank_template.md**          | Template für Datenbank            | ⏳ Geplant |

### Template verwenden

```bash
# 1. Template kopieren
cp shared/templates/exam_template.md [sprache]/[thema]/exam.md

# 2. Anpassen:
#    - Kontext ändern (Aufgaben-Formulierung)
#    - Zahlen/Werte variieren
#    - Syntax an Sprache anpassen

# 3. Varianten erstellen (v2, v3, v4, ...)
cp [sprache]/[thema]/exam.md [sprache]/[thema]/exam_v2.md
# ... anpassen ...

# 4. Lösungen schreiben
cp [sprache]/[thema]/exam.md [sprache]/[thema]/solutions.md
# ... Lösungen einfügen ...

# 5. Validierung + Wissensdatenbank
python3 scripts/validate_exams.py --language [sprache] --write-knowledge-base
```

## 🧠 variation_knowledge_base.json

Diese Datei wird automatisch erzeugt und enthält Fingerprints pro Aufgabe (A-D) je Variante.
Sie dient als technische Wissensdatenbank, um identische Aufgabenstellungen zu erkennen und bei neuer Variantenerstellung aktiv zu vermeiden.

**Aktualisierung:**

```bash
python3 scripts/validate_exams.py --write-knowledge-base
```

**Best Practice für neue Varianten:**

1. Neue Variante schreiben (gleiche Struktur, neue Aufgabenstellung)
2. Validierung inkl. Duplikatcheck ausfuehren
3. Knowledge-Base aktualisieren und committen

## 🧠 solution_rubrics_knowledge_base.json

Diese Datei wird aus allen `solutions*.md` erzeugt und enthält pro Aufgabe:

- Punktegesamtwert
- detaillierte Bewertungskriterien (`Punktbewertung`)
- typische Fehler (`Haeufige Fehler`)
- stabile `criterion_id` und `criterion_family_id` für Auto-Grading und Analytics

Sie ist die Grundlage für spaeteres teilautomatisches oder automatisches Grading im eLearning.

## 🧠 Schema-Dateien

Die folgenden Schema-Dateien definieren den technischen Vertrag der Wissensdatenbanken:

- `variation_knowledge_base_schema.json`
- `solution_rubrics_schema.json`

Sie werden durch `scripts/validate_exams.py` aktiv zur Validierung verwendet.

**Aktualisierung:**

```bash
python3 scripts/validate_exams.py --write-knowledge-base
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
