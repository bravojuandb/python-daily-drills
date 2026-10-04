"""
Drill 03 - Validate Fixed-Width Identifiers

Goal: check an identifier's format while preserving its textual meaning.
Prerequisites: Drill 02 and b/04's validity masks.

Contract:
- Given a string Series and a positive integer width, return one validity
  flag per row. width is guaranteed valid; no parameter validation is needed.
- A valid value contains exactly width ASCII digits (0-9). Leading zeros
  are valid; signs, spaces, letters, and non-ASCII digits are not.
- Missing or empty values are invalid. Return dtype "bool" with no missing
  flags, preserving the original index and name.
- Do not trim, pad, convert to numbers, or check uniqueness. Duplicate
  identifiers can each have a valid format. Shared chapter rules apply.

Examples (Series values -> validity flags):
width=4: ["0012", "12", "AB12", "0000", pd.NA]
    -> [True, False, False, True, False]
width=2: ["01", "01", "０１", " 1"] -> [True, True, False, False]
width=4: [] -> [] with dtype "bool"

Tools: pandas; regex or standard-library string checks are allowed.
Cost check: account for the number and length of identifiers examined.
Thinking goal: why does valid format not prove an identifier exists?
"""

import pandas as pd


def validate_identifier_format(values: pd.Series, width: int) -> pd.Series:
    raise NotImplementedError
