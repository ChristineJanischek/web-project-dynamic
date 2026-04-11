from __future__ import annotations

from dataclasses import replace
from datetime import datetime
from html import escape
from pathlib import Path
import json
import re
import shutil
import subprocess

from .models import CriterionStatus, EvaluationCriterion, EvaluationReport, RecommendationItem, RecommendationPlan
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
            "Automatische Erst-Korrekturhilfe auf Basis der Dateistruktur. "
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
        "# Korrekturhilfe (Draft)",
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

    if report.recommendation_plan is not None:
        plan = report.recommendation_plan
        lines.extend([
            "", "## Marschplan: Vertiefung bis Anfang Juni", "",
            plan.focus, "",
        ])
        for i, ext in enumerate(plan.extensions, start=1):
            lines.extend([
                f"### Erweiterung {i}: {ext.title}", "",
                ext.rationale, "",
                f"**Aufwand und Schritte:** {ext.effort_hint}", "",
            ])
        lines.extend(["### ToDo-Liste", ""])
        for todo in plan.todos_until_june:
            lines.append(f"- {todo}")
        lines.append("")

    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target_path


def write_report_html(target_path: Path, report: EvaluationReport) -> Path:
    status_counts = _count_statuses(report)
    now_text = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Raster-Zeilen (kompakte Uebersichtstabelle)
    raster_rows: list[str] = []
    for c in report.criteria:
        evidence_text = (
            " | ".join(c.evidence[:2])
            if c.evidence
            else (c.note.split("|")[0].strip() if c.note else "-")
        )
        raster_rows.append(
            "<tr>"
            f"<td>{escape(c.criterion_id)}</td>"
            f"<td>{escape(c.title)}</td>"
            f'<td style="text-align:right;">{c.awarded_points:.2f} / {c.max_points:.2f}</td>'
            f'<td><span class="{_status_css_class(c.status)}">{escape(_status_label(c.status))}</span></td>'
            f"<td>{escape(evidence_text)}</td>"
            "</tr>"
        )

    # Einzelkriterien mit paedagogischem Feedback
    detail_parts: list[str] = []
    for c in report.criteria:
        appreciation = _pedagogical_appreciation(c)
        next_step = _pedagogical_next_step(c)
        teacher_hint = _teacher_check_hint(c)
        evidence_items = (
            "".join(f"<li>{escape(e)}</li>" for e in c.evidence[:5])
            or "<li>&#8211;</li>"
        )
        note_text = escape(c.note) if c.note else "&#8211;"
        detail_parts.append(
            f"<h3>{escape(c.criterion_id)} &#8211; {escape(c.title)}</h3>\n"
            "<ul>\n"
            f"  <li>Punkte: {c.awarded_points:.2f} / {c.max_points:.2f}</li>\n"
            f'  <li>Status: <span class="{_status_css_class(c.status)}">{escape(_status_label(c.status))}</span></li>\n'
            f"  <li>Evidenz: <ul>{evidence_items}</ul></li>\n"
            f"  <li>Anmerkung: {note_text}</li>\n"
            f"  <li>Wuerdigung: {escape(appreciation)}</li>\n"
            f"  <li>Naechster Schritt: {escape(next_step)}</li>\n"
            f"  <li>Lehrkraft-Hinweis: {escape(teacher_hint)}</li>\n"
            "</ul>\n"
        )

    rec_block = _render_recommendation_html(report.recommendation_plan)

    css = (
        "  <style>\n"
        "    body {\n"
        "      margin: 1.5cm;\n"
        "      font-family: Calibri, 'Segoe UI', Arial, sans-serif;\n"
        "      font-size: 11pt;\n"
        "      color: #111;\n"
        "      line-height: 1.35;\n"
        "      background: #fff;\n"
        "      max-width: 180mm;\n"
        "    }\n"
        "    h1 { font-size: 19pt; margin-bottom: 0.5em; }\n"
        "    h2 { font-size: 14pt; margin-top: 1.2em; margin-bottom: 0.4em;"
        " border-bottom: 1px solid #b9c3d1; padding-bottom: 4px; }\n"
        "    h3 { font-size: 12pt; margin-top: 1em; margin-bottom: 0.3em; }\n"
        "    table { border-collapse: collapse; width: 100%; margin: 0.6em 0 1em 0;"
        " font-size: 10.5pt; table-layout: fixed; }\n"
        "    th, td { border: 1px solid #9ca9ba; padding: 6px 8px; vertical-align: top;"
        " overflow-wrap: anywhere; word-break: break-word; hyphens: auto; }\n"
        "    th { background: #e8eef7; text-align: left; }\n"
        "    th:nth-child(1), td:nth-child(1) { width: 6%; }\n"
        "    th:nth-child(2), td:nth-child(2) { width: 34%; }\n"
        "    th:nth-child(3), td:nth-child(3) { width: 14%; text-align: right; }\n"
        "    th:nth-child(4), td:nth-child(4) { width: 14%; }\n"
        "    th:nth-child(5), td:nth-child(5) { width: 32%; }\n"
        "    ul { margin-top: 0.3em; }\n"
        "    hr { border: 0; border-top: 1px solid #c8d0dd; margin: 1.1em 0; }\n"
        "    .erfuellt { color: #2d6a4f; font-weight: 700; }\n"
        "    .teilweise { color: #9a6700; font-weight: 700; }\n"
        "    .nicht-erfuellt { color: #9f1d1d; font-weight: 700; }\n"
        "    .manuell { color: #345a8a; font-weight: 700; }\n"
        "    .hinweis { background: #f4f8ff; border-left: 4px solid #345a8a;"
        " padding: 6px 10px; margin: 0.4em 0 0.8em 0; display: block; }\n"
        "    @media print {\n"
        "      body { margin: 1.2cm; max-width: none; }\n"
        "      h1, h2, h3 { page-break-after: avoid; }\n"
        "      table { page-break-inside: auto; }\n"
        "      tr { page-break-inside: avoid; page-break-after: auto; }\n"
        "    }\n"
        "  </style>\n"
    )

    html = (
        "<!DOCTYPE html>\n"
        '<html lang="de">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'  <title>Korrekturhilfe &#8211; {escape(report.student_project_name)}</title>\n'
        + css
        + "</head>\n"
        "<body>\n"
        "<h1>Korrekturhilfe</h1>\n"
        "<ul>\n"
        f"  <li>Datum: {escape(now_text)}</li>\n"
        f"  <li>Projekt: {escape(report.student_project_name)}</li>\n"
        f"  <li>Rubrik: {escape(report.rubric_id)}</li>\n"
        f"  <li>Projekttyp: {escape(report.project_type)}</li>\n"
        "</ul>\n"
        "<h2>Gesamtergebnis</h2>\n"
        "<ul>\n"
        f"  <li>Punkte: {report.awarded_points:.2f} / {report.max_points:.2f}</li>\n"
        f"  <li>Note (linear): {report.grade:.2f}</li>\n"
        f"  <li>Erfuellt: {status_counts[CriterionStatus.ERFUELLT]}"
        f" | Teilweise: {status_counts[CriterionStatus.TEILWEISE]}"
        f" | Nicht erfuellt: {status_counts[CriterionStatus.NICHT_ERFUELLT]}"
        f" | Manuell pruefen: {status_counts[CriterionStatus.MANUELL_PRUEFEN]}</li>\n"
        "</ul>\n"
        f"<p>{escape(report.summary)}</p>\n"
        "<h2>Korrekturhilfe-Raster</h2>\n"
        "<table>\n"
        "  <thead><tr>\n"
        "    <th>ID</th>\n"
        "    <th>Kriterium</th>\n"
        '    <th style="text-align:right;">Punkte</th>\n'
        "    <th>Status</th>\n"
        "    <th>Wichtigste Evidenz / Anmerkung</th>\n"
        "  </tr></thead>\n"
        "  <tbody>\n"
        + "".join(f"    {row}\n" for row in raster_rows)
        + "  </tbody>\n"
        "</table>\n"
        "<h2>Einzelkriterien und didaktisches Feedback</h2>\n"
        + "".join(detail_parts)
        + rec_block
        + "</body>\n"
        "</html>\n"
    )

    target_path.write_text(html, encoding="utf-8")
    return target_path


