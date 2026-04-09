# Roadmap Courses

# Marschplan fuer `edu-code-lab-courses`

Stand: Maerz 2026

---

# 1 Mission

`edu-code-lab-courses` liefert didaktisch hochwertige Informatik-Inhalte auf Basis der `core`-Plattform.

---

# 2 Phasenplan

## Phase 0 - Inhaltsrahmen und Struktur (2 bis 4 Wochen)

Ziele:

- einheitliche Kursstruktur festlegen
- Metadaten- und Bewertungsstandard verbindlich machen
- Themenkatalog aus [COURSES_THEMENPLAN.md](COURSES_THEMENPLAN.md) uebernehmen

Lieferobjekte:

- strukturierte Ordnerkonvention
- Aufgaben-Template fuer Autoren
- Freigaberegeln fuer Inhalte

## Phase 1 - Kernfaecher Informatik (6 bis 10 Wochen)

Ziele:

- Mindestabdeckung zentraler Themenbereiche
- je Themenbereich mindestens ein lauffaehiger Referenzkurs

Lieferobjekte:

- Grundlagen Programmierung (funktional)
- Webentwicklung
- Datenbanken
- Vertiefung OOP (Software Engineering)
- Künstliche Intelligenz mit Maschine Learning

## Phase 2 - Vertiefung und Differenzierung (8 bis 12 Wochen)

Ziele:

- mehrere Niveaustufen (Basis/Fortgeschritten)
- didaktische Varianten fuer unterschiedliche Lernwege

Lieferobjekte:

- Variantenbibliothek
- Fehlerkataloge je Themenfeld
- differenzierte Bewertungsraster

## Phase 3 - Qualitaet, Betrieb und Skalierung (laufend)

Ziele:

- stabile Content-Qualitaetsprozesse
- regelmaessige Releases und Wartung
- Lehrkraefte-Feedback in Iterationen einbauen

Lieferobjekte:

- Release-Rhythmus fuer Inhalte
- kuratierte Updates je Themenbereich
- dokumentierte Qualitaetsmetriken

---

# 3 Pflichtumfang fuer "alle Themen der Informatik"

"Alle Themen" bedeutet hier ein verbindlicher Mindestkatalog, der mindestens folgende Bereiche enthaelt:

1. Programmiergrundlagen
2. Algorithmen und Datenstrukturen
3. Objektorientierung
4. Webentwicklung (Frontend/Backend)
5. Datenbanken und Datenmodellierung
6. Software Engineering und Versionskontrolle
7. Modellierung (UML/BPMN/Struktogramme)
8. IT-Sicherheit und Datenschutz
9. KI/ML-Grundlagen

Die Detailauspraegung liegt in [COURSES_THEMENPLAN.md](COURSES_THEMENPLAN.md).

---

# 4 Abhaengigkeiten zu core

- neue Content-Typen nur auf stabilen core-Schnittstellen
- bei core-Breaking-Changes: geplanter Migrationszyklus
- courses-Releases referenzieren kompatible core-Versionen

---

# 5 Definition of Done pro Kursrelease

Ein Kursrelease gilt als fertig, wenn:

1. Metadaten vollstaendig sind
2. Aufgaben und Loesungen konsistent sind
3. Content-Checks in CI erfolgreich laufen
4. Lernziele und Bewertungslogik nachvollziehbar dokumentiert sind

