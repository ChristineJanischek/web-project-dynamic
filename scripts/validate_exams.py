#!/usr/bin/env python3
"""
Exam-System Validierungs-Script

Prüft die Konsistenz und Vollständigkeit des Exam-Systems:
- Verzeichnisstruktur
- Datei-Benennungen
- Varianten-Vollständigkeit (mindestens 4)
- Punktesummen (wenn in Dateien vorhanden)
- Metadata-Validierung
- Duplikatserkennung für Aufgabenstellungen
- Unicode-/Umlaut-Korrektheit (ae/oe/ue/ss → ä/ö/ü/ß)
- Optional: Aufbau einer Wissensdatenbank mit Aufgaben-Fingerprints

Usage:
    python3 scripts/validate_exams.py
    python3 scripts/validate_exams.py --verbose
    python3 scripts/validate_exams.py --language javascript
    python3 scripts/validate_exams.py --write-knowledge-base
"""

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

# Konstanten
REPO_ROOT = Path(__file__).parent.parent
EXAMS_DIR = Path(__file__).parent.parent / "docs/programmierung/grundlagen/exams"
EXPECTED_LANGUAGES = ["javascript", "php", "python"]
MIN_REQUIRED_VARIANTS = 4  # exam.md + exam_v2.md + exam_v3.md + exam_v4.md
EXPECTED_TOTAL_POINTS = 25.0
KNOWLEDGE_BASE_PATH = EXAMS_DIR / "shared" / "variation_knowledge_base.json"
SOLUTION_RUBRICS_KB_PATH = EXAMS_DIR / "shared" / "solution_rubrics_knowledge_base.json"
VARIATION_KB_SCHEMA_PATH = EXAMS_DIR / "shared" / "variation_knowledge_base_schema.json"
SOLUTION_RUBRICS_SCHEMA_PATH = EXAMS_DIR / "shared" / "solution_rubrics_schema.json"

# Farben für Terminal-Output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_success(msg: str):
    print(f"{Colors.GREEN}✓{Colors.ENDC} {msg}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠{Colors.ENDC} {msg}")

def print_error(msg: str):
    print(f"{Colors.RED}✗{Colors.ENDC} {msg}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ{Colors.ENDC} {msg}")

def print_header(msg: str):
    print(f"\n{Colors.BOLD}{msg}{Colors.ENDC}")

def get_all_themes(language_dir: Path) -> List[str]:
    """Findet alle Themen-Verzeichnisse für eine Sprache."""
    if not language_dir.exists():
        return []
    return [d.name for d in language_dir.iterdir() if d.is_dir()]

def parse_variant_number(file_name: str, base_name: str) -> int:
    """Extrahiert die Variantennummer aus exam/solutions Dateinamen."""
    if file_name == f"{base_name}.md":
        return 1

    match = re.fullmatch(rf"{re.escape(base_name)}_v(\d+)\.md", file_name)
    if match:
        return int(match.group(1))

    return 0

def collect_variant_files(theme_dir: Path, base_name: str) -> Dict[int, Path]:
    """Sammelt Varianten-Dateien eines Typs (exam oder solutions)."""
    variants: Dict[int, Path] = {}

    for file_path in theme_dir.glob(f"{base_name}*.md"):
        variant = parse_variant_number(file_path.name, base_name)
        if variant > 0:
            variants[variant] = file_path

    return dict(sorted(variants.items(), key=lambda item: item[0]))

def variant_name_from_number(variant: int, base_name: str) -> str:
    """Erzeugt standardisierte Dateinamen aus Variantennummern."""
    if variant == 1:
        return f"{base_name}.md"
    return f"{base_name}_v{variant}.md"

def slugify_identifier(value: str) -> str:
    """Erzeugt stabile ASCII-Identifier aus Texten."""
    normalized = value.lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = normalized.strip("-")
    return normalized or "item"

def parse_points(value: str) -> float:
    """Parst numerische Punktangaben aus Texten."""
    match = re.search(r"(\d+(?:\.\d+)?)", value)
    if not match:
        return 0.0
    return float(match.group(1))


# Regex: ASCII-Umlautmuster zwischen zwei Konsonanten (sehr hohe Treffsicherheit in deutschen Texten)
_CONSONANTS = r"bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
_UMLAUT_SUBSTITUTIONS: List[Tuple[re.Pattern, str]] = [
    (re.compile(rf"(?<=[{_CONSONANTS}])(ae|Ae|AE)(?=[{_CONSONANTS}])"), "ae → ä"),
    (re.compile(rf"(?<=[{_CONSONANTS}])(oe|Oe|OE)(?=[{_CONSONANTS}])"), "oe → ö"),
    (re.compile(rf"(?<=[{_CONSONANTS}])(ue|Ue|UE)(?=[{_CONSONANTS}])"), "ue → ü"),
    # 'ss' nur am Wortende oder vor Vokal (Gruss, Schluss → Gruß, Schluss) – als Warnung
]


