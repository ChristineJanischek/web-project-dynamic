#!/bin/bash
# Automatisches Update der Dokumentations-Tabelle in README.md
# Liest alle .md Dateien aus docs/ und generiert die Lernpfad-Tabelle

set -e

DOCS_DIR="docs"
README_FILE="README.md"
TEMP_FILE=$(mktemp)

# Assoziatives Array für Bereichsnamen und Beschreibungen
declare -A doc_info

# Dokumentations-Metadaten (manuell gepflegt)
doc_info["intro.md"]="Einstieg & Überblick|Was ist das Web? Rollen von Client/Server"
doc_info["html-grundgeruest.md"]="HTML Grundgerüst|Aufbau von \`<!DOCTYPE html>\`, Grundtags, Validierung"
doc_info["seitenstrukturelemente.md"]="Seitenstrukturelemente|Semantische Tags (\`header\`,\`nav\`,\`main\`,\`section\`,...)"
doc_info["css-einbinden.md"]="CSS einbinden|Externe, interne & inline CSS, Best Practices"
doc_info["css-basis.md"]="CSS Basis|Selektoren, Eigenschaften, erste Styles"
doc_info["css-formatierung.md"]="CSS Formatierung|Text, Farben, Abstände, Schatten, Transitions"
doc_info["box-modell.md"]="Box-Modell|\`margin\`, \`border\`, \`padding\`, \`content\`"
doc_info["flexible-layouts.md"]="Flexible Layouts|Flexbox & CSS Grid mit praktischen Beispielen"
doc_info["responsive-design.md"]="Responsive Design|Media Queries, Mobile Navigation, Breakpoints"
doc_info["bilder-grafiken.md"]="Bilder & Grafiken|Formate, Einbindung, Responsivität"
doc_info["galerien.md"]="Galerien|Einfache Bildgalerie, Grid/Flex"
doc_info["formulare.md"]="Formulare & Auswertung|Formulare erstellen & validieren"
doc_info["js.md"]="JavaScript Grundlagen|Variablen, Funktionen, DOM, Events"
doc_info["react.md"]="React Einstieg|Komponenten, Props, State"
doc_info["python.md"]="Python (Flask)|Minimales API Backend"
doc_info["php.md"]="PHP Grundlagen|Serverseitige Skripte, Ausgabe, Verarbeitung"
doc_info["datenbank.md"]="Datenbank (MySQL)|Tabellen, Abfragen, Verbindung"
doc_info["algorithmen-datenstrukturen.md"]="Algorithmen & Datenstrukturen|Listen, Arrays, Sortieren, Suchen"
doc_info["testen.md"]="Testen|Warum Tests? Einfache Beispiele (Jest/Pytest/PHPUnit)"

# Definierte Reihenfolge (Lernpfad)
ordered_docs=(
    "intro.md"
    "html-grundgeruest.md"
    "seitenstrukturelemente.md"
    "css-einbinden.md"
    "css-basis.md"
    "css-formatierung.md"
    "box-modell.md"
    "flexible-layouts.md"
    "responsive-design.md"
    "bilder-grafiken.md"
    "galerien.md"
    "formulare.md"
    "js.md"
    "react.md"
    "python.md"
    "php.md"
    "datenbank.md"
    "algorithmen-datenstrukturen.md"
    "testen.md"
)

echo "📝 Generiere Dokumentations-Tabelle..."

# Tabellen-Header generieren
table_header="## Inhalt / Lernpfade

| Bereich | Datei / Link | Kurzbeschreibung |
|--------|---------------|------------------|"

# Tabellen-Zeilen generieren
table_rows=""
for doc in "${ordered_docs[@]}"; do
    if [ -f "$DOCS_DIR/$doc" ]; then
        if [ -n "${doc_info[$doc]}" ]; then
            IFS='|' read -r bereich beschreibung <<< "${doc_info[$doc]}"
            table_rows+="
| $bereich | [\`docs/$doc\`](docs/$doc) | $beschreibung |"
        fi
    fi
done

# Vollständige Tabelle
new_table="$table_header$table_rows"

# README.md aktualisieren (zwischen Markern)
if [ -f "$README_FILE" ]; then
    # Extrahiere Inhalt vor und nach der Tabelle
    awk '
        BEGIN { before=1; after=0 }
        /^## Inhalt \/ Lernpfade/ { before=0; skip=1; next }
        skip && /^##/ && !/^## Inhalt \/ Lernpfade/ { after=1; skip=0 }
        before { print }
        after { buffer = buffer $0 "\n" }
        END { print buffer }
    ' "$README_FILE" > "$TEMP_FILE"
    
    # Zusammensetzen
    {
        awk '/^## Inhalt \/ Lernpfade/,/^##/ { if (/^##/ && !/^## Inhalt \/ Lernpfade/) exit } { print }' "$README_FILE" | head -n -1
        echo "$new_table"
        echo ""
        tail -n +1 "$TEMP_FILE" | awk 'NF'
    } > "${README_FILE}.new"
    
    mv "${README_FILE}.new" "$README_FILE"
    rm -f "$TEMP_FILE"
    
    echo "✅ README.md erfolgreich aktualisiert!"
    echo "📋 Anzahl Dokumentationen: ${#ordered_docs[@]}"
else
    echo "❌ Fehler: README.md nicht gefunden!"
    exit 1
fi
