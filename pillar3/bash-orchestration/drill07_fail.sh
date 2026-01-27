
#External commands & failure
#
# Goals
# Learn how scripts fail correctly. 
#
# Tasks
# - Use `curl` to download a small file
# - Add `set -e`
# - Force a failing URL and observe behavior
#
# Outcome
# - You know why pipelines must fail fast
# - You understand exit codes

#! usr/bin/env bash
set -euo pipefail 

echo "Trying valid download..."
curl -sf -o example.txt https://www.example.com 
echo "Valid download completed."

echo "Trying an invalid download..."
curl -sf -o does_not_exist.txt https://www.example.com/nonexistent-file.txt
echo "You should not see this message (if set -e works)"



# Curl + non-existent content: returns HTML content
# If -s (silent output): hides the default progress meter (download stats)
# echo $?: shows the exit code of the last command ( = 0: success, != 0: error)
# set -e: the first command that returns a non-zero exit code will stop the whole script
# curl does not treat HTTP errors as failure. It will exit with 0 if -f is not used
# if -f (fail on HTTP): makes curl exit with a non-zero code on HTTP errors (like 404 or 500)