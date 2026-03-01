#!/usr/bin/env python3
"""
Exam-System Validierungs-Script

Prüft die Konsistenz und Vollständigkeit des Exam-Systems:
- Verzeichnisstruktur
- Datei-Benennungen
- Varianten-Vollständigkeit
- Punktesummen (wenn in Dateien vorhanden)
- Metadata-Validierung

Usage:
    python3 scripts/validate_exams.py
    python3 scripts/validate_exams.py --verbose
    python3 scripts/validate_exams.py --language javascript
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Konstanten
EXAMS_DIR = Path(__file__).parent.parent / "docs/programmierung/grundlagen/exams"
EXPECTED_LANGUAGES = ["javascript", "php", "python"]
EXPECTED_VARIANTS = 4  # exam.md + exam_v2.md + exam_v3.md + exam_v4.md
EXPECTED_TOTAL_POINTS = 25.0

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

def validate_exam_files(language: str, theme: str) -> Dict[str, List[str]]:
    """Validiert Exam-Dateien für ein Thema."""
    theme_dir = EXAMS_DIR / language / theme
    errors = []
    warnings = []
    
    if not theme_dir.exists():
        errors.append(f"Verzeichnis {theme_dir} existiert nicht")
        return {"errors": errors, "warnings": warnings}
    
    # Prüfe Exam-Varianten
    expected_exams = ["exam.md", "exam_v2.md", "exam_v3.md", "exam_v4.md"]
    for exam_file in expected_exams:
        exam_path = theme_dir / exam_file
        if not exam_path.exists():
            errors.append(f"Fehlende Datei: {exam_path.relative_to(EXAMS_DIR)}")
    
    # Prüfe Solutions-Varianten
    expected_solutions = ["solutions.md", "solutions_v2.md", "solutions_v3.md", "solutions_v4.md"]
    for sol_file in expected_solutions:
        sol_path = theme_dir / sol_file
        if not sol_path.exists():
            errors.append(f"Fehlende Datei: {sol_path.relative_to(EXAMS_DIR)}")
    
    # Prüfe Structogramme-Verzeichnis
    struct_dir = theme_dir / "structogramme"
    if not struct_dir.exists():
        warnings.append(f"Fehlendes Verzeichnis: {struct_dir.relative_to(EXAMS_DIR)}")
    
    return {"errors": errors, "warnings": warnings}

def validate_points_in_file(file_path: Path) -> Tuple[bool, float, List[str]]:
    """Prüft ob Punktesumme in Datei = 25.0 ist."""
    if not file_path.exists():
        return False, 0, [f"Datei nicht gefunden: {file_path}"]
    
    content = file_path.read_text(encoding='utf-8')
    errors = []
    
    # Suche nach Punkteangaben (kann in verschiedenen Formaten sein)
    # Pattern: "5.0 Punkte", "7.5 Punkte", etc.
    points_pattern = r'(\d+\.?\d*)\s*Punkte'
    matches = re.findall(points_pattern, content)
    
    if matches:
        total = sum(float(p) for p in matches[:4])  # Nur erste 4 (A, B, C, D)
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
        
        if metadata.get("variants") != EXPECTED_VARIANTS:
            errors.append(f"metadata.json: variants={metadata.get('variants')} ≠ {EXPECTED_VARIANTS}")
        
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
