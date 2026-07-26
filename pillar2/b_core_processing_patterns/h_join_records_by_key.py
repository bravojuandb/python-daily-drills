"""
Drill 08 - Join Records by Key

Write enrich_orders(orders, products) -> list[dict]. Build a product index by
"sku", then return new order dictionaries containing "unit_price". Use None for
unknown SKUs. Preserve order order and avoid nested loops.

Target complexity: O(n + m) time for n orders and m products.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: an indexed join replaces repeated scans with direct lookup.
"""


def enrich_orders(orders: list[dict], products: list[dict]) -> list[dict]:
    pass
