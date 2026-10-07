import pandas as pd
import pytest

from pillar3.a_pandas_foundations_and_cleaning.a_dataframe_basics import (
    drill_01_create_and_inspect as create_and_inspect,
    drill_02_select_columns as select_columns,
    drill_03_filter_rows as filter_rows,
    drill_04_read_csv_as_strings as read_csv,
)


def test_create_inventory_returns_dataframe():
    result = create_and_inspect.create_inventory(["001", "002"], [4, 0])

    assert isinstance(result, pd.DataFrame)


def test_create_inventory_preserves_values():
    """Verify values, column names/order, and a zero-based RangeIndex with step 1."""
    result = create_and_inspect.create_inventory(["001", "002"], [4, 0])

    assert list(result.columns) == ["store_id", "units"]
    assert result["store_id"].tolist() == ["001", "002"]
    assert result["units"].tolist() == [4, 0]
    assert isinstance(result.index, pd.RangeIndex)
    assert result.index.start == 0
    assert result.index.stop == 2
    assert result.index.step == 1


def test_create_inventory_returns_expected_with_empty_lists():
    result = create_and_inspect.create_inventory([], [])

    assert result.shape == (0, 2)
    assert list(result.columns) == ["store_id", "units"]
    assert result["store_id"].tolist() == []
    assert result["units"].tolist() == []


def test_select_columns_returns_expected():
    """Verify DataFrame shape, values, and requested column order."""

    df = pd.DataFrame({"store_id": ["001", "002", "003"], "units": [4, 5, 6]})

    result = select_columns.select_columns(df, ["units", "store_id"])

    result_one_col = select_columns.select_columns(df, ["store_id"])

    assert result.shape == (3, 2)
    assert result["units"].tolist() == [4, 5, 6]
    assert result["store_id"].tolist() == ["001", "002", "003"]
    assert list(df.columns) == ["store_id", "units"]
    assert list(result.columns) == ["units", "store_id"]
    assert isinstance(result, pd.DataFrame)

    assert result_one_col.shape == (3, 1)
    assert list(result_one_col.columns) == ["store_id"]
    assert isinstance(result_one_col, pd.DataFrame)


def test_select_columns_empty_selection_preserves_index():
    """Selecting no columns preserves the original row labels and their order."""
    df = pd.DataFrame(
        {"store_id": ["001", "002", "003"], "units": [4, 5, 6]},
        index=[10, 30, 20],
    )

    result = select_columns.select_columns(df, [])

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 0)
    assert result.index.tolist() == [10, 30, 20]


def test_select_column_raises_KeyError_for_absent_column():
    df = pd.DataFrame({"store_id": ["001", "002", "003"], "units": [4, 5, 6]})

    with pytest.raises(KeyError):
        select_columns.select_columns(df, ["date"])


def test_filter_units_returns_expected():
    """Verify selected values, column names, and original row labels/order."""
    df = pd.DataFrame({"units": [4, 0, 4]}, index=[10, 30, 20])

    expected_column_names = ["units"]
    expected_values = [4, 4]
    expected_indexes = [10, 20]

    result = filter_rows.filter_units(df, 4)

    assert list(result.columns) == expected_column_names
    assert result["units"].tolist() == expected_values
    assert result.index.tolist() == expected_indexes


def test_filter_units_no_matches_returns_empty_table():
    """No matching rows leaves the column present and the row index empty."""
    df = pd.DataFrame({"units": [4, 0, 4]}, index=[10, 30, 20])

    result = filter_rows.filter_units(df, 5)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (0, 1)
    assert result.columns.tolist() == ["units"]
    assert result.index.tolist() == []


def test_read_csv_as_strings_returns_expected(tmp_path):
    """Verify CSV fields retain their text, including leading zeros, whitespace,
    quoted commas, empty strings, and NA literals, with string dtype in every column.
    """

    csv_path = tmp_path / "inventory.csv"
    csv_path.write_text(
        'store_id,units,note\n'
        '001,4,NA\n'
        '002,0,NULL\n'
        '003,,"  Keep these spaces  "\n'
        '004,12,"Delivery, morning"\n'
        '005,7,\n',
        encoding="utf-8"
    )

    result = read_csv.read_csv_as_strings(csv_path)


    assert result["store_id"].tolist() == ["001", "002", "003", "004", "005"]
    assert result["units"].tolist() == ["4", "0", "", "12", "7"]
    assert result["note"].tolist() == ["NA", "NULL", "  Keep these spaces  ", "Delivery, morning", ""]
    assert all(dtype == "string" for dtype in result.dtypes)
    assert not result.isna().any().any()


def test_read_csv_as_strings_returns_zero_rows_for_header_only_csv(tmp_path):

    csv_path = tmp_path / "header-only_inventory.csv"

    csv_path.write_text(
        'store_id,units,note\n',
        encoding="utf-8"
    )

    result = read_csv.read_csv_as_strings(csv_path)
    assert result.columns.tolist() == ["store_id", "units", "note"]
    assert result.shape == (0, 3)
    assert all(dtype == "string" for dtype in result.dtypes)