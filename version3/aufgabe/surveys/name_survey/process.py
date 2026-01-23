#!/usr/bin/env python3
"""
Aggregiert Antworten aus name_survey/data/responses.json und optional aus mehreren
Client-Downloads (responses_client_*.json). Gibt Ranking und Gewinner aus.

Ausführen:
    python3 version3/aufgabe/surveys/name_survey/process.py
"""
import json
import sys
from pathlib import Path
from statistics import mean

BASE = Path(__file__).parent
DATA = BASE / 'data'
OUTPUT = BASE / 'report.json'

CANDIDATES = ['mifa','edueco','greenmind']

def load_all() -> list:
    entries = []
    # Hauptdatei
    main = DATA / 'responses.json'
    if main.exists():
        try:
            with main.open('r', encoding='utf-8') as f:
                content = json.load(f)
                if isinstance(content, list):
                    entries.extend(content)
                elif isinstance(content, dict):
                    entries.append(content)
        except Exception as e:
            print(f"Warnung: Konnte {main} nicht laden: {e}")
    # Client-Downloads optional einsammeln
    for p in DATA.glob('responses_client_*.json'):
        try:
            with p.open('r', encoding='utf-8') as f:
                content = json.load(f)
                entries.append(content)
        except Exception as e:
            print(f"Warnung: Konnte {p} nicht laden: {e}")
    return entries

def aggregate(entries: list) -> dict:
    scores = {c: [] for c in CANDIDATES}
    own_names = []
    for e in entries:
        for c in CANDIDATES:
            v = e.get(c)
            try:
                if v is not None:
                    scores[c].append(int(v))
            except Exception:
                pass
        # eigene Vorschläge sammeln
        own = e.get('own', [])
        if isinstance(own, list):
            for n in own:
                n = (n or '').strip()
                if n:
                    own_names.append(n)
    # Mittelwerte
    stats = {}
    for c, arr in scores.items():
        stats[c] = {
            'count': len(arr),
            'avg': round(mean(arr), 2) if arr else 0.0
        }
    # Ranking
    ranking = sorted(
        [{'name': c, **stats[c]} for c in CANDIDATES],
        key=lambda x: (x['avg'], x['count']),
        reverse=True
    )
    winner = ranking[0]['name'] if ranking else None
    report = {
        'entries': len(entries),
        'stats': stats,
        'ranking': ranking,
        'winner': winner,
        'own_names': own_names
    }
    return report

def main():
    entries = load_all()
    report = aggregate(entries)
    with OUTPUT.open('w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    sys.exit(main())
