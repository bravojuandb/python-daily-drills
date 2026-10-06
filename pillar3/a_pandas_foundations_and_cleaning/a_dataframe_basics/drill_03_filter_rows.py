"""
Drill 03 - Filter Inventory by Units

Goal: select rows using a condition without confusing labels and positions.
Prerequisites: Drills 01-02 and integer comparisons.

Contract:
- frame contains a "units" column of integers with no missing values.
  Return rows where units is greater than or equal to minimum.
- Keep all columns and their dtypes. Preserve matching rows' original order
  and index labels; do not reset the index or remove duplicate records.
- No matches produces an empty table with the same columns and dtypes.
- Do not modify frame. The shared rules in ../README.md apply.

Examples, with units [4, 0, 4] at index [10, 30, 20]:
minimum=4 -> units [4, 4] at index [10, 20]
minimum=0 -> all three rows at index [10, 30, 20]
minimum=5 -> no rows

Tools: pandas row filtering; optional hints are in this folder's README.

Cost check: account for inspecting n rows and storing the selected table.
Thinking goal: why is label 20 not the third row's position?
"""

import pandas as pd


def filter_units(frame: pd.DataFrame, minimum: int) -> pd.DataFrame:
    above_min = frame[frame["units"] >= minimum]

    return above_min


if __name__ == "__main__":
    df = pd.DataFrame({"units": [4, 0, 4]}, index=[10, 30, 20])

    print(filter_units(df, 4))
    print(filter_units(df, 5))
    print(filter_units(df, 0))
