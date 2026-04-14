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
