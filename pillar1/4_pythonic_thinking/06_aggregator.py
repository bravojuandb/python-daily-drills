"""
Drill 06 - Aggregator

Write a function:
    analyze_sales(sales: list[int]) -> tuple[int, int, int]

Requirements:
1. Use built-ins to compute the total sum, minimum, and maximum.
2. Return them as `(total, minimum, maximum)`.
3. If the input list is empty, raise `ValueError`.

Example:
>>> analyze_sales([120, 85, 210, 95, 160])
(670, 85, 210)

Thinking goal:
This drill is about reaching for a direct built-in when the question is already built into Python.
"""

def analyze_temps(temps: list[int]) -> tuple[int, int, int]:
    if not temps:
        raise ValueError ("The list is empty")
    return sum(temps), min(temps), max(temps)

if __name__ == "__main__":
    temperatures =[15, 22, 18, 30, 25, 19, 17]
    print(analyze_temps(temperatures))
