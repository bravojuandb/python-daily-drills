import pandas as pd


from pillar3.a_pandas_foundations_and_cleaning.b_missing_values_and_text import(
    drill_01_trim_and_normalize_blanks as trim_and_normalize,
)
def test_trim_and_normalize_blanks_returns_expected():
    example = pd.Series(
        ["  North  Hub  ", "\n", "", "\t", pd.NA, "0", "NA"], 
        dtype="string", 
        name= "location")

    result = trim_and_normalize.trim_and_normalize_blanks(example)

    expected = pd.Series(
        ["North  Hub", pd.NA, pd.NA, pd.NA, pd.NA, "0", "NA"], 
        dtype="string", 
        name= "location")

    pd.testing.assert_series_equal(result, expected)
    assert isinstance(result, pd.Series)
    assert result.name == example.name
    assert list(result.index) == list(example.index)


def test_trim_and_nomalize_blanks_returns_empty_when_empty():
    example = pd.Series(
        [], 
        dtype="string", 
        name= "location")

    result = trim_and_normalize.trim_and_normalize_blanks(example)

    expected = pd.Series(
        [], 
        dtype="string", 
        name= "location")

    pd.testing.assert_series_equal(result, expected)
    assert isinstance(result, pd.Series)
    assert result.name == example.name
    assert list(result.index) == list(example.index)
