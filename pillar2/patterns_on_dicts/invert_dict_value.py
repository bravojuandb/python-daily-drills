"""
You are given a dictionary that maps keys to values, for example:

grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}

Write a function `invert_dict(d: dict[str, str]) -> dict[str, list[str]]`
that **inverts** the mapping so that each *value* becomes a *key*, and 
each *key* that shared that value becomes part of a list.

Expected output:
{
    "A": ["Alice", "Charlie"],
    "B": ["Bob"]
}

Rules:
- If multiple keys share the same value, group them in a list.
- Preserve insertion order.
- Use either `.setdefault()` or `defaultdict(list)` to make it efficient.
- Do not mutate the original dictionary.

Be quick and precise — this pattern is crucial when reversing lookup tables or 
re-indexing datasets in ETL pipelines.
"""



def invert_dict(a: dict[str, str]) -> dict[str, list[str]]:
    result = {}
    for k, v in a.items():
        result.setdefault(v, []).append(k)
    return result

grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}

print(invert_dict(grades))