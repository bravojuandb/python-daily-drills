"""
Drill 04 - Customer Transaction Summary

Each transaction contains customer, status, and amount. Keep paid positive
numeric amounts and return a dictionary per normalized customer containing
"total", "count", and "average". Skip malformed records without stopping.

Round averages to two decimals only after aggregation. Process input once.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: validate and maintain multiple accumulators per grouping key.
"""


def summarize_customers(transactions: list[dict]) -> dict[str, dict]:
    pass
