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

lowercase_unique_words(["Tree", "tree", "CAT", "Cat"])


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

group_by_length_basic(["cat", "house", "tree"])

# Block num: 3
# Goal: Given a dictionary of sets, return a dictionary of sorted lists.

def sort_grouped_words(groups: dict[int, set[str]]) -> dict[int, list[str]]:

    sorted_group = {}
    for length, words in groups.items():
        sorted_group[length] = sorted(words)

    return sorted_group

#def sort_grouped_words(groups: dict[int, set[str]]) -> dict[int, list[str]]:
#   return {length: sorted(list(words)) for length, words in sorted(groups.items())}


print(sort_grouped_words({3: {'dog', 'cat'}, 5: {'zebra', 'apple'}}))
# {3: ['cat', 'dog'], 5: ['apple', 'zebra']}