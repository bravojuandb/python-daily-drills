"""
Drill 05 - Loop with Zip

Write a function:
    pair_students(students: list[str], grades: list[int]) -> list[str]

Requirements:
1. Use a `for` loop with `zip()`.
2. Return one status string per student, in the original order.
3. Use `"pass"` for grades `60` or above and `"fail"` otherwise.
4. Keep the grade visible in the returned text.
5. Assume both input lists have the same length.

Example:
>>> pair_students(["Alice", "Bob"], [90, 75])
['Alice: 90 (pass)', 'Bob: 75 (pass)']
>>> pair_students(["Alice", "Bob"], [90, 55])
['Alice: 90 (pass)', 'Bob: 55 (fail)']

Thinking goal:
This drill is about combining aligned inputs while deciding the output format from a rule instead of copying one fixed case.
"""

def pair_students(students: list[str], grades: list[int]) -> list[str]:
    passed = []
    for key, val in zip(students, grades):
        if val >= 60:
            passed.append(f"{key}: {val} (pass)")
        else:
            passed.append(f"{key}: {val} (fail)")
    return passed

if __name__ == "__main__":
    print(pair_students(["Alice", "Bob", "Rob"], [90, 75, 30]))
