# Phase 1 – Konzeption & Design (60%)

## Ziele (Ergebnisse am Ende von Phase 1)
- Firmenname final (aus Survey)
- App‑Name für Mitfahrgelegenheits‑App final (aus Survey)
- Corporate Design Guide (Farben, Typografie, Logo‑Usage)
- Wireframes (Low‑Fi) für Start, Projekte, Services, Kontakt
- Content‑Strategie (Texte, Bildkonzept)

---

## Schritt-für-Schritt

### Schritt 1: Namensfindung (30–45 Min)
Ziel: Finaler Firmenname und App‑Name für die Mitfahrgelegenheits‑App.

1. Firmenname bewerten:
	- Öffne `../surveys/name_survey/form.html` im Browser (Rechtsklick → "Open with Live Server" oder Doppelklick).
	  **Hinweis:** Pfad von `phase1-concept/` aus gesehen: `../surveys/name_survey/form.html`
	- Bewerte jeden vorgeschlagenen Namen (Skala 1–5).
	- Ergänze eigene Namensideen (Freitextfeld) falls du bessere findest.
	- Klicke auf "Export" / "Download" (Form erzeugt eine JSON-Datei).
	- Benenne die Datei um zu: `results/firmenname_<datum>.json` (z.B. `results/firmenname_2025-11-30.json`).

2. App‑Name (Mitfahrgelegenheiten) bewerten:
	- Öffne `../../aufgabe/surveys/app_names/form.html` im Browser.
	- Bewerte die Arbeitsnamen und ergänze eigene Vorschläge.
	- Speichere die JSON-Ausgabe als `results/appname_mitfahr_<datum>.json`.

3. (Optional) Auswertung automatisieren:
	- Führe im Terminal (Repository-Wurzel) das Python-Skript aus:
	  ```bash
	  cd version3/aufgabe/surveys/name_survey
	  python3 process.py
	  cd ../app_names
	  python3 process.py
	  ```
	- Lege erzeugte Auswertungsdateien (`results.md` / Ranking) ebenfalls in `results/` ab (aktueller Ordner: phase1-concept/).

4. Ergebnis festhalten:
	- Wähle jeweils den höchstbewerteten Namen ODER begründe eine bewusste Abweichung.
	- Erstelle `results/names.json` mit folgendem Format:
	  ```json
	  {
		 "firma": "Mission Future Academy",
		 "app_mitfahr": "RideShare@School",
		 "alternativen_firma": ["EduEco Labs", "GreenMind Tech"],
		 "alternativen_app": ["SchulMobil", "EcoRide"],
		 "entscheidung_begruendung": "Gewählt wegen Klarheit, Nachhaltigkeitsbezug und Merkfähigkeit."
	  }
	  ```

5. Commit nicht vergessen:
	```bash
	git add version3/aufgabe/phase1-concept/results/
	git commit -m "docs: Namen für Firma und Mitfahr-App festgelegt"
	```

Ergebnis: Finaler Firmenname + App‑Name (Mitfahrgelegenheiten) dokumentiert.

**Automatische Validierung (Empfohlen):**

Bevor du Phase 1 abschließt, prüfe ob deine `names.json` korrekt ist:
```bash
python3 scripts/validate_names.py
```
Ausgabe-Beispiele:
- `✅ Struktur valide` → Alles gut.
- `⚠️ Begründung sehr kurz` → Ergänze mehr Argumente.
- `❌ Schlüssel fehlt: firma` → Struktur korrigieren.

Wenn du einen Pull Request erstellst oder pushst, läuft diese Prüfung automatisch (Workflow: `Validate Names Artifact`).

### Schritt 2: Corporate Design (90–120 Min)
- Nutze `templates/corporate-design-template.md`
- Definiere Farbpalette (Primär, Sekundär, Akzent) mit Begründung
- Wähle 2 Fonts (Headline + Fließtext) aus Google Fonts mit Begründung
- Lege Logo‑Usage fest (Schutzraum, Mindestgröße, Varianten)

### Schritt 3: Wireframes & Sitemap (90 Min)
- Erstelle eine Sitemap für 4+ Seiten
- Erstelle Low‑Fi‑Wireframes (nutze `templates/wireframe-vorlage.svg` oder Papier)
- Begründe das gewählte Layout (Lesbarkeit, Hierarchie, Fokus)

### Schritt 4: Content‑Strategie (60 Min)
- Formuliere Mission‑Statement, Tagline und Projektbeschreibungen
- Lege Bildkonzept fest (eigene Bilder/Stock, Stil, Farben)

---

## Abgabe (checkliste)
- [ ] `results/names.json` (Firmenname + App‑Name)
- [ ] `corporate-design.md` (Farben, Typografie, Logo‑Usage)
- [ ] `sitemap.md` + `wireframes.pdf/png` (Low‑Fi)
- [ ] `content-strategie.md` (Texte, Bildkonzept)

