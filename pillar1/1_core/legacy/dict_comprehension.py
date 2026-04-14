"""
You have two lists:

products = ["apple", "banana", "orange"]
quantities = [10, 5, 0]

1. Build a dictionary that maps each product to its quantity.
2. Use a dictionary comprehension.

Expected result:
{
    "apple": 10,
    "banana": 5,
    "orange": 0
}
"""
import logging
logging.basicConfig(level=logging.INFO)

def make_inventory(a: list[str], b: list[int]) -> dict:
    logging.info("Merging %d PRODUCTS with %d QUANTITIES", len(a), len(b))

    result = {a[i]: b[i] for i in range(len(a))}

    logging.info("Merge result has %d items", len(result))
    return result

products = ["apple", "banana", "orange"]
quantities = [10, 5, 0]

make_inventory(products, quantities)

