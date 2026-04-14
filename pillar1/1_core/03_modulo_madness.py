"""
Drill 03 - Modulo Madness

Write a function:
    classify_remainders(values: list[int], divisor: int) -> dict[str, list[int]]

Requirements:
1. If `divisor == 0`, raise `ValueError`.
2. Build and return a dictionary with three keys:
   - "zero_remainder": numbers divisible by `divisor`
   - "positive_remainder": numbers whose `n % divisor` is greater than 0
   - "negative_remainder": numbers whose `n % divisor` is less than 0
3. Preserve the original order inside each list.

Example:
>>> classify_remainders([10, 11, 12, 13], 2)
{
    "zero_remainder": [10, 12],
    "positive_remainder": [11, 13],
    "negative_remainder": [],
}

Thinking goal:
This drill forces you to look at modulo as more than a divisibility trick.
It helps you notice how remainder signs behave.
"""
