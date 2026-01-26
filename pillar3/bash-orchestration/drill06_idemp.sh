#! usr/bin/env bash

# Idempotency with files
#
# Goals
# Make scripts safe to re-run.
# 
# Tasks
# - Write a script that:
#   - Creates a file
#   - Skips creation if the file already exists
# - Run it twice
#
# Outcome
# - You understand idempotent behavior
# - You can explain “safe re-runs”

MOCK_FILE="output.txt"

# If file exists... 
if [[ -f "$MOCK_FILE" ]]; then
  echo "File '$MOCK_FILE' already exists. Skipping creation."
else
  echo "Creating file '$MOCK_FILE'..."
  echo "This is a generated file." > "$MOCK_FILE"
fi