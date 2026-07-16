"""
Problem: Aggregating Totals

You are given a list of (category, amount) pairs, like sales transactions.  
Write a function `aggregate_totals(data)` that returns a dictionary  
where each category key has the total sum of all its amounts.

Rules:
- Use a loop or comprehension with `sum()`.
- Do not use pandas or external libs.
- Group by the category key efficiently.

Example:
    Input:
        [
            ("fruit", 10),
            ("vegetable", 5),
            ("fruit", 4),
            ("dairy", 6),
            ("fruit", 1)
        ]
    Output:
        {"fruit": 15, "vegetable": 5, "dairy": 6}

Hint:
- You may use a dictionary accumulation pattern like:
      totals[key] = totals.get(key, 0) + value

Be quick and precise — this logic powers aggregations, metrics, and rollups in ETL pipelines.
"""


def aggregate_total(sales: list[tuple[str, int]]) -> dict[str, int]:

    totals = {}
    for category, amount in sales:
        totals[category] = totals.get(category, 0) + amount

    return totals


sales = [
    ("fruit", 10),
    ("vegetable", 5),
    ("fruit", 4),
    ("dairy", 6),
    ("fruit", 1)
]

print(aggregate_total(sales))