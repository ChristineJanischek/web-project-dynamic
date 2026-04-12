from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class RuleResult:
    passed: bool
    evidence: list[str] = field(default_factory=list)
    note: str = ""


def evaluate_rule(
    kind: str,
    config: dict[str, Any],
    project_root: Path,
    label: str = "",
) -> RuleResult:
    if kind == "manual":
        return RuleResult(passed=False, note="Manuelle Bewertung erforderlich.")

    if kind == "file_exists":
        return _rule_file_exists(config, project_root, label)

    if kind == "min_files_glob":
        return _rule_min_files_glob(config, project_root, label)

    if kind == "contains_regex":
        return _rule_contains_regex(config, project_root, label)

    if kind == "not_contains_regex":
        result = _rule_contains_regex(config, project_root, label)
        return RuleResult(passed=not result.passed, evidence=result.evidence, note=result.note)

    if kind == "any_of":
        return _rule_any_of(config, project_root)

    if kind == "all_of":
        return _rule_all_of(config, project_root)

    if kind == "syntax_check_glob":
        return _rule_syntax_check_glob(config, project_root, label)

    return RuleResult(passed=False, note=f"Unbekannter Regeltyp: '{kind}'.")


# ---------------------------------------------------------------------------
# Atomic rules
# ---------------------------------------------------------------------------

def _rule_file_exists(config: dict, root: Path, label: str) -> RuleResult:
    glob_pattern = config.get("glob", "")
    matches = _find_files(root, glob_pattern)
    if matches:
        rel = [str(p.relative_to(root)) for p in matches[:3]]
        return RuleResult(passed=True, evidence=rel, note=label or glob_pattern)
    return RuleResult(
        passed=False,
        note=f"Keine Datei für Muster '{glob_pattern}' gefunden.",
    )


def _rule_min_files_glob(config: dict, root: Path, label: str) -> RuleResult:
    glob_pattern = config.get("glob", "")
    minimum = int(config.get("min", 1))
    matches = _find_files(root, glob_pattern)
    if len(matches) >= minimum:
        rel = [str(p.relative_to(root)) for p in matches[:5]]
        return RuleResult(
            passed=True,
            evidence=rel,
            note=label or f"{len(matches)} Dateien für '{glob_pattern}' gefunden.",
        )
    return RuleResult(
        passed=False,
        note=(
            f"Nur {len(matches)} Datei(en) für '{glob_pattern}' gefunden, "
            f"Minimum ist {minimum}."
        ),
    )


def _rule_contains_regex(config: dict, root: Path, label: str) -> RuleResult:
    glob_pattern = config.get("glob", "**/*")
    pattern = config.get("regex", "")
    if not pattern:
        return RuleResult(passed=False, note="Kein Regex-Muster konfiguriert.")

    try:
        compiled = re.compile(pattern)
    except re.error as exc:
        return RuleResult(passed=False, note=f"Ungültiges Regex '{pattern}': {exc}")

    matches: list[str] = []
    for file_path in _find_files(root, glob_pattern):
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if compiled.search(text):
            matches.append(str(file_path.relative_to(root)))
        if len(matches) >= 5:
            break

    if matches:
        return RuleResult(
            passed=True,
            evidence=matches,
            note=label or f"Regex '{pattern}' gefunden.",
        )
    return RuleResult(
        passed=False,
        note=f"Regex '{pattern}' in keiner Datei für Muster '{glob_pattern}' gefunden.",
    )


def _rule_syntax_check_glob(config: dict, root: Path, label: str) -> RuleResult:
    glob_pattern = str(config.get("glob", "")).strip()
    language = str(config.get("language", "")).strip().lower()
    minimum = int(config.get("min", 1))
    if not glob_pattern:
        return RuleResult(passed=False, note="Kein Glob-Muster fuer Syntaxcheck konfiguriert.")

    files = _find_files(root, glob_pattern)
    if len(files) < minimum:
        return RuleResult(
            passed=False,
            note=(
                f"Nur {len(files)} Datei(en) fuer Syntaxcheck '{glob_pattern}' gefunden, "
                f"Minimum ist {minimum}."
            ),
        )

    if language in {"js", "javascript"}:
        return _check_javascript_syntax(files, root, label)
    if language == "css":
        return _check_css_syntax(files, root, label)
    return RuleResult(
        passed=False,
        note=f"Unbekannte Sprache fuer syntax_check_glob: '{language}'.",
    )


# ---------------------------------------------------------------------------
# Composite rules
# ---------------------------------------------------------------------------

def _rule_any_of(config: dict, root: Path) -> RuleResult:
    child_label = config.get("label", "")
    child_rules = config.get("rules", [])
    all_notes: list[str] = []

    for rule in child_rules:
        result = evaluate_rule(
            kind=rule.get("kind", ""),
            config=rule.get("config", {}),
            project_root=root,
            label=rule.get("label", ""),
        )
        if result.passed:
            return RuleResult(
                passed=True,
                evidence=result.evidence,
                note=child_label or result.note,
            )
        all_notes.append(result.note)

    return RuleResult(
        passed=False,
        note=f"Keine Teilregel erfüllt: {'; '.join(all_notes)}",
    )


