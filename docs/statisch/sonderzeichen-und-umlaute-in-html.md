# Sonderzeichen und Umlaute in HTML

Dieses Merkblatt zeigt, wie ihr Umlaute (`ä`, `ö`, `ü`, `Ä`, `Ö`, `Ü`), `ß` und andere Sonderzeichen in Webprojekten sicher verwendet.

## Warum treten Fehler auf?

Die meisten Fehler entstehen durch eine Mischung aus:

- falscher Datei-Codierung (nicht UTF-8)
- fehlendem oder falschem `charset`
- Copy/Paste aus Word, PDF, Messenger oder KI-Tools
- ungeeigneten Sonderzeichen in HTML-Attributen

Typische kaputte Ausgabe:

- `Müller` wird zu `MÃ¼ller`
- `Schüler` wird zu `SchÃ¼ler`

## Best Practice: Immer UTF-8 durchziehen

Verwendet UTF-8 in allen Ebenen gleichzeitig.

### 1. HTML-Dokument korrekt starten

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Über uns</title>
  </head>
  <body>
    <h1>Willkommen bei der Schülerfirma</h1>
  </body>
</html>
```

Wichtig: `<meta charset="UTF-8" />` muss im `<head>` stehen.

### 2. Datei wirklich als UTF-8 speichern

In VS Code unten rechts die Codierung prüfen:

- sollte `UTF-8` sein
- bei falscher Codierung: `Reopen with Encoding` oder `Save with Encoding` -> `UTF-8`

### 3. Server-Antwort mit UTF-8 senden (bei PHP)

```php
<?php
header('Content-Type: text/html; charset=UTF-8');
```

Wenn Header und Datei nicht zusammenpassen, entstehen oft Darstellungsfehler.

## Umlaute direkt schreiben oder als Entity?

Bei sauberem UTF-8 gilt:

- Umlaute im normalen Text direkt schreiben (`Über`, `für`, `größer`)
- Entities vor allem für reservierte HTML-Zeichen nutzen

Wichtige Entities:

- `&amp;` für `&`
- `&lt;` für `<`
- `&gt;` für `>`
- `&quot;` für `"`
- `&#39;` für `'`

Beispiel:

```html
<p>Tom &amp; Jerry</p>
<p>2 &lt; 5 und 8 &gt; 3</p>
```

## Typische Copy/Paste-Fallen

### 1. "Schlaue" Anführungszeichen

Aus Textverarbeitungen kommen oft `“` und `”` statt `"`.

Schlecht:

```html
<a title="“Mehr" erfahren” href="/about.html">Über uns</a>
```

Gut:

```html
<a title="Mehr erfahren" href="/about.html">Über uns</a>
```

### 2. Unsichtbare Sonderzeichen

Häufige Problemzeichen beim Einfügen:

- geschütztes Leerzeichen (NBSP)
- Gedankenstrich statt Minus
- Zero-Width-Zeichen

Best Practice:

- zuerst in einen reinen Texteditor einfügen
- dann in den Code übernehmen
- bei VS Code möglichst "als unformatierten Text" einfügen

### 3. HTML in Navigationen

Gerade in Menüs treten Fehler oft auf, wenn `&` nicht escaped ist.

Schlecht:

```html
<nav>
  <a href="team.html">Team & Kontakt</a>
</nav>
```

Gut:

```html
<nav>
  <a href="team.html">Team &amp; Kontakt</a>
</nav>
```

## Mini-Check vor Abgabe

1. Enthalten alle HTML-Dateien `<meta charset="UTF-8" />`?
2. Sind Dateien wirklich als `UTF-8` gespeichert?
3. Sind reservierte Zeichen korrekt escaped (`&amp;`, `&lt;`, `&gt;`)?
4. Sind nach Copy/Paste keine kaputten Zeichen sichtbar?
5. Sind Navigation, Formulare und Footer-Texte testweise im Browser geprüft?

## Schnelle Fehlerbehebung

Wenn ihr bereits kaputte Zeichen wie `MÃ¼ller` seht:

1. Datei in VS Code mit der vermuteten alten Codierung neu öffnen (`Reopen with Encoding`)
2. Direkt danach mit `UTF-8` speichern (`Save with Encoding`)
3. Browser-Cache leeren und Seite neu laden
4. Falls nötig, Textstelle neu eintragen (nicht erneut aus derselben fehlerhaften Quelle kopieren)

## Kurzfassung

- Standard: UTF-8 überall
- Umlaute im Fließtext direkt schreiben
- HTML-Sonderzeichen korrekt escapen
- Copy/Paste bewusst kontrollieren
- Vor Abgabe kurze Zeichensatz-Prüfung machen
