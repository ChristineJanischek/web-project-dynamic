# Vergleichsoperatoren und logische Operatoren in Python

[← Zurück zur Python-Übersicht](README.md) · [Weiter: Funktionen und Methoden](FUNKTIONEN_METHODEN.md)

## Lernziele

- Vergleichsoperatoren sicher einsetzen (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logische Operatoren kombinieren (`and`, `or`, `not`)
- Bedingungen in Funktionen kapseln und testbar machen

## Theorie kompakt

Vergleichsoperatoren liefern `True` oder `False` zurück. Mit logischen Operatoren können mehrere Bedingungen verknüpft werden.

- `and`: beide Bedingungen müssen wahr sein
- `or`: mindestens eine Bedingung muss wahr sein
- `not`: kehrt den Wahrheitswert um

## Deklaration & Implementierung

### Einfaches Beispiel: Volljährigkeit prüfen

```python
def ist_volljaehrig(alter):
    return alter >= 18

print("Test 1:", ist_volljaehrig(16))  # False
print("Test 2:", ist_volljaehrig(18))  # True
```

### Komplexeres Beispiel: Freigabe für Rabattaktion

Regel: Eine Bestellung ist rabattberechtigt, wenn

- der Warenkorb mindestens 100 € hat **und**
- der Kunde entweder Premium ist **oder** einen Gutschein hat **und**
- das Konto nicht gesperrt ist.

```python
def ist_rabatt_freigegeben(bestellwert, ist_premium, hat_gutschein, konto_gesperrt):
    mindestwert_erreicht = bestellwert >= 100
    kunde_qualifiziert = ist_premium or hat_gutschein
    konto_ist_aktiv = not konto_gesperrt

    return mindestwert_erreicht and kunde_qualifiziert and konto_ist_aktiv

print("Test A:", ist_rabatt_freigegeben(80, True, False, False))    # False
print("Test B:", ist_rabatt_freigegeben(120, False, True, False))   # True
print("Test C:", ist_rabatt_freigegeben(200, True, False, True))    # False
```

## Best Practices

- Teilbedingungen in gut lesbare Variablen auslagern
- Bedingungen bewusst klammern oder in Teilschritte trennen
- Grenzfälle explizit testen (z. B. genau 100)

## Häufige Fehler

- `=` (Zuweisung) und `==` (Vergleich) verwechseln
- Zu komplexe Bedingungen in einer einzigen Zeile formulieren
- `not` unübersichtlich mit langen Ausdrücken kombinieren
