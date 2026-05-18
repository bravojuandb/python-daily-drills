"""
Drill 08 - Truthy and Falsy

Write a function:
    describe_value(value: object) -> str

Requirements:
1. Return `"missing"` if the value is `None`.
2. Return `"empty"` if the value is falsy but not `None`.
3. Return `"present"` if the value is truthy.
4. Use Python truthiness directly.

Example:
>>> describe_value([])
'empty'
>>> describe_value(None)
'missing'

Thinking goal:
This drill is about combining a special identity check with general truthiness rules.
"""