def check_unicode_umlauts(file_path: Path) -> List[str]:
    """Prüft ob Markdown-Datei ASCII-kodierte Umlaute enthält (ae/oe/ue statt ä/ö/ü).

    Ignoriert Code-Blöcke (```...```) und Inline-Code (`...`).
    Gibt eine Liste von Fehlermeldungen zurück.
    """
    errors: List[str] = []
    try:
        raw = file_path.read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover
        return [f"Datei konnte nicht gelesen werden: {exc}"]

    # Code-Blöcke und Inline-Code maskieren – Newlines BEIBEHALTEN, damit Zeilennummern stimmen
    def _mask(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group())

    cleaned = re.sub(r"```[\s\S]*?```", _mask, raw)
    cleaned = re.sub(r"`[^`\n]+`", _mask, cleaned)

    for line_no, line in enumerate(cleaned.splitlines(), 1):
        for pattern, hint in _UMLAUT_SUBSTITUTIONS:
            match = pattern.search(line)
            if match:
                preview = raw.splitlines()[line_no - 1].strip()[:100]
                errors.append(
                    f"Zeile {line_no}: ASCII-Umlaut ({hint}) in: {preview}"
                )
                break  # ein Treffer pro Zeile reicht
    return errors


def validate_schema_node(data: object, schema: Dict[str, object], path: str = "$") -> List[str]:
    """Validiert ein JSON-Objekt gegen ein einfaches JSON-Schema-Subset."""
    errors: List[str] = []
    expected_type = schema.get("type")

    if expected_type == "object":
        if not isinstance(data, dict):
            return [f"{path}: erwartet object"]

        properties = schema.get("properties", {})
        required = schema.get("required", [])
        additional_allowed = schema.get("additionalProperties", True)

        for key in required:
            if key not in data:
                errors.append(f"{path}: Pflichtfeld '{key}' fehlt")

        if not additional_allowed:
            for key in data:
                if key not in properties:
                    errors.append(f"{path}: unerwartetes Feld '{key}'")

        for key, sub_schema in properties.items():
            if key in data:
                errors.extend(validate_schema_node(data[key], sub_schema, f"{path}.{key}"))

    elif expected_type == "array":
        if not isinstance(data, list):
            return [f"{path}: erwartet array"]

        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(data) < min_items:
            errors.append(f"{path}: mindestens {min_items} Eintraege erwartet")

        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(data):
                errors.extend(validate_schema_node(item, item_schema, f"{path}[{index}]"))

    elif expected_type == "string":
        if not isinstance(data, str):
            return [f"{path}: erwartet string"]
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(data) < min_length:
            errors.append(f"{path}: Mindestlaenge {min_length} unterschritten")

    elif expected_type == "number":
        if not isinstance(data, (int, float)) or isinstance(data, bool):
            return [f"{path}: erwartet number"]

    elif expected_type == "integer":
        if not isinstance(data, int) or isinstance(data, bool):
            return [f"{path}: erwartet integer"]

    elif expected_type == "boolean":
        if not isinstance(data, bool):
            return [f"{path}: erwartet boolean"]

    if "enum" in schema and data not in schema["enum"]:
        errors.append(f"{path}: Wert {data!r} nicht in enum {schema['enum']!r}")

    return errors

def validate_data_with_schema_file(data: Dict[str, object], schema_path: Path) -> List[str]:
    """Validiert JSON-Daten gegen eine Schema-Datei."""
    if not schema_path.exists():
        return [f"Schema fehlt: {schema_path.relative_to(REPO_ROOT)}"]

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"Schema ungueltig ({schema_path.name}): {error}"]

    return validate_schema_node(data, schema)

