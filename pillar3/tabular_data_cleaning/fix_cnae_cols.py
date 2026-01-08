"""
Drill 04 — Remove trailing `.0` from code-like columns

Goal:  
Fix formatting artifacts introduced by numeric parsing without changing meaning.

Problem:  
CNAE codes are defined as integer identifiers with no decimals by standard.
CNAE = Clasificación Nacional de Actividades Económicas

Rules (strict):
- Apply only to cnae columns (e.g. `cnae09_ppal`, `cnae09_local`)
- Remove only a trailing `.0`
- Keep dtype as pandas `string`
- Missing values (`pd.NA`) must remain untouched

Expected transformation:
- `"6910.0"` → `"6910"`
- `"7320"` → `"7320"`
- `"7.0"` → `"7"` 
- `"7.5"` → unchanged
- `pd.NA` → `pd.NA`

Note: column "portalt" has a similar issue. It contains trailing .0 
and the normalization of this column belongs to  drill 04.1

"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values

def fix_cnae_columns(df: pd.DataFrame) -> pd.DataFrame:
    "Remove the suffix .0 from cnae columns"

    cnae_cols = ["cnae09_ppal", "cnae09_local"]

    for col in cnae_cols:
        if col in df.columns:
            df[col] = df[col].str.replace(r"\.0$", "", regex=True)

    return df

def assert_fix_cnae_cols(df: pd.DataFrame, col: str) -> None:
    """Assert no non-missing values end with the suffix '.0' in the given column."""
    if col not in df.columns:
        return
    suffix_count = df[col].dropna().str.endswith(".0").sum()
    assert suffix_count == 0, f"Found {suffix_count} values still ending with '.0' in '{col}'"

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)

    df = fix_cnae_columns(df)

    assert_fix_cnae_cols(df, "cnae09_ppal")
    assert_fix_cnae_cols(df, "cnae09_local")

    print("passed: trailing '.0' removed from cnae columns.")

    print(df.head())
