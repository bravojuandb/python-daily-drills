"""
Pillar 1 Drill – Hard  
Title: group_by_length  
Subcategory: Dictionaries and Counting  
Category: Fluency & Logic  
Style: Turing-style assessment

Prompt:
    Write a function `group_by_length(words: list[str]) -> dict[int, list[str]]`
    that takes a list of words and returns a dictionary grouping the words by their length.
    The dictionary keys should be integers (lengths), and the values should be lists of words of that length.

Requirements:
    1. All words must be lowercased.
    2. The output lists should be sorted alphabetically.
    3. If the same word appears more than once in the input, it should only appear once in the output.
    4. The final dictionary should be sorted by increasing word length. (Returning any dict type is fine,
       but tests will compare sorted list of tuples.)

Example:
    >>> group_by_length(["Tree", "house", "CAT", "tree", "mouse", "cat", "House"])
    {
        3: ["cat"],
        4: ["tree"],
        5: ["house", "mouse"]
    }

Constraints:
    - Do not use any external libraries.
    - Must run in O(n log n) or better (average case).
    - Input list can have up to 10^5 words.

Hidden Test Case Ideas:
    - All words the same length, some repeated.
    - Empty input list.
    - Long list with one length group and many duplicates.
    - Multiple groups with varying case and unsorted input.
"""

def group_by_length(words: list[str]) -> dict[int, list[str]]:

    groups = {}
    seen = set()
    for word in words:
        word_lc = word.lower()
        if word_lc not in seen:
            seen.add(word_lc)
            lenght = len(word_lc)
            if lenght not in groups:
                groups[lenght] = set()
            groups[lenght].add(word_lc)

    print(groups)



group_by_length(["Tree", "house", "CAT", "tree", "mouse", "cat", "House"])