# Persistentes Schreiben in und Lesen aus Dateien in JavaScript

[← Zurück zur JavaScript-Übersicht](README.md) · [Weiter: Sprachvergleich](../VERGLEICH_JS_PY_PHP_OPERATOR_DATEI_IO.md)

## Lernziele

- Textdateien, CSV-Dateien und Log-Dateien mit Node.js lesen/schreiben
- Dateioperationen in Funktionen kapseln
- Praxisnahe Abläufe testbar aufbauen

## Theorie kompakt

Diese Beispiele gelten für **Node.js** (nicht Browser-JavaScript). Für Dateioperationen wird das Modul `fs` genutzt.

- CSV eignet sich für tabellarische Exportdaten
- Log-Dateien dokumentieren Ereignisse mit Zeitstempel
- Funktionen halten Lese-/Schreiblogik wiederverwendbar

## Deklaration & Implementierung

### Einfaches Beispiel: Notiz speichern und lesen

```javascript
const fs = require("fs");

function speichereNotiz(dateiPfad, text) {
  fs.writeFileSync(dateiPfad, text + "\n", "utf8");
}

function leseNotiz(dateiPfad) {
  return fs.readFileSync(dateiPfad, "utf8").trim();
}

speichereNotiz("notiz.txt", "Projektstart erfolgreich");
console.log("Test Notiz:", leseNotiz("notiz.txt"));
```

### Komplexeres Beispiel: CSV-Export und Ereignis-Logging

```javascript
const fs = require("fs");

function schreibeBestellungenAlsCsv(dateiPfad, bestellungen) {
  const header = "id,kunde,betrag,status";
  const zeilen = bestellungen.map((eintrag) => {
    return `${eintrag.id},${eintrag.kunde},${eintrag.betrag},${eintrag.status}`;
  });

  fs.writeFileSync(dateiPfad, [header, ...zeilen].join("\n") + "\n", "utf8");
}

function leseBestellungenAusCsv(dateiPfad) {
  const inhalt = fs.readFileSync(dateiPfad, "utf8").trim();
  const zeilen = inhalt.split("\n");
  const datenZeilen = zeilen.slice(1);

  return datenZeilen.map((zeile) => {
    const [id, kunde, betrag, status] = zeile.split(",");
    return {
      id: Number(id),
      kunde,
      betrag: Number(betrag),
      status,
    };
  });
}

function schreibeLogeintrag(logPfad, level, nachricht) {
  const zeit = new Date().toISOString();
  const zeile = `${zeit} [${level}] ${nachricht}\n`;
  fs.appendFileSync(logPfad, zeile, "utf8");
}

const beispielBestellungen = [
  { id: 1, kunde: "Mia", betrag: 129.9, status: "offen" },
  { id: 2, kunde: "Noah", betrag: 59.5, status: "bezahlt" },
];

schreibeBestellungenAlsCsv("bestellungen.csv", beispielBestellungen);
const geladen = leseBestellungenAusCsv("bestellungen.csv");
console.log("Test CSV:", geladen);

schreibeLogeintrag("app.log", "INFO", "CSV-Datei wurde erfolgreich erstellt");
schreibeLogeintrag("app.log", "INFO", `Anzahl Datensätze: ${geladen.length}`);
console.log("Test Log: app.log wurde erweitert");
```

## Best Practices

- Kodierung (`utf8`) explizit setzen
- Parsing- und Schreiblogik in getrennten Funktionen halten
- Log-Dateien ausschließlich per Append (`appendFileSync`) erweitern

## Häufige Fehler

- Browser- und Node.js-Umgebung verwechseln
- CSV-Werte ohne Datentypprüfung weiterverarbeiten
- Logs bei jedem Lauf überschreiben statt anhängen
