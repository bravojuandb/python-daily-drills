"""
# Pillar 2 — Applied Challenges
## Group Transactions by Customer (Quiz Scores Edition)

You are given a list of students:
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

Each student takes a random number of quizzes (between 5 and 10).
Each quiz score is a random number between 0 and 100.

TASK:
1. Generate the raw data as a list of (student, score) pairs — total of all quizzes.
2. Aggregate the scores into a dictionary where:
   - Key = student name
   - Value = average score across their quizzes

Example (values vary because of randomness):
{"Alice": 74.3, "Bob": 62.1, "Charlie": 88.0, "Diana": 70.5, "Eve": 91.2}

⏱️ Be quick and precise. Don’t overthink the random generation — focus on clean aggregation logic.
"""

import random
import statistics as stats


def raw_data_generator(
    students: list[str],
    *,
    min_quizzes: int = 5,
    max_quizzes: int = 10,
    min_score: int = 0,
    max_score: int = 100,
    seed: int | None = 42,
) -> list[tuple[str, int]]:
    """Create raw data: a list of (student, score) pairs."""
    rng = random.Random(seed) if seed is not None else random
    data: list[tuple[str, int]] = []

    for student in students:
        n_quizzes = rng.randint(min_quizzes, max_quizzes)
        for _ in range(n_quizzes):
            score = rng.randint(min_score, max_score)
            data.append((student, score))
    return data


def aggregate_sums_and_counts(
    pairs: list[tuple[str, int]]
) -> tuple[dict[str, int], dict[str, int]]:
    """Compute per-student sum and count using .get()."""
    sums: dict[str, int] = {}
    counts: dict[str, int] = {}

    for student, score in pairs:
        sums[student] = sums.get(student, 0) + score
        counts[student] = counts.get(student, 0) + 1

    return sums, counts


def averages_from_sums_counts(
    sums: dict[str, int], counts: dict[str, int], *, ndigits: int = 2
) -> dict[str, float]:
    """Compute rounded averages."""
    return {
        s: round(sums[s] / counts[s], ndigits) if counts[s] else float("nan")
        for s in sums
    }


if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    raw = raw_data_generator(students)
    sums, counts = aggregate_sums_and_counts(raw)
    avg = averages_from_sums_counts(sums, counts)

    print(avg)