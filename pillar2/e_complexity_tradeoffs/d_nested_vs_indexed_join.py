"""
Drill 04 - Nested versus Indexed Join

Implement nested_join(orders, products) and indexed_join(orders, products).
Both return (order_id, price_or_none) in order order. The first scans products
for every order; the second builds one SKU dictionary first.

State each time complexity for n orders and m products. Verify both functions
return identical output, including missing SKUs.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: recognize when preprocessing removes a multiplicative scan.
"""

from __future__ import annotations


def nested_join(
    orders: list[dict], products: list[dict]
) -> list[tuple[int, float | None]]:
    pass


def indexed_join(
    orders: list[dict], products: list[dict]
) -> list[tuple[int, float | None]]:
    pass
