"""
Drill 07 - Streaming Monthly CSV Totals

Write aggregate_monthly(lines) -> tuple[list[str], int]. Manually parse rows
customer_id,date,amount,status. Skip headers, comments, and blanks. PAID adds and
REFUND subtracts. Invalid shape/date/amount/status increments errors.

Aggregate by (customer, YYYY-MM) while consuming lines once. Return deterministic
CSV rows sorted by customer then month with totals formatted to two decimals.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: combine streaming validation, composite keys, reduction, and output.
"""

from collections.abc import Iterable


def aggregate_monthly(lines: Iterable[str]) -> tuple[list[str], int]:
    pass
