"""
Pillar 1 Drill: reverse_strings.py
Level: Medium
Focus: Sets and Logic Scanning

Problem:
Given a list of strings, return a list of all strings that have their reversed
counterpart also present in the list.

You must:
- Return each such string only once.
- Exclude palindromes (words that are the same when reversed).
- The output list can be in any order.

Examples:
>>> reverse_pairs(["abc", "cba", "xyz", "zyx", "hello", "olleh", "noon"])
['abc', 'xyz', 'hello']

>>> reverse_pairs(["madam", "damam", "madam", "madam"])
[]

>>> reverse_pairs(["deed", "live", "evil", "veed"])
['live']

Constraints:
- Input: list of strings `words` (length ≤ 10,000)
- Each string: lowercase ASCII, length ≤ 100

Requirements:
- Use sets for fast lookup.
- Scan the list only once if possible.
- Avoid returning duplicate results.
- Do not include palindromes.

"""


def reverse_pairs(words: list[str]) -> list[str]:

    words_set = set(words)
    result = set()

    for word in words:
        if word != word[::-1] and word[::-1] in words_set:
            if word > word[::-1]:
                result.add(word)
                
    return list(result)



print(reverse_pairs(["abc", "cba", "xyz", "zyx", "hello", "olleh", "noon"]))