import pytest
from drill_1 import build_histogram

def test_regular_case():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    expected = {"apple": 3, "banana": 2, "orange": 1}
    assert build_histogram(words) == expected

def test_empty_list():
    assert build_histogram([]) == {}

def test_case_sensitivity():
    words = ["Apple", "apple", "APPLE"]
    expected = {"Apple": 1, "apple": 1, "APPLE": 1}
    assert build_histogram(words) == expected

def test_punctuation():
    words = ["yes", "yes!", "yes."]
    expected = {"yes": 1, "yes!": 1, "yes.": 1}
    assert build_histogram(words) == expected

def test_single_word_repeated():
    words = ["test"] * 5
    expected = {"test": 5}
    assert build_histogram(words) == expected