def _count_statuses(report: EvaluationReport) -> dict[CriterionStatus, int]:
    counts = {status: 0 for status in CriterionStatus}
    for criterion in report.criteria:
        counts[criterion.status] += 1
    return counts


def _render_recommendation_html(plan: RecommendationPlan | None) -> str:
    if plan is None:
        return ""

    ext_blocks = ""
    for i, ext in enumerate(plan.extensions, start=1):
        ext_blocks += (
            f"<h3>Erweiterung {i}: {escape(ext.title)}</h3>\n"
            "<ul>\n"
            f"  <li>Begruendung: {escape(ext.rationale)}</li>\n"
            f'  <li><span class="hinweis">Aufwand und Schritte: {escape(ext.effort_hint)}</span></li>\n'
            "</ul>\n"
        )

    todos_html = "".join(f"  <li>{escape(t)}</li>\n" for t in plan.todos_until_june)

    return (
        "<h2>Marschplan: Vertiefung bis Anfang Juni</h2>\n"
        f'<p class="hinweis">{escape(plan.focus)}</p>\n'
        + ext_blocks
        + "<h3>ToDo-Liste bis zur Verteidigung</h3>\n"
        + f"<ul>\n{todos_html}</ul>\n"
    )


def _status_label(status: CriterionStatus) -> str:
    return {
        CriterionStatus.ERFUELLT: "Erfuellt",
        CriterionStatus.TEILWEISE: "Teilweise",
        CriterionStatus.NICHT_ERFUELLT: "Nicht erfuellt",
        CriterionStatus.MANUELL_PRUEFEN: "Manuell pruefen",
    }[status]


