"""
Drill 05 - Lambda One-Liner

Write:
    transform = lambda x: ...

Requirements:
1. Use a single lambda expression.
2. If `x` is even, return `x * x`.
3. If `x` is odd, return `x` unchanged.
4. Then map `transform` over `[1, 2, 3, 4, 5]` and convert the result to a list.

Example:
>>> list(map(transform, [1, 2, 3, 4, 5]))
[1, 4, 3, 16, 5]

Thinking goal:
This drill is about keeping a tiny conditional transformation compact without making it mysterious.
"""
