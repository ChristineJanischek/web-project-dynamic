from __future__ import annotations

import json
from pathlib import Path


def detect_project_type(project_root: Path) -> str:
    """Erkennt den Projekttyp anhand von Dateisignalen im Projekt-Root.

    Rückgabewerte (geordnet nach Spezifität):
    - 'web-vite'       – Vite-basiertes Projekt
    - 'web-react'      – React-Projekt (CRA oder Vite)
    - 'web-vue'        – Vue-Projekt
    - 'web-node'       – Unbekanntes Node-Projekt mit package.json
    - 'web-php-static' – PHP-Projekt ohne package.json
    - 'web-static'     – Reines HTML/CSS/JS-Projekt
    - 'web-unknown'    – Nicht eindeutig erkennbar
    """
    pkg_path = project_root / "package.json"
    if pkg_path.exists():
        return _detect_from_package_json(pkg_path)

    if any(project_root.rglob("*.php")):
        return "web-php-static"

    if (project_root / "index.html").exists():
        return "web-static"

    if any(project_root.glob("*.html")):
        return "web-static"

    return "web-unknown"


def _detect_from_package_json(pkg_path: Path) -> str:
    try:
        pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return "web-node"

    all_deps: dict = {}
    all_deps.update(pkg.get("dependencies", {}))
    all_deps.update(pkg.get("devDependencies", {}))

    if "vite" in all_deps:
        if "react" in all_deps or "@vitejs/plugin-react" in all_deps:
            return "web-react"
        if "vue" in all_deps or "@vitejs/plugin-vue" in all_deps:
            return "web-vue"
        return "web-vite"

    if "next" in all_deps:
        return "web-next"

    if "react" in all_deps:
        return "web-react"

    if "vue" in all_deps:
        return "web-vue"

    return "web-node"
