#Temporary directories
#
# Goals
# Avoid partial or corrupted outputs
#
# Tasks
# - Create a temporary directory
# - Write a file into it
# - Move the file to a final location
# - Delete the temporary directory
#
# Outcome
# - You understand atomic operations (make sense if there's some validation involved)
# - You know why temp folders exist

#!/usr/bin/env bash
set -euo pipefail

FINAL_DIR="data/output"
FINAL_FILE="${FINAL_DIR}/result.txt"

TMP_DIR="$(mktemp -d)"
echo "Created temp dir: $TMP_DIR"

trap 'rm -rf "$TMP_DIR"' EXIT

# Writes content in the temp folder
echo "This is a safe, atomic write." > "$TMP_DIR/result.txt"

mkdir -p "$FINAL_DIR" 

# Validation: -x checks for exact content, before moving anything
if grep -qx "This is a safe, atomic write." "$TMP_DIR/result.txt"; then
  mv "$TMP_DIR/result.txt" "$FINAL_FILE"
else
  echo "Invalid file, not moving."
  exit 1
fi


#  mktemp -d: creates a temp folder to be deleted using trap
# grep -q: search without printing anything (quiet mode)