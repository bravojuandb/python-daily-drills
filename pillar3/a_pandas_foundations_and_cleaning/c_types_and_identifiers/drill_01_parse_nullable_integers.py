"""
Drill 01 - Parse Integers Without Losing Missing Values

Goal: represent a quantity as an integer even when some rows are missing.
Prerequisites: subchapter b and the distinction between text and numbers.

Contract:
- Input is a string Series. Every nonmissing value is an optional + or -
  followed by one or more ASCII digits, with no whitespace. All such values
  fit signed 64-bit integers; invalid text is outside this drill's inputs.
- Return a Series of dtype "Int64", converting text to its exact integer
  value and preserving missing entries as pd.NA. Do not convert via float.
- Keep the index and name. Empty input returns an empty Int64 Series.
- Do not modify the input. The shared rules in ../README.md apply.

Examples (Series values):
["12", pd.NA, "-3", "+004"] -> [12, pd.NA, -3, 4]
["0", pd.NA] -> [0, pd.NA]
[] -> [] with dtype "Int64"

Tools: pandas conversion; optional hints are in this folder's README.
Cost check: account for reading numeric text and storing values and nulls.
Thinking goal: why would replacing a missing quantity with zero change it?
"""

import pandas as pd


def parse_nullable_integers(values: pd.Series) -> pd.Series:
    raise NotImplementedError
