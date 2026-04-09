from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


DEFAULT_DIRECTORY_MAP = {
    "archiv": "archiv",
    "ausgang": "ausgang",
    "batch_bewertungen": "batch_bewertungen",
    "boegen": "boegen",
    "eingang": "eingang",
    "entpackt": "entpackt",
    "logs": "logs",
}


def default_workspace_root() -> Path:
    return Path.home() / "Downloads" / "edu-assessment-owner"


@dataclass(slots=True)
class AssessmentWorkspaceConfig:
    workspace_root: Path = field(default_factory=default_workspace_root)
    repo_root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2])
    profile_name: str = "default"
    owner_visibility: str = "owner-only"
    allowed_archive_suffixes: tuple[str, ...] = (".zip",)
    allowed_rubric_suffixes: tuple[str, ...] = (".docx", ".md")
    directory_map: dict[str, str] = field(
        default_factory=lambda: dict(DEFAULT_DIRECTORY_MAP)
    )

    @property
    def config_dir(self) -> Path:
        return self.workspace_root / "config"

    @property
    def reports_dir(self) -> Path:
        return self.workspace_root / self.directory_map["ausgang"]

    def required_directories(self) -> dict[str, Path]:
        directories = {
            key: self.workspace_root / value for key, value in self.directory_map.items()
        }
        directories["config"] = self.config_dir
        return directories

    def to_dict(self) -> dict:
        return {
            "profile_name": self.profile_name,
            "owner_visibility": self.owner_visibility,
            "workspace_root": str(self.workspace_root),
            "allowed_archive_suffixes": list(self.allowed_archive_suffixes),
            "allowed_rubric_suffixes": list(self.allowed_rubric_suffixes),
            "directory_map": dict(self.directory_map),
            "security": {
                "workspace_root_must_be_outside_repo": True,
                "directory_mode": "700",
                "config_file_mode": "600",
                "generated_reports_are_sensitive": True,
            },
            "grading": {
                "scale": "linear",
                "grade_range": [1.0, 6.0],
                "decimal_places": 2,
            },
            "reporting": {
                "canonical_source": "markdown",
                "html_export": "copy-safe-for-word",
            },
        }

    def write_profile(self, profile_path: Path) -> None:
        payload = json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
        profile_path.write_text(f"{payload}\n", encoding="utf-8")
