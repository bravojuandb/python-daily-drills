"""
Drill 05 - Loop with Zip

Write a function:
    pair_students(students: list[str], grades: list[int]) -> list[str]

Requirements:
1. Use a `for` loop with `zip()`.
2. Each result item should look like `"Alice: 90 (pass)"` or `"Bob: 55 (fail)"`.
3. Assume both input lists have the same length.
4. Return the final list.
5. A grade of `60` or more is a pass.

Example:
>>> pair_students(["Alice", "Bob"], [90, 75])
['Alice: 90 (pass)', 'Bob: 75 (pass)']

Thinking goal:
This drill is about combining aligned inputs while making a fresh decision for each pair.
"""
