"""
Problem — Grouping (partition + aggregate)

You’re given a dataset of sales transactions, where each record represents one purchase event, like this:

[
    {"id": 1, "customer": "Anna", "country": "Spain", "amount": 85.00, "status": "paid"},
    {"id": 2, "customer": "Dan", "country": "Italy", "amount": 120.40, "status": "paid"},
    {"id": 3, "customer": "Bob", "country": "Germany", "amount": 200.00, "status": "paid"},
    {"id": 4, "customer": "Iris", "country": "Italy", "amount": 40.20, "status": "refunded"},
    {"id": 5, "customer": "Frank", "country": "France", "amount": 150.00, "status": "refunded"},
    {"id": 6, "customer": "Hugo", "country": "Spain", "amount": 130.00, "status": "refunded"},
    {"id": 7, "customer": "Cara", "country": "Spain", "amount": 175.25, "status": "paid"},
    {"id": 8, "customer": "Eve", "country": "France", "amount": 320.75, "status": "paid"},
    {"id": 9, "customer": "Jack", "country": "France", "amount": 500.00, "status": "paid"}
]

Task:
1️⃣ Group transactions by "customer" and compute each customer’s total **paid** amount.
2️⃣ Print the results sorted by total amount (descending), e.g.:
    Jack — €500.00
    Cara — €300.00
    Frank — €210.75
    Anna — €120.50
    ...

Constraints:
- Include only transactions where `status == "paid"`.
- Skip zero, negative, or invalid amounts.
- Use a **dictionary accumulator** or `collections.defaultdict(float)` — one pass, no nested loops.
- Avoid external libraries like pandas.

Hints:
- Build totals dynamically:
    totals[cust] = totals.get(cust, 0.0) + amount
- Sort with:
    sorted(totals.items(), key=lambda x: x[1], reverse=True)

Bonus:
- Track the number of paid transactions per customer.
- Print both total and average per customer:
    Jack — total €500.00 (1 tx), avg €500.00
    Cara — total €300.00 (1 tx), avg €300.00
    Anna — total €120.50 (1 tx), avg €120.50

⏱ Aim to complete in 8–10 minutes.
"""

from pathlib import Path
import json

def read_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# Explicit, didactic approach, partition without aggregation

def accumulator(recs: list[dict]):
    """
    Accumulates amounts per customer without aggregating them.

    Arguments:
    List of dictionaries containing records of sales transactions

    Returns:
    Dictionary with customer as key, and a list of amounts as values
    """
    groups = {}
    for r in recs:
        customer = r["customer"]
        amount = r["amount"]
        if customer not in groups:
            groups[customer] = []
        groups[customer].append(amount)
    return groups

# Didactic approach, partition and aggregation in one pass, no external libraries

def reducer(recs: list[dict]):
    """
    Accumulates and aggregates amounts per customer in one pass
    """
    totals = {}
    for r in recs:
        customer = r["customer"]
        amount = r["amount"]
        totals[customer] = totals.get(customer, 0) + amount
    return totals



# Pythonic approach: partition and aggregation in one pass using defaultdict

# Trick: defaultdict --- "Whenever a key is accessed cal this ( function )..."

def group_by_customer(transactions: list[dict]) -> dict:
    """
    Group by 'customer' and sum all paid transaction amounts.
    """
    from collections import defaultdict

    totals = defaultdict(float)

    for tx in transactions:
        status = tx["status"]
        amount = tx["amount"]
        customer = tx["customer"]

        if status == 'paid' and amount > 0:
            totals[customer] += amount

    return dict(totals)

# Bonus: 

def group_by_customer_with_counts(transactions: list[dict]) -> dict[str, dict]:
    """
    Group by 'customer' and compute both total and average.
    """
    from collections import defaultdict

    grouped = defaultdict(lambda: {"total": 0.0, "count": 0})

    for tx in transactions:
        if tx["status"] == "paid" and tx["amount"] > 0:
            cust = tx["customer"]
            grouped[cust]["total"] += tx["amount"]
            grouped[cust]["count"] += 1

    # compute averages
    for cust, data in grouped.items():
        total, count = data["total"], data["count"]
        data["avg"] = round(total / count, 2) if count else 0

    return dict(grouped)


if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent / "sales_transactions.json"
    file = read_json(FILE_PATH)

data= group_by_customer_with_counts(file)

for k, v in data.items():
    print(k, v)
