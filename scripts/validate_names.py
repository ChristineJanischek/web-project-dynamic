#!/usr/bin/env python3
"""
Validiert die Datei version3/aufgabe/phase1-concept/results/names.json

Prüft:
- Existenz der Datei
- Pflichtschlüssel und Typen
- Nicht-Leere Werte
- Listen-Inhalte sind Strings
- Keine Duplikate zwischen finalem Namen und Alternativen
- Mindestbegründungslänge

Exit-Code 0 = OK
Exit-Code 1 = Fehler / Warnung (für CI nutzbar)

Verwendung lokal:
    python3 scripts/validate_names.py

In GitHub Action (z.B. names-validation.yml):
    - name: Validate names.json
      run: python3 scripts/validate_names.py
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

REQUIRED_KEYS = {
    "firma": str,
    "app_mitfahr": str,
    "alternativen_firma": list,
    "alternativen_app": list,
    "entscheidung_begruendung": str,
}

RESULT_PATH = Path("version3/aufgabe/phase1-concept/results/names.json")


def error(msg: str) -> int:
    print(f"❌ {msg}")
    return 1


def warning(msg: str) -> None:
    print(f"⚠️  {msg}")


def validate_structure(data: dict) -> int:
    # Schlüssel & Typen
    for key, expected_type in REQUIRED_KEYS.items():
        if key not in data:
            return error(f"Schlüssel fehlt: {key}")
        if not isinstance(data[key], expected_type):
            return error(f"Falscher Typ bei '{key}': erwartet {expected_type.__name__}, erhalten {type(data[key]).__name__}")
        if expected_type is str and not data[key].strip():
            return error(f"Leerer String bei '{key}'")
        if expected_type is list:
            if not data[key]:
                warning(f"Liste '{key}' ist leer – falls keine Alternativen, ok")
            if not all(isinstance(x, str) for x in data[key]):
                return error(f"Liste '{key}' enthält Nicht-Strings")

    # Duplikate prüfen
    if data["firma"] in data.get("alternativen_firma", []):
        warning("Firmenname auch in alternativen_firma – entferne ihn aus der Alternativliste")
    if data["app_mitfahr"] in data.get("alternativen_app", []):
        warning("App-Name auch in alternativen_app – entferne ihn aus der Alternativliste")

    # Begründung Länge
    if len(data["entscheidung_begruendung"].split()) < 5:
        warning("Begründung sehr kurz – füge mehr Argumente hinzu")

    print("✅ Struktur valide")
    return 0


def main() -> int:
    if not RESULT_PATH.exists():
        return error(f"Datei nicht gefunden: {RESULT_PATH}")

    try:
        content = RESULT_PATH.read_text(encoding="utf-8")
        data = json.loads(content)
    except Exception as e:
        return error(f"JSON konnte nicht geladen werden: {e}")

    return validate_structure(data)


if __name__ == "__main__":
    sys.exit(main())
