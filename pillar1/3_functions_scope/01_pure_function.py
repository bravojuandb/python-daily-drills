"""
Drill 01 - Pure Function

Write a function:
    normalize_title(text: str) -> str

Requirements:
1. Return a new string without mutating external state.
2. Remove leading and trailing spaces.
3. Collapse repeated internal spaces to a single space.
4. Convert the result to title case.
5. If the cleaned text is empty, return `"Untitled"`.

Example:
>>> normalize_title("  the   odyssey ")
'The Odyssey'
>>> normalize_title("   ")
'Untitled'

Thinking goal:
This drill is about making a function deterministic while applying a small sequence of transformations.
"""

def normalize_title(text: str) -> str:

    words = text.split()

    if not words:
        return "Untitled"
    
    return " ".join(words).title()
    

if __name__ == "__main__":

    titles = [
        "  the   odyssey ",
        "",
        "war and peace",
        "   ",
        "a tale of two cities",
        "  data   engineering   basics",
        "THE LORD OF THE RINGS",
        "clean code",
        "  python    daily drills  ",
        "into the wild",
    ]
    for title in titles:
        normalized = normalize_title(title)
        print(repr(title), "----", normalized)
