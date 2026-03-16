#!/usr/bin/env python3
"""Synchronisiert Aufgabenstellungen aus exam*.md in solutions*.md rekursiv.

Regeln:
- exam*.md ist die Single Source of Truth fuer Aufgabenstellungen.
- Zu exam(_vX).md gehoert solutions(_vX).md im selben Verzeichnis.
- In der Loesung wird pro Aufgabe der Abschnitt zwischen
  "**Aufgabenstellung**" und "**Musterloesung**" ersetzt.
- Falls "**Aufgabenstellung**" fehlt, wird er vor "**Musterloesung**"
  (oder vor dem ersten Codeblock) eingefuegt.
"""

from __future__ import annotations

import re
from pathlib import Path

EXAM_FILE_RE = re.compile(r"^exam(?:_v\d+)?\.md$")
SOLUTION_FILE_RE = re.compile(r"^solutions(?:_v\d+)?\.md$")
TASK_HEADER_RE = re.compile(r"^## Aufgabe ([A-Z])\b.*$", re.MULTILINE)


def split_task_sections(md_text: str) -> list[tuple[str, str, int, int]]:
    """Gibt Task-Sektionen als (task_id, section_text, start, end) zurueck."""
    matches = list(TASK_HEADER_RE.finditer(md_text))
    sections: list[tuple[str, str, int, int]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        task_id = match.group(1)
        sections.append((task_id, md_text[start:end], start, end))
    return sections


def extract_exam_task_body(task_section: str) -> str:
    """Extrahiert den Aufgabenstellungstext aus einer Exam-Aufgabe.

    Enthalten bleibt die komplette Aufgabenbeschreibung inklusive Beispiele,
    aber ohne den Antwortbereich.
    """
    first_newline = task_section.find("\n")
    if first_newline == -1:
        return ""
    body = task_section[first_newline + 1 :].strip()

    # Antwortbereich entfernen (falls vorhanden).
    body = re.sub(
        r"\n\*\*Antwortbereich:\*\*\s*\n\s*```[\s\S]*?```\s*$",
        "",
        body,
        flags=re.MULTILINE,
    ).strip()
    return body


def sync_task_into_solution_section(solution_section: str, task_body: str) -> str:
    """Aktualisiert genau eine Aufgaben-Sektion in einer Loesungsdatei."""
    task_block = f"**Aufgabenstellung**\n\n{task_body}\n\n"

    if "**Aufgabenstellung**" in solution_section and "**Musterloesung**" in solution_section:
        updated = re.sub(
            r"\*\*Aufgabenstellung\*\*\s*[\s\S]*?\n\*\*Musterloesung\*\*",
            task_block + "**Musterloesung**",
            solution_section,
            count=1,
        )
        return updated

    if "**Musterloesung**" in solution_section:
        return solution_section.replace("**Musterloesung**", task_block + "**Musterloesung**", 1)

    # Fallback: vor ersten Codeblock einfuegen; wenn keiner existiert ans Ende.
    code_idx = solution_section.find("```")
    if code_idx != -1:
        return solution_section[:code_idx] + task_block + "**Musterloesung**\n\n" + solution_section[code_idx:]
    return solution_section.rstrip() + "\n\n" + task_block + "**Musterloesung**\n"


def sync_file_pair(exam_path: Path, solution_path: Path) -> bool:
    """Synchronisiert ein exam/solutions-Paar. Return True bei Aenderung."""
    exam_md = exam_path.read_text(encoding="utf-8")
    sol_md = solution_path.read_text(encoding="utf-8")

    exam_tasks = {
        task_id: extract_exam_task_body(section)
        for task_id, section, _start, _end in split_task_sections(exam_md)
    }
    sol_sections = split_task_sections(sol_md)
    if not sol_sections:
        return False

    rebuilt: list[str] = []
    cursor = 0
    changed = False

    for task_id, section_text, start, end in sol_sections:
        rebuilt.append(sol_md[cursor:start])
        if task_id in exam_tasks and exam_tasks[task_id]:
            new_section = sync_task_into_solution_section(section_text, exam_tasks[task_id])
            changed = changed or (new_section != section_text)
            rebuilt.append(new_section)
        else:
            rebuilt.append(section_text)
        cursor = end

    rebuilt.append(sol_md[cursor:])
    new_sol_md = "".join(rebuilt)

    if changed:
        solution_path.write_text(new_sol_md, encoding="utf-8")
        print(f"Synchronisiert: {solution_path}")
    return changed


def find_exam_solution_pairs(base_dir: Path) -> list[tuple[Path, Path]]:
    """Findet rekursiv passende exam/solutions-Paare."""
    pairs: list[tuple[Path, Path]] = []
    for exam_path in sorted(base_dir.rglob("exam*.md")):
        if not EXAM_FILE_RE.match(exam_path.name):
            continue
        suffix = exam_path.name[len("exam") :]
        solution_name = f"solutions{suffix}"
        solution_path = exam_path.with_name(solution_name)
        if solution_path.exists() and SOLUTION_FILE_RE.match(solution_path.name):
            pairs.append((exam_path, solution_path))
    return pairs


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent / "docs" / "programmierung" / "grundlagen" / "exams"
    pairs = find_exam_solution_pairs(base_dir)
    changed_count = 0

    for exam_path, solution_path in pairs:
        if sync_file_pair(exam_path, solution_path):
            changed_count += 1

    print(f"Paare geprueft: {len(pairs)} | Dateien geaendert: {changed_count}")


if __name__ == "__main__":
    main()
