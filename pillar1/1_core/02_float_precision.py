"""
Drill 02 - Float Precision

Write a function:
    inspect_floats() -> dict[str, float | bool | int]

Requirements:
1. Compute `0.1 + 0.2` and store it under `"sum_result"`.
2. Compare that result to `0.3` and store the boolean under `"exact_match"`.
3. Round `2.675` to 2 decimal places and store it under `"rounded_2675"`.
4. Store `math.floor(-3.7)` under `"floor_neg"`.
5. Store `math.ceil(-3.7)` under `"ceil_neg"`.
6. Store `round(7.5)` under `"round_75"`.
7. Store `round(8.5)` under `"round_85"`.

Return all results in one dictionary.

Thinking goal:
This drill is about understanding that numeric output is not always intuitive.
It should make you explain, at least to yourself, why binary floats and rounding
can produce surprising results.
"""

import math


def inspect_floats() -> dict[str, float | bool | int]:
    sum_result = 0.1 + 0.2

    return {
        "sum_result": sum_result,
        "exact_match": sum_result == 0.3,
        "rounded_2675": round(2.675, 2),
        "floor_neg": math.floor(-3.7),
        "ceil_neg": math.ceil(-3.7),
        "round_75": round(7.5),
        "round_85": round(8.5),
    }


if __name__ == "__main__":
    for key, value in inspect_floats().items():
        print(f"{key}: {value}")
