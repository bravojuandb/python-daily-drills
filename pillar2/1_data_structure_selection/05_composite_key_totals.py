"""
Drill 05 - Composite-Key Totals

Each sale is (store, product, amount). Write aggregate_sales(sales) returning a
dictionary keyed by (store, product) tuples with summed amounts.

Example: [("north", "pen", 2), ("north", "pen", 3)] becomes
{("north", "pen"): 5}. Process the input in one pass.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: use a hashable tuple when a lookup key has multiple components.
"""


def aggregate_sales(
    sales: list[tuple[str, str, int]],
) -> dict[tuple[str, str], int]:
    pass
