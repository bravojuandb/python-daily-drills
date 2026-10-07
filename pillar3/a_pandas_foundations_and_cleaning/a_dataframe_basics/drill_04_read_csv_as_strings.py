"""
Drill 04 - Read CSV Without Interpreting Its Values

Goal: preserve source text before choosing cleaning rules.
Prerequisites: Drills 01-03 and a local file path.

Contract:
- Read a UTF-8, comma-separated CSV from path. Its first row has unique,
  nonempty column names; records are well formed with no blank lines.
- Return every column with pandas dtype "string", in source order, and a
  RangeIndex starting at 0. Preserve field text after CSV quote parsing.
- Keep leading zeros, whitespace, empty fields as "", and literals such as
  "NA" and "NULL" as text. Do not infer numbers or missing values.
- A header-only file returns zero rows with the named string columns.
  Propagate file-reading errors, including FileNotFoundError.
- Do not write files. The shared rules in ../README.md apply.

Examples (CSV content -> DataFrame columns):
'store_id,units,note\n001,0,NA\n002,,\n'
    -> {"store_id": ["001", "002"], "units": ["0", ""], "note": ["NA", ""]}
'store_id,units\n' -> {"store_id": [], "units": []}, both dtype "string"

Tools: pandas CSV reader; optional hints are in this folder's README.
Cost check: relate work and memory to file size and the returned table.
Thinking goal: what information could numeric inference destroy here?
"""

from pathlib import Path

import pandas as pd


def read_csv_as_strings(path: str | Path) -> pd.DataFrame:

    df = pd.read_csv(
        path, sep=",", 
        header=0, 
        dtype="string", 
        encoding="utf-8",
        keep_default_na=False)
    return df

if __name__ == "__main__":
    root = Path(__file__).parent.parent.parent
    file = root / "utils" / "inventory.csv"

    result = read_csv_as_strings(file)
    print(result)
    print(result.dtypes)