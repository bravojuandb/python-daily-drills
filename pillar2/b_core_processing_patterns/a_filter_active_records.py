"""
Drill 01 - Filter Active Records

Write filter_active(records) -> list[dict]. Keep records whose "status" equals
"active" case-insensitively. Missing status is inactive. Preserve input order
and do not mutate the input records.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: filtering may reduce collection size without changing each item.
"""


def filter_active(records: list[dict]) -> list[dict]:
    result = []
    for record in records:
        if record.get("status", "").strip().lower() == "active":
            result.append(record)
    return result

# Worst-case time: O(n), because each record is checked once.
# Worst-case extra space: O(n), because every record may enter the result list.
# A list preserves input order and allows duplicate records.
