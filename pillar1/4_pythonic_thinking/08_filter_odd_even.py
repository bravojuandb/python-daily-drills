"""
Drill 08 - Filter Active and Inactive

Write a function:
    split_users(usernames: list[str]) -> tuple[list[str], list[str]]

Requirements:
1. A username is active if it does not start with `"guest_"`.
2. Use `filter()` to extract the active usernames.
3. Use `filter()` again to extract the guest usernames.
4. Return `(active_users, guest_users)`.
5. Preserve the original order inside each result.

Example:
>>> split_users(["ana", "guest_14", "mike", "guest_temp", "zoe"])
(['ana', 'mike', 'zoe'], ['guest_14', 'guest_temp'])

Thinking goal:
This drill is about separating a sequence into two views without manually managing indexes.
"""
