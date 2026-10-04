"""
Drill 01 - Create and Inspect an Inventory Table

Goal: turn Python lists into a table and explain its structure.
Prerequisites: lists, dictionaries, functions, and pandas installed.

Contract:
- Given equal-length lists of store IDs (strings) and units (integers),
  return a DataFrame with columns ["store_id", "units"] in that order.
- Each position supplies one row. Preserve values, including leading zeros.
- Use a RangeIndex starting at 0. Empty lists produce shape (0, 2).
- Let pandas infer dtypes for this first drill; no exact dtype is required.
- Do not modify the lists. The shared rules in ../README.md apply.

Examples:
create_inventory(["001", "002"], [4, 0])
    -> {"store_id": ["001", "002"], "units": [4, 0]}
create_inventory([], []) -> {"store_id": [], "units": []}

After implementing: inspect shape, columns, and dtypes for both examples.
Tools: pandas table construction; optional hints are in this folder's README.

Cost check: what data must be stored for n inventory records?
Thinking goal: how does one column differ from the whole table?
"""

import pandas as pd


def create_inventory(store_ids: list[str], units: list[int]) -> pd.DataFrame:
    df = pd.DataFrame({
        "store_id": store_ids,
        "units": units,
    })
    return df


if __name__ == "__main__":
    populated = create_inventory(["001", "002"], [4, 0])
    empty = create_inventory([], [])

    assert populated.shape == (2, 2)
    assert empty.shape == (0, 2)

    for name, df in (("populated", populated), ("empty", empty)):
        assert list(df.columns) == ["store_id", "units"]
        print("")
        print(name)
        print("shape:", df.shape)
        print("columns:", df.columns)
        print("dtypes:", df.dtypes)
        print("index:", df.index)
