"""
Write a script that:

	•	Starts with a list of messy customer records
	•	Cleans them
	•	Skips the missing names
	•	Stores only the valid ones
	•	Prints the cleaned results

"""

# Data to be cleaned
raw_customers = [
    {"name": "  john smith ", "city": " new york"},
    {"name": "MARY-JANE O'HARA", "city": "chicago"},
    {"name": "  alice   cooper", "city": "  boston "},
    {"name": "", "city": "madrid"}  # Invalid entry: missing name
]

# List to store cleaned and validated customer records
cleaned_customers = []

# Loop through each raw customer record
for raw_customer in raw_customers:
    name_raw = raw_customer["name"]  # Extract raw name field
    city_raw = raw_customer["city"]  # Extract raw city field

    # Skip and report if the name is missing or only whitespace
    if not name_raw.strip():
        print("Skipped: Missing name")
        continue

    # Clean name: strip leading/trailing spaces and capitalize properly
    name = name_raw.strip().title()

    # Clean city: strip spaces and convert to uppercase
    city = city_raw.strip().upper()

    # Append the cleaned customer record to the results list
    cleaned_customers.append({
        "name": name,
        "city": city
    })

# Print out all cleaned customer records
print("Cleaned customer data:")
for customer in cleaned_customers:
    print(customer)

