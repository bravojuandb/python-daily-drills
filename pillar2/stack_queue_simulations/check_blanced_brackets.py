"""
Challenge: Check Balanced Brackets (stack)

Write a function `is_balanced(s: str) -> bool` that returns True iff all brackets
in `s` are properly opened/closed and correctly nested.

Brackets considered: (), {}, []
Non-bracket characters must be ignored.

Examples:
- "([]){}"         ➜ True
- "([)]"           ➜ False
- "(abc[12]{x})"   ➜ True
- "((("            ➜ False
- ""               ➜ True

Rules:
- Use a stack implemented with a Python list: .append() / .pop()
- Single pass over the string (O(n)) with early failure when possible
- Do not reverse strings or use recursion
- Return only a boolean (no printing)

Edge cases to handle:
- Closing bracket with empty stack
- Mismatched pairs like '(' with ']'
- Extra opening brackets left in stack at the end

Be quick and precise — this pattern powers parsers, validators, and lint checks.
"""

def is_balanced(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


print(is_balanced("([]){}"))        # True
print(is_balanced("([)]"))          # False
print(is_balanced("(abc[12]{x})"))  # True
print(is_balanced("((("))           # False
print(is_balanced(""))              # True
