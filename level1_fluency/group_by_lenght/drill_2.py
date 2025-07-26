"""
Three building blocks of group_by_lenght drill.

"""
# Block num 1: Normalize & Deduplicate
# Goal: Convert a list of words to lowercase and remove duplicates.

def lowercase_unique_words (words: list[str]) -> set[str]:
    unique = set()
    for word in words:
        word_lc = word.lower()
        unique.add(word_lc)
    return unique

def lowercase_unique_words (words: list[str]) -> set[str]:
    return set(word.lower() for word in words)

print(lowercase_unique_words(["Tree", "tree", "CAT", "Cat"]))


# Block num 2: Group words by lenght
# Goal: Given a list of lowercase, unique words, group them by their length.

def group_by_length_basic(words: list[str]) -> dict[int, list[str]]:

    groups = {}
    for word in words:
        lenght = len(word)
        if lenght not in groups:
            groups[lenght] = []
        groups[lenght].append(word)
    return groups

print(group_by_length_basic(["cat", "house", "tree"]))