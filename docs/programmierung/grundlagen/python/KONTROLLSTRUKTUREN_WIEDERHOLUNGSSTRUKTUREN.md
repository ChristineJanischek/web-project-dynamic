# Kontrollstrukturen: Wiederholungsstrukturen in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Datenstrukturen](DATENSTRUKTUREN.md)

## Lernziele

- Schleifen mit `for` und `while` nutzen
- Durchläufe kontrollieren und beenden
- Endlosschleifen vermeiden

## Theorie kompakt

- `for` iteriert über Sequenzen
- `while` läuft solange eine Bedingung wahr ist

## Deklaration & Implementierung

```python
for i in range(1, 6):
    print(f"Runde {i}")
```

```python
zaehler = 3
while zaehler > 0:
    print(f"Noch {zaehler}")
    zaehler -= 1
```

## Best Practices

- Schleifen kurz und klar halten
- Abbruchbedingungen sichtbar machen

## Häufige Fehler

- Endlosschleifen durch fehlende Aktualisierung
- Falscher Bereich bei `range`
