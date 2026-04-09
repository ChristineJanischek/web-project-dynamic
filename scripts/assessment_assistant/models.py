from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import List


class CriterionStatus(str, Enum):
    ERFUELLT = "erfuellt"
    TEILWEISE = "teilweise"
    NICHT_ERFUELLT = "nicht_erfuellt"
    MANUELL_PRUEFEN = "manuell_pruefen"


@dataclass(slots=True)
class EvaluationCriterion:
    criterion_id: str
    title: str
    max_points: float
    awarded_points: float = 0.0
    status: CriterionStatus = CriterionStatus.MANUELL_PRUEFEN
    evidence: List[str] = field(default_factory=list)
    note: str = ""

    def to_dict(self) -> dict:
        payload = asdict(self)
        payload["status"] = self.status.value
        return payload


@dataclass(slots=True)
class RecommendationItem:
    title: str
    rationale: str
    effort_hint: str


@dataclass(slots=True)
class RecommendationPlan:
    focus: str
    extensions: List[RecommendationItem] = field(default_factory=list)
    todos_until_june: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "focus": self.focus,
            "extensions": [asdict(item) for item in self.extensions],
            "todos_until_june": list(self.todos_until_june),
        }


@dataclass(slots=True)
class EvaluationReport:
    report_id: str
    rubric_id: str
    project_type: str
    student_project_name: str
    max_points: float
    awarded_points: float = 0.0
    grade: float = 6.0
    criteria: List[EvaluationCriterion] = field(default_factory=list)
    summary: str = ""
    recommendation_plan: RecommendationPlan | None = None

    def to_dict(self) -> dict:
        payload = {
            "report_id": self.report_id,
            "rubric_id": self.rubric_id,
            "project_type": self.project_type,
            "student_project_name": self.student_project_name,
            "max_points": self.max_points,
            "awarded_points": self.awarded_points,
            "grade": self.grade,
            "summary": self.summary,
            "criteria": [criterion.to_dict() for criterion in self.criteria],
        }

        if self.recommendation_plan is not None:
            payload["recommendation_plan"] = self.recommendation_plan.to_dict()

        return payload