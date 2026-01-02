"""
Drill 01 — Read CSV as strings on purpose

Load the raw CSV file while deliberately preventing pandas from inferring data types.  
The goal is to preserve identifiers (codes, postal codes, IDs) 
exactly as they appear in the source data 
and avoid silent numeric coercion (loss of leading zeros, `.0` artifacts, unintended nulls).

This drill establishes a defensive baseline: 
the dataset is ingested as-is, 
with all values treated as strings and missing values handled explicitly later in the pipeline.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

assert DATA_PATH.exists(), "CSV file does not exist at expected path"

# Read everything as a string on purpose to preserve data integrity
navarra_df = pd.read_csv(
    DATA_PATH,
    dtype="string",
    keep_default_na=False  # Don't let pandas convert strings to nulls
)

def assert_all_columns_are_string(df: pd.DataFrame) -> None:
    """
    Assert that all columns were loaded using pandas 'string' dtype.
    """
    non_string_cols = df.dtypes[df.dtypes != "string"]
    assert non_string_cols.empty, (
        f"Non-string columns detected:\n{non_string_cols}"
    )

def assert_no_nulls_present(df: pd.DataFrame) -> None:
    """
    Assert that pandas did not implicitly convert any values to nulls.
    """
    null_count = df.isna().sum().sum()
    assert null_count == 0, f"Unexpected nulls found: {null_count}"

def assert_identifiers_preserved(df: pd.DataFrame, column: str) -> None:
    """
    Assert that identifier-like columns preserve raw string values,
    including empty strings and placeholders.
    """
    value_counts = df[column].value_counts(dropna=False)
    assert value_counts.index.isna().sum() == 0, (
        f"Null values detected in identifier column '{column}'"
    )

print(navarra_df.head())
print(navarra_df.dtypes)

# Assertions — Drill 01 guarantees
assert_all_columns_are_string(navarra_df)
assert_no_nulls_present(navarra_df)
assert_identifiers_preserved(navarra_df, "codpost")

print("passed: all columns are string, no nulls, identifiers preserved.")
