from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import json
import re

from .models import CriterionStatus, EvaluationCriterion, EvaluationReport
from .profile_loader import GradingProfile
from .rule_engine import evaluate_rule
from .profile_loader import GradingProfile
from .rule_engine import evaluate_rule


POINTS_REGEX = re.compile(
    r"(?P<points>\d+(?:[\.,]\d+)?)\s*(?:punkte|punkt|pts|p)\b",
    re.IGNORECASE,
)

CRITERION_HINTS = (
    "kriter",
    "bewert",
    "anforder",
    "punkt",
    "mvc",
    "funktion",
    "layout",
    "css",
    "html",
    "php",
    "javascript",
    "js",
    "sql",
)


def parse_rubric_to_criteria(rubric_lines: list[str], limit: int = 30) -> list[EvaluationCriterion]:
    criteria: list[EvaluationCriterion] = []
    seen_titles: set[str] = set()

    for line in rubric_lines:
        if len(criteria) >= limit:
            break

        lowered = line.lower()
        if not any(token in lowered for token in CRITERION_HINTS):
            continue

        points_match = POINTS_REGEX.search(line)
        points = 1.0
        if points_match is not None:
            points = float(points_match.group("points").replace(",", "."))

        title = _clean_title(line)
        if len(title) < 4:
            continue

        title_key = title.lower()
        if title_key in {"kriterium", "bewertung", "punkte"}:
            continue
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)

        criteria.append(
            EvaluationCriterion(
                criterion_id=f"kriterium_{len(criteria) + 1:02d}",
                title=title,
                max_points=points,
            )
        )

    return criteria


def evaluate_project(
    project_name: str,
    project_root: Path,
    rubric_id: str,
    criteria: list[EvaluationCriterion],
) -> EvaluationReport:
    file_index = _build_file_index(project_root)
    evaluated: list[EvaluationCriterion] = []

    for criterion in criteria:
        evidence = _collect_evidence(criterion.title, file_index)
        if evidence:
            evaluated.append(
                replace(
                    criterion,
                    awarded_points=criterion.max_points,
                    status=CriterionStatus.ERFUELLT,
                    evidence=evidence,
                    note="Automatisch erkannt ueber Dateistruktur.",
                )
            )
        else:
            evaluated.append(
                replace(
                    criterion,
                    awarded_points=0.0,
                    status=CriterionStatus.MANUELL_PRUEFEN,
                    evidence=[],
                    note="Kein automatischer Treffer, bitte manuell pruefen.",
                )
            )

    max_points = sum(item.max_points for item in evaluated)
    awarded_points = sum(item.awarded_points for item in evaluated)
    grade = compute_grade(awarded_points, max_points)

    return EvaluationReport(
        report_id=f"{project_name}_report",
        rubric_id=rubric_id,
        project_type="web_project",
        student_project_name=project_name,
        max_points=max_points,
        awarded_points=awarded_points,
        grade=grade,
        criteria=evaluated,
        summary=(
            "Automatische Erstbewertung auf Basis der Dateistruktur. "
            "Alle Kriterien mit Status manuell_pruefen oder unscharfer Evidenz nachpruefen."
        ),
    )


def compute_grade(awarded_points: float, max_points: float) -> float:
    if max_points <= 0:
        return 6.0

    percent = awarded_points / max_points
    grade = 6.0 - (percent * 5.0)
    grade = min(6.0, max(1.0, grade))
    return round(grade, 2)


def write_report_json(target_path: Path, report: EvaluationReport) -> Path:
    payload = json.dumps(report.to_dict(), indent=2, ensure_ascii=False)
    target_path.write_text(f"{payload}\n", encoding="utf-8")
    return target_path


def write_report_markdown(target_path: Path, report: EvaluationReport) -> Path:
    lines = [
        "# Bewertungsbericht (Draft)",
        "",
        f"Projekt: {report.student_project_name}",
        f"Rubrik: {report.rubric_id}",
        f"Punkte: {report.awarded_points:.2f} / {report.max_points:.2f}",
        f"Note: {report.grade:.2f}",
        "",
        "## Kriterien",
        "",
    ]

    for criterion in report.criteria:
        lines.append(
            (
                f"- [{criterion.status.value}] {criterion.criterion_id}: {criterion.title} "
                f"({criterion.awarded_points:.2f}/{criterion.max_points:.2f})"
            )
        )
        if criterion.evidence:
            lines.append(f"  Evidenz: {', '.join(criterion.evidence[:3])}")
        if criterion.note:
            lines.append(f"  Hinweis: {criterion.note}")

    lines.extend(["", "## Zusammenfassung", "", report.summary])
    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target_path