def validate_exam_files(language: str, theme: str) -> Dict[str, List[str]]:
    """Validiert Exam-Dateien für ein Thema."""
    theme_dir = EXAMS_DIR / language / theme
    errors = []
    warnings = []
    
    if not theme_dir.exists():
        errors.append(f"Verzeichnis {theme_dir} existiert nicht")
        return {"errors": errors, "warnings": warnings}
    
    exam_variants = collect_variant_files(theme_dir, "exam")
    solution_variants = collect_variant_files(theme_dir, "solutions")

    if 1 not in exam_variants:
        errors.append(f"Fehlende Datei: {(theme_dir / 'exam.md').relative_to(EXAMS_DIR)}")

    if 1 not in solution_variants:
        errors.append(f"Fehlende Datei: {(theme_dir / 'solutions.md').relative_to(EXAMS_DIR)}")

    if len(exam_variants) < MIN_REQUIRED_VARIANTS:
        errors.append(
            f"Zu wenige Exam-Varianten: {len(exam_variants)} < {MIN_REQUIRED_VARIANTS}"
        )

    if len(solution_variants) < MIN_REQUIRED_VARIANTS:
        errors.append(
            f"Zu wenige Lösungs-Varianten: {len(solution_variants)} < {MIN_REQUIRED_VARIANTS}"
        )

    exam_variant_set = set(exam_variants.keys())
    solution_variant_set = set(solution_variants.keys())

    for variant in sorted(exam_variant_set - solution_variant_set):
        missing_solution = variant_name_from_number(variant, "solutions")
        errors.append(f"Fehlende Datei: {(theme_dir / missing_solution).relative_to(EXAMS_DIR)}")

    for variant in sorted(solution_variant_set - exam_variant_set):
        missing_exam = variant_name_from_number(variant, "exam")
        errors.append(f"Fehlende Datei: {(theme_dir / missing_exam).relative_to(EXAMS_DIR)}")
    
    # Prüfe Structogramme-Verzeichnis
    struct_dir = theme_dir / "structogramme"
    if not struct_dir.exists():
        warnings.append(f"Fehlendes Verzeichnis: {struct_dir.relative_to(EXAMS_DIR)}")
    
    return {"errors": errors, "warnings": warnings}

def extract_task_sections(markdown_content: str) -> Dict[str, str]:
    """Extrahiert die Aufgaben A-D aus einer Exam-Datei."""
    pattern = re.compile(
        r"##\s+Aufgabe\s+([A-D])\b.*?(?=\n##\s+Aufgabe\s+[A-D]\b|\Z)",
        re.IGNORECASE | re.DOTALL,
    )

    sections: Dict[str, str] = {}
    for match in pattern.finditer(markdown_content):
        sections[match.group(1).upper()] = match.group(0)
    return sections

def normalize_task_text(task_text: str) -> str:
    """Normalisiert Aufgabeninhalt für robusten Textvergleich."""
    normalized = re.sub(r"```.*?```", " ", task_text, flags=re.DOTALL)
    normalized = re.sub(r"`", " ", normalized)
    normalized = re.sub(r"[\*_>#\-|\[\]\(\)]", " ", normalized)
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized

