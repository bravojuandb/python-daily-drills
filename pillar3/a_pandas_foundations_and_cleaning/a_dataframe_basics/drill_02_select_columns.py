"""
Drill 02 - Select Columns in a Requested Order

Goal: project a table onto the fields a consumer needs.
Prerequisites: Drill 01 and the difference between a Series and a DataFrame.

Contract:
- Return only the requested columns, in the supplied order. The column-name
  list contains no duplicates; raise KeyError if any name is absent.
- Always return a DataFrame, including when one column is requested.
- Keep every row, its index label, and the selected columns' dtypes.
- An empty selection produces zero columns with the original row index.
- Do not modify either input. The shared rules in ../README.md apply.

Examples, with frame = {"store_id": ["001"], "units": [4]}:
["units", "store_id"] -> {"units": [4], "store_id": ["001"]}
["units"] -> {"units": [4]} with shape (1, 1)
["price"] -> KeyError

Tools: pandas selection; optional hints are in this folder's README.

Cost check: distinguish n input rows, k selected columns, and copied data.
Thinking goal: why should selecting one column still preserve two dimensions?
"""

import pandas as pd


def select_columns(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    present_cols = list(frame.columns)

    # This is optional in case a custom message is needed. 
    # Pandas already raises KeyError when selecting absent columns
    for column in columns:
        if column not in present_cols:
            raise KeyError(f"requested column: --{column}-- is absent")

    return frame[columns]


if __name__ == "__main__":
    store_ids = ["001", "002", "003"]
    units = [4, 5, 6]

    df = pd.DataFrame({
        "store_id": store_ids,
        "units": units,
    })

    result = select_columns(df, [])
    print(result.shape)