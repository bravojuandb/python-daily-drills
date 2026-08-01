"""
Drill 06 - Build an Index

Write index_prices(products) -> dict[str, float]. Map each "sku" to its numeric
"price". If a SKU repeats, the later record wins. Do not mutate products.

Then explain in a comment why repeated lookup is faster in the returned index
than repeatedly scanning the product list.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: pay O(n) once to enable average O(1) keyed lookups.
"""


def index_prices(products: list[dict]) -> dict[str, float]:
    result = {}
    for product in products:
        result[product["sku"]] = product["price"]
    return result


# Time: O(n) because the for loop processes each product once,
# and each dictionary insertion or update is O(1) in average.
# Space: O(n) since adding new SKUs produces an index of n entries.
# A dictionary is a good choice because it allows unique keys,
# and repeated SKUs overwrite earlier prices.