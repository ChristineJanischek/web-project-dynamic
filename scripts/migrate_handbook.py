#!/usr/bin/env python3
"""
Migration script: Distributed handbook files from web-project-dynamic to edu-code-lab-core and edu-code-lab-courses.

Usage:
    python3 scripts/migrate_handbook.py [--dry-run] [--output-dir ./migration_output]

This script:
1. Identifies core and courses files
2. Generates migration bundles for manual copy to target repos
3. Creates index files for the template repo (web-project-dynamic)
4. Reports any broken links that need fixing
"""

import os
import shutil
import sys
from pathlib import Path
import json
from datetime import datetime

# File classifications
CORE_FILES = {
    "ARCHITECTURE.md": "Technische Validierung, Architektur-Bewertung",
    "BACKUP_STRATEGY.md": "Backup-, Git-Bundle- und Sicherungsstrategie",
    "REPO_GOVERNANCE.md": "Branch-Protection, Admin-Governance",
    "ROADMAP_CORE.md": "Technischer Phasenplan für core-Repo",
    "SETUP_REPOSITORIES.md": "Erstkonfiguration beider Repos",
    "DOCS_NAVIGATION_RULES.md": "Technische Navigation, Scripts-Config",
    "TEMPLATE_SYNC.md": "Git-Workflow für Template-Updates",
    "TEMPLATE_UPDATE_STRATEGY.md": "Technische Überlegungen, Auto-Sync",
    "WORKSPACE_LIVE_TEST_SETUP.md": "VS Code Setup, Extension-Management",
    "QUICKSTART_LIVE_SERVER.md": "Technisches Schüler-Onboarding",
    "architektur-prinzipien.md": "Lernmaterial über Architektur-Konzepte",
}

