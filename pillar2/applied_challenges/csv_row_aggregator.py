"""
CSV Row Aggregator — manual parsing only

You’re given a *large* CSV-like text stream (no using `csv` or `pandas`). 
Each non-empty line represents a transaction:

    customer_id,date,amount_eur,status

Rules
- `customer_id`: string without commas (e.g., "C-001")
- `date`: ISO "YYYY-MM-DD" (aggregate by month "YYYY-MM")
- `amount_eur`: decimal number (e.g., 123.45)
- `status`: either "PAID" or "REFUND" (refunds *subtract* from totals)
- Lines may have leading/trailing spaces.
- A header may or may not be present; ignore it if detected.
- Skip blank lines and lines starting with '#'.
- **Do not** import `csv` or `pandas`. Parse manually (e.g., `split(',')`, `.strip()`).
- Process in a streaming fashion (assume the file may not fit in memory).
- Output should be **deterministic** and sorted by (`customer_id` ASC, `month` ASC).

Task
Write a function that reads the stream line-by-line and produces monthly *net* totals 
per customer:

    customer_id,month,total_eur

Where:
- `month` is "YYYY-MM"
- `total_eur` is shown with exactly two decimals (round half away from zero or bankers’ — your choice, but be consistent)

Error handling
- If a line has the wrong number of fields, an invalid date, or a non-numeric amount: skip it and increment an `errors` counter.
- Return both the aggregated rows and the `errors` count.

Performance
- Time: O(n) over lines
- Space: O(k) where k = unique (customer_id, month) keys

Example Input
    # (Header present, comments, spacing, and a bad row included)

    customer_id,date,amount_eur,status
    C-001,2025-01-03,100.00,PAID
    C-001,2025-01-18,25.50,REFUND
    C-002,2025-01-09,  300.00 , PAID
    # ignored comment
    C-001,2025-02-01,75.00,PAID
    C-002,2025-01-xx,50.00,PAID   # bad date → count as error
    C-002,2025-01-11,20,REFUND


Expected Output

    C-001,2025-01,74.50
    C-001,2025-02,75.00
    C-002,2025-01,280.00

Errors: 1

Stretch goals (optional)
- Support surrounding double quotes and inner spaces: e.g., `"C-003", "2025-03-05", "1,200.00", "PAID"` 
  (you may ignore thousands separators or normalize them).
- Use `decimal.Decimal` for currency-safe arithmetic.
- Emit results as an iterator (generator) to avoid building a large list in memory.
"""
# ------------------------------------------------------------------------------
# Raw input

file = """

customer_id,date,amount_eur,status

C-001,2025-01-03,    100.00,PAID
C-001,2025-01-18,25.50,REFUND

C-002,2025-01-09,  300.00 , PAID
# ignored comment
C-001,2025-02-01,75.00,PAID
"This is a corrupted line"

C-001,2025-02-02,75.00
C-002,2025-01-xx,50.00,PAID
C-002,2025-01-11,20,REFUND

"""


def row_aggregator(file: str) -> dict:
    """
    Aggregate CSV-like transaction rows by customer and month 
    without using csv or pandas.
    """
    errors = 0
    totals = {}

    for raw in file.split("\n"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue # Skip comments or blank lines
        if line.lower().startswith("customer_id"):
            continue # Skip column names row

        # Analyze each line
        parts = [p.strip() for p in line.split(",")]

        # Sanity check for missing fields
        if len(parts) != 4:
            errors += 1
            continue

        customer_id, date, amount_eur, status = parts

        # Date to month ------------------------------------------------------
        if not (len(date) == 10 and date[4] == "-" and date[7] == "-"):
            errors += 1
            continue
        month = date[:7]

        # Amount (negative if REFUND)-----------------------------------------
        try:
            amount = float(amount_eur)
        except ValueError:
            error += 1
            continue
        if status.upper() == "REFUND":
            amount = -amount
        elif status.upper() != "PAID":
            error += 1
            continue

        # Build dictionary (composite key : aggregated amount per month)-------
        key = (customer_id, month)
        totals[key] = totals.get(key, 0.0) + amount

    rows = []

    for (cid, m), total in sorted(totals.items()):
        rows.append(f"{cid},{m},{total:.2f}")

    return rows, errors



rows, errors = row_aggregator(file)

# join the rows with newline characters
print("\n".join(rows))
print(f"\nErrors: {errors}")