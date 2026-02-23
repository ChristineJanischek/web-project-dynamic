#!/usr/bin/env sh
set -eu

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TIMESTAMP="$(date -u +%Y%m%d-%H%M%SZ)"
OUTPUT_DIR="${1:-$ROOT_DIR/backups/$TIMESTAMP}"

mkdir -p "$OUTPUT_DIR"

BUNDLE_FILE="$OUTPUT_DIR/repository-$TIMESTAMP.bundle"
ARCHIVE_FILE="$OUTPUT_DIR/worktree-$TIMESTAMP.tar.gz"
MANIFEST_FILE="$OUTPUT_DIR/manifest.txt"
CHECKSUM_FILE="$OUTPUT_DIR/SHA256SUMS.txt"

printf "Creating git bundle...\n"
git -C "$ROOT_DIR" bundle create "$BUNDLE_FILE" --all

printf "Creating source archive...\n"
git -C "$ROOT_DIR" archive --format=tar.gz -o "$ARCHIVE_FILE" HEAD

{
  echo "timestamp=$TIMESTAMP"
  echo "repository=$ROOT_DIR"
  echo "head=$(git -C "$ROOT_DIR" rev-parse HEAD)"
  echo "branch=$(git -C "$ROOT_DIR" branch --show-current)"
  echo "bundle=$(basename "$BUNDLE_FILE")"
  echo "archive=$(basename "$ARCHIVE_FILE")"
} > "$MANIFEST_FILE"

(
  cd "$OUTPUT_DIR"
  sha256sum "$(basename "$BUNDLE_FILE")" "$(basename "$ARCHIVE_FILE")" "$(basename "$MANIFEST_FILE")" > "$(basename "$CHECKSUM_FILE")"
)

printf "Backup snapshot created: %s\n" "$OUTPUT_DIR"
printf "Verify with: cd %s && sha256sum -c SHA256SUMS.txt\n" "$OUTPUT_DIR"
