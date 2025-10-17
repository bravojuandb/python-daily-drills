"""
Challenge: Remove Duplicates from a List using Sets

You are given a list of city names that may contain duplicates.  
Your task is to remove all duplicates efficiently — keeping only one instance of each unique element.

Example:
    cities = ["Madrid", "Paris", "Berlin", "Madrid", "Rome", "Berlin"]

Expected output:
    ["Madrid", "Paris", "Berlin", "Rome"]   # order may vary because sets are unordered

Rules:
- Use a `set` to eliminate duplicates in O(n) time.
- Optionally, convert it back to a list.
- Demonstrate what happens when you preserve the original order using a comprehension or `dict.fromkeys()`.

⚡️ Be quick and precise: 
1. Write a function `remove_duplicates(items: list[str]) -> list[str]`
2. Test it on a short list of repeated values.
3. Explain the difference between `set(items)` and `list(dict.fromkeys(items))`.
"""

# Output sorted alphabetically
def remove_duplicates(items: list[str]) -> list[str]:
    return sorted(list(set(items)))


# Output preserves original order, concise
def remove_duplicates(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


# Output preserves original order, comprehension
def remove_duplicates(items: list[str]) -> list[str]:
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]


cities = ["Madrid", "Paris", "Berlin", "Madrid", "Rome", "Berlin"]

print(remove_duplicates(cities))
