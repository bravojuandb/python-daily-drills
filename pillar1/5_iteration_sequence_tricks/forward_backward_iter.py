"""
Write a function `mirror_iter(words: list[str]) -> list[str]`.

Rules:
- First iterate forward through the list and collect all elements.
- Then iterate backward through the same list and collect them again.
- Return the combined list.

Example:
words = ["sun", "moon", "stars"]
mirror_iter(words) = ["sun", "moon", "stars", "stars", "moon", "sun"]

Go! Solve it quickly.
"""
# Using reversed()

def mirror_iter(words: list[str]) -> list[str]:
    result = []
    for word in words:
        result.append(word)
    
    for word in reversed(words):
        result.append(word)
    return result

# Using no helper

def mirror_iter(words: list[str]) -> list[str]:
    result = []
    for word in words:
        result.append(word)
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    return result



words = ["sun", "moon", "stars"]
print(mirror_iter(words))