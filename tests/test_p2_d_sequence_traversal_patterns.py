import pytest
from pillar2.d_sequence_traversal_patterns.a_two_pointer_pair_sum import (
    has_pair_with_sum,
)
from pillar2.d_sequence_traversal_patterns.c_fixed_sliding_window import (
    max_window_sum,
)


def test_has_pair_with_sum_returns_true():
    true_cases = {
        "finds a pair at opposite ends": ([1, 2, 4, 7, 11], 12),
        "finds a non-consecutive pair": ([1, 2, 4, 7, 11], 9),
        "allows equal values at different indices": ([3, 3, 8], 6),
    }

    for case_name, (numbers, target) in true_cases.items():
        assert has_pair_with_sum(numbers, target) is True, case_name


def test_has_pair_with_sum_returns_false():
    false_cases = {
        "returns false when no pair has the target sum": ([1, 2, 4, 7, 11], 10),
        "does not pair a value with itself": ([3], 6),
        "returns false for an empty list": ([], 0),
    }

    for case_name, (numbers, target) in false_cases.items():
        assert has_pair_with_sum(numbers, target) is False, case_name


def test_max_window_sum_returns_greatest_sum():
    assert max_window_sum([1, 4, 5, 2], 2) == 9


def test_max_window_sum_handles_negative_numbers():
    assert max_window_sum([-5, -2, -3, -8], 2) == -5


def test_max_window_sum_handles_size_one():
    assert max_window_sum([3, -2, 7, 1], 1) == 7


def test_max_window_sum_handles_whole_list():
    assert max_window_sum([3, -2, 7, 1], 4) == 9


def test_max_window_sum_rejects_invalid_sizes():
    for size in (-1, 0, 4):
        with pytest.raises(ValueError):
            max_window_sum([1, 2, 3], size)
