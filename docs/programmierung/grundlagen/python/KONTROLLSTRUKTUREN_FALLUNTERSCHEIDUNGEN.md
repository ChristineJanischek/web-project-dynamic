# Kontrollstrukturen: Fallunterscheidungen in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Kontrollstrukturen: Wiederholungsstrukturen](KONTROLLSTRUKTUREN_WIEDERHOLUNGSSTRUKTUREN.md)

## Lernziele

- `if`, `elif`, `else` sicher einsetzen
- Bedingungen korrekt formulieren
- Programmabläufe nachvollziehbar steuern

## Theorie kompakt

Fallunterscheidungen wählen abhängig von Bedingungen verschiedene Codepfade.

## Deklaration & Implementierung

```python
punkte = 74

if punkte >= 90:
    print("Note 1")
elif punkte >= 75:
    print("Note 2")
elif punkte >= 60:
    print("Note 3")
else:
    print("Verbesserungsbedarf")
```

## Best Practices

- Bedingungen lesbar halten
- Verschachtelung begrenzen
- Bei Vergleichen Klarheit vor Kürze

## Häufige Fehler

- `=` statt `==`
- Falsche Einrückung
