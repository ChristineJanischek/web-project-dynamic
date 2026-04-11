from __future__ import annotations

from dataclasses import replace
from html import escape
from pathlib import Path
import json
import re

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
    rows: list[str] = []

    for criterion in report.criteria:
        status_label = _status_label(criterion.status)
        status_style = _status_style(criterion.status)
        evidence = _format_html_list(criterion.evidence) or "-"
        appreciation = escape(_pedagogical_appreciation(criterion))
        next_step = escape(_pedagogical_next_step(criterion))
        teacher_check = escape(_teacher_check_hint(criterion))
        note = escape(criterion.note) if criterion.note else "-"

        rows.append(
            "".join(
                [
                    "<tr>",
                    _cell(escape(criterion.criterion_id), width="7%", bold=True),
                    _cell(escape(criterion.title), width="17%", bold=True),
                    _cell(escape(status_label), width="10%", extra_style=status_style, bold=True),
                    _cell(f"{criterion.awarded_points:.2f} / {criterion.max_points:.2f}", width="10%"),
                    _cell(evidence, width="16%"),
                    _cell(appreciation, width="14%"),
                    _cell(next_step, width="14%"),
                    _cell(teacher_check, width="12%"),
                    "</tr>",
                    "<tr>",
                    _cell("Lehrkraft-Notiz", width="14%", header_like=True),
                    _cell(note, colspan=7),
                    "</tr>",
                ]
            )
        )

    html = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Bewertungsbericht - {project_name}</title>
</head>
<body style="margin:24px; font-family:Calibri, Arial, sans-serif; font-size:11pt; color:#222222; background:#ffffff;">
  <h1 style="font-size:18pt; margin:0 0 12px 0;">Bewertungsbericht</h1>
  <table style="border-collapse:collapse; width:100%; margin-bottom:18px;" border="1" cellpadding="6" cellspacing="0">
    <tr>
      <td style="width:25%; background:#f2f2f2;"><strong>Projekt</strong></td>
      <td style="width:25%;">{project_name}</td>
      <td style="width:25%; background:#f2f2f2;"><strong>Rubrik</strong></td>
      <td style="width:25%;">{rubric_id}</td>
    </tr>
    <tr>
      <td style="background:#f2f2f2;"><strong>Punkte</strong></td>
      <td>{awarded_points:.2f} / {max_points:.2f}</td>
      <td style="background:#f2f2f2;"><strong>Note</strong></td>
      <td>{grade:.2f}</td>
    </tr>
  </table>

  <h2 style="font-size:13pt; margin:18px 0 8px 0;">Gesamtbild</h2>
  <p style="margin:0 0 10px 0; line-height:1.45;">{summary}</p>
  <table style="border-collapse:collapse; width:100%; margin-bottom:18px;" border="1" cellpadding="6" cellspacing="0">
    <tr style="background:#f2f2f2;">
      <th align="left">Erfuellt</th>
      <th align="left">Teilweise</th>
      <th align="left">Nicht erfuellt</th>
      <th align="left">Manuell pruefen</th>
      <th align="left">Do Next</th>
    </tr>
    <tr>
      <td>{count_erfuellt}</td>
      <td>{count_teilweise}</td>
      <td>{count_nicht}</td>
      <td>{count_manuell}</td>
      <td>{overall_next_step}</td>
    </tr>
  </table>

  <h2 style="font-size:13pt; margin:18px 0 8px 0;">Kriterien und Feedback</h2>
  <p style="margin:0 0 10px 0; line-height:1.45;">Diese Tabelle ist bewusst einfach aufgebaut, damit sie beim Kopieren nach Word als Tabelle erhalten bleibt und dort direkt weiterbearbeitet werden kann.</p>
  <table style="border-collapse:collapse; width:100%;" border="1" cellpadding="6" cellspacing="0">
    <tr style="background:#f2f2f2;">
      <th align="left" style="width:7%;">ID</th>
      <th align="left" style="width:17%;">Kriterium</th>
      <th align="left" style="width:10%;">Status</th>
      <th align="left" style="width:10%;">Punkte</th>
      <th align="left" style="width:16%;">Beobachtung / Evidenz</th>
      <th align="left" style="width:14%;">Wuerdigung</th>
      <th align="left" style="width:14%;">Naechster Schritt</th>
      <th align="left" style="width:12%;">Manuelle Pruefung</th>
    </tr>
    {rows}
  </table>
  {recommendation_block}
