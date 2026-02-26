#!/usr/bin/env bash
set -euo pipefail

OWNER="${1:-ChristineJanischek}"
REPO="${2:-web-project-dynamic}"
BRANCH="${3:-main}"
ADMIN_USER="${4:-ChristineJanischek}"

if ! command -v gh >/dev/null 2>&1; then
  echo "❌ GitHub CLI (gh) nicht gefunden."
  echo "   Installiere gh und führe dann aus:"
  echo "   gh auth login"
  exit 1
fi

echo "🔐 Setze Branch Protection für ${OWNER}/${REPO} (${BRANCH})"
echo "👤 Push-Berechtigung wird auf User '${ADMIN_USER}' eingeschränkt"

payload="$(cat <<JSON
{
  "required_status_checks": {
    "strict": true,
    "contexts": []
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1
  },
  "restrictions": {
    "users": ["${ADMIN_USER}"],
    "teams": [],
    "apps": []
  },
  "required_linear_history": false,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "lock_branch": false,
  "allow_fork_syncing": true
}
JSON
)"

gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/${OWNER}/${REPO}/branches/${BRANCH}/protection" \
  --input - <<<"${payload}"

echo "✅ Branch Protection wurde gesetzt."
echo "ℹ️ Prüfe in GitHub zusätzlich unter Settings → Rules / Branches, ob alle gewünschten Regeln aktiv sind."
