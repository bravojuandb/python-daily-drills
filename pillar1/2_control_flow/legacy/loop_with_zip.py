"""
Write a function `pair_students(students: list[str], grades: list[int]) -> list[str]`.

Rules:
- Use a `for` loop with `zip()`.
- Each element in the result should look like: "Alice: 90".
- Assume both lists have the same length.

Example:
students = ["Alice", "Bob", "Charlie"]
grades = [90, 75, 82]

pair_students(students, grades) → ["Alice: 90", "Bob: 75", "Charlie: 82"]

Try to solve it quickly — under 90 seconds!
"""

def pair_students(students: list[str], grades: list[int]) -> list[str]:

    if len(students) == len(grades):
        print("Let's proceed to zipping.")
    else:
        print("Incompatible lists")
    result = []
    for student, grade in zip(students, grades):
        result.append(f"{student}: {grade}")
    return result


students = ["Alice", "Bob", "Charlie"]
grades = [90, 75, 82]

print(pair_students(students, grades))


