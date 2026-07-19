"""
Drill 04 - ID Lookup Index

Write index_by_id(records) -> dict[int, dict]. Each record contains an integer
"id". Build an index allowing direct lookup by ID. If an ID repeats, raise
ValueError. Do not mutate the records.

Example:
    records = [
        {"id": 7, "name": "Ada", "role": "engineer"},
        {"id": 12, "name": "Grace", "role": "admiral"},
        {"id": 3, "name": "Linus", "role": "engineer"},
    ]

    index_by_id(records) returns:
    {
        7: {"id": 7, "name": "Ada", "role": "engineer"},
        12: {"id": 12, "name": "Grace", "role": "admiral"},
        3: {"id": 3, "name": "Linus", "role": "engineer"},
    }

The resulting index makes a lookup such as result[12] direct. An empty input
returns an empty dictionary. If two records have the same ID, raise ValueError
instead of silently replacing the earlier record.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: use a dictionary when repeated lookup by a unique key dominates.
"""


def index_by_id(records: list[dict]) -> dict[int, dict]:
    result = {}

    for record in records:
        key = record["id"]

        if key in result:
            raise ValueError("Repeated ID")
        
        result[key] = record

    return result

