"""
Drill 06 - Append Log Entry

Write a function:
    append_log(path: str, message: str) -> None

Requirements:
1. Open the file in append mode.
2. Add the message as a new line at the end.
3. Preserve the existing file contents.
4. If `message` is empty, do not write anything.

Example:
If the file already contains:
start

And `message` is `"next"`, the file should become:
start
next

Thinking goal:
This drill is about the difference between extending a file and replacing it.
"""
