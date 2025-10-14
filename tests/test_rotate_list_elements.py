import pytest
from pillar2.patterns_on_lists.rotate_list_elements import rotate_to_the_right

@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([10, 20, 30, 40, 50], 1, [50, 10, 20, 30, 40]),
        ([10, 20, 30, 40, 50], 2, [40, 50, 10, 20, 30]),
        ([10, 20, 30, 40, 50], 5, [10, 20, 30, 40, 50]),     # k == len(nums)
        ([10, 20, 30, 40, 50], 10, [10, 20, 30, 40, 50]),    # k > len(nums)
        ([10, 20, 30, 40, 50], 0, [10, 20, 30, 40, 50]),     # k == 0
        ([1], 3, [1]),                                       # single element
        ([], 3, []),                                         # empty list
        ([1, 2, 3, 4], -1, [2, 3, 4, 1]),                    # negative k (normalized)
    ]
)
def test_rotate_right_happy_paths(nums, k, expected):
    assert rotate_to_the_right(nums, k) == expected


@pytest.mark.parametrize(
    "nums,k,exc",
    [
        ("not-a-list", 2, TypeError),
        ([1, 2, 3], "2", TypeError),
    ]
)
def test_rotate_right_type_errors(nums, k, exc):
    with pytest.raises(exc):
        rotate_to_the_right(nums, k)