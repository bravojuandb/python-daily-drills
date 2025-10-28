"""
Drill — Recursively Flatten Nested Dict *

You’re given a deeply nested dictionary that can contain other dictionaries inside.

ask:
Write a function `flatten_dict(data: dict, parent_key: str = "", sep: str = "_") -> dict`
that returns a **flattened version** of the nested dictionary:

{
    "user_name": "Alice",
    "user_address_city": "Madrid",
    "user_address_coords_lat": 40.4,
    "user_address_coords_lon": -3.7,
    "meta_active": True,
    "meta_roles": ["admin", "editor"]
}

Rules:
1. If a value is a dict → recurse deeper.
2. If a value is not a dict → include it directly in the flat result.
3. Combine parent and child keys using the `sep` (default `_`).
4. Skip empty dicts (don’t add blank keys).

⚡ Challenge:
Support arbitrarily deep nesting — your recursion should stop only when no dicts remain.

Aim: 15 minutes.
Be methodical — recursion + key concatenation = real-world ETL flattening pattern.
"""

nested = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Madrid",
            "coords": {"lat": 40.4, "lon": -3.7}
        }
    },
    "meta": {
        "active": True,
        "roles": ["admin", "editor"]
    }
}


test_one_level = {
    "user": {
        "name": "Alice",
    }
}

def flatten_dict(data: dict, parent_key: str = "", sep: str = "_") -> dict:

    result = {}

    for key, val in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(val, dict):
            child_flat = flatten_dict(val, new_key, sep=sep)
            result.update(child_flat)
        else:
            result[new_key] = val

    return result


for key, val in flatten_dict(nested).items():
    print(key, val)

