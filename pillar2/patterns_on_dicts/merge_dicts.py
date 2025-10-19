"""
You are given two dictionaries that may share some keys:

dict_a = {"apples": 10, "bananas": 5, "pears": 7}
dict_b = {"bananas": 3, "pears": 9, "oranges": 4}

Write a function `merge_dicts_with_rules(a: dict[str, int], b: dict[str, int]) -> dict[str, int]`
that merges both dictionaries according to these rules:

1. If a key appears **only in one dict**, keep it as-is.
2. If a key appears **in both**, combine the values using a rule:
      - for this drill, let’s say the rule is: **take the maximum** of both values.
3. The function should not mutate either input dictionary.

Expected output for the example above:
{
    "apples": 10,
    "bananas": 5,   # max(5, 3)
    "pears": 9,     # max(7, 9)
    "oranges": 4
}

Be quick and precise — this logic underlies how data engineers resolve conflicts when merging datasets.
"""

def merge_dicts_with_rules_loop(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    merged = {}
    for k in a.keys() | b.keys(): # Looping over a set containing all keys
        merged[k] = max(a.get(k, 0), b.get(k, 0))
    return merged


# Single line version
def merge_dicts_with_rules_comp(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    merged = {}
    return {k: max(a.get(k, 0), b.get(k, 0)) for k in a.keys() | b.keys()}


dict_a = {"apples": 10, "bananas": 5, "pears": 7}
dict_b = {"bananas": 3, "pears": 9, "oranges": 4}

print(merge_dicts_with_rules_comp(dict_a, dict_b))