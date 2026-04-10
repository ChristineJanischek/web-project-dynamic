from __future__ import annotations

import re
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
