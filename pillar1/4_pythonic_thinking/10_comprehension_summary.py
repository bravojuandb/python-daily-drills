"""
Drill 10 - Comprehension Summary

Write a function:
    summarize_tags(tags: list[str]) -> dict[str, int]

Requirements:
1. Use one dictionary comprehension.
2. Normalize each tag by stripping whitespace and converting it to lowercase.
3. Include only tags with length at least `4` after normalization.
4. Use the normalized tag as the key.
5. Use the length of the normalized tag as the value.
6. If the same tag appears with different capitalization, it should collapse to one key naturally.

Example:
>>> summarize_tags([" Python ", "api", "Data", "PYTHON", " ml "])
{'python': 6, 'data': 4}

Thinking goal:
This drill is about mixing normalization, filtering, and mapping in one readable expression.
"""

def summarize_tags(tags: list[str]) -> dict[str, int]:
    return {
        normalized_tag: len(normalized_tag)
        for tag in tags
        if len(normalized_tag := tag.strip().lower()) >= 4
    }

if __name__ == "__main__":
    tags = [" Python ", "api", "Data", "PYTHON", " ml "]
    print(summarize_tags(tags))
