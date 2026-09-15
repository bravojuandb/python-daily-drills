from pillar2.d_sequence_traversal_patterns.a_two_pointer_pair_sum import (
    has_pair_with_sum,
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

