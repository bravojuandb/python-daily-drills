"""
Drill 05 - Clean a Status While Preserving Free Text

Goal: transfer a known cleaning rule to a table without changing other fields.
Prerequisites: Drill 03 and DataFrame column selection.

Contract:
- frame contains string columns "status" and "note"; each row is a support
  record. Additional columns may exist.
- Normalize only status using Drill 03's rule: trim, lowercase, map "wip"
  to "pending" and "done" to "closed", and turn blanks into pd.NA.
- Keep note and every other column exactly as supplied, including whitespace,
  capitalization, blank strings, literal markers, missing values, and dtypes.
- Return the same rows, index, column order, and dtypes. Do not modify frame.
  The shared rules in ../README.md apply.

Examples (DataFrame columns):
{"status": [" DONE "], "note": ["  Keep CASE!  "]}
    -> {"status": ["closed"], "note": ["  Keep CASE!  "]}
{"status": [" ", pd.NA], "note": ["NA", ""]}
    -> {"status": [pd.NA, pd.NA], "note": ["NA", ""]}

Tools: pandas; you may reuse your solved normalize_status helper.
Cost check: distinguish transformed text from any copied table data.
Thinking goal: what check proves that cleaning did not alter the notes?
"""

import pandas as pd


def clean_status_preserve_notes(frame: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError
