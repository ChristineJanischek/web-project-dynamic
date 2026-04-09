from __future__ import annotations

import os
import stat
from pathlib import Path


def ensure_path_is_outside_repo(workspace_root: Path, repo_root: Path) -> None:
    workspace_root = workspace_root.resolve()
    repo_root = repo_root.resolve()

    try:
        workspace_root.relative_to(repo_root)
    except ValueError:
        return

    raise ValueError(
        "Der owner-only Workspace darf nicht innerhalb des Repositorys liegen. "
        "Bitte einen Pfad ausserhalb von repo_root verwenden."
    )


def ensure_directory(path: Path, mode: int = 0o700) -> None:
    path.mkdir(parents=True, exist_ok=True)
    os.chmod(path, mode)


def ensure_file_mode(path: Path, mode: int = 0o600) -> None:
    current_mode = stat.S_IMODE(path.stat().st_mode)
    if current_mode != mode:
        os.chmod(path, mode)