def _status_css_class(status: CriterionStatus) -> str:
    return {
        CriterionStatus.ERFUELLT: "erfuellt",
        CriterionStatus.TEILWEISE: "teilweise",
        CriterionStatus.NICHT_ERFUELLT: "nicht-erfuellt",
        CriterionStatus.MANUELL_PRUEFEN: "manuell",
    }[status]


def _pedagogical_appreciation(criterion: EvaluationCriterion) -> str:
    topic = _criterion_topic(criterion.title)
    if criterion.status == CriterionStatus.ERFUELLT:
        return f"Die Grundanforderung im Bereich {topic} ist sichtbar umgesetzt. Darauf kann weiter aufgebaut werden."
    if criterion.status == CriterionStatus.TEILWEISE:
        return f"Im Bereich {topic} ist ein tragfaehiger Ansatz erkennbar, die Umsetzung ist aber noch nicht vollstaendig abgesichert."
    if criterion.status == CriterionStatus.NICHT_ERFUELLT:
        return f"Im Bereich {topic} fehlt derzeit ein belastbarer Nachweis im Projektstand."
    return f"Im Bereich {topic} ist eine faire Bewertung nur mit fachlicher Sichtung durch die Lehrkraft moeglich."


def _pedagogical_next_step(criterion: EvaluationCriterion) -> str:
    lowered = criterion.title.lower()
    if "struktur" in lowered or "quellcode" in lowered:
        return "Ordner, Dateinamen und Include-Pfade vereinheitlichen; danach die Lesbarkeit gezielt nacharbeiten."
    if "layout" in lowered or "inhalt" in lowered:
        return "Seitenaufbau im Browser pruefen und fehlende responsive oder semantische Elemente nachziehen."
    if "bilder" in lowered or "galerie" in lowered:
        return "Bildverzeichnis, Alt-Texte und Galerie-Navigation vervollstaendigen; Dateigroessen mitpruefen."
    if "verweise" in lowered or "links" in lowered:
        return "Navigation systematisch testen und externe Links mit sauberem Zielverhalten absichern."
    if "php" in lowered or "formulare" in lowered:
        return "Formularfluss mit Testdaten durchspielen und serverseitige Verarbeitung nachvollziehbar dokumentieren."
    if "version" in lowered or "git" in lowered:
        return "Repository-Link, Commit-Historie und sinnvolle Arbeitsschritte fuer die Bewertung sichtbar machen."
    if "dokumentation" in lowered:
        return "Quellcode an Schluesselstellen kommentieren und kurz begruenden, warum die Loesung so aufgebaut ist."
    if "design" in lowered or "farb" in lowered:
        return "Gestaltung auf Konsistenz, Lesbarkeit und mobile Darstellung hin ueberarbeiten."
    if "impressum" in lowered or "datenschutz" in lowered or "ki" in lowered:
        return "Pflichtseiten und Quellenangaben inhaltlich vervollstaendigen und gut sichtbar verlinken."
    if criterion.status == CriterionStatus.ERFUELLT:
        return "Das Kriterium ist tragfaehig angelegt; jetzt auf Qualitaet, Sauberkeit und Vollstaendigkeit optimieren."
    return "Dieses Kriterium gezielt mit der Aufgabenstellung abgleichen und danach den Nachweis im Projekt ergaenzen."


