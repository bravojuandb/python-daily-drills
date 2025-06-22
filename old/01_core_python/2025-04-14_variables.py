"""
# Daily Data Engineering Exercise #5

# ask: Categorize Product Prices into Buckets

# Real-World Relevance

Categorizing numerical values (like price, quantity, or score) 
into **discrete buckets** is a common transformation in data engineering — 
used in reporting, analytics, and data cleaning. 
You’ll use variables, if-else logic, and string labeling 
to process a list of raw product data.

---

##Your Task

Given a list of products with messy price strings, write a script that:

1. Extracts and cleans the `price` field
2. Converts it to a `float`
3. Adds a new field: `price_category`, based on the price:
   - `"low"` if price < 10  
   - `"medium"` if 10 ≤ price < 50  
   - `"high"` if price ≥ 50
4. Skips rows that fail to convert the price


"""

products = [
    {"name": "Notebook", "price": " 4.99 "},
    {"name": "Backpack", "price": " 47.00"},
    {"name": "Laptop", "price": " 599.99"},
    {"name": "Pen", "price": "free"},
    {"name": "Desk Lamp", "price": "29.99"}
]

# Initialize an empty list to store cleaned and categorized product data
cleaned_products = []

# loop trough each product in the list
for product in products: 
    name = product["name"]
    price_raw = product["price"]

    try:
        # Attempt to clean and convert the price to a float
        price = float(price_raw.strip())
    except ValueError:
        # If conversion fails, skip this product
        print(f"Skipped line: invalid price for {name}")
        continue

    # Assign price category based on the numeric value
    if price < 10:
        price_category = "low"
    elif price < 50:
        price_category = "medium"
    else:
        price_category = "high"
    
    # Add the clean and categorized product to the result list
    cleaned_products.append({  
        "name": name,
        "price": price,
        "price_category": price_category
    })

# Print each clenaned and categorized product record
for product in cleaned_products: 
    print(product)