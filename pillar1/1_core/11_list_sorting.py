"""
Drill 11 - List Sorting

Write a function:
    compare_sorts(prices: list[int]) -> tuple[list[int], list[int]]

Requirements:
1. Create one ascending version using in-place sorting on a copy.
2. Create one descending version using `sorted()`.
3. Do not mutate the original input list.
4. Return `(ascending, descending)`.

Example:
>>> compare_sorts([199, 49, 350, 120, 75])
([49, 75, 120, 199, 350], [350, 199, 120, 75, 49])

Thinking goal:
This drill makes you distinguish mutation from non-mutation, which matters a lot later.
"""

def compare_sorts(prices: list[int]) -> tuple[list[int],  list[int]]:

    ascending = prices.copy()
    ascending.sort()

    descending = sorted(prices, reverse=True)

    return ascending, descending

if __name__ == "__main__":

    print(compare_sorts([199, 49, 350, 120, 75]))    