def _teacher_check_hint(criterion: EvaluationCriterion) -> str:
    if criterion.status == CriterionStatus.MANUELL_PRUEFEN:
        return "Hier braucht es eine fachliche Sichtung durch die Lehrkraft; insbesondere Abgabekontext oder Git-Historie pruefen."
    if criterion.status == CriterionStatus.TEILWEISE:
        return "Zwischenstand vorhanden; bitte Umfang, Qualitaet und Eigenleistung differenziert einstufen."
    if criterion.status == CriterionStatus.NICHT_ERFUELLT:
        return "Pruefen, ob der Nachweis nur anders benannt oder tiefer in Unterordnern abgelegt wurde."
    return "Automatischen Treffer kurz gegen Browserbild oder Quelltext querpruefen."


def _overall_next_step(report: EvaluationReport) -> str:
    manual = sum(1 for item in report.criteria if item.status == CriterionStatus.MANUELL_PRUEFEN)
    partial = sum(1 for item in report.criteria if item.status == CriterionStatus.TEILWEISE)
    failed = sum(1 for item in report.criteria if item.status == CriterionStatus.NICHT_ERFUELLT)

    if manual >= 2:
        return "Zuerst alle manuell zu pruefenden Kriterien mit Aufgabenblatt, Git-Verlauf und Browseransicht abgleichen."
    if partial or failed:
        return "Zuerst die teilweise oder nicht erfuellten Kriterien nacharbeiten, danach die Punktevergabe fein justieren."
    return "Automatische Treffer sind stark; jetzt nur noch fachliche Feinkontrolle und endgueltige Punktabstufung vornehmen."


def _criterion_topic(title: str) -> str:
    lowered = title.lower()
    if "struktur" in lowered or "quellcode" in lowered:
        return "Projektstruktur und Codequalitaet"
    if "layout" in lowered or "inhalt" in lowered:
        return "Layout und Inhaltsaufbau"
    if "bilder" in lowered or "galerie" in lowered:
        return "Bilder und Medienarbeit"
    if "verweise" in lowered or "links" in lowered:
        return "Navigation und Verlinkung"
    if "php" in lowered or "formulare" in lowered:
        return "PHP-Logik und Formulare"
    if "version" in lowered or "git" in lowered:
        return "Versionsverwaltung"
    if "dokumentation" in lowered:
        return "Dokumentation"
    if "design" in lowered or "farb" in lowered:
        return "Gestaltung"
    if "impressum" in lowered or "datenschutz" in lowered or "ki" in lowered:
        return "Pflichtangaben und Quellenarbeit"
    return "fachliche Umsetzung"


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
        if crit.criterion_id == "A1":
            evaluated.append(_evaluate_formales_criterion(project_name, project_root, crit))
            continue

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
        f"Profil-basierte Erst-Korrekturhilfe '{profile.profile_name}'. "
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
        recommendation_plan=_generate_recommendation_plan(evaluated),
    )


