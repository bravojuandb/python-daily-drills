"""
Write a function count_all_duplicates(lst) that:

Returns a dictionary containing only the elements that appear more than once.
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
Time complexity: O(n)

"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def count_all_duplicates(l:list) -> dict:
    """ 
    Count all duplicates in a list using dictionary comprehensions.
    Return a dictionary where the keys are items that appear more than once,
    and values are the total number of times they appear.
    """
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
    """
    Count all the duplicates in a list using step by step logic.
    Tracks items as they appear and builds the duplicates dictionary
    during the counting process (avoids a second pass)
    """
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