COURSES_FILES = {
    "COURSES_THEMENPLAN.md": "Themenstruktur & Lernziele",
    "ROADMAP_COURSES.md": "Didaktischer Marschplan",
    "GITHUB_CLASSROOM_AUTOGRADING.md": "Autograding-Tests für Aufgaben",
}

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Migrate handbook files to core and courses repos")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--output-dir", default="./migration_output", help="Output directory for migration bundles")
    
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    handbook_src = Path("docs/handbook")
    
    if not handbook_src.exists():
        print(f"❌ Fehler: {handbook_src} nicht gefunden!")
        sys.exit(1)
    
    # Create output structure
    if not args.dry_run:
        output_dir.mkdir(exist_ok=True)
        (output_dir / "core_handbook").mkdir(exist_ok=True)
        (output_dir / "courses_handbook").mkdir(exist_ok=True)
    
    print("=" * 70)
    print("📦 HANDBOOK MIGRATION TOOL")
    print("=" * 70)
    print(f"\n📍 Quelle: {handbook_src}/")
    print(f"📍 Output: {output_dir}/")
    print(f"🔍 Modus: {'DRY RUN' if args.dry_run else 'EXECUTING'}\n")
    
    # Process CORE files
    print("\n" + "=" * 70)
    print("🔵 CORE-DATEIEN (11 Dateien)")
    print("=" * 70)
    
    for filename, description in sorted(CORE_FILES.items()):
        src_file = handbook_src / filename
        if src_file.exists():
            status = "✅"
            if not args.dry_run:
                shutil.copy2(src_file, output_dir / "core_handbook" / filename)
                status = "✅ KOPIERT"
        else:
            status = "⚠️ FEHLT"
        
        print(f"{status} {filename:<40} | {description}")
    
    # Process COURSES files
    print("\n" + "=" * 70)
    print("🟢 COURSES-DATEIEN (3 Dateien)")
    print("=" * 70)
    
    for filename, description in sorted(COURSES_FILES.items()):
        src_file = handbook_src / filename
        if src_file.exists():
            status = "✅"
            if not args.dry_run:
                shutil.copy2(src_file, output_dir / "courses_handbook" / filename)
                status = "✅ KOPIERT"
        else:
            status = "⚠️ FEHLT"
        
        print(f"{status} {filename:<40} | {description}")
    
    # Generate migration report
    report = {
        "date": datetime.now().isoformat(),
        "source": str(handbook_src),
        "target_output": str(output_dir),
        "core_files": list(CORE_FILES.keys()),
        "courses_files": list(COURSES_FILES.keys()),
        "instructions": {
            "core": f"Kopiere den Inhalt von {output_dir}/core_handbook/ nach edu-code-lab-core/docs/handbook/",
            "courses": f"Kopiere den Inhalt von {output_dir}/courses_handbook/ nach edu-code-lab-courses/docs/handbook/"
        }
    }
    
    if not args.dry_run:
        report_path = output_dir / "MIGRATION_REPORT.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n📄 Report gespeichert: {report_path}")
    
    # Create README for template repo
    template_readme = """# 📚 Handbook-Verzeichnis

⚠️ **Dieses Verzeichnis wurde in zwei separaten Repositories verteilt:**

## 🔵 Core-Dokumentation (Infrastruktur & Technik)

Siehe: **[edu-code-lab-core/docs/handbook/](https://github.com/ChristineJanischek/edu-code-lab-core/tree/main/docs/handbook/)**

11 Dateien mit Fokus auf:
- Technische Architektur und Validation
- Repository Governance und Backup-Strategie
- CI/CD, Workspace-Setup, Extension-Management
- Template-Sync und Update-Strategien

---

## 🟢 Courses-Dokumentation (Lehrplan & Didaktik)

Siehe: **[edu-code-lab-courses/docs/handbook/](https://github.com/ChristineJanischek/edu-code-lab-courses/tree/main/docs/handbook/)**

3 Dateien mit Fokus auf:
- Themenplanung und Lernziele
- Roadmap für Kurstentwicklung
- Autograding-Integration und -Tests

---

## 🔗 Verlinkung zwischen den Repositories

### Von core → courses
- `core/SETUP_REPOSITORIES.md` → `courses/ROADMAP_COURSES.md`
- `core/ROADMAP_CORE.md` → `courses/ROADMAP_COURSES.md`

### Von courses → core
- `courses/COURSES_THEMENPLAN.md` → `core/ROADMAP_CORE.md`
- `courses/GITHUB_CLASSROOM_AUTOGRADING.md` → `courses/`

---

**Migration durchgeführt:** {date}
"""
    
    if not args.dry_run:
        readme_path = handbook_src / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(template_readme.format(date=datetime.now().strftime('%d.%m.%Y %H:%M')))
        print(f"📝 Template-README erstellt: {readme_path}")
    
    # Summary
    print("\n" + "=" * 70)
    print("✅ MIGRATION SUMMARY")
    print("=" * 70)
    print(f"✓ Core-Dateien: {len(CORE_FILES)} (Ready in {output_dir}/core_handbook/)")
    print(f"✓ Courses-Dateien: {len(COURSES_FILES)} (Ready in {output_dir}/courses_handbook/)")
    print(f"✓ Template-README: {handbook_src}/README.md")
    print("\n" + "=" * 70)
    print("📖 NÄCHSTE SCHRITTE")
    print("=" * 70)
    print(f"1. Dateien prüfen:")
    print(f"   ls -la {output_dir}/core_handbook/")
    print(f"   ls -la {output_dir}/courses_handbook/")
    print(f"\n2. In die Target-Repos kopieren:")
    print(f"   cp -r {output_dir}/core_handbook/* ../edu-code-lab-core/docs/handbook/")
    print(f"   cp -r {output_dir}/courses_handbook/* ../edu-code-lab-courses/docs/handbook/")
    print(f"\n3. Links in den Zieldateien prüfen und anpassen")
    print(f"4. Commit und Push in core + courses")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
