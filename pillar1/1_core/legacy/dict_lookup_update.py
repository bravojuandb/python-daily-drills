"""
You have a dictionary of product stock:

inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0
}

1. Lookup how many bananas are in stock.
2. Safely lookup "pear" stock (default to 0 if not found).
3. Update the stock: add 7 apples, and set oranges to 12.

Return the updated dictionary.
Expected result:
{
    "apple": 17,
    "banana": 5,
    "orange": 12,
    "pear": 0
}
"""

def stock_per_item(item: str, inventory: dict) -> int:
    stock = 0
    if item in inventory:
        for key, val in inventory.items():
            if key == item:
                stock += val
    else:
        return 0
    return stock

# Pythonic way:

def stock_per_item(item: str, inventory: dict) -> int:
    return inventory.get(item, 0)


def stock_updater(item: str, quantity: int, inventory: dict) -> dict:
    inventory[item] = inventory.get(item, 0) + quantity
    return inventory


inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0
}

print(stock_per_item('banana', inventory))
print(stock_per_item('pear', inventory))
print(stock_updater('pear', 7, inventory))