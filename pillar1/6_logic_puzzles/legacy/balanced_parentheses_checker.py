"""
Write a function `is_balanced(s: str) -> bool` that checks if all parentheses are balanced.

Rules:
- Use a stack (list in Python) to push/pop characters.
- Only `(` and `)` matter — other characters can be ignored.
- Return True if every opening parenthesis has a closing one in the correct order.
- Return False otherwise.

Examples:
- "(()())" → True
- "())(" → False
- "(a + b) * (c + d)" → True
"""

def is_balanced(s: str) -> bool:
    stack = []
    for ch in s:
        print(f"{ch}round")
        print(stack)
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("(()())"))

