"""
Drill 06 - Flatten Nested Data

Write flatten_dict(data, sep=".") -> dict[str, object]. Recursively flatten
nested dictionaries by joining keys. Keep lists and scalar values unchanged.
Skip empty dictionaries. Raise ValueError if two source paths produce the same
flattened key.

Example: {"user": {"name": "Ada"}} becomes {"user.name": "Ada"}.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: recursively transform self-similar structure with collision policy.
"""


def flatten_dict(data: dict, sep: str = ".") -> dict[str, object]:
    pass
