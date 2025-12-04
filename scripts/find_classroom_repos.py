#!/usr/bin/env python3
"""
GitHub Classroom Repos Extractor
Findet alle Repos die aus einem Template erstellt wurden und exportiert sie
im Format für DEPENDENT_REPOS

Verwendung:
  python3 find_classroom_repos.py <ORGANISATION> [PATTERN]

Beispiel:
  python3 find_classroom_repos.py github-classroom-webentwicklung web-project
  python3 find_classroom_repos.py ChristineJanischek web-project
"""

import subprocess
import json
import sys
from typing import List, Tuple

def run_gh_command(cmd: str) -> Tuple[str, str, int]:
    """Führe gh CLI Befehl aus"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

def get_repos(org: str, pattern: str = "web-project") -> List[str]:
    """
    Hole alle Repos einer Organisation die dem Pattern entsprechen
    
    Args:
        org: GitHub Organisation (z.B. "github-classroom-webentwicklung")
        pattern: Suchpattern für Repo-Namen (z.B. "web-project")
    
    Returns:
        Liste der Repos im Format owner/repo
    """
    print(f"🔍 Durchsuche Organisation: {org}")
    print(f"   Pattern: {pattern}")
    
    # Hole alle Repos
    cmd = f'gh repo list {org} --limit 1000 --json name,owner 2>/dev/null'
    stdout, stderr, code = run_gh_command(cmd)
    
    if code != 0:
        print(f"❌ Fehler beim Zugriff auf {org}")
        print(f"   Stelle sicher dass die Organisation existiert und du Zugriff hast")
        return []
    
    if not stdout:
        print(f"⚠️  Keine Repos gefunden in {org}")
        return []
    
    try:
        repos_data = json.loads(stdout)
    except json.JSONDecodeError:
        print(f"❌ Fehler beim Parsen der Repos")
        return []
    
    # Filtere nach Pattern
    filtered = []
    for repo in repos_data:
        if pattern.lower() in repo["name"].lower():
            full_name = f"{repo['owner']['login']}/{repo['name']}"
            filtered.append(full_name)
            print(f"  ✓ {full_name}")
    
    return sorted(filtered)

def format_for_yaml(repos: List[str]) -> str:
    """Formatiere Repos für DEPENDENT_REPOS im Workflow"""
    lines = [
        "env:",
        "  DEPENDENT_REPOS: |"
    ]
    for repo in repos:
        lines.append(f"    {repo}")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("❌ Zu wenig Argumente!")
        print()
        print("Verwendung:")
        print("  python3 find_classroom_repos.py <ORGANISATION> [PATTERN]")
        print()
        print("Beispiele:")
        print("  python3 find_classroom_repos.py github-classroom-webentwicklung web-project")
        print("  python3 find_classroom_repos.py ChristineJanischek web-project")
        print()
        print("Häufige Organisationen:")
        print("  - ChristineJanischek (direkt unter Benutzername)")
        print("  - github-classroom-webentwicklung (Klassenzimmer-Org)")
        print("  - github-classroom-190190248 (Klassenzimmer nach ID)")
        sys.exit(1)
    
    org = sys.argv[1]
    pattern = sys.argv[2] if len(sys.argv) > 2 else "web-project"
    
    print("╔════════════════════════════════════════════════════════════╗")
    print("║  GitHub Classroom Repos Extractor                         ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    repos = get_repos(org, pattern)
    
    print()
    print("━" * 60)
    print()
    
    if not repos:
        print("❌ Keine Repos gefunden!")
        print()
        print("💡 Tipps:")
        print("1. Prüfe die Organisation:")
        print(f"   gh repo list {org} --limit 10")
        print()
        print("2. Liste alle Organisationen auf:")
        print("   gh org list")
        print()
        print("3. Wenn keine Standard-Org, nutze manuelle Methode:")
        print("   Öffne https://classroom.github.com")
        print("   Drücke F12 und führe das JavaScript-Snippet aus")
        sys.exit(1)
    
    print(f"✅ {len(repos)} Repos gefunden!")
    print()
    print("📋 YAML Format für template-sync.yml:")
    print()
    print(format_for_yaml(repos))
    print()
    print("━" * 60)
    print()
    print("📝 Schritte zum Einbauen:")
    print()
    print("1. Kopiere die YAML oben")
    print("2. Öffne: .github/workflows/template-sync.yml")
    print("3. Ersetze Zeile 31-45 mit der YAML")
    print("4. Speichern (Ctrl+S)")
    print("5. Commit: git add -A && git commit -m 'Configure DEPENDENT_REPOS'")
    print("6. Push: git push")
    print()

if __name__ == "__main__":
    main()
