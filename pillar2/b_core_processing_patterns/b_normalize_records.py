"""
Drill 02 - Normalize Records

Write normalize_users(records) -> list[dict[str, str]]. For every record, strip
and title-case "name", strip and lowercase "email", and uppercase "country".
Return the same number of records in the same order using new dictionaries.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: mapping preserves cardinality while changing representation.
"""


def normalize_users(records: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []

    for record in records:
        norm_record = {}

        norm_record["name"] = record.get("name").strip().title()
        norm_record["email"] = record.get("email").strip().lower()
        norm_record["country"] = record.get("country").strip().upper()
        normalized.append(norm_record)

    return normalized

