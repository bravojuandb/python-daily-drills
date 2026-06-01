"""
Drill 01 - List Comprehension Transformation

Write a function:
    clean_tags(tags: list[str]) -> list[str]

Requirements:
1. Use one list comprehension.
2. Strip surrounding whitespace from each tag.
3. Convert each cleaned tag to lowercase.
4. Skip any tag that becomes empty after stripping.
5. Keep duplicates if the same normalized tag appears more than once.

Example:
>>> clean_tags(["  Python ", "", " Data ", "PYTHON", "   "])
['python', 'data', 'python']

Thinking goal:
This drill is about using one readable comprehension to clean user input in a way that feels realistic.
"""

def clean_tags(tags: list[str]) -> list[str]:

    return [tag.strip().lower() for tag in tags if tag.strip()]


if __name__ == "__main__":

    raw_tags = [
        "  Python ",
        "SQL",
        " data engineering ",
        "ETL",
        "etl ",
        " Airflow ",
        " logging ",
        "Testing",
        " testing ",
        "CI/CD",
        " ci/cd ",
        "Linux",
        " linux ",
        " Bash ",
        "bash",
        "  "
    ]

    print(clean_tags(raw_tags))