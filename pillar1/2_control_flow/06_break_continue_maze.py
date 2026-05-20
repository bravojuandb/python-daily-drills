"""
Drill 06 - Break and Continue Maze

Write a function:
    first_affordable(price_tags: list[int], budget: int) -> int

Requirements:
1. Scan the prices from left to right.
2. Negative values represent broken tags and should be ignored.
3. Return the first usable price that does not exceed `budget`.
4. Stop searching as soon as you know the answer.
5. If no usable affordable price exists, return `-1`.
6. Use both `continue` and `break`.

Example:
>>> first_affordable([-5, 120, 80, 150], 100)
80

Thinking goal:
This drill is about deciding which values should be ignored, which value should end the search, and how to encode that control flow directly.
"""

def first_affordable(price_tags: list[int], budget: int) -> int:
    result = -1

    for price in price_tags:
        if price < 0:
            continue

        if price <= budget:
            result = price
            break

    return result


if __name__ == "__main__":
    print(first_affordable([-5, 120, 150], 100))