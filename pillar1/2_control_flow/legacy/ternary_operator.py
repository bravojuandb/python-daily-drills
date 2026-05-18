"""
Ternary Operator Drill 🚀

Rewrite this function using a single ternary operator:

def classify(num: int) -> str:
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Example:
# classify(7) → "odd"
# classify(12) → "even"
"""

def classify(num: int) -> str:
    return  "even" if num % 2 == 0 else "odd"


print(classify(7))
print(classify(12))


"""
Nested Ternary Drill 🎯

Write a function that classifies a number as:
- "negative" if num < 0
- "zero" if num == 0
- "positive" if num > 0

Use ONLY nested ternary operators (no if/else blocks).

# Examples:
# classify(-3) → "negative"
# classify(0)  → "zero"
# classify(9)  → "positive"
"""

def classifier(num: int) -> str:
    return "negative" if num < 0 else "zero" if num == 0 else "possitive"

print(classifier(0))