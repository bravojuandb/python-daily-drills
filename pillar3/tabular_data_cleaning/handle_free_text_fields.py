"""
Drill 07 — Minimal cleaning of free-text fields

Goal:

- Enforce string dtype for all free-text columns
- Assert those columns are strings
- Assert no leading/trailing whitespaces in htese columns.

Notes: 
- All columns were originally read as string dtype, for safety
- str.strip() was already applied in drill 2

"""

from pathlib import Path
import pandas as pd

from .read_csv import read_registry
from .normalize_csv import normalize_registry
from .handle_nulls import handle_missing_values
from .fix_cnae_cols import fix_cnae_columns
from .fix_portalt_col import fix_portalt_column
from .cast_year_to_int import enforce_year_to_integer
from .preserve_codes_as_strings import preserve_identifiers

def ensure_string_columns(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Ensure selected columns use pandas string dtype
    """
    for col in cols:
        if col in df.columns and not pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].astype("string")
    return df

def assert_columns_are_string(df: pd.DataFrame, cols: list[str]) -> None:
    non_string = [
        col for col in cols
        if col in df.columns and not pd.api.types.is_string_dtype(df[col])
    ]
    assert not non_string, f"Non-string columns detected: {non_string}"

def assert_no_edge_whitespace(df: pd.DataFrame, cols: list[str]) -> None:
    subset = df[cols].dropna()
    has_edge_ws = subset.apply(
        lambda s: s.str.match(r"^\s|\s$", na=False)
    ).any().any()

    assert not has_edge_ws, "Leading/trailing whitespace detected"

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "navarra_trimmed.csv"

if __name__ == "__main__":

    text_cols = [
        "nombre",
        "callet",
        "nombre_cmun",
        "cnae09_descrip_ppal",
        "cnae09_descrip_local",
        "denominacion_entidad",
    ]
        
    df = read_registry(FILE_PATH)
    df = normalize_registry(df)
    df = handle_missing_values(df)
    df = fix_cnae_columns(df)
    df = fix_portalt_column(df)
    df = enforce_year_to_integer(df)
    df = preserve_identifiers(df, verbose=False)

    df = ensure_string_columns(df, text_cols)

    assert_columns_are_string(df, text_cols)
    assert_no_edge_whitespace(df, text_cols)

    # Quick sanity checks
    print("\nDtypes:\n", df.dtypes)
    print("\nSample rows:\n", df.head(5))
