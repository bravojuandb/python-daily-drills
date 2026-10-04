import pytest
import pandas as pd

from pillar3.a_pandas_foundations_and_cleaning.a_dataframe_basics import (
    drill_01_create_and_inspect as create_and_inspect,
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


