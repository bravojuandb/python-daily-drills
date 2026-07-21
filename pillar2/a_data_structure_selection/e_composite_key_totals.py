"""
Drill 05 - Composite-Key Totals

Each sale is (store, product, amount). Write aggregate_sales(sales) returning a
dictionary keyed by (store, product) tuples with summed amounts.

Example:
    sales = [
        ("north", "pen", 2),
        ("south", "pen", 4),
        ("north", "notebook", 3),
        ("north", "pen", 5),
        ("south", "pen", 1),
    ]

    aggregate_sales(sales) returns:
    {
        ("north", "pen"): 7,
        ("south", "pen"): 5,
        ("north", "notebook"): 3,
    }

Sales are combined only when both the store and product match. An empty input
returns an empty dictionary. Process the input in one pass.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: use a hashable tuple when a lookup key has multiple components.
"""


def aggregate_sales(
    sales: list[tuple[str, str, int]],
) -> dict[tuple[str, str], int]:
    result = {}

    for store, item, amount in sales:
        key = store, item
        result[key] = result.get(key, 0) + amount

    return result

# Worst-case time: O(n), assuming average O(1) dictionary access for each sale.
# Worst-case extra space: O(k), where k is the number of distinct store-product pairs.
# The main cost is processing all n sales once, while a dictionary with hashable
# (store, product) tuple keys efficiently finds and updates each pair's total.