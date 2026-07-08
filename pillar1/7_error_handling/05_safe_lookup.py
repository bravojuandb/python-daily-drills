"""
Drill 05 - Safe Lookup

Write a function:
    lookup_price(prices: dict[str, int], item: str) -> int | str

Requirements:
1. Return the value for `item` if it exists.
2. If the key is missing, return `"Error: Unknown item"`.
3. Use `try` / `except KeyError`.

Example:
>>> prices = {
...     "apple": 3,
...     "banana": 2,
...     "orange": 4,
...     "mango": 6,
...     "blueberries": 8,
... }
>>> lookup_price(prices, "mango")
6
>>> lookup_price(prices, "pear")
'Error: Unknown item'

Thinking goal:
This drill is about handling a missing key intentionally instead of assuming the data is always complete.
"""


def lookup_price(prices: dict[str, int], item: str) -> int | str:
    try:
        return prices[item]
    except KeyError:
        return "Error: Unknown item"


if __name__ == "__main__":

    prices = {
        "apple": 3,
        "banana": 2,
        "orange": 4,
        "mango": 6,
        "blueberries": 8
    }

    print(lookup_price(prices, "pear"))
