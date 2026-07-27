"""Tests for pillar2/b_core_processing_patterns.py"""

# Test for a_filter_active_records.py

from pillar2.b_core_processing_patterns.a_filter_active_records import filter_active


def test_filter_active_keeps_active_records():
    records = [
        {"id": 1, "name": "Ana", "status": "active"},
        {"id": 2, "name": "Luis", "status": "inactive"},
    ]

    expected = [records[0]]

    assert filter_active(records) == expected


def test_filter_active_keeps_upper_active_records():
    records = [{"id": 3, "name": "Marta", "status": "ACTIVE"}]
    expected = records

    assert filter_active(records) == expected


def test_filter_active_strips_whitespace():
    records = [{"id": 1, "status": " active "}]
    expected = records

    assert filter_active(records) == expected


def test_filter_active_handles_missing_status_key():
    records = [{"id": 4, "name": "Pedro"}]
    expected = []

    assert filter_active(records) == expected


def test_filter_active_preserves_order():
    records = [
        {"id": 1, "name": "Ana", "status": "active"},
        {"id": 2, "name": "Luis", "status": "inactive"},
        {"id": 3, "name": "Marta", "status": "ACTIVE"},
    ]
    expected = [records[0], records[2]]

    assert filter_active(records) == expected


def test_filter_active_does_not_mutate_input_records():
    records = [
        {"id": 1, "status": " active "},
        {"id": 2, "status": "inactive"},
    ]
    original = [record.copy() for record in records]

    filter_active(records)

    assert records == original
