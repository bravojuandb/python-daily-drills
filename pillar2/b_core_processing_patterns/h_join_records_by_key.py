"""
Drill 08 - Join Records by Key

Write enrich_orders(orders, products) -> list[dict].

Each order is a dictionary containing a "sku" key. Each product is a dictionary
containing "sku" and "unit_price" keys.

Return a new list in which every order is copied and enriched with the matching
product's "unit_price". If an order's SKU is not present in products, set its
"unit_price" to None.

Requirements:
- Preserve the original order of the orders.
- Do not mutate the input lists or dictionaries.
- Build a product index keyed by "sku" and use direct lookups; do not use nested
  loops.
- If products contains the same SKU more than once, the last product wins.

Target complexity: O(n + m) time for n orders and m products.

Complexity check:
State the extra-space Big-O. In one sentence, explain why building an index
avoids repeatedly scanning products for every order.

Thinking goal: an indexed join replaces repeated scans with direct lookup.
"""


def enrich_orders(orders: list[dict], products: list[dict]) -> list[dict]:
    result = []
    sku_to_price = {}

    for product in products:
        prod = product["sku"]
        price = product["unit_price"]

        sku_to_price[prod] = price

    for order in orders:
        sku = order["sku"]
        order_copy = order.copy()

        order_copy["unit_price"] = sku_to_price.get(sku)
        result.append(order_copy)

    return result


# Time: O(n + m) on average, because products and orders are each processed
# once, with average O(1) dictionary operations.
# Extra space: O(n + m), because the result stores n copied orders and the
# product index may store m distinct SKUs.