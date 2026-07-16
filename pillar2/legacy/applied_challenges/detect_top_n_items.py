"""
Detect Top-N Items — sorting by counts

You’re given a collection (list, dict, or Counter) representing item frequencies, e.g.:

    counts = {
    "USD": 1523,
    "EUR": 1780,
    "JPY": 940,
    "GBP": 875,
    "AUD": 655,
    "CAD": 720,
    "CHF": 460,
    "CNY": 1340,
    "BTC": 0.5,    # Bitcoin
    "ETH": 9,      # Ethereum
    "USDT": 770,   # Tether
    "BNB": 430,    # Binance Coin
    "SOL": 395,    # Solana
    "DOGE": 315,   # Dogecoin
    "ADA": 365,    # Cardano
    "XRP": 550,    # Ripple
    "MXN": 510,
    "SGD": 390,
    "KRW": 1180,
    "INR": 970,
    "ZAR": 250,
    "TRY": 305,
    "BRL": 435,
    "THB": 420,
    "AED": 370
}

Task:
Write a function `top_n_items(counts: dict[str, int], n: int) -> list[tuple[str, int]]`
that returns the *n* items with the highest counts, sorted from highest to lowest.

Rules:
- Do not mutate the original dict.
- Use `sorted()` with a `key` function (e.g., `key=lambda x: x[1]`) to sort by the count.
- Handle the case where `n` is greater than the number of items.
- If two items have the same count, preserve the original insertion order.
- O(k log k) time where k = number of items.

Expected output:
    top_n_items(counts, 2)
    → [("orange", 7), ("apple", 5)]

Stretch:
- Re-implement using `heapq.nlargest()` for efficiency when k is large and n is small.

Be quick and precise — this pattern is essential for leaderboards, frequency analysis, 
and analytics dashboards.
"""

def top_n_items(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]


currencies = {
    "USD": 1523,
    "EUR": 1780,
    "JPY": 940,
    "GBP": 875,
    "AUD": 655,
    "CAD": 720,
    "CHF": 460,
    "CNY": 1340,
    "BTC": 0.5,    # Bitcoin
    "ETH": 9,      # Ethereum
    "USDT": 770,   # Tether
    "BNB": 430,    # Binance Coin
    "SOL": 395,    # Solana
    "DOGE": 315,   # Dogecoin
    "ADA": 365,    # Cardano
    "XRP": 550,    # Ripple
    "MXN": 510,
    "SGD": 390,
    "KRW": 1180,
    "INR": 970,
    "ZAR": 250,
    "TRY": 305,
    "BRL": 435,
    "THB": 420,
    "AED": 370
}


for item, count in top_n_items(currencies, 13):
    print(f"{item:<5} {count:>6}")

