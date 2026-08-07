from pillar2.c_searching_ordering_ranking.a_linear_search import linear_search


def test_linear_search_returns_first_occurrence():
    assert linear_search([2, 4, 6, 8, 6], 6) == 2


def test_linear_search_returns_expected_for_absent_target():
    assert linear_search([2, 4, 6, 8, 6], 5) == -1


def test_linear_search_returns_minus_one_for_empty_list():
    assert linear_search([], 6) == -1
