"""
Drill 07 - Word Split and Join

Write a function:
    normalize_title(text: str) -> str

Requirements:
1. Split the input into words.
2. Ignore extra spaces between words.
3. Lowercase every word.
4. Join the words back together with `-`.
5. Return the final normalized string.

Example:
>>> normalize_title("  Python   IS Fun To Learn ")
"python-is-fun-to-learn"

Thinking goal:
The exercise is about cleaning and reshaping text with a small, reliable pipeline.
"""

def normalize_title_v1(text: str) -> str:
    text = text.split()
    normalized = [word.lower() for word in text]
    return "-".join(normalized)

# Condensed version
def normalize_title_v2(text: str) -> str:
    return "-".join(word.lower() for word in text.split())

if __name__ == "__main__":
    print(normalize_title_v2("  Python   IS Fun To Learn "))
