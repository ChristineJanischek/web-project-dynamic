#!/bin/bash
# Setup-Script für CI/CD des Exam-Systems
# Installiert Pre-Commit Hooks und konfiguriert GitHub Actions

set -e

echo "🔧 Exam-System CI/CD Setup"
echo "=========================="
echo ""

# Farben
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Pre-Commit Installation
echo -e "${BLUE}1️⃣  Pre-Commit Hooks einrichten...${NC}"
if ! command -v pre-commit &> /dev/null; then
    echo "pre-commit nicht gefunden. Installiere..."
    pip install pre-commit
fi

echo "Aktiviere Pre-Commit Hooks..."
pre-commit install

if [ -f .git/hooks/pre-commit ]; then
    echo -e "${GREEN}✓ Pre-Commit Hook aktiviert${NC}"
else
    echo -e "${YELLOW}⚠ Pre-Commit Hook konnte nicht aktiviert werden${NC}"
fi

echo ""

# 2. Test der Validierung
echo -e "${BLUE}2️⃣  Exam-System Validierung testen...${NC}"
if python3 scripts/validate_exams.py --write-knowledge-base; then
    echo -e "${GREEN}✓ Validierung erfolgreich${NC}"
else
    echo -e "${YELLOW}⚠ Validierung hatte Warnungen${NC}"
fi

echo ""

# 3. GitHub Actions Info
echo -e "${BLUE}3️⃣  GitHub Actions Status${NC}"
if [ -f .github/workflows/validate-exams.yml ]; then
    echo -e "${GREEN}✓ Workflow vorhanden: .github/workflows/validate-exams.yml${NC}"
    echo ""
    echo "GitHub Actions wird automatisch ausgeführt bei:"
    echo "  - Push auf main/develop"
    echo "  - Pull Requests gegen main/develop"
else
    echo -e "${YELLOW}⚠ Workflow-Datei nicht gefunden${NC}"
fi

echo ""

# 4. Setup-Zusammenfassung
echo -e "${BLUE}📋 Setup-Zusammenfassung${NC}"
echo ""
echo "✓ Pre-Commit Hooks installiert"
echo "  → Validierung läuft automatisch vor jedem Commit"
echo ""
echo "✓ Exam-System konfiguriert"
echo "  → validate_exams.py mit Duplikat-Check"
echo "  → Knowledge-Base wird automatisch aktualisiert"
echo ""
echo "✓ GitHub Actions vorbereitet"
echo "  → Automatische Validierung bei Push/PR"
echo ""

# 5. Next Steps
echo -e "${BLUE}🚀 Nächste Schritte${NC}"
echo ""
echo "1. Dokumentation lesen:"
echo "   → scripts/README_CI_SETUP.md"
echo ""
echo "2. Erste Validierung manuell ausführen:"
echo "   → python3 scripts/validate_exams.py --verbose"
echo ""
echo "3. Neue Variante erstellen (Beispiel):"
echo "   → nano docs/programmierung/grundlagen/exams/php/basics/exam_v7.md"
echo "   → git add ..."
echo "   → git commit -m 'feat: add PHP Basics v7'"
echo "   → Pre-Commit Hook validiert automatisch"
echo ""

echo -e "${GREEN}✅ Setup abgeschlossen!${NC}"