def _generate_recommendation_plan(
    criteria: list[EvaluationCriterion],
) -> RecommendationPlan:
    """Erzeugt einen individualisierten Marschplan mit 2 Vertiefungsthemen fuer die Projektverteidigung."""
    title_status: dict[str, CriterionStatus] = {c.title.lower(): c.status for c in criteria}

    def _status(*keywords: str) -> CriterionStatus | None:
        for t, s in title_status.items():
            if any(k in t for k in keywords):
                return s
        return None

    erfuellt_count = sum(1 for c in criteria if c.status == CriterionStatus.ERFUELLT)
    total = len(criteria)
    strong_profile = total > 0 and erfuellt_count / total >= 0.7

    form_status = _status("formul", "php-eigen")
    design_status = _status("farb", "design")

    # Erweiterung 1: Versionsverwaltung – fuer alle sinnvoll und direkt in Verteidigung zeigbar
    ext_version = RecommendationItem(
        title="Versionsverwaltung mit Git und GitHub",
        rationale=(
            "Git gehoert heute zum Handwerkszeug jeder Webentwicklerin. "
            "Ein sauberes GitHub-Repository mit nachvollziehbaren Commits zeigt in der Verteidigung, "
            "dass du professionell und strukturiert arbeitest. "
            "Das Thema ist gut in Eigenregie erlernbar und der Aufwand ist klar begrenzt."
        ),
        effort_hint=(
            "Zeitaufwand: ca. 3 Abende. "
            "Schritte: (1) GitHub-Account und oeffentliches Repository anlegen, "
            "(2) Projekt mit 'git init' initialisieren und in regelmaessigen Commits den Fortschritt dokumentieren, "
            "(3) einen Feature-Branch ('erweiterung-formular' o.ae.) erstellen, bearbeiten und mergen, "
            "(4) README.md mit Projektbeschreibung, Screenshot und Laufzeitanleitung ergaenzen. "
            "Dokumentation: Je Commit erklaeren, was geaendert wurde und warum."
        ),
    )

    # Erweiterung 2: individuell je Projektstatus gewaehlt
    if form_status not in (CriterionStatus.ERFUELLT,):
        ext_second = RecommendationItem(
            title="Serverseitige Formularauswertung und Validierung",
            rationale=(
                "Formulare sind das wichtigste Interaktionsmittel zwischen Benutzer und Webanwendung. "
                "Eine vollstaendige serverseitige Auswertung (Validierung, Rueckmeldung, Fehlerbehandlung) "
                "zeigt, dass du PHP nicht nur zur Darstellung, sondern zur echten Logikverarbeitung einsetzt. "
                "Dieses Thema ist direkt am Projekt demonstrierbar und beeindruckt in der Verteidigung."
            ),
            effort_hint=(
                "Zeitaufwand: ca. 4 Abende. "
                "Schritte: (1) Bestehendes Kontakt- oder Suchformular auswaehlen, "
                "(2) serverseitige Pflichtfeld-Validierung mit aussagekraeftigen Fehlermeldungen ergaenzen, "
                "(3) XSS-Schutz durch htmlspecialchars() konsequent einsetzen, "
                "(4) Erweiterung: Formularinhalt per PHP-Mail-Funktion oder als Log-Datei speichern. "
                "Dokumentation: Jeden Validierungsschritt im Code kommentieren."
            ),
        )
    elif strong_profile:
        ext_second = RecommendationItem(
            title="KI-API-Integration: Grundlagen Machine Learning in der Praxis",
            rationale=(
                "Da dein Projekt bereits fundiert umgesetzt ist, bietet sich ein Blick in aktuelle KI-Werkzeuge an. "
                "Das Einbinden einer einfachen KI-API (z.B. OpenAI-Text-API, HuggingFace oder eine Bildklassifikation) "
                "zeigt technologische Offenheit und ist ein starkes Argument in der Verteidigung. "
                "Du musst kein ML-Modell trainieren – das Verstehen und Einbinden einer API reicht vollstaendig."
            ),
            effort_hint=(
                "Zeitaufwand: ca. 4-5 Abende. "
                "Schritte: (1) Kostenlosen API-Key bei OpenAI oder HuggingFace anlegen, "
                "(2) einfachen PHP-curl-Aufruf zur API bauen (z.B. Textzusammenfassung oder Bildanalyse), "
                "(3) Ergebnis sauber im Browser anzeigen und Fehlerbehandlung einbauen, "
                "(4) API-Key in einer .env-Datei oder Config-Datei sicher auslagern (nicht im HTML). "
                "Dokumentation: Welche API, welche Eingabe, welche Ausgabe, Screenshot des Ergebnisses."
            ),
        )
    else:
        ext_second = RecommendationItem(
            title="Algorithmen und Datenstrukturen in PHP: Suchen und Sortieren",
            rationale=(
                "Algorithmen und Datenstrukturen sind das theoretische Fundament jeder Programmierung. "
                "Wenn du in deinem Projekt eine eigene Sortier- oder Suchfunktion in PHP implementierst, "
                "beweist du, dass du Logik nicht nur reproduzierst, sondern selbst entwickelst. "
                "Das ist in der Verteidigung ein wertvolles Demonstrationsobjekt."
            ),
            effort_hint=(
                "Zeitaufwand: ca. 3-4 Abende. "
                "Schritte: (1) Einen realen Anwendungsfall im eigenen Projekt identifizieren "
                "(z.B. Produktliste sortieren, Suchfunktion fuer Eintraege), "
                "(2) Lineare Suche und Bubble-Sort in PHP von Hand implementieren (kein usort()), "
                "(3) Beide Algorithmen mit einem realen Datensatz aus dem Projekt testen, "
                "(4) Laufzeitvergleich: einmal sort() und einmal eigener Algorithmus, Ergebnis dokumentieren. "
                "Dokumentation: Flussdiagramm des Algorithmus als Kommentar oder README-Abschnitt."
            ),
        )

    weak_topics = [
        c.title for c in criteria
        if c.status in (CriterionStatus.NICHT_ERFUELLT, CriterionStatus.TEILWEISE)
    ]
    first_weak = weak_topics[0] if weak_topics else None

    todos = [
        "Woche 1-2: Git-Repository anlegen, Projekt einpflegen, ersten Feature-Branch erstellen.",
        f"Woche 2-3: Erweiterungsthema '{ext_second.title}' recherchieren und Umsetzungsplan notieren.",
        f"Woche 3-5: Erweiterung '{ext_second.title}' implementieren und Schritt fuer Schritt dokumentieren.",
        "Woche 5-6: Beide Erweiterungen im Browser demonstrieren und fuer die Verteidigung aufbereiten.",
        "Woche 6: Kurzes Verteidigungsskript erstellen: Was hast du getan, was hast du gelernt, was wuerdest du anders machen?",
    ]
    if first_weak:
        todos.insert(1, f"Parallel: Kriterium '{first_weak}' gezielt nacharbeiten – das staerkt die Gesamtbewertung.")

    focus = (
        "Zeige in der Verteidigung Anfang Juni, dass du dein Projekt nicht nur abgegeben, sondern weiterentwickelt hast. "
        "Zwei klar abgegrenzte Erweiterungen, gut dokumentiert und im Browser demonstrierbar, sind das Ziel."
    )

    return RecommendationPlan(
        focus=focus,
        extensions=[ext_version, ext_second],
        todos_until_june=todos,
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


def _evaluate_formales_criterion(project_name: str, project_root: Path, crit) -> EvaluationCriterion:
    php_files = sorted(project_root.rglob("*.php"))
    syntax_points, syntax_evidence, syntax_note = _check_php_syntax(project_root, php_files)
    mvc_ok, mvc_evidence = _check_mvc_structure(project_root)
    nodyn_ok, nodyn_evidence = _check_no_dynamic_rechner_automat(project_root)
    timing_points, timing_note = _submission_timing_points(project_name)

    score = 0.0
    evidence: list[str] = []
    note_parts: list[str] = []

    score += syntax_points
    evidence.extend(syntax_evidence)
    note_parts.append(syntax_note)

    if mvc_ok:
        score += 1.0
    evidence.extend(mvc_evidence)
    note_parts.append("MVC-Konzept angewendet." if mvc_ok else "MVC-Konzept nicht eindeutig umgesetzt (Ordner controllers/models/views fehlen).")

    if nodyn_ok:
        score += 1.0
    evidence.extend(nodyn_evidence)
    note_parts.append(
        "Kein dynamischer Teil (Rechner/Automat) gefunden."
        if nodyn_ok
        else "Dynamischer Teil (Rechner/Automat) erkannt."
    )

    score += timing_points
    note_parts.append(timing_note)

    awarded = min(crit.max_points, round(score, 2))
    if awarded >= 3.5:
        status = CriterionStatus.ERFUELLT
    elif awarded >= 1.0:
        status = CriterionStatus.TEILWEISE
    else:
        status = CriterionStatus.NICHT_ERFUELLT

    if crit.evidence_hint:
        note_parts.append(crit.evidence_hint)

    return EvaluationCriterion(
        criterion_id=crit.criterion_id,
        title=crit.title,
        max_points=crit.max_points,
        awarded_points=awarded,
        status=status,
        evidence=evidence[:10],
        note=" | ".join(note_parts),
    )


def _check_php_syntax(project_root: Path, php_files: list[Path]) -> tuple[float, list[str], str]:
    if not php_files:
        return 0.0, ["Keine PHP-Dateien gefunden"], "Syntaxcheck nicht bestanden: keine PHP-Dateien gefunden."

    php_cmd = shutil.which("php")
    if php_cmd is None:
        return 1.0, ["PHP-CLI nicht verfuegbar"], "Syntaxcheck nicht ausfuehrbar (php nicht installiert), neutral bewertet."

    failed: list[str] = []
    checked = 0
    for path in php_files:
        checked += 1
        result = subprocess.run(
            [php_cmd, "-l", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            failed.append(str(path.relative_to(project_root)))

    if failed:
        return 0.0, [f"Syntaxfehler in {name}" for name in failed[:3]], f"Syntaxfehler in {len(failed)} Datei(en)."
    return 1.0, [f"Syntax ok ({checked} PHP-Dateien geprueft)"], "Syntaxfehlerfreiheit gegeben."


def _check_mvc_structure(project_root: Path) -> tuple[bool, list[str]]:
    mvc_dirs = [
        project_root / "controllers",
        project_root / "models",
        project_root / "views",
    ]
    missing = [d.name for d in mvc_dirs if not d.exists()]
    if missing:
        return False, [f"Fehlende MVC-Ordner: {', '.join(missing)}"]
    return True, ["MVC-Ordner vorhanden: controllers, models, views"]


def _check_no_dynamic_rechner_automat(project_root: Path) -> tuple[bool, list[str]]:
    suspect = re.compile(r"(?i)\b(?:rechner|calculator|automat|vending)\b")
    hits: list[str] = []
    for file_path in list(project_root.rglob("*.php")) + list(project_root.rglob("*.js")):
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if suspect.search(text):
            hits.append(str(file_path.relative_to(project_root)))
            if len(hits) >= 5:
                break

    if hits:
        return False, [f"Dynamik-Hinweis in {name}" for name in hits[:3]]
    return True, ["Kein Rechner/Automat-Code erkannt"]


def _submission_timing_points(project_name: str) -> tuple[float, str]:
    lowered = project_name.lower()
    if "kostia" in lowered or "nikita" in lowered:
        return 0.5, "Abgabe 20 Minuten verspaetet (milde bewertet)."
    return 1.0, "Abgabe puenktlich."
