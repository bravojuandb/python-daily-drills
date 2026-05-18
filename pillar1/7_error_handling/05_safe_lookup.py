"""
Drill 05 - Safe Lookup

Write a function:
    lookup_price(prices: dict[str, int], item: str) -> int | str

Requirements:
1. Return the value for `item` if it exists.
2. If the key is missing, return `"Error: Unknown item"`.
3. Use `try` / `except KeyError`.

Example:
>>> lookup_price({"apple": 3, "banana": 2}, "apple")
3
>>> lookup_price({"apple": 3, "banana": 2}, "pear")
'Error: Unknown item'

Thinking goal:
This drill is about handling a missing key intentionally instead of assuming the data is always complete.
"""
