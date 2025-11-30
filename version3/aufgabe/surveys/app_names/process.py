#!/usr/bin/env python3
"""
Aggregiert Antworten aus app_names/data/*.json und erzeugt Rankings pro App‑Kategorie.

Ausführen:
    python3 version3/aufgabe/surveys/app_names/process.py
"""
import json
import sys
from pathlib import Path
from statistics import mean

BASE = Path(__file__).parent
DATA = BASE / 'data'
OUTPUT = BASE / 'report.json'

CATS = {
    'rideshare': 'Mitfahr‑App',
    'mindlink': 'LernApp',
    'carbon': 'CO2‑Tracker'
}


def load_all() -> list:
    entries = []
    # Hauptdatei optional
    for p in DATA.glob('responses*.json'):
        try:
            with p.open('r', encoding='utf-8') as f:
                content = json.load(f)
                if isinstance(content, list):
                    entries.extend(content)
                else:
                    entries.append(content)
        except Exception as e:
            print(f"Warnung: Konnte {p} nicht laden: {e}")
    return entries


def aggregate(entries: list) -> dict:
    scores = {k: [] for k in CATS.keys()}
    own = {k: [] for k in CATS.keys()}
    for e in entries:
        for k in CATS.keys():
            v = e.get(k)
            try:
                if v is not None:
                    scores[k].append(int(v))
            except Exception:
                pass
        if e.get('ownRide'):
            own['rideshare'].append(e['ownRide'])
        if e.get('ownMind'):
            own['mindlink'].append(e['ownMind'])
        if e.get('ownCO2'):
            own['carbon'].append(e['ownCO2'])
    stats = {}
    for k, arr in scores.items():
        stats[k] = {
            'count': len(arr),
            'avg': round(mean(arr), 2) if arr else 0.0
        }
    ranking = sorted(
        [{'cat': k, 'label': CATS[k], **stats[k]} for k in CATS.keys()],
        key=lambda x: (x['avg'], x['count']),
        reverse=True
    )
    winners = {r['cat']: r for r in ranking}
    return {
        'entries': len(entries),
        'stats': stats,
        'ranking': ranking,
        'winners': winners,
        'own_suggestions': own
    }


def main():
    entries = load_all()
    report = aggregate(entries)
    with OUTPUT.open('w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    sys.exit(main())
