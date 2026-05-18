"""
Challenge 01 - Tag and Filter Scores

Write a function:
    tag_scores(scores: list[int]) -> list[str]

Requirements:
1. Loop through the scores in order.
2. Skip any negative score.
3. For each remaining score:
   - use `"pass"` if the score is `60` or more
   - use `"fail"` otherwise
4. Return strings like `"75: pass"` in the original order.
5. Do not use a comprehension.

Example:
>>> tag_scores([80, -1, 55, 60])
['80: pass', '55: fail', '60: pass']

Thinking goal:
This challenge mixes filtering, branching, and ordered result-building in one small loop.
"""
