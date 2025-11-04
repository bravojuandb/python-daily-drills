"""
Mapping & Transformation (adapted to your dataset)

You’re given a **multi-line string** with a CSV header and rows:

check: pillar2/common_patterns/customers.csv

id,name,email,country,status,spend
1,Anna,anna@example.com,Spain,active,120.50
2,Bob,bob@example.com,Germany,inactive,80.00
3, ........
......

Task (same-size mapping, new meaning):
1) Parse the text (skip the header) into a **list of dicts** with proper types:
   {
     "id": int,
     "name": str,
     "email": str,
     "country": str,
     "status": str,
     "spend": float
   }

2) Add these **derived fields** for each record (no filtering — output must have 20 items):
   - "is_active": status == "active"
   - "email_domain": the part after "@" in email
   - "country_code": map {"Spain":"ES","Germany":"DE","France":"FR","Italy":"IT"}
   - "spend_tier":
        "gold"   if spend >= 300
        "silver" if 150 <= spend < 300
        "bronze" otherwise

3) Print each transformed record as:
   <id> | <name> [<country_code>] — €<spend:2f> — <email_domain> — active=<is_active> — tier=<spend_tier>

Bonus (still mapping, not reducing):
- Validate types safely; if a row is malformed, **skip it** but continue.
- Implement the transformation using a **single list comprehension** (you may prepare helper dicts/functions above it).
- Keep the **original order** of rows.

Be quick and precise — aim for 8–10 minutes.
"""