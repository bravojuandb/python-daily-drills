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