def task_fingerprint(task_text: str) -> str:
    """Erzeugt einen stabilen Fingerprint für eine Aufgabe."""
    normalized = normalize_task_text(task_text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

def validate_variant_uniqueness(language: str, theme: str) -> Dict[str, List[str]]:
    """Prüft, dass Aufgabenstellungen in Varianten nicht identisch sind."""
    theme_dir = EXAMS_DIR / language / theme
    errors: List[str] = []
    warnings: List[str] = []

    exam_variants = collect_variant_files(theme_dir, "exam")
    if len(exam_variants) <= 1:
        return {"errors": errors, "warnings": warnings}

    fingerprints_by_task: Dict[str, Dict[str, List[str]]] = {
        "A": {},
        "B": {},
        "C": {},
        "D": {},
    }
    full_exam_fingerprints: Dict[str, List[str]] = {}

    for variant, exam_path in exam_variants.items():
        content = exam_path.read_text(encoding="utf-8")
        sections = extract_task_sections(content)
        label = variant_name_from_number(variant, "exam")

        for task_letter in ["A", "B", "C", "D"]:
            section = sections.get(task_letter)
            if not section:
                warnings.append(f"{label}: Aufgabe {task_letter} nicht gefunden")
                continue

            fingerprint = task_fingerprint(section)
            if fingerprint not in fingerprints_by_task[task_letter]:
                fingerprints_by_task[task_letter][fingerprint] = []
            fingerprints_by_task[task_letter][fingerprint].append(label)

        joined = " ".join(
            normalize_task_text(sections.get(task_letter, ""))
            for task_letter in ["A", "B", "C", "D"]
        ).strip()
        full_exam_fingerprint = hashlib.sha256(joined.encode("utf-8")).hexdigest()
        if full_exam_fingerprint not in full_exam_fingerprints:
            full_exam_fingerprints[full_exam_fingerprint] = []
        full_exam_fingerprints[full_exam_fingerprint].append(label)

    for task_letter, grouped in fingerprints_by_task.items():
        for files in grouped.values():
            if len(files) > 1:
                errors.append(
                    f"Identische Aufgabenstellung erkannt (Aufgabe {task_letter}): "
                    f"{', '.join(sorted(files))}"
                )

    for files in full_exam_fingerprints.values():
        if len(files) > 1:
            errors.append(
                "Zwei oder mehr Varianten sind vollstaendig identisch: "
                f"{', '.join(sorted(files))}"
            )

    return {"errors": errors, "warnings": warnings}

def extract_block_after_heading(section_text: str, heading_regex: str) -> str:
    """Extrahiert den Block nach einer gegebenen Überschrift innerhalb einer Aufgabe."""
    match = re.search(heading_regex, section_text, flags=re.MULTILINE)
    if not match:
        return ""

    start = match.end()
    remainder = section_text[start:]
    stop_match = re.search(r"^###\s+|^####\s+|^##\s+Aufgabe\s+[A-D]\b", remainder, flags=re.MULTILINE)
    if stop_match:
        return remainder[:stop_match.start()].strip()
    return remainder.strip()

def parse_point_criteria(block: str) -> List[Dict[str, object]]:
    """Parst Bewertungskriterien aus Bullet- oder Tabellen-Format."""
    criteria: List[Dict[str, object]] = []

    # 1) Bullet-Format: - 2.0 Punkte: ...
    for line in block.splitlines():
        bullet_match = re.match(r"^-\s*(\d+(?:\.\d+)?)\s*Punkte?:\s*(.+)$", line.strip())
        if bullet_match:
            criteria.append(
                {
                    "points": float(bullet_match.group(1)),
                    "criterion": bullet_match.group(2).strip(),
                    "hint": "",
                }
            )

    if criteria:
        return criteria

    # 2) Tabellen-Format
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if re.match(r"^\|\s*-+", stripped):
            continue

        cells = [part.strip() for part in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if "summe aufgabe" in cells[0].lower():
            continue

        points = parse_points(cells[1])
        if points <= 0:
            continue

        criteria.append(
            {
                "points": points,
                "criterion": cells[0],
                "hint": cells[2] if len(cells) > 2 else "",
            }
        )

    return criteria

def parse_common_errors(block: str) -> List[str]:
    """Parst häufige Fehler aus Bullet-Listen."""
    errors: List[str] = []
    for line in block.splitlines():
        match = re.match(r"^-\s+(.+)$", line.strip())
        if match:
            errors.append(match.group(1).strip())
    return errors

def parse_task_total_points(task_section: str) -> float:
    """Extrahiert Gesamtpunkte aus Aufgabenüberschrift."""
    match = re.search(r"\((\d+(?:\.\d+)?)\s*Punkte\)", task_section)
    if not match:
        return 0.0
    return float(match.group(1))

def enrich_criteria_with_ids(
    criteria: List[Dict[str, object]],
    language: str,
    theme: str,
    variant_key: str,
    task_letter: str,
) -> List[Dict[str, object]]:
    """Ergaenzt Kriterien um stabile IDs fuer Auto-Grading und Analytics."""
    enriched: List[Dict[str, object]] = []
    for index, criterion in enumerate(criteria, start=1):
        criterion_name = str(criterion.get("criterion", ""))
        criterion_key = slugify_identifier(criterion_name)
        enriched.append(
            {
                "criterion_index": index,
                "criterion_key": criterion_key,
                "criterion_id": (
                    f"{language}.{theme}.{variant_key}.{task_letter.lower()}."
                    f"{index:02d}.{criterion_key}"
                ),
                "criterion_family_id": f"{language}.{theme}.{task_letter.lower()}.{criterion_key}",
                "points": float(criterion.get("points", 0.0)),
                "criterion": criterion_name,
                "hint": str(criterion.get("hint", "")),
            }
        )
    return enriched

def validate_solution_rubrics_semantics(knowledge_base: Dict[str, object]) -> List[str]:
    """Prueft semantische Integritaet der Rubrics-Wissensdatenbank."""
    errors: List[str] = []
    entry_ids: set[str] = set()
    criterion_ids: set[str] = set()

    for entry in knowledge_base.get("entries", []):
        if not isinstance(entry, dict):
            continue

        entry_id = str(entry.get("entry_id", ""))
        if entry_id in entry_ids:
            errors.append(f"Doppelte entry_id: {entry_id}")
        entry_ids.add(entry_id)

        criteria = entry.get("criteria", [])
        points_total = float(entry.get("points_total", 0.0))
        criteria_sum = 0.0
        for criterion in criteria:
            if not isinstance(criterion, dict):
                continue
            criterion_id = str(criterion.get("criterion_id", ""))
            if criterion_id in criterion_ids:
                errors.append(f"Doppelte criterion_id: {criterion_id}")
            criterion_ids.add(criterion_id)
            criteria_sum += float(criterion.get("points", 0.0))

        if abs(criteria_sum - points_total) > 0.01:
            errors.append(
                f"{entry_id}: Kriterien-Summe {criteria_sum} ≠ Aufgabensumme {points_total}"
            )

    return errors

def build_solution_rubrics_knowledge_base(languages: List[str]) -> Dict[str, object]:
    """Baut maschinenlesbare Bewertungsrubriken aus allen solutions-Dateien."""
    entries: List[Dict[str, object]] = []

    for language in languages:
        language_dir = EXAMS_DIR / language
        for theme in get_all_themes(language_dir):
            theme_dir = language_dir / theme
            solution_variants = collect_variant_files(theme_dir, "solutions")

            for variant, solution_path in solution_variants.items():
                content = solution_path.read_text(encoding="utf-8")
                task_sections = extract_task_sections(content)
                variant_label = variant_name_from_number(variant, "solutions")
                variant_key = Path(variant_label).stem

                for task_letter in ["A", "B", "C", "D"]:
                    section = task_sections.get(task_letter, "")
                    if not section:
                        continue

                    points_block = extract_block_after_heading(section, r"^###\s+Punktbewertung\s*$|^####\s+Punktbewertung\s*$")
                    errors_block = extract_block_after_heading(section, r"^###\s+Häufige Fehler\s*$|^####\s+Häufige Fehler\s*$")
                    criteria = enrich_criteria_with_ids(
                        parse_point_criteria(points_block),
                        language,
                        theme,
                        variant_key,
                        task_letter,
                    )
                    task_id = f"{language}.{theme}.{variant_key}.{task_letter.lower()}"

                    entries.append(
                        {
                            "entry_id": task_id,
                            "language": language,
                            "theme": theme,
                            "variant": variant_label,
                            "task": task_letter,
                            "task_id": task_id,
                            "points_total": parse_task_total_points(section),
                            "criteria": criteria,
                            "common_errors": parse_common_errors(errors_block),
                            "path": str(solution_path.relative_to(EXAMS_DIR)),
                        }
                    )

    knowledge_base = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "schema_ref": str(SOLUTION_RUBRICS_SCHEMA_PATH.relative_to(EXAMS_DIR)),
        "strategy": {
            "source": "solutions_markdown",
            "task_keys": ["A", "B", "C", "D"],
            "points_unit": "points",
            "criterion_ids": "language.theme.variant.task.index.slug",
        },
        "entries": sorted(
            entries,
            key=lambda item: (
                str(item["language"]),
                str(item["theme"]),
                str(item["variant"]),
                str(item["task"]),
            ),
        ),
    }
    return knowledge_base

def write_solution_rubrics_knowledge_base(languages: List[str]) -> Path:
    """Schreibt solution_rubrics_knowledge_base.json in shared/."""
    knowledge_base = build_solution_rubrics_knowledge_base(languages)
    schema_errors = validate_data_with_schema_file(knowledge_base, SOLUTION_RUBRICS_SCHEMA_PATH)
    schema_errors.extend(validate_solution_rubrics_semantics(knowledge_base))
    if schema_errors:
        raise ValueError("; ".join(schema_errors))
    SOLUTION_RUBRICS_KB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SOLUTION_RUBRICS_KB_PATH, "w", encoding="utf-8") as kb_file:
        json.dump(knowledge_base, kb_file, ensure_ascii=True, indent=2)
        kb_file.write("\n")
    return SOLUTION_RUBRICS_KB_PATH

