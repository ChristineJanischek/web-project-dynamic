from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
import json
import shutil


@dataclass(slots=True)
class EvaluationSnapshot:
    project_name: str
    report_id: str
    rubric_id: str
    project_type: str
    awarded_points: float
    max_points: float
    grade: float
    source_json: Path

    @property
    def percent(self) -> float:
        if self.max_points <= 0:
            return 0.0
        return (self.awarded_points / self.max_points) * 100.0


def generate_batch_reports(reports_dir: Path) -> dict[str, Path]:
    snapshots = collect_evaluation_snapshots(reports_dir)

    overview_md = reports_dir / "korrekturhilfeuebersicht.md"
    overview_html = reports_dir / "korrekturhilfeuebersicht.html"
    ranking_md = reports_dir / "rangliste.md"
    ranking_html = reports_dir / "rangliste.html"

    write_overview_markdown(overview_md, snapshots)
    write_overview_html(overview_html, snapshots)
    write_ranking_markdown(ranking_md, snapshots)
    write_ranking_html(ranking_html, snapshots)

    return {
        "overview_markdown": overview_md,
        "overview_html": overview_html,
        "ranking_markdown": ranking_md,
        "ranking_html": ranking_html,
    }


def export_html_reports_to_downloads(reports_dir: Path, download_dir: Path) -> list[Path]:
    target_dir = download_dir / "edu-assessment-html"
    target_dir.mkdir(parents=True, exist_ok=True)

    exported: list[Path] = []
    for html_file in sorted(reports_dir.glob("*.html")):
        target_path = target_dir / html_file.name
        shutil.copy2(html_file, target_path)
        exported.append(target_path)

    return exported


def collect_evaluation_snapshots(reports_dir: Path) -> list[EvaluationSnapshot]:
    snapshots: list[EvaluationSnapshot] = []
    json_files = sorted(reports_dir.glob("*_korrekturhilfe_draft.json"))
    if not json_files:
        json_files = sorted(reports_dir.glob("*_bewertung_draft.json"))

    for json_file in json_files:
        payload = json.loads(json_file.read_text(encoding="utf-8"))

        snapshots.append(
            EvaluationSnapshot(
                project_name=str(payload.get("student_project_name", json_file.stem)),
                report_id=str(payload.get("report_id", "")),
                rubric_id=str(payload.get("rubric_id", "")),
                project_type=str(payload.get("project_type", "")),
                awarded_points=float(payload.get("awarded_points", 0.0)),
                max_points=float(payload.get("max_points", 0.0)),
                grade=float(payload.get("grade", 6.0)),
                source_json=json_file,
            )
        )

    return snapshots


