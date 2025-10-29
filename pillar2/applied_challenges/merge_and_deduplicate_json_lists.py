"""
Drill — Merge and Deduplicate JSON-like Lists *

You are given two JSON-like lists of "user" records. Each record is a dict.

Goal: 
Write a function merge_users(a: list[dict], b: list[dict]) -> list[dict]
that returns ONE merged list of users with NO duplicates.

Rules:
1. Two records represent the same user if they have the same "email" (treat email as unique identifier).
2. If the same user appears in both lists, the record from list_b should WIN (overwrite list_a’s version).
   - Example: Bob appears in both → keep Bob from list_b.
3. The final result should contain each unique email exactly once.

Expected shape (order doesn’t have to match this, but it’s fine if it does):
[
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob B.", "email": "bob@example.com"},   # from list_b
    {"id": 3, "name": "Carol", "email": "carol@example.com"},
    {"id": 4, "name": "Dave", "email": "dave@example.com"},
    {"id": 5, "name": "Elena", "email": "elena@example.com"},
]

Hints you’re allowed to use:
- You can use a dict internally where keys are emails and values are the full user objects.
- At the end, return just the dict’s values as a list.

Aim: under 10 minutes.
Be quick and precise. After you paste your solution, I’ll tell you what breaks in real ETL merges.
"""

list_a = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob",   "email": "bob@example.com"},
    {"id": 3, "name": "Carol", "email": "carol@example.com"},
]

list_b = [
    {"id": 2, "name": "Bob B.",    "email": "bob@example.com"},     # same user, slightly diff name
    {"id": 4, "name": "Dave",      "email": "dave@example.com"},
    {"id": 5, "name": "Elena",     "email": "elena@example.com"},
    {"id": 3, "name": "Carol",     "email": "carol@example.com"},   # duplicate of Carol
]

def merge_users(a: list[dict], b: list[dict]) -> list[dict]:
    """
    Merge two JSON-like lists of user records, using email as the unique key.

    Args:
        a (list[dict]): First list of user records (base list).
        b (list[dict]): Second list of user records; entries here overwrite duplicates from `a`.

    Returns:
        list[dict]: Merged list of unique users, where same email users are removed
                    and records from list b take precedence.

    """
    
    merged = {user["email"]: user for user in a}

    merged.update({user["email"]: user for user in b})

    return [val for key, val in merged.items()]

print(merge_users(list_a, list_b))

for user in merge_users(list_a, list_b):
    print(user)