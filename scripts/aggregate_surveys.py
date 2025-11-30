#!/usr/bin/env python3
"""
Sammelt und aggregiert alle Survey-Antworten für Schülerfirma-Namen und App-Namen.

- Liest JSONs aus:
  - version3/aufgabe/surveys/name_survey/data/
  - version3/aufgabe/surveys/app_names/data/
- Erzeugt zusammengefasste Reports:
  - scripts/out/survey_report.json
  - scripts/out/survey_report.md

Ausführen:
    python3 scripts/aggregate_surveys.py
"""
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).parent.parent
OUT_DIR = ROOT / 'scripts' / 'out'
OUT_DIR.mkdir(parents=True, exist_ok=True)

NAME_DIR = ROOT / 'version3' / 'aufgabe' / 'surveys' / 'name_survey' / 'data'
APP_DIR  = ROOT / 'version3' / 'aufgabe' / 'surveys' / 'app_names' / 'data'

CANDIDATES = ['mifa','edueco','greenmind']
APP_CATS = {
    'rideshare': 'Mitfahr‑App',
    'mindlink': 'LernApp',
    'carbon': 'CO2‑Tracker'
}

def read_jsons(folder: Path):
    entries = []
    for p in folder.glob('*.json'):
        try:
            with p.open('r', encoding='utf-8') as f:
                content = json.load(f)
                if isinstance(content, list):
                    entries.extend(content)
                else:
                    entries.append(content)
        except Exception as e:
            print(f"Warnung: Datei {p} übersprungen: {e}")
    return entries

def aggregate_names(entries):
    scores = {c: [] for c in CANDIDATES}
    own = []
    for e in entries:
        for c in CANDIDATES:
            v = e.get(c)
            if v is not None:
                try:
                    scores[c].append(int(v))
                except Exception:
                    pass
        own_list = e.get('own', [])
        if isinstance(own_list, list):
            own.extend([s for s in own_list if (s or '').strip()])
    stats = {c: {
        'count': len(arr),
        'avg': round(mean(arr),2) if arr else 0.0
    } for c, arr in scores.items()}
    ranking = sorted(
        [{'name': c, **stats[c]} for c in CANDIDATES],
        key=lambda x: (x['avg'], x['count']), reverse=True
    )
    winner = ranking[0]['name'] if ranking else None
    return {'entries': len(entries), 'stats': stats, 'ranking': ranking, 'winner': winner, 'own_suggestions': own}

def aggregate_apps(entries):
    scores = {k: [] for k in APP_CATS}
    own = {k: [] for k in APP_CATS}
    for e in entries:
        for k in APP_CATS:
            v = e.get(k)
            if v is not None:
                try:
                    scores[k].append(int(v))
                except Exception:
                    pass
        if e.get('ownRide'):
            own['rideshare'].append(e['ownRide'])
        if e.get('ownMind'):
            own['mindlink'].append(e['ownMind'])
        if e.get('ownCO2'):
            own['carbon'].append(e['ownCO2'])
    stats = {k: {
        'count': len(arr),
        'avg': round(mean(arr),2) if arr else 0.0
    } for k, arr in scores.items()}
    ranking = sorted(
        [{'cat': k, 'label': APP_CATS[k], **stats[k]} for k in APP_CATS],
        key=lambda x: (x['avg'], x['count']), reverse=True
    )
    winners = {r['cat']: r for r in ranking}
    return {'entries': len(entries), 'stats': stats, 'ranking': ranking, 'winners': winners, 'own_suggestions': own}

def write_reports(name_report, app_report):
    # JSON
    out_json = OUT_DIR / 'survey_report.json'
    with out_json.open('w', encoding='utf-8') as f:
        json.dump({'firm_name': name_report, 'apps': app_report}, f, ensure_ascii=False, indent=2)
    # Markdown
    md = [
        '# Survey Report',
        '',
        '## Schülerfirma‑Name',
        f"Einträge: {name_report['entries']}",
        '### Ranking',
    ]
    for r in name_report['ranking']:
        md.append(f"- {r['name']}: ⌀ {r['avg']} ({r['count']} Stimmen)")
    md.append(f"**Gewinner:** {name_report['winner']}")
    if name_report['own_suggestions']:
        md.append('### Eigene Vorschläge')
        for s in name_report['own_suggestions']:
            md.append(f"- {s}")
    md.extend(['', '## App‑Namen', f"Einträge: {app_report['entries']}", '### Ranking'])
    for r in app_report['ranking']:
        md.append(f"- {r['label']}: ⌀ {r['avg']} ({r['count']} Stimmen)")
    md.append('### Eigene Vorschläge je Kategorie')
    for k, lst in app_report['own_suggestions'].items():
        md.append(f"- {APP_CATS[k]}:")
        for s in lst:
            md.append(f"  - {s}")
    out_md = OUT_DIR / 'survey_report.md'
    with out_md.open('w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"✅ Reports geschrieben: {out_json} und {out_md}")

if __name__ == '__main__':
    name_entries = read_jsons(NAME_DIR)
    app_entries  = read_jsons(APP_DIR)
    name_report  = aggregate_names(name_entries)
    app_report   = aggregate_apps(app_entries)
    write_reports(name_report, app_report)
