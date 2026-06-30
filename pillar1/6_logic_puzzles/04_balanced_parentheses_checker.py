"""
Drill 04 - Balanced Parentheses Checker

Write a function:
    is_balanced(text: str) -> bool

Requirements:
1. Support all three bracket pairs: `()`, `[]`, and `{}`.
2. Ignore non-bracket characters.
3. Use a stack implemented with a list.
4. Return `False` as soon as a closing bracket cannot match the stack top.
5. Return `True` only if the stack is empty at the end.

Example:
>>> is_balanced("([]{})")
True
>>> is_balanced("([)]")
False
>>> is_balanced("(a + b) * [c + {d / e}]")
True
>>> is_balanced("(((()")
False

Challenge bar:
- Correct counts are not enough; nesting order matters.
- Keep the matching rules data-driven instead of writing one branch per pair.

Thinking goal:
This drill is about maintaining a stack invariant while several bracket types compete for order.
"""

def is_balanced(text: str) -> bool:
    stack = []

    matching_brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    opening_brackets = set(matching_brackets.values())

    for char in text:
        if char in opening_brackets:
            stack.append(char)

        elif char in matching_brackets:
            if not stack:
                return False

            if stack[-1] != matching_brackets[char]:
                return False

            stack.pop()

    return stack == [] 


if __name__ == "__main__":
    print(is_balanced("(a + b) * [c + {d / e}]"))