def validate_solution_guidance(language: str, theme: str) -> Dict[str, List[str]]:
    """Prüft, ob Lösungen pro Aufgabe Punktbewertung und häufige Fehler enthalten."""
    theme_dir = EXAMS_DIR / language / theme
    errors: List[str] = []
    warnings: List[str] = []

    solution_variants = collect_variant_files(theme_dir, "solutions")
    for variant, solution_path in solution_variants.items():
        content = solution_path.read_text(encoding="utf-8")
        task_sections = extract_task_sections(content)
        label = variant_name_from_number(variant, "solutions")

        for task_letter in ["A", "B", "C", "D"]:
            section = task_sections.get(task_letter)
            if not section:
                errors.append(f"{label}: Aufgabe {task_letter} fehlt in {solution_path.name}")
                continue

            has_points = bool(re.search(r"^###\s+Punktbewertung\s*$|^####\s+Punktbewertung\s*$", section, flags=re.MULTILINE))
            has_errors = bool(re.search(r"^###\s+Häufige Fehler\s*$|^####\s+Häufige Fehler\s*$", section, flags=re.MULTILINE))

            if not has_points:
                errors.append(f"{label}: Aufgabe {task_letter} ohne Punktbewertung")
            if not has_errors:
                errors.append(f"{label}: Aufgabe {task_letter} ohne Häufige Fehler")

            if has_points:
                points_block = extract_block_after_heading(section, r"^###\s+Punktbewertung\s*$|^####\s+Punktbewertung\s*$")
                criteria = parse_point_criteria(points_block)
                if not criteria:
                    warnings.append(f"{label}: Aufgabe {task_letter} hat Punktbewertung ohne parsebare Kriterien")
                task_total = parse_task_total_points(section)
                criteria_total = sum(float(criterion.get("points", 0.0)) for criterion in criteria)
                if task_total > 0 and abs(criteria_total - task_total) > 0.01:
                    errors.append(
                        f"{label}: Aufgabe {task_letter} Kriterien-Summe {criteria_total} ≠ {task_total}"
                    )

            if has_errors:
                errors_block = extract_block_after_heading(section, r"^###\s+Häufige Fehler\s*$|^####\s+Häufige Fehler\s*$")
                common_errors = parse_common_errors(errors_block)
                if not common_errors:
                    warnings.append(f"{label}: Aufgabe {task_letter} hat Häufige Fehler ohne Einträge")

    return {"errors": errors, "warnings": warnings}

