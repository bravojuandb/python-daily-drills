"""
Drill 08 - ETL Capstone

Write run_etl(rows) -> dict[str, list[dict]]. Each row may contain customer,
country, amount, currency, and status. Normalize text, accept only paid EUR rows
with positive numeric amounts, and count rejected rows by reason.

Return {"summary": [...], "errors": [{"reason": ..., "row": ...}]}. Summary
contains country, total, customers, and average, ordered by total descending then
country ascending. Customer identity is case-insensitive. Do not mutate rows.

State the time and auxiliary-space complexity in comments after solving.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: design clear validation, transformation, aggregation, and reporting stages.
"""


def run_etl(rows: list[dict]) -> dict[str, list[dict]]:
    pass
