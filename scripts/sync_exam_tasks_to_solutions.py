#!/usr/bin/env python3
"""
Synchronisiert Aufgabenstellungen aus exam*.md in die zugehörigen solutions*.md-Dateien.
- Sucht im gleichen Verzeichnis nach exam*.md und solutions*.md
- Kopiert die Aufgabenstellungen (## Aufgabe ...) in die Lösung und ersetzt dort den Bereich zwischen Aufgabenstellung-Start/End-Kommentaren.
- Fügt Aufgabenstellung ein, falls sie fehlt.
- Kann als Pre-Commit-Hook oder manuell ausgeführt werden.
"""
import os
import re
from pathlib import Path

EXAM_PATTERN = re.compile(r"^exam(_v\d+)?\\.md$")
SOLUTION_PATTERN = re.compile(r"^solutions(_v\d+)?\\.md$")
TASK_HEADER_PATTERN = re.compile(r"^## Aufgabe [A-Z] ", re.MULTILINE)

TASK_START = "<!-- AUFGABENSTELLUNG_START -->"
TASK_END = "<!-- AUFGABENSTELLUNG_END -->"


def extract_tasks(md_text):
    """Extrahiert alle Aufgabenstellungen als Dict: {task_id: aufgaben_md} """
    tasks = {}
    matches = list(TASK_HEADER_PATTERN.finditer(md_text))
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        header = md_text[start:md_text.find('\n', start)]
        task_id = header.split()[2]  # z.B. 'A', 'B', ...
        tasks[task_id] = md_text[start:end].strip()
    return tasks


def sync_tasks(exam_path, solution_path):
    with open(exam_path, encoding="utf-8") as f:
        exam_md = f.read()
    with open(solution_path, encoding="utf-8") as f:
        sol_md = f.read()
    tasks = extract_tasks(exam_md)
    # Für jede Aufgabe im exam, suche im solution nach Platzhaltern
    for task_id, task_md in tasks.items():
        # Suche nach Aufgabenstellung-Kommentar für diese Aufgabe
        pattern = re.compile(
            rf"(## Aufgabe {task_id} [^\n]*\n)(.*?){TASK_START}.*?{TASK_END}(.*?)(?=^## Aufgabe |\Z)",
            re.DOTALL | re.MULTILINE)
        replacement = rf"\1{TASK_START}\n{task_md}\n{TASK_END}\n\3"
        if pattern.search(sol_md):
            sol_md = pattern.sub(replacement, sol_md)
        else:
            # Falls kein Platzhalter: Füge Aufgabenstellung nach Überschrift ein
            header_pat = re.compile(rf"(## Aufgabe {task_id} [^\n]*\n)", re.MULTILINE)
            sol_md = header_pat.sub(rf"\1{TASK_START}\n{task_md}\n{TASK_END}\n", sol_md)
    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(sol_md)
    print(f"Synchronisiert: {solution_path}")


def main():
    base = Path(__file__).parent.parent / "docs/programmierung/grundlagen/exams/php/basics"
    files = os.listdir(base)
    exams = [f for f in files if EXAM_PATTERN.match(f)]
    for exam in exams:
        suffix = exam[4:]  # z.B. .md, _v2.md
        sol = f"solutions{suffix}"
        if sol in files:
            sync_tasks(base / exam, base / sol)

if __name__ == "__main__":
    main()
