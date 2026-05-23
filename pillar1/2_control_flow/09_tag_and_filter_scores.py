"""
Drill 09 - Tag and Filter Scores

Write a function:
    tag_scores(scores: list[int]) -> list[str]

Requirements:
1. Loop through the scores in order.
2. Negative values are invalid and should not appear in the output.
3. For each valid score, return a label string that keeps both the score and its status.
4. Use `"pass"` for scores `60` or above and `"fail"` otherwise.
5. Preserve the original order of valid scores.
6. Do not use a comprehension.

Example:
>>> tag_scores([80, -1, 55, 60])
['80: pass', '55: fail', '60: pass']

Thinking goal:
This drill mixes filtering, branching, and ordered result-building in one loop without spelling out every line of the solution for you.
"""

def tag_scores(scores: list[int]) -> list[str]:
    result = []

    for score in scores:
        if score < 0:
            continue
        
        if score >= 60:
            label = "pass"
        else:
            label = "fail"
        result.append(f"{score}: {label}")

    return result


if __name__ == "__main__":
    print(tag_scores([80, -1, 55, 60]))
