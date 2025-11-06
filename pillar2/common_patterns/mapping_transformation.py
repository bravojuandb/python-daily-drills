"""
Problem — Mapping & Transformation (adapted to your dataset)

You’re given a **multi-line string** with a CSV header and rows:

See below.

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

⏱ Be quick and precise — aim for 8–10 minutes.
"""

data = """id,name,email,country,status,spend
1,Anna,anna@example.com,Spain,active,120.50
2,Bob,bob@example.com,Germany,inactive,80.00
3,Cara,cara@example.com,Spain,active,300.00
4,Dan,dan@example.com,Italy,active,50.00
5,Eve,eve@example.com,Spain,inactive,0
6,Frank,frank@example.com,France,active,210.75
7,Gina,gina@example.com,Germany,active,95.60
8,Hugo,hugo@example.com,Spain,active,150.00
9,Iris,iris@example.com,Italy,inactive,40.20
10,Jack,jack@example.com,France,active,500.00
11,Kate,kate@example.com,Germany,inactive,0
12,Liam,liam@example.com,Spain,active,275.30
13,Mona,mona@example.com,France,active,125.00
14,Nico,nico@example.com,Italy,inactive,15.00
15,Olga,olga@example.com,Germany,active,230.00
16,Paul,paul@example.com,Spain,active,60.00
17,Quinn,quinn@example.com,Italy,active,110.10
18,Rita,rita@example.com,France,inactive,20.00
19,Sam,sam@example.com,Spain,active,340.90
20,Tina,tina@example.com,Germany,active,410.00"""

from typing import Optional

COUNTRY_MAP = {"Spain": "ES", "Germany": "DE", "France": "FR", "Italy": "IT"}

def _spend_tier(spend: float) -> str:
   if spend >= 300:
       return "gold"
   if spend >= 150:
       return "silver"
   return "bronze"

def converter(data: str) -> list[dict[str,str]]:
    """
    Convert a CSV-shaped multiline string (first line is the header)
    into a list of dictionaries every value is still a string
    """
    lines = data.strip().splitlines()
    header, *rows = lines
    keys = header.split(",")
    return [dict(zip(keys, row.split(","))) for row in rows]

def transform(records: list[dict[str, str]]) -> list[dict]:
    """
    Map stringly records -> typed + derived fields.
    Skips malformed rows safely.
    """
    return [
        {
            "id": int(r["id"]),
            "name": r["name"],
            "email": r["email"],
            "country": r["country"],
            "status": r["status"],
            "spend": float(r["spend"]),
            "is_active": r["status"] == "active",
            "email_domain": r["email"].split("@")[-1],
            "country_code": COUNTRY_MAP.get(r["country"], "??"),
            "spend_tier": _spend_tier(float(r["spend"])),
        }
        for r in records
        if (
            r.get("id") is not None
            and r.get("name") is not None
            and r.get("email") is not None
            and r.get("country") is not None
            and r.get("status") is not None
            and r.get("spend") is not None
            and (lambda _id, _sp: _id.isdigit() 
                 and _sp.replace(".", "", 1).isdigit())(r["id"], r["spend"])
        )
    ]

if __name__ == "__main__":
    # 1) parse raw CSV-shaped string into list[dict[str,str]]
    rows = converter(data)
    # 2) map to typed records with derived fields
    enriched = transform(rows)

    # 3) print per the spec:
    for r in enriched:
        print(f'{r["id"]} | {r["name"]} [{r["country_code"]}] — €{r["spend"]:.2f} — '
              f'{r["email_domain"]} — active={r["is_active"]} — tier={r["spend_tier"]}')