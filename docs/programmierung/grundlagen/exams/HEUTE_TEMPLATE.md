# 📅 HEUTE.md – Daily Template

> **Dieses Template jeden Tag kopieren und aktualisieren**

---

## Verwendung

```bash
# Jeden Abend: HEUTE.md für morgen vorbereiten
cd /workspaces/web-project-dynamic/docs/programmierung/grundlagen/exams

# Datum anpassen, TODOs aktualisieren
```

---

## Template

```markdown
# 📅 Heute: [Wochentag], [DD.MM.YYYY]

> **Phase [X]:** [Status] – Tag [N] von 81

---

## ✅ Was heute erreicht wurde

1. ✅ [Aufgabe 1]
2. ✅ [Aufgabe 2]
3. ✅ [Aufgabe 3]

---

## 📋 Morgen ([Wochentag], [DD.MM.YYYY])

**Tag [N+1]: [Thema] – [Untertitel]**

### Zeitplan

**08:00–09:00** – [Aufgabe]

- [ ] [Detail 1]
- [ ] [Detail 2]

**09:00–11:00** – [Aufgabe]

- [ ] [Detail]

**11:00–12:00** – [Aufgabe]

- [ ] [Detail]

**12:00–13:00** – Mittagspause 🍽️

**14:00–15:00** – [Aufgabe]

- [ ] [Detail]

**15:00–17:00** – [Puffer/Aufgabe]

---

## 📊 Fortschritt

**Phase 2 Fortschritt:**
```

Woche 1: Datenstrukturen [#### ] 50%
Woche 2: Funktionen [ ] 0%
Woche 3: Kontrollstrukturen [ ] 0%
Woche 4: Dateien + DB [ ] 0%

```

**Gesamt:** [X]/81 Tage = [Y]%

---

## 💡 Notizen

- [Erkenntnisse des Tages]
- [Offene Fragen]
- [Ideen für später]

---

**Nächster Eintrag:** [DD.MM.YYYY]
```

---

## Beispiel (ausgefüllt)

```markdown
# 📅 Heute: Montag, 03.03.2026

> **Phase 2:** Themen-Ausbau – Tag 1 von 81

---

## ✅ Was heute erreicht wurde

1. ✅ Template `exam_datenstrukturen_template.md` finalisiert
2. ✅ JavaScript `datenstrukturen/exam.md` (v1) geschrieben
3. ✅ Lösungen `solutions.md` erstellt
4. ✅ Validierung erfolgreich (0 Fehler)
5. ✅ Commit + Push

---

## 📋 Morgen (Dienstag, 04.03.2026)

**Tag 2: Datenstrukturen – JavaScript v2–v4**

### Zeitplan

**08:00–10:00** – exam_v2.md

- [ ] Kontext ändern (neues Beispiel wählen)
- [ ] Zahlen/Werte variieren
- [ ] Strukturogramme anpassen (falls vorhanden)

**10:00–12:00** – exam_v3.md

- [ ] Erstellung
- [ ] Review

**12:00–13:00** – Mittagspause 🍽️

**14:00–16:00** – exam_v4.md

- [ ] Erstellung
- [ ] Review

**16:00–17:00** – Lösungen

- [ ] solutions_v2.md
- [ ] solutions_v3.md
- [ ] solutions_v4.md

**17:00–17:30** – Validierung + Commit

---

## 📊 Fortschritt

**Phase 2 Fortschritt:**
```

Woche 1: Datenstrukturen [## ] 25%
Woche 2: Funktionen [ ] 0%
Woche 3: Kontrollstrukturen [ ] 0%
Woche 4: Dateien + DB [ ] 0%

```

**Gesamt:** 1/81 Tage = 1.2%

---

## 💡 Notizen

- Array-Methoden in JavaScript: map/filter/reduce sehr beliebt
- Nested Arrays: Schwierigkeit gut dosiert bei 6.0 Punkten
- Idee: Visualisierungen für Datenstrukturen (Phase 3?)

---

**Nächster Eintrag:** 04.03.2026
```

---

## Automatisierung (Optional für später)

```python
# scripts/update_heute.py
import datetime

def generate_heute_md(date, phase, day, tasks):
    template = f"""# 📅 Heute: {date.strftime('%A, %d.%m.%Y')}

> **Phase {phase}:** ... – Tag {day} von 81

---

## ✅ Was heute erreicht wurde

{chr(10).join([f'{i+1}. ✅ {task}' for i, task in enumerate(tasks)])}

---

[... rest of template ...]
"""
    return template

# Verwendung:
today = datetime.date.today()
tasks = ["Aufgabe 1", "Aufgabe 2"]
md = generate_heute_md(today, 2, 5, tasks)
print(md)
```

---

**Letzte Aktualisierung:** 01.03.2026
