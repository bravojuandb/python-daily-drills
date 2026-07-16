"""
Challenge — Optimize Nested Loops into Dict Lookup

You’re given two collections:

purchases = [
    {"order_id": 101, "sku": "A12", "qty": 2},
    {"order_id": 102, "sku": "B07", "qty": 1},
    {"order_id": 103, "sku": "X99", "qty": 5},   # note: not in price_list
    {"order_id": 104, "sku": "A12", "qty": 3},
]

price_list = [
    {"sku": "A12", "price": 9.50, "currency": "EUR"},
    {"sku": "B07", "price": 3.20, "currency": "EUR"},
]

A junior wrote an O(n·m) join:

result = []
for p in purchases:
    price = None
    for item in price_list:
        if item["sku"] == p["sku"]:
            price = item["price"]
            break
    result.append({**p, "unit_price": price})

Task:
1) Rewrite it in O(n + m) by building a dict index from price_list, then enriching purchases.
   - Preserve the original order of purchases.
   - If a SKU is missing in the index, set unit_price=None and add "note": "missing_sku".
2) Compute a "line_total" = qty * unit_price when unit_price is not None; else omit line_total.
3) Print the enriched rows, one per line, aligned like: order_id, sku, qty, unit_price, line_total (if present).
4) State the time complexity of your approach and why it’s better than the nested loops.

Bonus (optional, 5 minutes):
- Handle a second lookup table:
    discounts = [{"sku":"A12","pct":0.1}, {"sku":"B07","pct":0.05}]
  Apply discounted_total = line_total * (1 - pct) when both price and discount exist.
- Show a minimal micro-benchmark comparing the nested-loop version vs your dict-lookup version using time.perf_counter() on larger synthetic data.

Be quick and precise.
"""


purchases = [
    {"order_id": 101, "sku": "A12", "qty": 2},
    {"order_id": 102, "sku": "B07", "qty": 1},
    {"order_id": 103, "sku": "X99", "qty": 5},   # note: not in price_list
    {"order_id": 104, "sku": "A12", "qty": 3},
]

price_list = [
    {"sku": "A12", "price": 9.50, "currency": "EUR"},
    {"sku": "B07", "price": 3.20, "currency": "EUR"},
]

# A junior wrote an O(n·m) join:

result = []
for p in purchases:
    price = None
    for item in price_list:
        if item["sku"] == p["sku"]:
            price = item["price"]
            break
    result.append({**p, "unit_price": price})




def calculate_totals(purchases= list[dict], prices= list[dict]) -> list[dict]:

    # Create an index for price list
    price_index = {item["sku"]: item for item in prices}

    enriched = []
    for entry in purchases:
        price_item = price_index.get(entry["sku"]) # returns None when the key is missing

        if price_item:
            unit_price = price_item["price"]
            line_total = entry["qty"] * unit_price

            enriched.append({
                ** entry,
                "unit_price" : unit_price,
                "line_total" : round(line_total, 2),
            })

        else:
            enriched.append({
                **entry,
                "unit_price" : None,
                "note" : "missing_sku",
            })
    
    return enriched



result = calculate_totals(purchases, price_list)

for i in result:
    print(i)