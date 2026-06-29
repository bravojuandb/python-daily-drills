"""
Drill 04 - Balanced Parentheses Checker

Write a function:
    is_balanced(text: str) -> bool

Requirements:
1. Use a stack implemented with a list.
2. Only `(` and `)` matter; ignore other characters.
3. Return `False` as soon as a closing parenthesis has nothing to match.
4. Return `True` only if the stack is empty at the end.

Example:
>>> is_balanced("(()())")
True
>>> is_balanced("())(")
False
>>> is_balanced("(a + b) * (c + d)")
True

Thinking goal:
This drill is about maintaining an invariant through the whole scan, not just checking counts at the end.
"""

def is_balanced(text: str) -> bool:
    stack = []
    for char in text:
        if char == "(":
            stack.append(char)

        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return stack == [] 


if __name__ == "__main__":
    print(is_balanced("(()())"))
