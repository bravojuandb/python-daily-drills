"""
Tests for pillar2/1_data_structure_selection
"""

# Test for 01_ordered_event_log.py

from pillar2 import append_event

"""
Test accoding to expected behaviour of the function:

- The function intends to append a string to an existing list. 
- Function appends an element to an empty list
- Function returns a new list, not the original list mutated

"""
def test_append_event_adds_event():
    appended = append_event(["2", "4", "6"], "Event")

    assert appended == ["2", "4", "6", "Event"]

def test_append_event_returns_does_not_modify_original_list():
    original = ["2", "4", "6"]
    appended = append_event(original, "Event")

    assert original == ["2", "4", "6"]

def test_append_event_adds_event_to_empty_list():
    appended = append_event([], "Event")

    assert appended == ["Event"]
