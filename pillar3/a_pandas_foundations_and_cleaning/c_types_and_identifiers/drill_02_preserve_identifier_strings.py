"""
Drill 02 - Preserve Raw Identifiers as Strings

Goal: protect identifiers from numeric interpretation and invented repairs.
Prerequisites: Drill 01 and missing-value checks from subchapter b.

Contract:
- Input is an object or string Series of scalar values. Return dtype "string".
- Preserve every existing string exactly, including leading zeros, spaces,
  blank strings, and literal "NA". Do not trim, pad, or normalize identifiers.
- Convert missing values (None, NaN, or pd.NA) to pd.NA.
- If any nonmissing value is not a string, raise TypeError. Do not guess the
  original identifier from a number or stringify arbitrary values.
- Keep the index and name without modifying the input.
  The shared rules in ../README.md apply.

Examples (raw Series values):
["0012", "12", None] -> ["0012", "12", pd.NA]
[" 007 ", "", "NA"] -> [" 007 ", "", "NA"]
["0012", 12] -> TypeError

Tools: pandas and standard-library type checks; optional README hints apply.
Cost check: account for validating n values and creating a string Series.
Thinking goal: what evidence would justify turning numeric 12 into "0012"?
"""

import pandas as pd


def preserve_identifier_strings(values: pd.Series) -> pd.Series:
    raise NotImplementedError
