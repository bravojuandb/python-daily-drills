"""
Drill 05 - Merge Records with Conflict Rules

Write merge_users(base, updates) -> tuple[list[dict], int]. Email identifies a
user case-insensitively. Valid update records replace matching base records;
new users append. Preserve first-seen email order. Skip missing/blank emails and
return the number skipped. Do not mutate either input list or its dictionaries.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: make identity, precedence, order, copying, and error policy explicit.
"""


def merge_users(
    base: list[dict], updates: list[dict]
) -> tuple[list[dict], int]:
    pass
