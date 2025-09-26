"""
Write a recursive function `factorial(n)`.

Rules:
1. If n == 0 or n == 1 → return 1  (base case).
2. Otherwise → return n * factorial(n-1).
3. Do NOT use loops, only recursion.

Example:
factorial(5) → 120
factorial(0) → 1

⚡ Solve it fast — under 2 minutes!
"""

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
    
print(factorial(5))
print(factorial(0))
