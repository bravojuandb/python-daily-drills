"""
Group Transactions by Customer — using dict of lists

You receive a list of transactions, each represented as a tuple:

    (customer_id, date, amount)

Goal:
Group all transactions belonging to the same customer into a dictionary 
where each key is a `customer_id`, and each value is a list of their transactions.

Rules:
- Keep the order of transactions as they appear.
- Do not mutate the original list.
- Use either `dict.setdefault()` or `collections.defaultdict(list)`.
- O(n) time, O(k) space — one pass over the list.

Example Input:
transactions = [
    ("C-001", "2025-01-03", 100.00),
    ("C-002", "2025-01-09", 300.00),
    ("C-001", "2025-01-18", 25.50),
    ("C-002", "2025-01-11", 20.00),
]

Expected Output:
{
    "C-001": [
        ("C-001", "2025-01-03", 100.00),
        ("C-001", "2025-01-18", 25.50)
    ],
    "C-002": [
        ("C-002", "2025-01-09", 300.00),
        ("C-002", "2025-01-11", 20.00)
    ]
}

Stretch:
- Sort each customer’s list by date or amount.
- Add a summary dict with total per customer.
- Return both grouped transactions and summary totals.

Be quick and precise — this pattern underpins grouping in ETL, pandas `.groupby()`,
and SQL `GROUP BY` clauses.
"""

transactions = [
    ("C-001", "2025-01-03", 100.00),
    ("C-002", "2025-01-09", 300.00),
    ("C-001", "2025-01-18", 25.50),
    ("C-002", "2025-01-11", 20.00),
]

def group_transactions(
        trs: list[tuple[str, str, float]]) -> dict[
            list[tuple[str, str, float]]]:

    grouped = {}
    for transaction in trs:
        customer_id  = transaction[0]
        grouped.setdefault(customer_id, []).append(transaction)

    return grouped

for customer, txs in group_transactions(transactions).items():
    print(f"{customer}: {txs}")