def _rule_all_of(config: dict, root: Path) -> RuleResult:
    child_rules = config.get("rules", [])
    passed_count = 0
    all_evidence: list[str] = []
    failed_notes: list[str] = []

    for rule in child_rules:
        result = evaluate_rule(
            kind=rule.get("kind", ""),
            config=rule.get("config", {}),
            project_root=root,
            label=rule.get("label", ""),
        )
        if result.passed:
            passed_count += 1
            all_evidence.extend(result.evidence)
        else:
            failed_notes.append(result.note)

    total = len(child_rules)
    all_passed = passed_count == total

    note_parts = [f"{passed_count}/{total} Teilregeln erfüllt"]
    if failed_notes:
        note_parts.append("Nicht erfüllt: " + "; ".join(failed_notes))

    return RuleResult(
        passed=all_passed,
        evidence=all_evidence[:10],
        note=". ".join(note_parts),
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_files(root: Path, glob_pattern: str) -> list[Path]:
    if not glob_pattern:
        return []
    if glob_pattern.startswith("**/"):
        return [p for p in root.rglob(glob_pattern[3:]) if p.is_file()]
    return [p for p in root.glob(glob_pattern) if p.is_file()]


def _check_javascript_syntax(files: list[Path], root: Path, label: str) -> RuleResult:
    node_cmd = shutil.which("node")
    failed: list[str] = []
    checked = 0

    if node_cmd is not None:
        for file_path in files:
            checked += 1
            result = subprocess.run(
                [node_cmd, "--check", str(file_path)],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                failed.append(str(file_path.relative_to(root)))
        if failed:
            return RuleResult(
                passed=False,
                evidence=[f"Syntaxfehler in {name}" for name in failed[:5]],
                note=f"JavaScript-Syntaxfehler in {len(failed)} Datei(en).",
            )
        return RuleResult(
            passed=True,
            evidence=[str(p.relative_to(root)) for p in files[:5]],
            note=label or f"JS-Syntax ok ({checked} Datei(en) geprueft).",
        )

    # Fallback ohne Node: Basispruefung auf ausgeglichene Klammern und nicht geschlossene Strings/Kommentare.
    for file_path in files:
        checked += 1
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            failed.append(str(file_path.relative_to(root)))
            continue
        ok, _ = _check_code_balance(text)
        if not ok:
            failed.append(str(file_path.relative_to(root)))

    if failed:
        return RuleResult(
            passed=False,
            evidence=[f"Syntaxverdacht in {name}" for name in failed[:5]],
            note=(
                "Node-CLI nicht verfuegbar; Basis-Syntaxpruefung fehlgeschlagen "
                f"in {len(failed)} Datei(en)."
            ),
        )
    return RuleResult(
        passed=True,
        evidence=[str(p.relative_to(root)) for p in files[:5]],
        note=(
            label
            or f"Node-CLI nicht verfuegbar; Basis-Syntaxpruefung ok ({checked} Datei(en))."
        ),
    )


def _check_css_syntax(files: list[Path], root: Path, label: str) -> RuleResult:
    failed: list[str] = []
    checked = 0

    for file_path in files:
        checked += 1
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            failed.append(str(file_path.relative_to(root)))
            continue

        ok, _ = _check_code_balance(text)
        if not ok:
            failed.append(str(file_path.relative_to(root)))

    if failed:
        return RuleResult(
            passed=False,
            evidence=[f"Syntaxverdacht in {name}" for name in failed[:5]],
            note=f"CSS-Syntaxverdacht in {len(failed)} Datei(en).",
        )
    return RuleResult(
        passed=True,
        evidence=[str(p.relative_to(root)) for p in files[:5]],
        note=label or f"CSS-Basissyntax ok ({checked} Datei(en) geprueft).",
    )


def _check_code_balance(text: str) -> tuple[bool, str]:
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack: list[str] = []

    in_single = False
    in_double = False
    in_line_comment = False
    in_block_comment = False
    escaped = False

    i = 0
    while i < len(text):
        ch = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""

        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
            i += 1
            continue

        if in_block_comment:
            if ch == "*" and nxt == "/":
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue

        if in_single:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == "'":
                in_single = False
            i += 1
            continue

        if in_double:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_double = False
            i += 1
            continue

        if ch == "/" and nxt == "/":
            in_line_comment = True
            i += 2
            continue
        if ch == "/" and nxt == "*":
            in_block_comment = True
            i += 2
            continue

        if ch == "'":
            in_single = True
            i += 1
            continue
        if ch == '"':
            in_double = True
            i += 1
            continue

        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False, "Klammern nicht ausgeglichen"
            stack.pop()

        i += 1

    if in_single or in_double:
        return False, "String nicht geschlossen"
    if in_block_comment:
        return False, "Blockkommentar nicht geschlossen"
    if stack:
        return False, "Klammern nicht ausgeglichen"
    return True, "ok"
