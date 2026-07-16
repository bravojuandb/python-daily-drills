"""
Drill — Simple ETL Transform (clean → aggregate → output)

You're given raw ecommerce transactions. Each row is one purchase event.

raw_data = [
    {"customer": " alice ", "country": "ES", "amount": "100.50", "currency": "eur"},
    {"customer": "Bob",    "country": "ES", "amount": "200",    "currency": "EUR"},
    {"customer": "ALICE",  "country": "ES", "amount": "50.5",   "currency": "EUR"},
    {"customer": "bob ",   "country": "FR", "amount": "20",     "currency": "eur"},
    {"customer": "carol",  "country": "FR", "amount": "",       "currency": "eur"},  # bad amount
    {"customer": "dave",   "country": "ES", "amount": "N/A",    "currency": "usd"},  # other currency
]


Your job: write ONE function etl(data: list[dict]) -> dict that returns final aggregates.

Step 1. CLEAN (T stage: standardize & validate)
    - customer: strip spaces and lowercase the name, then title-case it.
        e.g. " alice " -> "Alice", "bob " -> "Bob"
    - amount: convert to float. If it's missing, "", "N/A", or not numeric → skip that row completely.
    - currency: only keep rows where currency is EUR (case-insensitive). Drop the rest.
    - country: leave as-is.

Step 2. AGGREGATE
    Build a nested summary:
    {
        "ES": {
            "Alice": total_spent_in_eur,
            "Bob": total_spent_in_eur,
            ...
        },
        "FR": {
            "Bob": ...,
            "Carol": ...,
        }
    }

    - Sum amounts per (country, customer).
    - Use float sums (no rounding yet).

Step 3. OUTPUT FORMAT
    Return that nested dict.

Edge rules you MUST handle:
    - If a country ends up with no valid rows (e.g. all dropped), it should NOT appear in the result.
    - If a customer appears multiple times in same country, they should appear once with the total.
    - Ignore USD rows entirely.

Example (not exact numbers): "ES" -> {"Alice": 151.0, "Bob": 200.0}

Your function signature:
    def etl(data: list[dict]) -> dict:
        ...

Be quick. Be precise.
"""
raw_data = [
    {"customer": " alice ", "country": "ES", "amount": "100.50", "currency": "eur"},
    {"customer": "Bob",    "country": "ES", "amount": "200",    "currency": "EUR"},
    {"customer": "ALICE",  "country": "ES", "amount": "50.5",   "currency": "EUR"},
    {"customer": "bob ",   "country": "FR", "amount": "20",     "currency": "eur"},
    {"customer": "carol",  "country": "FR", "amount": "",       "currency": "eur"},  # bad amount
    {"customer": "dave",   "country": "ES", "amount": "N/A",    "currency": "usd"},  # other currency
]


def etl(data: list[dict]) -> dict:
    aggregate = {}
    for entry in data:
        customer = entry["customer"].lower().strip().title()
        if entry["currency"].lower().strip() == "eur":
            try:
                amount = float(entry["amount"])
            except (ValueError, TypeError):
                continue
            country = entry["country"]
        else:
            continue

        if country not in aggregate:
            aggregate[country] = {}
        if customer not in aggregate[country]:
            aggregate[country][customer] = 0.0
        aggregate[country][customer] += amount

    return aggregate


print(etl(raw_data))