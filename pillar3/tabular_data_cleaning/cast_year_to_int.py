"""
Drill 05 — Enforce year as nullable integer

Goal:
Apply correct numeric typing to year fields without losing information.

Rules:
- Convert the `anio` column using pd.to_numeric(errors="coerce")
- Cast the result to pandas nullable integer type (Int64)
- Preserve missing or invalid values as pd.NA
- Do not infer, fill, or impute missing years
- Do not modify non-year columns

Completion criteria:
- `anio` dtype is Int64
- Non-numeric or empty values become pd.NA
- No rows are dropped
- Transformation is explicit, minimal, and reversible
"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values
from .fix_cnae_cols import fix_cnae_columns
from .fix_portalt_col import fix_portalt_column

def enforce_year_to_integer(df: pd.DataFrame) -> pd.DataFrame:

    df["anio"] = pd.to_numeric(df["anio"], errors="coerce").astype("Int64")

    return df

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)

    df = fix_cnae_columns(df)
    df = fix_portalt_column(df)

    df = enforce_year_to_integer(df)

    print("passed: anio enforced as nullable Int64.")

