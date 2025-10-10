"""
Comprehensive test suite for detect_duplicates()
Module under test:
    pillar2.foundational_algorithms.detecting_duplicates
"""

import pytest
from pillar2.foundational_algorithms.detecting_duplicates import detect_duplicates


# --- 1. Basic correctness -----------------------------------------------------

def test_duplicates_present():
    """Should return True when at least one duplicate exists."""
    items = [1, 2, 3, 4, 4, 6]
    assert detect_duplicates(items) is True


def test_no_duplicates():
    """Should return False when all elements are unique."""
    items = [1, 2, 3, 4, 5, 6]
    assert detect_duplicates(items) is False


# --- 2. Edge cases ------------------------------------------------------------

def test_empty_list():
    """Empty list has no duplicates."""
    assert detect_duplicates([]) is False


def test_single_element():
    """A single element cannot have duplicates."""
    assert detect_duplicates(["apple"]) is False


def test_two_identical_elements():
    """Two identical elements are a duplicate."""
    assert detect_duplicates(["x", "x"]) is True


# --- 3. Mixed data types ------------------------------------------------------

def test_mixed_types_with_duplicates():
    """Detect duplicates across mixed hashable types."""
    data = [1, "1", 1.0]  # 1 == 1.0 in Python
    # set({1, "1"}) has len 2, list has len 3 → still a duplicate due to 1 == 1.0
    assert detect_duplicates(data) is True


def test_mixed_types_no_duplicates():
    """Distinct objects across different types."""
    data = ["1", 1, (1,)]
    assert detect_duplicates(data) is False


# --- 4. Case sensitivity (string lists) --------------------------------------

def test_case_sensitivity():
    """'Apple' and 'apple' are different strings."""
    items = ["Apple", "apple"]
    assert detect_duplicates(items) is False


# --- 5. Large input performance sanity check ---------------------------------

def test_large_input():
    """Should handle large lists efficiently."""
    data = list(range(10_000)) + [9999]  # only last is a duplicate
    assert detect_duplicates(data) is True


# --- 6. Non-hashable items (should raise TypeError) ---------------------------

def test_unhashable_items():
    """Lists are unhashable; function should raise TypeError."""
    with pytest.raises(TypeError):
        detect_duplicates([[1], [1]])


# --- 7. Boolean edge case -----------------------------------------------------

def test_boolean_equivalence():
    """True == 1 and False == 0, so should count as duplicates."""
    assert detect_duplicates([True, 1, False, 0]) is True