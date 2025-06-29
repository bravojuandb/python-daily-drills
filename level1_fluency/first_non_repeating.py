"""
Given a list of integers,
return the first element that doesn`t repeat
If all lements repeat, return none

"""
import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def first_unique(l:list[int]) -> int | None:
    """ 
    Return the first unique number in the list.
    If all elements repeat, return None.
    """
    logging.info(f"Input list: {l}")

    counts  = Counter(l)
    logging.debug(f"Element counts: {counts}")

    for num in l:
        logging.debug(f"Checking {num}: count = {counts[num]}")
        if counts[num] == 1:
            logging.info(f"First unique number found: {num}")
            return num
        
    logging.info("No unique number found.")
    return None

integers = [2,2,2,2,5,7,9]
result = first_unique(integers)

