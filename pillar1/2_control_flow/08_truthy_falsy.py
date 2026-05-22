"""
Drill 08 - Truthy and Falsy

Write a function:
    describe_value(value: object) -> str

Requirements:
1. Return `"missing"` if the value is `None`.
2. Return `"empty"` if the value is present but evaluates to `False`.
3. Return `"present"` if the value evaluates to `True`.
4. Do not compare the value to specific empty containers like `[]` or `""`.
5. Use Python truthiness directly.

Example:
>>> describe_value([])
'empty'
>>> describe_value(None)
'missing'

Thinking goal:
This drill is about combining a special identity check with general truthiness rules.
"""


def describe_value(value: object) -> str:
    if value is None:
        return "missing"
    elif not value:
        return "empty"
    else:
        return "present"


def describe_value_ternary(value: object) -> str:
    return "missing" if value is None else "empty" if not value else "present"


if __name__ == "__main__":

    values = [
    "",          # empty string -> falsy
    [],          # empty list -> falsy
    {},          # empty dict -> falsy
    (),          # empty tuple -> falsy
    set(),       # empty set -> falsy
    None,        # falsy
    False,       # falsy
    True,        # truthy
    "hello",     # truthy
    [1, 2, 3],   # truthy
    {"a": 1},    # truthy
    (1, 2),      # truthy
    {1, 2},      # truthy
    0,           # falsy
    1,           # truthy
    ]

    for value in values:
        print(repr(value), describe_value(value))

    for value in values:
        print(repr(value), describe_value_ternary(value))