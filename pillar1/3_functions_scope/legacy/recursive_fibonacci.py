"""
Write a recursive function `fibonacci(n)`.

Rules:
1. The Fibonacci sequence starts with:
   F(0) = 0, F(1) = 1
2. For n > 1:
   F(n) = F(n-1) + F(n-2)
3. Use recursion (no loops).

Examples:
fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(5) → 5   # sequence is 0, 1, 1, 2, 3, 5
fibonacci(7) → 13

⚡ Be quick — under 2 minutes — and don’t forget the two base cases!
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
    

print(fibonacci(7))