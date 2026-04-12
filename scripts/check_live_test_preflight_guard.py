#!/usr/bin/env python3
"""Prueft, dass Bewertungslaeufe den Live-Test-Preflight standardmaessig erzwingen.

Der Check ist absichtlich statisch (AST-basiert), damit er in CI ohne VS-Code-CLI
oder Extension-Installation ausgefuehrt werden kann.
"""

from __future__ import annotations

import ast
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    PROJECT_ROOT / "scripts" / "process_assessment_uploads.py",
    PROJECT_ROOT / "scripts" / "batch_assess.py",
]
REQUIRED_IMPORT_MODULE = "assessment_assistant.live_test_setup"
REQUIRED_IMPORT_NAME = "ensure_live_test_extensions"
REQUIRED_GUARD_ARG = "skip_live_test_setup"


class GuardViolation(Exception):
    pass


def _has_required_import(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == REQUIRED_IMPORT_MODULE:
            if any(alias.name == REQUIRED_IMPORT_NAME for alias in node.names):
                return True
    return False


def _is_required_guard_test(test: ast.expr) -> bool:
    # Erwartet: if not args.skip_live_test_setup:
    if not isinstance(test, ast.UnaryOp) or not isinstance(test.op, ast.Not):
        return False

    operand = test.operand
    return (
        isinstance(operand, ast.Attribute)
        and operand.attr == REQUIRED_GUARD_ARG
        and isinstance(operand.value, ast.Name)
        and operand.value.id == "args"
    )


def _contains_preflight_call(statements: list[ast.stmt]) -> bool:
    for stmt in statements:
        for node in ast.walk(stmt):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Name) and func.id == REQUIRED_IMPORT_NAME:
                    return True
    return False


def _main_guard_present(tree: ast.AST) -> bool:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            for stmt in node.body:
                if isinstance(stmt, ast.If) and _is_required_guard_test(stmt.test):
                    return _contains_preflight_call(stmt.body)
    return False


def _check_file(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    if not _has_required_import(tree):
        raise GuardViolation(
            f"{path}: Import von {REQUIRED_IMPORT_NAME} aus {REQUIRED_IMPORT_MODULE} fehlt."
        )

    if not _main_guard_present(tree):
        raise GuardViolation(
            f"{path}: Guard 'if not args.{REQUIRED_GUARD_ARG}:' mit Aufruf von "
            f"{REQUIRED_IMPORT_NAME}(...) in main() fehlt."
        )


def main() -> int:
    violations: list[str] = []

    for target in TARGETS:
        if not target.exists():
            violations.append(f"Datei nicht gefunden: {target}")
            continue
        try:
            _check_file(target)
        except (GuardViolation, SyntaxError) as exc:
            violations.append(str(exc))

    if violations:
        print("FEHLER: Live-Test-Preflight-Guard verletzt:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("OK: Live-Test-Preflight-Guard in allen Bewertungs-Einstiegsskripten vorhanden.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
