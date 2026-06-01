"""
Drill 04 - Generator Expression

Write:
    gen = ...

Requirements:
1. Create a generator expression that yields filenames from `files`.
2. Include only names that end with `.csv`, ignoring case.
3. Convert each yielded filename to lowercase.
4. The generator should produce values lazily.
5. If `files = ["README.md", "SALES.CSV", "users.csv", "notes.txt"]`, the first two generated values should be `"sales.csv"` and `"users.csv"`.

Example:
If `files = ["README.md", "SALES.CSV", "users.csv", "notes.txt"]`,
the full generator sequence should be:
"sales.csv", "users.csv"

Thinking goal:
This drill is about understanding that a generator is consumed over time, not built all at once.
"""
