"""
Write a function count_all_duplicates(lst) that:

Returns a dictionary containing only the elements that appear more than once.
Tracks duplicate counts as you go.
Avoids a second pass (i.e. don’t filter after counting)

>>> count_all_duplicates([1, 2, 2, 3, 1, 1])
{2: 2, 1: 3}
>>> count_all_duplicates(["a", "b", "a", "c", "b", "b"])
{'a': 2, 'b': 3}
>>> count_all_duplicates(["x", "y", "z"])
{}

Use two dictionaries:

    counts: to track how many times each element appears
    duplicates: to store elements only when their count reaches 2

Return duplicates at the end.
Avoid dictionary comprehensions or collections.Counter
Time complexity: O(n)

"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def count_all_duplicates(l:list) -> dict:
    counts = {}
    logger.debug(f"Starting count of items in list: {l}")

    # Fills in counts dictionary
    for item in l:
        counts[item] = counts.get(item, 0) + 1
        logger.debug(f"Seen '{item}' → count = {counts[item]}")

    # Dictionary comprehension, filters values > 1
    duplicates = {k: v for k, v in counts.items() if v > 1}
    logger.debug(f"Final duplicate counts: {duplicates}")

    return duplicates


def count_all_duplicates_long(l:list) -> dict:
    
    counts = {}
    duplicates = {}
    logger.debug(f"Starting count of items in list: {l}")

    for char in l:

         # Counts every occurence
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
        logger.debug(f"Seen '{char}' → count = {counts[char]}")

        if counts[char] == 2:
            duplicates[char] = counts[char]
            
        elif counts[char] > 2:
            duplicates[char] += 1

    logger.debug(f"Final duplicates: {duplicates}")
    return duplicates




count_all_duplicates_long(["a", "b", "a", "c", "b", "b"])