"""
Daily Data Engineering Exercise #6

Task: Parse Dates and Extract Weekdays

Real-World Relevance

Raw datasets often include timestamps or dates in inconsistent string formats. As a Data Engineer, you're frequently asked to **parse dates**, validate them, and extract useful components like weekdays, month names, or years — for analytics, time-series pipelines, or aggregation logic.

---

Your Task

Given a list of records with `event_name` and `event_date` as strings, write a script that:

1. Assigns each field to a variable
2. Parses the `event_date` string to a `datetime` object
3. Extracts the weekday name (e.g., `"Monday"`)
4. Stores the cleaned and enriched record in a new list
5. Skips records with invalid or unparsable dates

"""
# Import the datetime module to handle date parsing and formatting
from datetime import datetime

# Raw input data: a list of event dictionaries with various date formats
events = [
    {"event_name": "Kickoff", "event_date": "2024-12-31"},
    {"event_name": "Launch", "event_date": "2025-01-01"},
    {"event_name": "Anniversary", "event_date": "2025/04/01"},
    {"event_name": "Promo Day", "event_date": "invalid_date"},
    {"event_name": "End Year Review", "event_date": "2024-12-30"}
]

# Initialize an empty list to store successfully cleaned and parsed events
cleaned_events = []

# Loop through each event in the original data
for event in events:
    name = event["event_name"]         # Extract the event name
    date_str = event["event_date"]     # Extract the date as a string

    try:
        # Attempt to parse the date in two possible formats
        try:
            # First, try the standard YYYY-MM-DD format
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            # If that fails, try the alternate YYYY/MM/DD format
            date = datetime.strptime(date_str, "%Y/%m/%d")

        # Extract the weekday name from the successfully parsed date
        weekday = date.strftime("%A")

    except ValueError:
        # If both formats fail, print a message and skip this event
        print(f"Skipped: Invalid date for {name}")
        continue

    # If date parsing succeeded, build a new record with weekday info
    cleaned_events.append({
        "event_name": name,
        "event_date": date_str,
        "weekday": weekday
    })

# Loop through the cleaned list and print each enriched event record
for e in cleaned_events: