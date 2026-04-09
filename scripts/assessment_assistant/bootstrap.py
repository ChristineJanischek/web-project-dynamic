from __future__ import annotations

from pathlib import Path

from .config import AssessmentWorkspaceConfig
from .security import ensure_directory, ensure_file_mode, ensure_path_is_outside_repo


README_CONTENT = """# Owner-only Assessment Workspace

Dieser Bereich ist fuer sensible Bewertungsdaten reserviert.

- Keine Inhalte aus diesem Verzeichnis committen oder in Templates uebernehmen.
- ZIP-Archive mit Schuelerprojekten liegen in eingang/.
- Bewertungsboegen liegen in boegen/.
- Generierte Markdown-, HTML- und spaetere Word-Artefakte liegen in ausgang/.
- Abgeschlossene oder ersetzte Daten werden in archiv/ verschoben.

Sicherheitsregel:
- Verzeichnisrechte nur fuer den Owner.
- Bewertungsdaten gelten immer als vertraulich.
"""


def bootstrap_workspace(config: AssessmentWorkspaceConfig) -> dict[str, Path]:
    ensure_path_is_outside_repo(config.workspace_root, config.repo_root)
    ensure_directory(config.workspace_root)

    created_directories: dict[str, Path] = {}
    for name, path in config.required_directories().items():
        ensure_directory(path)
        created_directories[name] = path

    readme_path = config.workspace_root / "README.md"
    if not readme_path.exists():
        readme_path.write_text(README_CONTENT, encoding="utf-8")
    ensure_file_mode(readme_path)

    profile_path = config.config_dir / "owner_profile.json"
    if not profile_path.exists():
        config.write_profile(profile_path)
    ensure_file_mode(profile_path)

    return created_directories