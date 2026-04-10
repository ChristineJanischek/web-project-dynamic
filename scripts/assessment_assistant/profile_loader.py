from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class GradeScale:
    best: float
    worst: float


@dataclass(slots=True)
class CriterionProfile:
    criterion_id: str
    title: str
    description: str
    max_points: float
    kind: str
    config: dict[str, Any]
    evidence_hint: str = ""


@dataclass(slots=True)
class GradingProfile:
    profile_id: str
    profile_name: str
    project_type: str
    max_points: float
    grade_scale: GradeScale
    criteria: list[CriterionProfile]
    point_levels: dict[str, int] = field(default_factory=dict)
    version: str = "1.0"


def load_profile(path: Path) -> GradingProfile:
    raw = json.loads(path.read_text(encoding="utf-8"))
    _validate_raw(raw, path)

    grade_scale = GradeScale(
        best=float(raw["grade_scale"]["best"]),
        worst=float(raw["grade_scale"]["worst"]),
    )

    criteria: list[CriterionProfile] = []
    seen_ids: set[str] = set()
    for item in raw["criteria"]:
        cid = str(item["id"])
        if cid in seen_ids:
            raise ValueError(
                f"Profil '{path}': Doppelte Kriterium-ID '{cid}'."
            )
        seen_ids.add(cid)
        criteria.append(
            CriterionProfile(
                criterion_id=cid,
                title=str(item["title"]),
                description=str(item.get("description", "")),
                max_points=float(item["max_points"]),
                kind=str(item["kind"]),
                config=dict(item.get("config", {})),
                evidence_hint=str(item.get("evidence_hint", "")),
            )
        )

    declared_max = float(raw["max_points"])
    computed_max = sum(c.max_points for c in criteria)
    if abs(declared_max - computed_max) > 0.01:
        raise ValueError(
            f"Profil '{path}': max_points ({declared_max}) stimmt nicht mit "
            f"Summe der Kriterien ({computed_max}) überein."
        )

    return GradingProfile(
        profile_id=str(raw["profile_id"]),
        profile_name=str(raw["profile_name"]),
        project_type=str(raw["project_type"]),
        max_points=declared_max,
        grade_scale=grade_scale,
        point_levels=dict(raw.get("point_levels", {})),
        criteria=criteria,
        version=str(raw.get("version", "1.0")),
    )


def find_profile(profiles_dir: Path, profile_id: str) -> Path | None:
    for path in profiles_dir.glob("*.json"):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if raw.get("profile_id") == profile_id:
                return path
        except (json.JSONDecodeError, KeyError):
            continue
    return None


def _validate_raw(raw: dict, path: Path) -> None:
    required = ("profile_id", "profile_name", "project_type", "max_points", "grade_scale", "criteria")
    missing = [key for key in required if key not in raw]
    if missing:
        raise ValueError(
            f"Profil '{path}' fehlen Pflichtfelder: {', '.join(missing)}"
        )
    if not isinstance(raw["criteria"], list) or not raw["criteria"]:
        raise ValueError(f"Profil '{path}': 'criteria' muss eine nicht-leere Liste sein.")
