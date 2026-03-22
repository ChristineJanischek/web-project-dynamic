#!/usr/bin/env python3
"""
Helper-Skript: Cross-Repo Link-Updater für Handbook-Migration

Dieses Skript hilft, die Links in migrierten Dateien zu korrigieren:
- Interne Links zwischen Repository-Dateien in externe URLs umwandeln
- Relative Links zu Scripts/ und anderen Ressourcen validieren

Usage:
    python3 scripts/update_handbook_links.py --target [core|courses] --mode [validate|fix] [--dry-run]
"""

import re
import sys
from pathlib import Path

# Link-Mappings pro Target-Repository
LINK_MAPPINGS = {
    "core": {
        "COURSES_THEMENPLAN.md": "https://github.com/ChristineJanischek/edu-code-lab-courses/blob/main/docs/handbook/COURSES_THEMENPLAN.md",
        "ROADMAP_COURSES.md": "https://github.com/ChristineJanischek/edu-code-lab-courses/blob/main/docs/handbook/ROADMAP_COURSES.md",
        "GITHUB_CLASSROOM_AUTOGRADING.md": "https://github.com/ChristineJanischek/edu-code-lab-courses/blob/main/docs/handbook/GITHUB_CLASSROOM_AUTOGRADING.md",
        "scripts/": "../../scripts/",  # Relative path lookup
    },
    "courses": {
        "ROADMAP_CORE.md": "https://github.com/ChristineJanischek/edu-code-lab-core/blob/main/docs/handbook/ROADMAP_CORE.md",
        "SETUP_REPOSITORIES.md": "https://github.com/ChristineJanischek/edu-code-lab-core/blob/main/docs/handbook/SETUP_REPOSITORIES.md",
        "scripts/": "../../scripts/",  # Note: courses might not have scripts/
    }
}

def validate_links(handbook_dir, target_repo):
    """Validate all links in handbook files."""
    print(f"\n🔍 Validiere Links in {handbook_dir} für {target_repo}-Repo\n")
    
    issues = []
    
    for md_file in handbook_dir.glob("*.md"):
        content = md_file.read_text(encoding='utf-8')
        
        # Find all markdown links
        md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        
        for link_text, link_url in md_links:
            # Check if it's a relative link that needs fixing
            if link_url.startswith('../') or link_url.startswith('./'):
                # Check if it points to a handbook file
                for mapped_file in LINK_MAPPINGS[target_repo]:
                    if mapped_file != "scripts/" and mapped_file in link_url:
                        issues.append({
                            'file': md_file.name,
                            'text': link_text,
                            'old': link_url,
                            'new': LINK_MAPPINGS[target_repo][mapped_file],
                            'severity': 'CROSS-REPO'
                        })
            
            # Check if files exist (for relative links)
            elif link_url.startswith('../../scripts/'):
                resolved = handbook_dir.parent.parent / link_url.replace('../../', '')
                if not resolved.exists() and 'scripts' in str(resolved):
                    issues.append({
                        'file': md_file.name,
                        'text': link_text,
                        'url': link_url,
                        'severity': 'MISSING-SCRIPT'
                    })
    
    if issues:
        print(f"⚠️ Gefundene Link-Probleme: {len(issues)}\n")
        for issue in issues:
            print(f"  📄 {issue['file']}")
            print(f"     Text: {issue['text']}")
            if issue['severity'] == 'CROSS-REPO':
                print(f"     Alt:  {issue['old']}")
                print(f"     Neu:  {issue['new']}")
            else:
                print(f"     URL:  {issue.get('url', issue.get('old'))}")
            print(f"     Typ:  {issue['severity']}\n")
    else:
        print("✅ Alle Links sind in Ordnung!")
    
    return issues

def fix_links(handbook_dir, target_repo, dry_run=False):
    """Fix cross-repo links in handbook files."""
    print(f"\n🔧 Korrigiere Links in {handbook_dir} für {target_repo}-Repo\n")
    
    fixed = 0
    
    for md_file in handbook_dir.glob("*.md"):
        content = md_file.read_text(encoding='utf-8')
        original = content
        
        # Replace handbook-file links with external URLs
        for source_file, target_url in LINK_MAPPINGS[target_repo].items():
            if source_file == "scripts/":
                continue
            
            # Find patterns like [text](FILENAME.md) or [text](./FILENAME.md)
            patterns = [
                f'\\[([^\\]]+)\\]\\({source_file}\\)',
                f'\\[([^\\]]+)\\]\\(\\./{source_file}\\)',
                f'\\[([^\\]]+)\\]\\(.*/{source_file}\\)',
            ]
            
            for pattern in patterns:
                def replace_link(match):
                    text = match.group(1)
                    return f'[{text}]({target_url})'
                
                new_content = re.sub(pattern, replace_link, content)
                if new_content != content:
                    print(f"  ✅ {md_file.name}: {source_file} → external link")
                    content = new_content
                    fixed += 1
        
        # Write back if changed
        if content != original:
            if not dry_run:
                md_file.write_text(content, encoding='utf-8')
            else:
                print(f"  [DRY-RUN] Would save changes to {md_file.name}")
    
    print(f"\n✅ {fixed} Link(s) korrigiert {'(DRY-RUN)' if dry_run else ''}\n")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Update handbook links for migration")
    parser.add_argument("--target", choices=["core", "courses"], required=True,
                        help="Target repository type")
    parser.add_argument("--mode", choices=["validate", "fix"], default="validate",
                        help="Mode: validate or fix links")
    parser.add_argument("--handbook-dir", default="docs/handbook",
                        help="Path to handbook directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without making changes")
    
    args = parser.parse_args()
    
    handbook_dir = Path(args.handbook_dir)
    
    if not handbook_dir.exists():
        print(f"❌ Fehler: {handbook_dir} nicht gefunden!")
        sys.exit(1)
    
    print("=" * 70)
    print(f"🔗 HANDBOOK LINK UPDATER ({args.target.upper()}-Repo)")
    print("=" * 70)
    
    if args.mode == "validate":
        issues = validate_links(handbook_dir, args.target)
        sys.exit(1 if issues else 0)
    else:
        fix_links(handbook_dir, args.target, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