def write_overview_markdown(target_path: Path, snapshots: list[EvaluationSnapshot]) -> Path:
    lines = [
        "# Korrekturhilfeuebersicht",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    if not snapshots:
        lines.extend([
            "Keine Korrekturhilfe-Daten gefunden.",
            "",
        ])
        target_path.write_text("\n".join(lines), encoding="utf-8")
        return target_path

    avg_grade = sum(item.grade for item in snapshots) / len(snapshots)
    avg_percent = sum(item.percent for item in snapshots) / len(snapshots)

    lines.extend(
        [
            f"Anzahl Berichte: {len(snapshots)}",
            f"Durchschnittsnote: {avg_grade:.2f}",
            f"Durchschnittliche Punkteausbeute: {avg_percent:.2f}%",
            "",
            "| Projekt | Rubrik | Punkte | Erfuellung | Note | Quelle |",
            "| --- | --- | ---: | ---: | ---: | --- |",
        ]
    )

    for item in sorted(snapshots, key=lambda x: x.project_name.lower()):
        lines.append(
            "| "
            f"{item.project_name} | "
            f"{item.rubric_id or '-'} | "
            f"{item.awarded_points:.2f}/{item.max_points:.2f} | "
            f"{item.percent:.2f}% | "
            f"{item.grade:.2f} | "
            f"{item.source_json.name} |"
        )

    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target_path


def write_overview_html(target_path: Path, snapshots: list[EvaluationSnapshot]) -> Path:
    now_text = datetime.now().strftime("%Y-%m-%d %H:%M")

    if snapshots:
        avg_grade = sum(item.grade for item in snapshots) / len(snapshots)
        avg_percent = sum(item.percent for item in snapshots) / len(snapshots)
        summary_row = (
            f"<p style=\"margin:0 0 12px 0;\">Anzahl Berichte: <strong>{len(snapshots)}</strong> "
            f"| Durchschnittsnote: <strong>{avg_grade:.2f}</strong> "
            f"| Durchschnittliche Punkteausbeute: <strong>{avg_percent:.2f}%</strong></p>"
        )
        rows = "\n".join(
            [
                (
                    "<tr>"
                    f"<td>{escape(item.project_name)}</td>"
                    f"<td>{escape(item.rubric_id) or '-'}</td>"
                    f"<td>{item.awarded_points:.2f} / {item.max_points:.2f}</td>"
                    f"<td>{item.percent:.2f}%</td>"
                    f"<td>{item.grade:.2f}</td>"
                    f"<td>{escape(item.source_json.name)}</td>"
                    "</tr>"
                )
                for item in sorted(snapshots, key=lambda x: x.project_name.lower())
            ]
        )
    else:
        summary_row = "<p style=\"margin:0 0 12px 0;\">Keine Korrekturhilfe-Daten gefunden.</p>"
        rows = "<tr><td colspan=\"6\">Keine Eintraege vorhanden.</td></tr>"

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
    <title>Korrekturhilfeuebersicht</title>
</head>
<body style="margin:24px; font-family:Calibri, Arial, sans-serif; font-size:11pt; color:#222;">
    <h1 style="margin:0 0 8px 0;">Korrekturhilfeuebersicht</h1>
  <p style="margin:0 0 12px 0;">Stand: {escape(now_text)}</p>
  {summary_row}
  <table style="border-collapse:collapse; width:100%;" border="1" cellpadding="6" cellspacing="0">
    <tr style="background:#f2f2f2;">
      <th align="left">Projekt</th>
      <th align="left">Rubrik</th>
      <th align="left">Punkte</th>
      <th align="left">Erfuellung</th>
      <th align="left">Note</th>
      <th align="left">Quelle</th>
    </tr>
    {rows}
  </table>
</body>
</html>
"""

    target_path.write_text(html + "\n", encoding="utf-8")
    return target_path


def write_ranking_markdown(target_path: Path, snapshots: list[EvaluationSnapshot]) -> Path:
    lines = [
        "# Rangliste",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    if not snapshots:
        lines.extend([
            "Keine Korrekturhilfe-Daten gefunden.",
            "",
        ])
        target_path.write_text("\n".join(lines), encoding="utf-8")
        return target_path

    lines.extend(
        [
            "| Rang | Projekt | Note | Punkte | Erfuellung | Rubrik |",
            "| ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )

    for rank, item in enumerate(_sorted_for_ranking(snapshots), start=1):
        lines.append(
            "| "
            f"{rank} | "
            f"{item.project_name} | "
            f"{item.grade:.2f} | "
            f"{item.awarded_points:.2f}/{item.max_points:.2f} | "
            f"{item.percent:.2f}% | "
            f"{item.rubric_id or '-'} |"
        )

    target_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target_path


def write_ranking_html(target_path: Path, snapshots: list[EvaluationSnapshot]) -> Path:
    if snapshots:
        rows = "\n".join(
            [
                (
                    "<tr>"
                    f"<td>{rank}</td>"
                    f"<td>{escape(item.project_name)}</td>"
                    f"<td>{item.grade:.2f}</td>"
                    f"<td>{item.awarded_points:.2f} / {item.max_points:.2f}</td>"
                    f"<td>{item.percent:.2f}%</td>"
                    f"<td>{escape(item.rubric_id) or '-'}</td>"
                    "</tr>"
                )
                for rank, item in enumerate(_sorted_for_ranking(snapshots), start=1)
            ]
        )
    else:
        rows = "<tr><td colspan=\"6\">Keine Eintraege vorhanden.</td></tr>"

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Rangliste</title>
</head>
<body style="margin:24px; font-family:Calibri, Arial, sans-serif; font-size:11pt; color:#222;">
  <h1 style="margin:0 0 8px 0;">Rangliste</h1>
  <p style="margin:0 0 12px 0;">Stand: {escape(datetime.now().strftime('%Y-%m-%d %H:%M'))}</p>
  <table style="border-collapse:collapse; width:100%;" border="1" cellpadding="6" cellspacing="0">
    <tr style="background:#f2f2f2;">
      <th align="left">Rang</th>
      <th align="left">Projekt</th>
      <th align="left">Note</th>
      <th align="left">Punkte</th>
      <th align="left">Erfuellung</th>
      <th align="left">Rubrik</th>
    </tr>
    {rows}
  </table>
</body>
</html>
"""

    target_path.write_text(html + "\n", encoding="utf-8")
    return target_path


def _sorted_for_ranking(snapshots: list[EvaluationSnapshot]) -> list[EvaluationSnapshot]:
    return sorted(
        snapshots,
        key=lambda item: (item.grade, -item.percent, item.project_name.lower()),
    )
