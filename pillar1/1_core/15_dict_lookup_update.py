"""
Drill 15 - Dictionary Lookup and Update

Write a function:
    update_inventory(inventory: dict[str, int]) -> dict[str, int]

Scenario:
You receive a stock dictionary like:
    {"apple": 10, "banana": 5, "orange": 0}

Requirements:
1. Read the stock for `"banana"`.
2. Safely read the stock for `"pear"` using a default of `0`.
3. Add 7 to the stock of `"apple"`.
4. Set the stock of `"orange"` to `12`.
5. Ensure `"pear"` exists in the returned dictionary with value `0`.
6. Return the updated dictionary.

Expected result:
>>> update_inventory({"apple": 10, "banana": 5, "orange": 0})
{"apple": 17, "banana": 5, "orange": 12, "pear": 0}

Thinking goal:
This drill is about safe access and intentional mutation of dictionary state.
"""

def update_inventory(inventory: dict[str, int]) -> dict[str, int]:

    _banana = inventory["banana"]

    pear = inventory.get("pear", 0)

    inventory["pear"] = pear
    inventory["apple"] += 7
    inventory["orange"] = 12

    return inventory


if __name__ == "__main__":
    print(update_inventory({"apple": 10, "banana": 5, "orange": 0}))