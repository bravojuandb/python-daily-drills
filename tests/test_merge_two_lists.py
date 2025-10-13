import builtins
from typing import Any
import pytest


from pillar2.patterns_on_lists.merge_two_lists import merge_lists

@pytest.mark.parametrize(
    "keys, vals, expected",
    [
        (["Alice", "Bob", "Charlie"], [85, 92, 78],
         ["Alice", 85, "Bob", 92, "Charlie", 78]),
        (["A", "B", "C", "D"], [1, 2, 3],
         ["A", 1, "B", 2, "C", 3, "D"]),
        (["X", "Y"], [10, 20, 30, 40],
         ["X", 10, "Y", 20, 30, 40]),
        ([], [], []),
    ],
)
def test_merge_lists_basic(keys, vals, expected):
    out = merge_lists(keys, vals)
    assert out == expected


def test_inputs_not_mutated():
    keys = ["k1", "k2", "k3"]
    vals = [100, 200]
    keys_snapshot = list(keys)
    vals_snapshot = list(vals)

    _ = merge_lists(keys, vals)

    assert keys == keys_snapshot, "keys list was mutated"
    assert vals == vals_snapshot, "vals list was mutated"


def test_non_string_keys_still_supported():
    # Function should be agnostic to element types
    keys: list[Any] = [1, 2, 3]
    vals = [10, 20]
    out = merge_lists(keys, vals)
    assert out == [1, 10, 2, 20, 3]


def test_notice_on_different_lengths(capsys):
    keys = ["A", "B", "C"]
    vals = [1, 2]
    _ = merge_lists(keys, vals)
    captured = capsys.readouterr()
    # Accept either exact or case-insensitive contains depending on your implementation
    assert "different" in captured.out.lower()
    assert "length" in captured.out.lower()


def test_large_input_performance_sanity():
    # Not a strict perf test, just sanity for larger sizes
    n, m = 500, 300
    keys = [f"k{i}" for i in range(n)]
    vals = list(range(m))
    out = merge_lists(keys, vals)
    # Length should be n + m
    assert len(out) == n + m
    # Order should be alternating while both have elements
    assert out[0] == "k0" and out[1] == 0
    assert out[2] == "k1" and out[3] == 1
    # Tail should contain remaining keys once vals are exhausted
    assert out[-1] == f"k{n-1}"