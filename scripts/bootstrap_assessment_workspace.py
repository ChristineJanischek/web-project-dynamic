#!/usr/bin/env python3
"""Bootstrap fuer den owner-only Workspace der Bewertungsassistenz."""

from __future__ import annotations

import argparse
from pathlib import Path

from assessment_assistant.bootstrap import bootstrap_workspace
from assessment_assistant.config import AssessmentWorkspaceConfig, default_workspace_root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Legt einen abgesicherten Owner-Workspace fuer Bewertungsdaten an."
    )
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=default_workspace_root(),
        help="Pfad fuer owner-only Bewertungsdaten, standardmaessig unter ~/Downloads/edu-assessment-owner",
    )
    parser.add_argument(
        "--profile-name",
        default="default",
        help="Name des Owner-Profils fuer spaetere Mehrfach-Konfigurationen",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = AssessmentWorkspaceConfig(
        workspace_root=args.workspace_root,
        profile_name=args.profile_name,
    )
    created_directories = bootstrap_workspace(config)

    print("Owner-only Assessment Workspace initialisiert:")
    for name, path in created_directories.items():
        print(f"- {name}: {path}")

    print(f"- profile: {config.config_dir / 'owner_profile.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())