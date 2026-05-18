"""
Drill 04 - Generator Expression

Write:
    gen = ...

Requirements:
1. Create a generator expression that yields cubes from `1` to `10`.
2. Exclude numbers divisible by `3`.
3. The generator should produce values lazily.
4. After creating it, the first two generated values should be `1` and `8`.

Example:
The full generator sequence should be:
1, 8, 64, 125, 343, 512, 1000

Thinking goal:
This drill is about understanding that a generator is consumed over time, not built all at once.
"""
