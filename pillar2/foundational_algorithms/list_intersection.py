"""
You are given two lists of customer IDs: 
one representing users who made a purchase last month,
and another representing users who made a purchase this month.

Write a function `find_returning_customers(last_month, this_month)` 
that returns a list of customers who purchased in both months 
(sorted in ascending order).

Example:
    last_month = [102, 205, 303, 404, 505]
    this_month = [101, 205, 303, 606]

Expected output:
    [205, 303]

Be quick and precise. 
"""

from typing import TypeVar

# Create a variable for all hashable types called T
T = TypeVar("T", bound= hash)

def intersect_ids(l1: list[T], l2:list[T]) -> list[T]:
    result= set(l1) & set(l2)
    return sorted(result) # sorted() alway produces a list

last_month = [102, 205, 303, 404, 505]
this_month = [101, 205, 303, 606]

if __name__ == "__main__":

    print(intersect_ids(last_month, this_month))