</body>
</html>
""".format(
        project_name=escape(report.student_project_name),
        rubric_id=escape(report.rubric_id),
        awarded_points=report.awarded_points,
        max_points=report.max_points,
        grade=report.grade,
        summary=escape(report.summary),
        count_erfuellt=status_counts[CriterionStatus.ERFUELLT],
        count_teilweise=status_counts[CriterionStatus.TEILWEISE],
        count_nicht=status_counts[CriterionStatus.NICHT_ERFUELLT],
        count_manuell=status_counts[CriterionStatus.MANUELL_PRUEFEN],
        overall_next_step=escape(_overall_next_step(report)),
        rows="\n    ".join(rows),
        recommendation_block=_render_recommendation_html(report.recommendation_plan),
    )

    target_path.write_text(html + "\n", encoding="utf-8")
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
        ext_blocks += f"""
  <h3 style="font-size:12pt; margin:14px 0 4px 0; color:#1a3a5c;">Erweiterung {i}: {escape(ext.title)}</h3>
  <p style="margin:0 0 6px 0; line-height:1.45;">{escape(ext.rationale)}</p>
  <p style="margin:0 0 10px 0; background:#f7f9fc; border-left:4px solid #345a8a; padding:6px 10px; line-height:1.4;">
    <strong>Aufwand und Schritte:</strong> {escape(ext.effort_hint)}
  </p>"""

    todos_html = "".join(f"<li style='margin-bottom:4px;'>{escape(t)}</li>" for t in plan.todos_until_june)

    return f"""
  <h2 style="font-size:13pt; margin:24px 0 8px 0; color:#1a3a5c; border-top:2px solid #345a8a; padding-top:12px;">
    Marschplan: Vertiefung bis Anfang Juni
  </h2>
  <p style="margin:0 0 12px 0; line-height:1.45; font-style:italic;">{escape(plan.focus)}</p>
  {ext_blocks}
  <h3 style="font-size:12pt; margin:14px 0 6px 0; color:#1a3a5c;">ToDo-Liste bis zur Verteidigung</h3>
  <ul style="margin:0 0 12px 0; padding-left:22px; line-height:1.5;">
    {todos_html}
  </ul>"""


def _status_label(status: CriterionStatus) -> str:
    return {
        CriterionStatus.ERFUELLT: "Erfuellt",
        CriterionStatus.TEILWEISE: "Teilweise",
        CriterionStatus.NICHT_ERFUELLT: "Nicht erfuellt",
        CriterionStatus.MANUELL_PRUEFEN: "Manuell pruefen",
    }[status]


def _status_style(status: CriterionStatus) -> str:
    return {
        CriterionStatus.ERFUELLT: "color:#2d6a4f;",
        CriterionStatus.TEILWEISE: "color:#9a6700;",
        CriterionStatus.NICHT_ERFUELLT: "color:#9f1d1d;",
        CriterionStatus.MANUELL_PRUEFEN: "color:#345a8a;",
    }[status]


def _cell(
    content: str,
    width: str | None = None,
    colspan: int | None = None,
    bold: bool = False,
    header_like: bool = False,
    extra_style: str = "",
) -> str:
    styles = ["vertical-align:top;", "line-height:1.35;"]
    if width:
        styles.append(f"width:{width};")
    if bold:
        styles.append("font-weight:700;")
    if header_like:
        styles.append("background:#f7f7f7; font-weight:700;")
    if extra_style:
        styles.append(extra_style)

    colspan_attr = f' colspan="{colspan}"' if colspan else ""
    return f'<td{colspan_attr} style="{" ".join(styles)}">{content}</td>'


def _format_html_list(items: list[str]) -> str:
    if not items:
        return ""
    return "<ul style=\"margin:0; padding-left:18px;\">" + "".join(
        f"<li>{escape(item)}</li>" for item in items[:5]
    ) + "</ul>"


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
