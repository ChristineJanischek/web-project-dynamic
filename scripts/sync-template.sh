#!/bin/bash
# Template-Sync Manager für Lehrende
# Hilft beim Verwalten von Template-Updates für abhängige Repositories

set -e

REPO_URL="https://github.com/ChristineJanischek/web-project-dynamic.git"
TEMPLATE_REMOTE="template"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
LOG_FILE="template_sync_$TIMESTAMP.log"

echo "🔄 Template-Sync Manager"
echo "========================"
echo ""

# Funktion: Hilfsmeldung
show_help() {
    cat << 'EOF'
Verwendung: ./sync-template.sh [COMMAND] [OPTIONS]

Befehle:
  setup              Richte Template-Remote in diesem Repo ein
  check              Prüfe auf verfügbare Updates
  list-changes       Zeige alle Änderungen seit letztem Sync
  apply              Übernehme Updates selektiv
  status             Zeige Sync-Status
  help               Zeige diese Hilfe

Beispiele:
  ./sync-template.sh setup
  ./sync-template.sh check
  ./sync-template.sh list-changes
  ./sync-template.sh apply --include="docs/* version3/*"

Optionen für 'apply':
  --include="PATTERN"    Nur diese Patterns übernehmen
  --dry-run             Zeige was übernommen würde (ohne zu pushen)
  --no-commit           Merge ohne Commit (für manuelle Bearbeitung)

EOF
}

# Funktion: Setup
setup_template() {
    echo "📋 Richte Template-Remote ein..."
    
    if git remote get-url $TEMPLATE_REMOTE &>/dev/null; then
        echo "⚠️  Template-Remote existiert bereits:"
        git remote get-url $TEMPLATE_REMOTE
        read -p "Überschreiben? (j/n): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Jj]$ ]]; then
            git remote remove $TEMPLATE_REMOTE
            echo "✓ Altes Remote entfernt"
        else
            return 0
        fi
    fi
    
    git remote add $TEMPLATE_REMOTE "$REPO_URL"
    echo "✅ Template-Remote hinzugefügt:"
    git remote get-url $TEMPLATE_REMOTE
    
    echo ""
    echo "🔽 Lade Template-Änderungen..."
    git fetch $TEMPLATE_REMOTE
    
    echo "✅ Setup abgeschlossen!"
    echo ""
    echo "Nächster Schritt: ./sync-template.sh check"
}

# Funktion: Check Updates
check_updates() {
    echo "🔍 Prüfe auf Updates..."
    echo ""
    
    if ! git remote get-url $TEMPLATE_REMOTE &>/dev/null; then
        echo "❌ Template-Remote nicht konfiguriert"
        echo "Führe zuerst aus: ./sync-template.sh setup"
        return 1
    fi
    
    git fetch $TEMPLATE_REMOTE main
    
    # Vergleiche mit lokalem main
    BEHIND=$(git rev-list --count main..template/main 2>/dev/null || echo "0")
    
    if [ "$BEHIND" -eq 0 ]; then
        echo "✅ Repo ist aktuell - keine Updates verfügbar"
        return 0
    fi
    
    echo "⚠️  $BEHIND Commits verfügbar!"
    echo ""
    echo "Commits vom Template:"
    git log --oneline main..template/main
    echo ""
    echo "Um Updates zu sehen: ./sync-template.sh list-changes"
    echo "Um Updates zu übernehmen: ./sync-template.sh apply"
}

# Funktion: Liste Änderungen
list_changes() {
    echo "📊 Änderungen seit letztem Sync:"
    echo "================================"
    echo ""
    
    if ! git remote get-url $TEMPLATE_REMOTE &>/dev/null; then
        echo "❌ Template-Remote nicht konfiguriert"
        return 1
    fi
    
    git fetch $TEMPLATE_REMOTE main
    
    echo "Geänderte Dateien:"
    git diff --name-status main..template/main | sed 's/^/  /'
    
    echo ""
    echo "Detaillierter Diff:"
    git diff --stat main..template/main
}

# Funktion: Übernehme Updates
apply_updates() {
    echo "📥 Übernehme Updates..."
    echo ""
    
    if ! git remote get-url $TEMPLATE_REMOTE &>/dev/null; then
        echo "❌ Template-Remote nicht konfiguriert"
        return 1
    fi
    
    # Prüfe auf ungespeicherte Änderungen
    if ! git diff-index --quiet HEAD --; then
        echo "❌ Ungespeicherte Änderungen vorhanden!"
        echo "   Bitte erst committen: git add . && git commit -m 'work in progress'"
        return 1
    fi
    
    git fetch $TEMPLATE_REMOTE main
    
    # Dry-Run wenn gewünscht
    if [[ " $* " =~ " --dry-run " ]]; then
        echo "🔍 Dry-Run Modus (keine Änderungen):"
        git merge --no-commit --no-ff template/main --dry-run
        git merge --abort
        echo "✅ Dry-Run abgeschlossen"
        return 0
    fi
    
    # Erstelle Backup-Branch vor Merge
    BACKUP_BRANCH="backup_before_template_sync_$TIMESTAMP"
    git branch $BACKUP_BRANCH
    echo "💾 Backup-Branch erstellt: $BACKUP_BRANCH"
    
    # Starte Merge
    echo "🔀 Starte Merge mit template/main..."
    
    if git merge --no-edit template/main; then
        echo "✅ Update erfolgreich übernommen!"
        echo ""
        echo "📝 Zusammenfassung:"
        git log --oneline -5
        
        echo ""
        echo "💡 Tipps:"
        echo "  - Prüfe die Änderungen: git diff HEAD~1 HEAD"
        echo "  - Teste die Anwendung"
        echo "  - Bei Problemen: git reset --hard $BACKUP_BRANCH"
        
    else
        echo "⚠️  Merge-Konflikte erkannt!"
        echo ""
        echo "Bitte manuell auflösen:"
        echo "  1. git status  # Zeige Konflikte"
        echo "  2. Bearbeite konflikt­hafte Dateien"
        echo "  3. git add ."
        echo "  4. git commit -m 'Merge template updates'"
        echo ""
        echo "Oder abbrechen: git merge --abort"
        return 1
    fi
}

# Funktion: Status
show_status() {
    echo "📊 Template-Sync Status"
    echo "========================"
    echo ""
    
    if git remote get-url $TEMPLATE_REMOTE &>/dev/null; then
        echo "✅ Template-Remote konfiguriert:"
        git remote get-url $TEMPLATE_REMOTE
    else
        echo "❌ Template-Remote NICHT konfiguriert"
        echo "   Führe aus: ./sync-template.sh setup"
    fi
    
    echo ""
    echo "Lokale Branches:"
    git branch | sed 's/^/  /'
    
    echo ""
    echo "Zuletzt gesyncte Commits:"
    git log --grep="template\|sync\|update" --oneline -5 2>/dev/null || \
    git log --oneline -5
}

# Hauptprogramm
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

COMMAND=$1
shift

case $COMMAND in
    setup)
        setup_template
        ;;
    check)
        check_updates
        ;;
    list-changes|list)
        list_changes
        ;;
    apply)
        apply_updates "$@"
        ;;
    status)
        show_status
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "❌ Unbekannter Befehl: $COMMAND"
        echo ""
        show_help
        exit 1
        ;;
esac

echo ""
echo "Log gespeichert in: $LOG_FILE" 2>&1 | tee -a "$LOG_FILE"
