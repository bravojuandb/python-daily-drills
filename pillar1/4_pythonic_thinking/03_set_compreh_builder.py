"""
Drill 03 - Set Comprehension Builder

Write a function:
    collect_extensions(filenames: list[str]) -> set[str]

Requirements:
1. Use one set comprehension.
2. Include only filenames that contain a dot.
3. Store the file extension in lowercase without the leading dot.
4. Duplicates should disappear naturally.

Example:
>>> collect_extensions(["report.PDF", "photo.jpg", "archive.zip", "notes.txt", "logo.JPG"])
{'pdf', 'jpg', 'zip', 'txt'}

Thinking goal:
This drill is about letting the data structure do part of the work instead of duplicating effort.
"""
