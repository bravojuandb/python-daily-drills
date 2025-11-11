"""
Turing-style problem — Grouping (partition + aggregate)

You’re given a dataset of sales transactions, where each record represents one purchase event:

[
    {"id": 1, "customer": "Anna", "country": "Spain", "amount": 120.50, "status": "paid"},
    {"id": 2, "customer": "Bob", "country": "Germany", "amount": 80.00, "status": "refunded"},
    {"id": 3, "customer": "Cara", "country": "Spain", "amount": 300.00, "status": "paid"},
    {"id": 4, "customer": "Dan", "country": "Italy", "amount": 50.00, "status": "paid"},
    {"id": 5, "customer": "Eve", "country": "France", "amount": 0.00, "status": "pending"},
    {"id": 6, "customer": "Frank", "country": "France", "amount": 210.75, "status": "paid"},
    {"id": 7, "customer": "Gina", "country": "Germany", "amount": 95.60, "status": "paid"},
    {"id": 8, "customer": "Hugo", "country": "Spain", "amount": 150.00, "status": "paid"},
    {"id": 9, "customer": "Iris", "country": "Italy", "amount": 40.20, "status": "refunded"},
    {"id": 10, "customer": "Jack", "country": "France", "amount": 500.00, "status": "paid"}
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
    




if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent / "sales_transactions.json"
    file = read_json(FILE_PATH)

    for rec in file:
        print(rec)
