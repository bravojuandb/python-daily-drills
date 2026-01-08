"""
Drill 04.1 — Normalize address portal numbers

Goal:  
Enforce domain rules for address portal numbers (portalt colum) without affecting free-text values.

- Apply the rule: portal numbers must be integers (no decimals)
- Remove trailing `.0` from numeric portal values (e.g. `"6.0"` → `"6"`)
- Do **not** modify non-numeric tokens (`"PBJ"`, `"BAJO"`, `"ENT"`, etc.)
- Preserve original meaning of address components

"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values
from .fix_cnae_cols import fix_cnae_columns

def fix_portalt_column(df: pd.DataFrame) -> pd.DataFrame:
    "Remove the suffix .0 from portalt column"

    df["portalt"] = df["portalt"].str.replace(r"\.0$", "", regex=True)

    return df

def assert_fix_portalt_col(df: pd.DataFrame, col: str) -> None:
    """Assert no non-missing values end with the suffix '.0' in the given column."""

    suffix_count = df[col].dropna().str.endswith(".0").sum()
    assert suffix_count == 0, f"Found {suffix_count} values still ending with '.0' in '{col}'"

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)

    df = fix_cnae_columns(df)
    df = fix_portalt_column(df)

    assert_fix_portalt_col(df, "portalt")

    print("passed: trailing '.0' removed from portalt column.")