def build_variation_knowledge_base(languages: List[str]) -> Dict[str, object]:
    """Baut die Wissensdatenbank mit Aufgaben-Fingerprints."""
    entries: List[Dict[str, str]] = []

    for language in languages:
        language_dir = EXAMS_DIR / language
        for theme in get_all_themes(language_dir):
            theme_dir = language_dir / theme
            exam_variants = collect_variant_files(theme_dir, "exam")

            for variant, exam_path in exam_variants.items():
                content = exam_path.read_text(encoding="utf-8")
                sections = extract_task_sections(content)

                for task_letter in ["A", "B", "C", "D"]:
                    task_text = sections.get(task_letter)
                    if not task_text:
                        continue

                    entries.append(
                        {
                            "language": language,
                            "theme": theme,
                            "variant": variant_name_from_number(variant, "exam"),
                            "task": task_letter,
                            "fingerprint": task_fingerprint(task_text),
                            "preview": normalize_task_text(task_text)[:180],
                            "path": str(exam_path.relative_to(EXAMS_DIR)),
                        }
                    )

    knowledge_base = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "schema_ref": str(VARIATION_KB_SCHEMA_PATH.relative_to(EXAMS_DIR)),
        "strategy": {
            "normalization": "markdown-stripped-lowercase-alnum",
            "hash": "sha256",
            "scope": "task-level-and-variant-level",
        },
        "entries": sorted(
            entries,
            key=lambda item: (
                item["language"],
                item["theme"],
                item["variant"],
                item["task"],
            ),
        ),
    }
    return knowledge_base

def write_variation_knowledge_base(languages: List[str]) -> Path:
    """Schreibt variation_knowledge_base.json in shared/."""
    knowledge_base = build_variation_knowledge_base(languages)
    schema_errors = validate_data_with_schema_file(knowledge_base, VARIATION_KB_SCHEMA_PATH)
    if schema_errors:
        raise ValueError("; ".join(schema_errors))
    KNOWLEDGE_BASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(KNOWLEDGE_BASE_PATH, "w", encoding="utf-8") as kb_file:
        json.dump(knowledge_base, kb_file, ensure_ascii=True, indent=2)
        kb_file.write("\n")
    return KNOWLEDGE_BASE_PATH

def validate_points_in_file(file_path: Path) -> Tuple[bool, float, List[str]]:
    """Prüft ob Punktesumme in Datei = 25.0 ist."""
    if not file_path.exists():
        return False, 0, [f"Datei nicht gefunden: {file_path}"]
    
    content = file_path.read_text(encoding='utf-8')
    errors = []
    
    # Suche gezielt im Abschnitt "Punkteuebersicht" nach genau vier Aufgabenwerten.
    section_match = re.search(
        r"\*\*Punkteuebersicht.*?\*\*(.*?)(?:\n\*\*|\n---|\Z)",
        content,
        flags=re.DOTALL,
    )

    search_area = section_match.group(1) if section_match else content

    # Pattern fuer Aufgabenzeilen wie:
    # - A ...: 5.0 Punkte
    # - B ...: 7.5 Punkte
    task_points_pattern = r"-\s*[A-D][^\n]*?:\s*(\d+\.?\d*)\s*Punkte"
    matches = re.findall(task_points_pattern, search_area)
    
    if matches:
        total = sum(float(p) for p in matches[:4])
        if abs(total - EXPECTED_TOTAL_POINTS) > 0.01:
            errors.append(f"Punktesumme {total} ≠ {EXPECTED_TOTAL_POINTS}")
            return False, total, errors
        return True, total, []
    else:
        # Keine Punkte gefunden - das ist OK, wird als Warning behandelt
        return True, 0, []

