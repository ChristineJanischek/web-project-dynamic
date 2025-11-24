# Datenbank (MySQL)

Speichert Daten dauerhaft in Tabellen.

## Grundbegriffe
- Tabelle: Sammlung ähnlicher Datensätze.
- Zeile (Row): Ein Eintrag.
- Spalte (Column): Merkmal/Attribut.
- Primary Key: Eindeutige Kennung.

Beispiel SQL:
```sql
CREATE TABLE schueler (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL
);
```
Weiter: `algorithmen-datenstrukturen.md`.
