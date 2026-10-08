"""
Drill 01 - Trim Text and Normalize Blanks

Goal: distinguish useful text from an absent value.
Prerequisites: subchapter a; Series and pandas' missing marker pd.NA.

Contract:
- Given a string Series, remove leading and trailing whitespace from each
  nonmissing value. Whitespace includes spaces, tabs, and newlines.
- Replace text that becomes empty with pd.NA; keep existing missing values.
- Preserve internal whitespace, letter case, punctuation, and literal "NA".
- Return a string Series with the same index and name, including when empty.
- Do not modify the input. The shared rules in ../README.md apply.

Examples (Series values):
["  North  Hub  ", "", pd.NA] -> ["North  Hub", pd.NA, pd.NA]
[" \t ", " NA ", "0"] -> [pd.NA, "NA", "0"]
[] -> [] with dtype "string"

Tools: pandas text operations; optional hints are in this folder's README.

Cost check: account for row count, total text length, and the output.
Thinking goal: why are "0" and "NA" not automatically missing?
"""

import pandas as pd


def trim_and_normalize_blanks(values: pd.Series) -> pd.Series:
    values = values.str.strip().replace("", pd.NA)

    return values


if __name__ == "__main__":

    location = ["  North  Hub  ", "\n", "", "\t", pd.NA]
    location = pd.Series(location, dtype="string", name= "location")

    print("\nSeries before processing:")
    print(location.dtype)
    print(isinstance(location, pd.Series))
    print(location.map(repr))

    result = trim_and_normalize_blanks(location)

    print("\nSeries after processing:")
    print(result.dtype)
    print(isinstance(result, pd.Series))
    print(result.map(repr))
