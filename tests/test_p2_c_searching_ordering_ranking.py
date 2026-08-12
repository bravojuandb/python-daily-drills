from pillar2.c_searching_ordering_ranking.a_linear_search import linear_search
from pillar2.c_searching_ordering_ranking.b_binary_search import binary_search


def test_linear_search_returns_first_occurrence():
    assert linear_search([2, 4, 6, 8, 6], 6) == 2


def test_linear_search_returns_expected_for_absent_target():
    assert linear_search([2, 4, 6, 8, 6], 5) == -1


def test_linear_search_returns_minus_one_for_empty_list():
    assert linear_search([], 6) == -1


# Test for b_binary_search.py


def test_binary_search_returns_minus_one_for_not_present_target():
    items = [0, 1, 2, 7, 23, 34, 45]
    target = 56
    assert binary_search(items, target) == -1


def test_binary_search_finds_first_item():
    items = [0, 1, 2, 7, 23, 34, 45]
    assert binary_search(items, 0) == 0


def test_binary_search_finds_middle_item():
    items = [0, 1, 2, 7, 23, 34, 45]
    assert binary_search(items, 7) == 3


def test_binary_search_finds_one_occurrence_when_duplicates_exist():
    items = [1, 2, 2, 2, 3]
    result = binary_search(items, 2)

    assert result in (1, 2, 3)
    assert items[result] == 2


def test_binary_search_works_with_negative_numbers():
    items = [-20, -10, -3, 0, 8]
    assert binary_search(items, -10) == 1