def _clean_title(line: str) -> str:
    title = POINTS_REGEX.sub("", line)
    title = title.replace("-", " ")
    title = re.sub(r"\s+", " ", title).strip(" :;,.\t")
    return title


def _build_file_index(project_root: Path) -> list[str]:
    result: list[str] = []
    for path in project_root.rglob("*"):
        if path.is_file():
            result.append(path.relative_to(project_root).as_posix().lower())
    return result


def _collect_evidence(title: str, file_index: list[str]) -> list[str]:
    lowered = title.lower()
    patterns: list[str] = []

    if "controller" in lowered:
        patterns.extend(["controller", "controllers/"])
    if "model" in lowered:
        patterns.extend(["model", "models/"])
    if "view" in lowered or "layout" in lowered:
        patterns.extend(["view", "views/", "layout", "layouts/"])
    if "css" in lowered:
        patterns.append(".css")
    if "javascript" in lowered or " js" in f" {lowered}":
        patterns.append(".js")
    if "php" in lowered:
        patterns.append(".php")
    if "html" in lowered:
        patterns.append(".html")
    if "sql" in lowered or "datenbank" in lowered:
        patterns.append(".sql")

    if not patterns:
        return []

    matches: list[str] = []
    for rel_path in file_index:
        if any(pattern in rel_path for pattern in patterns):
            matches.append(rel_path)
        if len(matches) >= 5:
            break

    return matches


# ---------------------------------------------------------------------------
# Profilbasierte Bewertung (bevorzugter Weg)
# ---------------------------------------------------------------------------

def evaluate_project_with_profile(
    project_name: str,
    project_root: Path,
    profile: GradingProfile,
) -> EvaluationReport:
    """Bewertet ein Projekt anhand eines strukturierten JSON-Profils.

    Bewertungslogik je Kriterium:
    - 'manual'       → MANUELL_PRUEFEN, 0 Punkte (Lehrkraft trägt ein)
    - Regel erfüllt  → ERFUELLT, max_points (vorläufig; Lehrkraft passt auf 4/3/2/1 an)
    - Teils erfüllt  → TEILWEISE, 0 Punkte (Lehrkraft passt an)
    - Nicht erfüllt  → NICHT_ERFUELLT, 0 Punkte
    """
    evaluated: list[EvaluationCriterion] = []

    for crit in profile.criteria:
        rule_result = evaluate_rule(
            kind=crit.kind,
            config=crit.config,
            project_root=project_root,
            label=crit.title,
        )
        status, awarded = _resolve_status_and_points(crit.kind, rule_result, crit.max_points)

        note_parts = [rule_result.note]
        if crit.evidence_hint:
            note_parts.append(crit.evidence_hint)

        evaluated.append(
            EvaluationCriterion(
                criterion_id=crit.criterion_id,
                title=crit.title,
                max_points=crit.max_points,
                awarded_points=awarded,
                status=status,
                evidence=rule_result.evidence,
                note=" | ".join(filter(None, note_parts)),
            )
        )

    awarded_total = sum(c.awarded_points for c in evaluated)
    grade = compute_grade(awarded_total, profile.max_points)
    manual_count = sum(1 for c in evaluated if c.status == CriterionStatus.MANUELL_PRUEFEN)

    summary = (
        f"Profil-basierte Erstbewertung '{profile.profile_name}'. "
        f"{manual_count} von {len(evaluated)} Kriterien erfordern manuelle Prüfung. "
        "Vorläufige Punkte bei ERFUELLT auf der 4/3/2/1-Skala anpassen."
    )

    return EvaluationReport(
        report_id=f"{project_name}_report",
        rubric_id=profile.profile_id,
        project_type=profile.project_type,
        student_project_name=project_name,
        max_points=profile.max_points,
        awarded_points=awarded_total,
        grade=grade,
        criteria=evaluated,
        summary=summary,
    )


def _resolve_status_and_points(
    kind: str,
    rule_result,
    max_points: float,
) -> tuple[CriterionStatus, float]:
    if kind == "manual":
        return CriterionStatus.MANUELL_PRUEFEN, 0.0
    if rule_result.passed:
        return CriterionStatus.ERFUELLT, max_points
    # Prüfe ob all_of teilweise erfüllt war
    teilweise = re.search(r"(\d+)/(\d+) Teilregeln", rule_result.note or "")
    if teilweise and int(teilweise.group(1)) > 0:
        return CriterionStatus.TEILWEISE, 0.0
    return CriterionStatus.NICHT_ERFUELLT, 0.0
