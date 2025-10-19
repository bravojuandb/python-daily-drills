"""
🧩 Challenge: Nested Dict Access (safe `.get()`)

You are given nested dictionaries representing users and their profiles.  
Your task: write a function `safe_get(data: dict, path: list[str]) -> any`  
that safely retrieves a nested value without raising a `KeyError`.

Example:
profile = {
    "user": {
        "info": {
            "name": "Alice",
            "contacts": {"email": "alice@example.com"}
        }
    }
}

safe_get(profile, ["user", "info", "contacts", "email"])  ➜  "alice@example.com"
safe_get(profile, ["user", "preferences", "theme"])       ➜  None

Rules:
- Do *not* use try/except.
- Use `.get()` in a loop.
- Return `None` if any key in the path is missing.
- Do not mutate the original dictionary.

Be quick and precise — this access pattern appears constantly in ETL pipelines and JSON parsing.
"""

def safe_get(data: dict, path: list[str]) -> any:

    current = data
    for key in path:
        current = current.get(key) if isinstance(current, dict) else None
        if current is None:
            break
    return current
    

profile = {
    "user": {
        "info": {
            "name": "Alice",
            "contacts": {"email": "alice@example.com"}
        }
    }
}

print(safe_get(profile, ["user", "info", "contacts", "email"]))