````markdown
# Algorithmen in Python

## Lernziele

- Den Begriff Algorithmus sicher erklären
- Probleme in eindeutige Schritte zerlegen
- Einfache Algorithmen in Python umsetzen

## Theorie kompakt

Ein Algorithmus ist eine endliche, eindeutige Folge von Schritten, die ein Problem löst.

Typischer Ablauf:

1. Eingabe festlegen
2. Verarbeitungsschritte beschreiben
3. Ausgabe definieren

## Deklaration & Implementierung

Beispiel: Größten Wert in einer Liste finden.

```python
zahlen = [4, 9, 2, 11, 7]
maximum = zahlen[0]

for zahl in zahlen:
	if zahl > maximum:
		maximum = zahl

print(f"Maximum: {maximum}")
```

## Best Practices

- Zuerst als Pseudocode planen
- Mit kleinen Testdaten starten
- Randfälle prüfen (leere Liste, negative Zahlen)

## Häufige Fehler

- Falschen Startwert wählen
- Randfälle nicht berücksichtigen
````
