#!/usr/bin/env python3
"""Blockiert versehentlich versionierte sensible Korrekturhilfe-Artefakte.

Dieses Skript prueft den aktuell getrackten Git-Dateibestand und bricht mit Exit-Code 1 ab,
sobald sensible Bewertungs-/Korrekturhilfe-Dateien im Repository liegen.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


FORBIDDEN_PATH_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(^|/)exports/", re.IGNORECASE),
    re.compile(r"(^|/)downloads/", re.IGNORECASE),
    re.compile(r"(^|/)assessment-owner/", re.IGNORECASE),
    re.compile(r"(^|/)batch_bewertungen/", re.IGNORECASE),
    re.compile(r"_korrekturhilfe_draft\.(json|md|html)$", re.IGNORECASE),
    re.compile(r"_korrekturhilfe_start\.md$", re.IGNORECASE),
    re.compile(r"_bewertung_draft\.(json|md|html)$", re.IGNORECASE),
    re.compile(r"_bewertung_start\.md$", re.IGNORECASE),
    re.compile(r"(^|/)(korrekturhilfe|bewertungs)uebersicht\.(md|html)$", re.IGNORECASE),
    re.compile(r"(^|/)rangliste\.(md|html)$", re.IGNORECASE),
)

# In material/uploads sind nur bewusst freigegebene Vorlagen erlaubt.
ALLOWED_UPLOAD_FILES = {
    "material/uploads/korrekturhilfe_abdul.html",
}


def git_tracked_files(repo_root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print("Fehler: git ls-files konnte nicht ausgefuehrt werden.", file=sys.stderr)
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(2)

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def find_violations(paths: list[str]) -> list[str]:
    violations: list[str] = []

    for rel_path in paths:
        rel_posix = rel_path.replace("\\", "/")

        for pattern in FORBIDDEN_PATH_PATTERNS:
            if pattern.search(rel_posix):
                violations.append(rel_posix)
                break

        if rel_posix.startswith("material/uploads/") and rel_posix not in ALLOWED_UPLOAD_FILES:
            violations.append(rel_posix)

    # Deduplizieren, stabile Reihenfolge
    seen: set[str] = set()
    ordered: list[str] = []
    for item in violations:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    tracked = git_tracked_files(repo_root)
    violations = find_violations(tracked)

    if not violations:
        print("OK: Keine sensiblen Korrekturhilfe-Artefakte im Repository getrackt.")
        return 0

    print("FEHLER: Sensible Korrekturhilfe-Dateien duerfen nicht im Repository liegen:")
    for path in violations:
        print(f"  - {path}")

    print("\nEmpfehlung:")
    print("  1) Dateien aus Git entfernen: git rm --cached <pfad>")
    print("  2) Falls noetig lokal behalten (.gitignore greift)")
    print("  3) Check erneut ausfuehren")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
