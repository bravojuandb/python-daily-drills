"""
Drill 04 - Report Invalid Integer Conversions

Goal: convert quantities while making rejected source values traceable.
Prerequisites: Drill 01, validity masks, and selecting rows by their index.

Contract:
- Given a string Series, return (converted, failures).
- Valid text is an optional + or - followed by one or more ASCII digits.
  Such values are guaranteed to fit Int64. Spaces, decimals, empty text,
  and other strings are invalid; do not normalize them before validation.
- converted has dtype "Int64", the original index/name, exact integers for
  valid text, and pd.NA for both missing input and invalid text.
- failures contains only invalid, nonmissing inputs, in source row order.
  Its columns are ["row_label", "original_value"], with dtypes "int64" and
  "string". Store the original index labels and unchanged rejected strings.
- failures has a new RangeIndex from 0; keep its columns/dtypes when empty.
  Do not modify values. The shared rules in ../README.md apply.

Examples:
values ["5", "oops", pd.NA, "2.5"], index [10, 30, 20, 50]
    -> converted [5, pd.NA, pd.NA, pd.NA] with the same index;
       failures {"row_label": [30, 50], "original_value": ["oops", "2.5"]}
values ["+004", pd.NA] -> converted [4, pd.NA]; no failure rows
empty input -> empty Int64 Series and empty two-column failures table

Tools: pandas and standard-library helpers; earlier solved helpers are allowed.
Cost check: include validation, conversion, and storage for r rejected rows.
Thinking goal: how can you distinguish source nulls from failed conversions?
"""

import pandas as pd


def report_invalid_conversions(values: pd.Series) -> tuple[pd.Series, pd.DataFrame]:
    raise NotImplementedError
