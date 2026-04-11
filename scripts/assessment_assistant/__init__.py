"""Owner-zentrierte Bewertungsassistenz fuer Projektkorrekturen."""

from .bootstrap import bootstrap_workspace
from .aggregation import generate_batch_reports, export_html_reports_to_downloads
from .config import AssessmentWorkspaceConfig, default_workspace_root
from .ingestion import (
    UploadSelection,
    copy_upload_file,
    detect_criterion_candidates,
    extract_project_archive,
    load_rubric_lines,
    select_latest_uploads,
    write_kickoff_report,
    write_rubric_markdown,
)
from .evaluation import (
    evaluate_project,
    evaluate_project_with_profile,
    parse_rubric_to_criteria,
    write_report_json,
    write_report_markdown,
)
from .models import EvaluationReport, EvaluationCriterion, RecommendationPlan
from .profile_loader import GradingProfile, CriterionProfile, GradeScale, load_profile, find_profile
from .project_detector import detect_project_type
from .rule_engine import evaluate_rule, RuleResult

__all__ = [
    "AssessmentWorkspaceConfig",
    "EvaluationCriterion",
    "EvaluationReport",
    "RecommendationPlan",
    "UploadSelection",
    "bootstrap_workspace",
    "generate_batch_reports",
    "export_html_reports_to_downloads",
    "copy_upload_file",
    "detect_criterion_candidates",
    "default_workspace_root",
    "CriterionProfile",
    "GradeScale",
    "GradingProfile",
    "RuleResult",
    "detect_project_type",
    "evaluate_project",
    "evaluate_project_with_profile",
    "evaluate_rule",
    "extract_project_archive",
    "find_profile",
    "load_profile",
    "load_rubric_lines",
    "parse_rubric_to_criteria",
    "select_latest_uploads",
    "write_kickoff_report",
    "write_report_json",
    "write_report_markdown",
    "write_rubric_markdown",
]