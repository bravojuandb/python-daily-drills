"""Tests for pillar2/a_data_structure_selection"""

import pytest

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


# Test for c_unique_normalized_tags.py

from pillar2.a_data_structure_selection.c_unique_tags import unique_normalized_tags

def test_function_normalization_and_uniqueness():
    tags = [" Python ", "python   ", "ETL", "", "    "]
    result = unique_normalized_tags(tags)
    assert result == {"python", "etl"}

def test_function_returns_empty_set_for_empty_list():
    assert unique_normalized_tags([]) == set()



# Test for d_id_lookup_index.py

from pillar2.a_data_structure_selection.d_id_lookup_index import index_by_id


def test_index_by_id_builds_lookup_without_mutating_records():
    records = [
        {"id": 7, "name": "Ada", "role": "engineer"},
        {"id": 12, "name": "Grace", "role": "admiral"},
        {"id": 3, "name": "Linus", "role": "engineer"},
    ]
    original = [record.copy() for record in records]

    result = index_by_id(records)

    assert result == {7: records[0], 12: records[1], 3: records[2]}
    assert records == original


def test_index_by_id_returns_empty_dict_for_empty_input():
    assert index_by_id([]) == {}


def test_index_by_id_rejects_duplicate_ids():
    records = [{"id": 7, "name": "Ada"}, {"id": 7, "name": "Grace"}]

    with pytest.raises(ValueError, match="Repeated ID"):
        index_by_id(records)


# Test for e_composite_key_totals.py 


from pillar2.a_data_structure_selection.e_composite_key_totals import aggregate_sales

def test_aggregate_sales_return_aggregated_result():

    sales = [
        ("north", "pen", 2),
        ("north", "pen", 4),
        ("south", "notebook", 3),
    ]
    result = aggregate_sales(sales)

    assert result == {
        ("north", "pen"): 6,
        ("south", "notebook"): 3,
    }

def test_aggregate_sales_returns_empty_dict():
    assert aggregate_sales([]) == {}