def validate_rubrics_json() -> Dict[str, List[str]]:
    """Validiert shared/rubrics.json."""
    rubrics_path = EXAMS_DIR / "shared" / "rubrics.json"
    errors = []
    warnings = []
    
    if not rubrics_path.exists():
        errors.append(f"Fehlende Datei: {rubrics_path.relative_to(EXAMS_DIR)}")
        return {"errors": errors, "warnings": warnings}
    
    try:
        with open(rubrics_path, 'r', encoding='utf-8') as f:
            rubrics = json.load(f)
        
        # Prüfe Struktur
        if "rubrics" not in rubrics:
            errors.append("rubrics.json fehlt 'rubrics' Schlüssel")
            return {"errors": errors, "warnings": warnings}
        
        # Prüfe Punktesumme
        total_points = 0
        for key in ["aufgabe_a", "aufgabe_b", "aufgabe_c", "aufgabe_d"]:
            if key not in rubrics["rubrics"]:
                errors.append(f"rubrics.json fehlt '{key}'")
            else:
                total_points += rubrics["rubrics"][key].get("points", 0)
        
        if abs(total_points - EXPECTED_TOTAL_POINTS) > 0.01:
            errors.append(f"Punktesumme in rubrics.json: {total_points} ≠ {EXPECTED_TOTAL_POINTS}")
        
    except json.JSONDecodeError as e:
        errors.append(f"JSON-Fehler in rubrics.json: {e}")
    except Exception as e:
        errors.append(f"Fehler beim Lesen von rubrics.json: {e}")
    
    return {"errors": errors, "warnings": warnings}

def validate_metadata_json(language: str, theme: str) -> Dict[str, List[str]]:
    """Validiert metadata.json (optional)."""
    metadata_path = EXAMS_DIR / language / theme / "metadata.json"
    errors = []
    warnings = []
    
    if not metadata_path.exists():
        # Metadata ist optional - kein Fehler
        return {"errors": errors, "warnings": warnings}
    
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Prüfe erwartete Felder
        required_fields = ["theme", "language", "variants"]
        for field in required_fields:
            if field not in metadata:
                warnings.append(f"metadata.json fehlt optionales Feld: '{field}'")
        
        # Prüfe Werte
        if metadata.get("language") != language:
            errors.append(f"metadata.json: language='{metadata.get('language')}' ≠ '{language}'")
        
        if metadata.get("theme") != theme:
            errors.append(f"metadata.json: theme='{metadata.get('theme')}' ≠ '{theme}'")
        
        metadata_variants = metadata.get("variants")
        if isinstance(metadata_variants, int) and metadata_variants < MIN_REQUIRED_VARIANTS:
            errors.append(f"metadata.json: variants={metadata_variants} < {MIN_REQUIRED_VARIANTS}")
        
    except json.JSONDecodeError as e:
        errors.append(f"JSON-Fehler in {metadata_path.name}: {e}")
    except Exception as e:
        errors.append(f"Fehler beim Lesen von {metadata_path.name}: {e}")
    
    return {"errors": errors, "warnings": warnings}

