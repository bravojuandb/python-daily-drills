# 💡 Daily Data Engineering Exercise #1
#
# ✅ Task: Parse & Inspect Data Types in a CSV Inventory
#
# 🌍 Real-World Relevance:
# As a Data Engineer, you'll often receive CSVs from vendors, legacy systems,
# or data scraping jobs. These files frequently contain inconsistent formatting
# and incorrect data types. Before transforming or storing this data,
# you need to validate and convert it properly—
# this is a foundational part of every ETL pipeline.
#
# 🛠️ Your Task:
# Write a Python script that does the following:
#
# 1. Reads a CSV file named `inventory.csv`
# 2. For each row:
#    - Assign values to variables with clear, descriptive names
#    - Print the original values and their data types using `type()`
#    - Clean the string fields (e.g., using `.strip()`)
#    - Convert the `price` field to a `float`
#    - Print the cleaned values and their types
#
# 📥 Input Example (`inventory.csv`) using io.StringIO
#
# title,author,price
# "The Republic","Plato",12.99
# "Nicomachean Ethics","Aristotle"," 15.5 "

# Setup

import csv  # Helps us read the data like a spreadsheet
import io  # Lets us fake a file using a string (so no real file needed)

inventory = """title,author,price
"  The Republic ","Plato", 12.99
"Nicomachean Ethics", "Aristotle", " 15.5 "
"Summa Theologica", , 39.95
"Phaedo",Plato, not_available
"Confessions","Augustine",21
"City of God", "Augustine",  18.75
"Metaphysics", Aristotle, 17.00
"  On the Trinity ", "  Augustine ", "19.9"
"""

csv_file = io.StringIO(inventory)
reader = csv.DictReader(csv_file)



# Assign raw (uncleaned) values from each CSV column to clearly named variables
  
for row in reader:
    title_raw = row["title"]
    author_raw = row["author"]
    price_raw = row["price"]

      # These variables now hold the original data exactly as it appears in the CSV file

    print("Original values and types:")
    print(f"   title={title_raw!r}, type={type(title_raw)}")  # !r shows the string exactly as it is.
    print(f"   author={author_raw!r}, type={type(author_raw)}")
    print(f"   price={price_raw!r}, type={type(price_raw)}")
    print("-" * 50)


