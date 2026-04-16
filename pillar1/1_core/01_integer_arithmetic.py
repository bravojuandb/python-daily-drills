"""
Drill 01 - Integer Arithmetic

Write a function:
    summarize_transaction(a: int, b: int) -> dict[str, int | float | None]

Scenario:
You are checking two integer values from a tiny ledger entry.

Requirements:
1. Return a dictionary with these keys:
   - "sum"
   - "difference"
   - "product"
   - "quotient"
   - "floor_division"
   - "remainder"
   - "power_ab"
2. Use `a` as the left operand and `b` as the right operand.
3. If `b == 0`, do not crash:
   - set "quotient" to `None`
   - set "floor_division" to `None`
   - set "remainder" to `None`
4. Keep the power operation as `a ** b`.

Example:
>>> summarize_transaction(10, 3)
{
    "sum": 13,
    "difference": 7,
    "product": 30,
    "quotient": 3.3333333333333335,
    "floor_division": 3,
    "remainder": 1,
    "power_ab": 1000,
}

Thinking goal:
This is not just operator recall. The drill tests whether you can apply the right
operator, preserve operand order, and handle an edge case cleanly.
"""

def summarize_transaction(a: int, b: int) -> dict[str, int | float | None]:
    transactions = {}

    transactions["sum"] = a + b
    transactions["difference"] = a - b
    transactions["product"] = a * b

    if b == 0:
        transactions["quotient"] = None
        transactions["floor_division"] = None
        transactions["remainder"] = None
    else:
        transactions["quotient"] = a / b
        transactions["floor_division"] = a // b
        transactions["remainder"] = a % b

    transactions["power_ab"] = a ** b

    return transactions

# -------- TESTS ------------------------------

assert summarize_transaction(10, 3) == {
    "sum": 13,
    "difference": 7,
    "product": 30,
    "quotient": 10 / 3,
    "floor_division": 3,
    "remainder": 1,
    "power_ab": 1000,
}

assert summarize_transaction(12, 0) == {
    "sum": 12,
    "difference": 12,
    "product": 0,
    "quotient": None,
    "floor_division": None,
    "remainder": None,
    "power_ab": 1,
}

assert summarize_transaction(-7, 3) == {
    "sum": -4,
    "difference": -10,
    "product": -21,
    "quotient": -7 / 3,
    "floor_division": -3,
    "remainder": 2,
    "power_ab": -343,
}

assert summarize_transaction(-7, -3) == {
    "sum": -10,
    "difference": -4,
    "product": 21,
    "quotient": -7 / -3,
    "floor_division": 2,
    "remainder": -1,
    "power_ab": -0.0029154518950437317,
}
