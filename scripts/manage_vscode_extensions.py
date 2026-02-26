#!/usr/bin/env python3
"""
Verwaltet VS Code Extensions für dieses Repository zentral.

Funktionen:
- install: installiert Extensions aus einem Profil
- sync: aktualisiert .vscode/extensions.json aus dem Manifest
- check: prüft, ob .vscode/extensions.json mit dem Manifest übereinstimmt

Verwendung:
    python3 scripts/manage_vscode_extensions.py install --profile live-test
    python3 scripts/manage_vscode_extensions.py sync
    python3 scripts/manage_vscode_extensions.py check
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PROJECT_ROOT / "scripts" / "config" / "vscode_extensions.json"
WORKSPACE_EXTENSIONS_PATH = PROJECT_ROOT / ".vscode" / "extensions.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verwaltet VS Code Extensions aus zentralem Manifest.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install", help="Installiert Extensions für ein Profil.")
    install_parser.add_argument("--profile", default=None, help="Profilname aus dem Manifest (z. B. live-test, full)")
    install_parser.add_argument(
        "--cli",
        default=None,
        help="Explizites VS-Code-CLI Kommando (z. B. code, code-insiders, codium)",
    )
    install_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Nur anzeigen, welche Extensions installiert würden.",
    )

    sync_parser = subparsers.add_parser("sync", help="Schreibt .vscode/extensions.json aus Manifest.")
    sync_parser.add_argument("--profile", default=None, help="Profilname aus dem Manifest")

    check_parser = subparsers.add_parser("check", help="Prüft Manifest-Abgleich von .vscode/extensions.json.")
    check_parser.add_argument("--profile", default=None, help="Profilname aus dem Manifest")

    return parser.parse_args()


def load_manifest() -> Dict:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest nicht gefunden: {MANIFEST_PATH}")
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def dedupe_keep_order(items: List[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def resolve_profile(manifest: Dict, profile_name: str | None) -> str:
    if profile_name:
        return profile_name
    default_profile = manifest.get("defaultProfile")
    if not default_profile:
        raise ValueError("defaultProfile fehlt im Manifest.")
    return default_profile


def get_extensions_for_profile(manifest: Dict, profile_name: str) -> List[str]:
    profiles = manifest.get("profiles", {})
    groups = manifest.get("groups", {})

    if profile_name not in profiles:
        available = ", ".join(sorted(profiles.keys()))
        raise ValueError(f"Unbekanntes Profil: {profile_name}. Verfügbar: {available}")

    resolved: List[str] = []
    for group_name in profiles[profile_name]:
        if group_name not in groups:
            raise ValueError(f"Unbekannte Gruppe im Profil '{profile_name}': {group_name}")
        group_extensions = groups[group_name]
        if not isinstance(group_extensions, list):
            raise ValueError(f"Gruppe '{group_name}' muss eine Liste sein.")
        resolved.extend(group_extensions)

    return dedupe_keep_order(resolved)


def create_workspace_extensions_payload(extensions: List[str]) -> Dict[str, List[str]]:
    return {
        "recommendations": extensions,
        "unwantedRecommendations": [],
    }


def write_workspace_extensions_file(payload: Dict[str, List[str]]) -> None:
    WORKSPACE_EXTENSIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    WORKSPACE_EXTENSIONS_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def read_existing_workspace_extensions_payload() -> Dict:
    if not WORKSPACE_EXTENSIONS_PATH.exists():
        return {}
    return json.loads(WORKSPACE_EXTENSIONS_PATH.read_text(encoding="utf-8"))


def detect_vscode_cli(explicit_cli: str | None = None) -> str:
    if explicit_cli:
        if shutil.which(explicit_cli):
            return explicit_cli
        raise RuntimeError(f"CLI '{explicit_cli}' nicht gefunden.")

    candidates = ["code", "code-insiders", "codium"]
    for candidate in candidates:
        if shutil.which(candidate):
            return candidate

    raise RuntimeError(
        "Kein VS-Code-CLI gefunden (code/code-insiders/codium). "
        "Nutze in VS Code alternativ: 'Show Recommended Extensions' → 'Install Workspace Recommended Extensions'."
    )


def install_extensions(extensions: List[str], cli_command: str, dry_run: bool) -> int:
    print(f"📦 Profil enthält {len(extensions)} Extensions.")
    if dry_run:
        for extension in extensions:
            print(f"- {extension}")
        return 0

    for extension in extensions:
        print(f"➡️  Installiere: {extension}")
        result = subprocess.run([cli_command, "--install-extension", extension], check=False)
        if result.returncode != 0:
            print(f"❌ Installation fehlgeschlagen: {extension}")
            return result.returncode

    print("✅ Installation abgeschlossen.")
    return 0


def run_sync(manifest: Dict, profile_name: str | None) -> int:
    profile = resolve_profile(manifest, profile_name)
    extensions = get_extensions_for_profile(manifest, profile)
    payload = create_workspace_extensions_payload(extensions)
    write_workspace_extensions_file(payload)
    print(
        f"✅ {WORKSPACE_EXTENSIONS_PATH.relative_to(PROJECT_ROOT)} mit "
        f"{len(extensions)} Empfehlungen aus Profil '{profile}' aktualisiert."
    )
    return 0


def run_check(manifest: Dict, profile_name: str | None) -> int:
    profile = resolve_profile(manifest, profile_name)
    expected = create_workspace_extensions_payload(get_extensions_for_profile(manifest, profile))
    current = read_existing_workspace_extensions_payload()

    if expected == current:
        print("✅ .vscode/extensions.json ist mit dem Manifest synchron.")
        return 0

    print("⚠️ .vscode/extensions.json weicht vom Manifest ab.")
    print("   Führe aus: python3 scripts/manage_vscode_extensions.py sync")
    return 2


def main() -> int:
    args = parse_args()
    manifest = load_manifest()

    if args.command == "sync":
        return run_sync(manifest, args.profile)

    if args.command == "check":
        return run_check(manifest, args.profile)

    if args.command == "install":
        profile = resolve_profile(manifest, args.profile)
        extensions = get_extensions_for_profile(manifest, profile)
        cli_command = detect_vscode_cli(args.cli)
        return install_extensions(extensions, cli_command, args.dry_run)

    raise ValueError(f"Unbekannter Befehl: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())