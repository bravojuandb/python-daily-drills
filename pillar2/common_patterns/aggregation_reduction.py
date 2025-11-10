"""
Aggregation (Reduction)

You’re given a JSON-like list of sales records called `sales_transactions`, 
where each item represents one purchase event made by a customer.

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
1️⃣ Compute the **total revenue** (sum of `amount`) considering only `status == "paid"`.
2️⃣ Compute the **average purchase value** for paid transactions.
3️⃣ Print results in this format:
    Paid transactions: 7
    Total revenue: €1,426.85
    Average ticket: €203.84

Bonus:
- Ignore invalid or missing `amount` fields (e.g., None or negative values).
- Do it in a **single pass** (one loop or comprehension).
- Round to two decimals with `round(value, 2)` or formatted f-string.
- Keep country statistics optional (extra challenge below).

Optional extension:
Group totals **per country** (Spain, Germany, France, Italy) and print like:
    Spain — €570.50
    Germany — €175.60
    France — €710.75
    Italy — €90.20

"""
import json
from pathlib import Path


def read_file(file_path: Path) -> list[dict[str, str]]:

    with open(file_path, encoding="UTF-8") as f:
        return json.load(f)

def aggregate_records(records: list[dict[str, str]]):
    
    rows = [
        row for row in records if 
        row["status"] == "paid" and 
        float(row["amount"]) > 0
        ]
    paid_amounts = [row["amount"] for row in records]
    
    total = sum(paid_amounts)

    mean = total / len(paid_amounts if paid_amounts else 0)

    print(f"""
        Paid transactions: {len(paid_amounts)}\n 
        Total revenue: {round(total, 2)}\n
        Average ticket: {round(mean, 2)}\n """
    )


BASE_PATH = Path(__file__).parent
FILE_PATH = BASE_PATH / "sales_transactions.json"


if __name__ == "__main__":
    file = read_file(FILE_PATH)
    aggr = aggregate_records(file)
    print(aggr)