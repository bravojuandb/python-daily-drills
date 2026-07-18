"""Tests for pillar2/a_data_structure_selection"""

# Test for a_ordered_event_log.py

from pillar2.a_data_structure_selection.a_ordered_event_log import append_event

def test_append_event_adds_event():
    appended = append_event(["2", "4", "6"], "Event")

    assert appended == ["2", "4", "6", "Event"]

def test_append_event_does_not_modify_original_list():
    original = ["2", "4", "6"]
    appended = append_event(original, "Event")

    assert original == ["2", "4", "6"]
    assert appended is not original

def test_append_event_adds_event_to_empty_list():
    appended = append_event([], "Event")

    assert appended == ["Event"]

def test_append_event_preserves_duplicates():
    original = ["a", "b", "a"]
    appended = append_event(original, "a")

    assert appended == ["a", "b", "a", "a"]


# Test for b_inmutable_coordinate_records.py

from pillar2.a_data_structure_selection.b_immutable_coordinate_records import make_coordinate, move_coordinate

def test_input_tuple_remains_immutable():
    original = 1, 1, "B"

    moved = move_coordinate(original, 2, 2)
    
    assert moved == (3, 3, "B")
    assert original == (1, 1, "B")
    assert moved is not original