def main():
    """Hauptfunktion."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validiere Exam-System Struktur")
    parser.add_argument("--verbose", "-v", action="store_true", help="Ausführliche Ausgabe")
    parser.add_argument("--language", "-l", choices=EXPECTED_LANGUAGES, help="Nur eine Sprache prüfen")
    parser.add_argument(
        "--write-knowledge-base",
        action="store_true",
        help="Aktualisiert shared/variation_knowledge_base.json und shared/solution_rubrics_knowledge_base.json",
    )
    args = parser.parse_args()
    
    print_header("🔍 Exam-System Validierung")
    print(f"Verzeichnis: {EXAMS_DIR}\n")
    
    all_errors = []
    all_warnings = []
    
    # 1. Prüfe shared/rubrics.json
    print_header("1. Prüfe shared/rubrics.json")
    rubrics_result = validate_rubrics_json()
    if rubrics_result["errors"]:
        for error in rubrics_result["errors"]:
            print_error(error)
            all_errors.append(error)
    else:
        print_success("rubrics.json ist valide")
    
    for warning in rubrics_result["warnings"]:
        print_warning(warning)
        all_warnings.append(warning)
    
    # 2. Prüfe Sprachen und Themen
    languages = [args.language] if args.language else EXPECTED_LANGUAGES
    
    for language in languages:
        print_header(f"2. Prüfe Sprache: {language}")
        
        language_dir = EXAMS_DIR / language
        if not language_dir.exists():
            error = f"Verzeichnis {language}/ existiert nicht"
            print_error(error)
            all_errors.append(error)
            continue
        
        # Finde alle Themen
        themes = get_all_themes(language_dir)
        if not themes:
            warning = f"Keine Themen in {language}/ gefunden"
            print_warning(warning)
            all_warnings.append(warning)
            continue
        
        print_info(f"Gefundene Themen: {', '.join(themes)}")
        
        for theme in themes:
            print(f"\n  📝 Theme: {theme}")
            
            # Validiere Dateien
            file_result = validate_exam_files(language, theme)
            for error in file_result["errors"]:
                print_error(f"  {error}")
                all_errors.append(f"{language}/{theme}: {error}")
            
            for warning in file_result["warnings"]:
                print_warning(f"  {warning}")
                all_warnings.append(f"{language}/{theme}: {warning}")
            
            if not file_result["errors"]:
                print_success(f"  Alle erforderlichen Dateien vorhanden")
            
            # Validiere Punktesumme in exam.md
            if args.verbose:
                exam_path = EXAMS_DIR / language / theme / "exam.md"
                is_valid, total, errors = validate_points_in_file(exam_path)
                if total > 0:
                    if is_valid:
                        print_success(f"  Punktesumme: {total}")
                    else:
                        for error in errors:
                            print_error(f"  {error}")
                            all_errors.append(f"{language}/{theme}: {error}")
            
            # Validiere metadata.json (optional)
            metadata_result = validate_metadata_json(language, theme)
            for error in metadata_result["errors"]:
                print_error(f"  {error}")
                all_errors.append(f"{language}/{theme}: {error}")
            
            for warning in metadata_result["warnings"]:
                if args.verbose:
                    print_warning(f"  {warning}")
                all_warnings.append(f"{language}/{theme}: {warning}")

            # Prüfe Lösungs-Qualität (Punktbewertung + Häufige Fehler)
            guidance_result = validate_solution_guidance(language, theme)
            for error in guidance_result["errors"]:
                print_error(f"  {error}")
                all_errors.append(f"{language}/{theme}: {error}")

            for warning in guidance_result["warnings"]:
                if args.verbose:
                    print_warning(f"  {warning}")
                all_warnings.append(f"{language}/{theme}: {warning}")

            # Pruefe Aufgabenvariation (keine identischen Aufgabenstellungen)
            uniqueness_result = validate_variant_uniqueness(language, theme)
            for error in uniqueness_result["errors"]:
                print_error(f"  {error}")
                all_errors.append(f"{language}/{theme}: {error}")

            for warning in uniqueness_result["warnings"]:
                if args.verbose:
                    print_warning(f"  {warning}")
                all_warnings.append(f"{language}/{theme}: {warning}")

            # Pruefe Unicode-Umlaute (ae/oe/ue → ä/ö/ü)
            theme_dir = EXAMS_DIR / language / theme
            for md_file in sorted(theme_dir.glob("*.md")):
                umlaut_errors = check_unicode_umlauts(md_file)
                for error in umlaut_errors:
                    msg = f"{md_file.relative_to(EXAMS_DIR)}: {error}"
                    print_error(f"  {msg}")
                    all_errors.append(msg)

    if args.write_knowledge_base:
        knowledge_base_path = write_variation_knowledge_base(languages)
        print_info(
            f"Wissensdatenbank aktualisiert: {knowledge_base_path.relative_to(REPO_ROOT)}"
        )
        rubrics_kb_path = write_solution_rubrics_knowledge_base(languages)
        print_info(
            f"Rubrics-Wissensdatenbank aktualisiert: {rubrics_kb_path.relative_to(REPO_ROOT)}"
        )
    
    # 3. Zusammenfassung
    print_header("📊 Zusammenfassung")
    print(f"Fehler: {len(all_errors)}")
    print(f"Warnungen: {len(all_warnings)}")
    
    if all_errors:
        print_error(f"\n{len(all_errors)} Fehler gefunden:")
        for error in all_errors[:10]:  # Zeige max 10
            print(f"  - {error}")
        if len(all_errors) > 10:
            print(f"  ... und {len(all_errors) - 10} weitere")
        sys.exit(1)
    else:
        print_success("\n✓ Alle Validierungen bestanden!")
        if all_warnings and args.verbose:
            print_warning(f"\n{len(all_warnings)} Warnungen (nicht kritisch)")
        sys.exit(0)

if __name__ == "__main__":
    main()
