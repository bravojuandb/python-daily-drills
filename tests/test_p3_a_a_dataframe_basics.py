import pytest
import pandas as pd

from pillar3.a_pandas_foundations_and_cleaning.a_dataframe_basics import (
    drill_01_create_and_inspect as create_and_inspect,
    drill_02_select_columns as select_columns,
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
    """expected shape and values, is a df, columns with supplied order """

    df = pd.DataFrame({
        "store_id": ["001", "002", "003"],
        "units": [4, 5, 6]
    })

    result = select_columns.select_columns(
        df, ["units", "store_id"]
    )

    result_one_col = select_columns.select_columns(
        df, ["store_id"]
    )

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

    df = pd.DataFrame({
        "store_id": ["001", "002", "003"],
        "units": [4, 5, 6]
    })

    with pytest.raises(KeyError):
        select_columns.select_columns(df, ["date"])
