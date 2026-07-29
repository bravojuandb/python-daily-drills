"""
Drill 03 - Reduce Transaction Totals

Write total_paid(transactions) -> float. Sum numeric "amount" values only when
"status" is "paid". Ignore other statuses. An empty input returns 0.0. Complete
the reduction in one pass without constructing a second list.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: reduction turns many values into one accumulated result.
"""


def total_paid(transactions: list[dict]) -> float:
    result = 0
    for t in transactions:
        if t["status"] == "paid":
            result += float(t["amount"])
            
    return float(result)

# Time: O(n), because each transaction is examined once.
# Extra space: O(1), because only one running total is stored - it usese only one accumulator
# A one-pass reduction fits because many transaction amounts are accumulated 
# into one result without creating another collection.