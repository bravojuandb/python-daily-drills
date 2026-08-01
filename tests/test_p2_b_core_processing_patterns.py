"""Tests for pillar2/b_core_processing_patterns.py"""

from pillar2.b_core_processing_patterns.a_filter_active_records import filter_active
from pillar2.b_core_processing_patterns.b_normalize_records import normalize_users
from pillar2.b_core_processing_patterns.c_reduce_transaction_totals import total_paid
from pillar2.b_core_processing_patterns.d_count_frequencies import count_frequencies
from pillar2.b_core_processing_patterns.e_group_records import group_by_department


# Test for a_filter_active_records.py

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


# Test for b_normalilze_records.py

def test_normalize_user_returns_new_dictionaries():
    records = [
    {
        "name": "  juan bravo  ",
        "email": "  JUAN.BRAVO@EXAMPLE.COM  ",
        "country": "  spain  ",
    },
    {
        "name": "mARÍA lópez",
        "email": " Maria.Lopez@Example.com ",
        "country": "colombia",
    },
    {
        "name": "  anna kowalska",
        "email": "ANNA.KOWALSKA@EXAMPLE.COM",
        "country": "  poland ",
    },
    ]
    normalized = normalize_users(records)

    assert normalized is not records
    assert all(
        norm_record is not orig_record 
        for norm_record, orig_record 
        in zip(normalized, records)
    )

def test_normalize_returns_normalized_dicts_in_same_order():
    records = [
        {
            "name": "  juan bravo  ",
            "email": "  JUAN.BRAVO@EXAMPLE.COM  ",
            "country": "  spain  ",
        },
        {
            "name": "  anna kowalska",
            "email": "ANNA.KOWALSKA@EXAMPLE.COM",
            "country": "  poland ",
        },
    ]
    normalized = normalize_users(records)
    assert normalized[0] == {
        "name": "Juan Bravo",
        "email": "juan.bravo@example.com",
        "country": "SPAIN",
    }
    assert normalized[1] == {
        "name": "Anna Kowalska",
        "email": "anna.kowalska@example.com",
        "country": "POLAND",
    }

# Test for c_reduce_transaction_totals.py

def test_reduce_transactions_return_float_with_empty_input():
    transactions = []
    assert total_paid(transactions) == 0.0


def test_reduce_transactions_sums_only_paid_amounts():
    transactions = [
        {"id": "1", "status": "paid", "amount": "34.0"},
        {"id": "2", "status": "pending", "amount": "56"},
        {"id": "3", "status": "paid", "amount": "23"},
        {"id": "4", "status": "", "amount": "45"},
    ]

    assert total_paid(transactions) == 57.0


# Test for d_count_frequencies.py

def test_count_frequencies_returns_expected():
    items = ["pen", "notebook", "pen", "stapler", "notebook", "pen"]

    assert count_frequencies(items) == {
        "pen": 3,
        "notebook": 2,
        "stapler": 1,
    }


def test_count_frequencies_preserve_order():
    items = ["notebook", "pen", "notebook", "stapler", "pen"]

    assert list(count_frequencies(items)) == ["notebook", "pen", "stapler"]

# Test for e_group_records.py

def test_group_by_department_groups_records_under_department_keys():

    employees = [
        {"id": 101, "name": "Ana", "department": "Engineering", "level": "Senior"},
        {"id": 102, "name": "Luis", "department": "Sales", "level": "Junior"},
        {"id": 103, "name": "Marta", "department": "Engineering", "level": "Junior"},
        {"id": 104, "name": "Omar", "department": "Finance", "level": "Senior"},
        {"id": 105, "name": "Sofia", "department": "Sales", "level": "Senior"},
        {"id": 106, "name": "Diego", "department": "Engineering", "level": "Mid"},
        {"id": 107, "name": "Elena", "department": "Finance", "level": "Junior"},
    ]

    expected = {
        "Engineering": [
            {"id": 101, "name": "Ana", "department": "Engineering", "level": "Senior"},
            {"id": 103, "name": "Marta", "department": "Engineering", "level": "Junior"},
            {"id": 106, "name": "Diego", "department": "Engineering", "level": "Mid"},
        ],
        "Sales": [
            {"id": 102, "name": "Luis", "department": "Sales", "level": "Junior"},
            {"id": 105, "name": "Sofia", "department": "Sales", "level": "Senior"},
        ],
        "Finance": [
            {"id": 104, "name": "Omar", "department": "Finance", "level": "Senior"},
            {"id": 107, "name": "Elena", "department": "Finance", "level": "Junior"},
        ],
    }
    result = group_by_department(employees)

    assert result == expected


def test_group_by_department_preserves_first_department_appearance():

    employees = [
        {"id": 101, "department": "Engineering"},
        {"id": 102, "department": "Sales"},
        {"id": 103, "department": "Engineering"},
        {"id": 104, "department": "Finance"},
        {"id": 105, "department": "Sales"},
        {"id": 106, "department": "Engineering"},
        {"id": 107, "department": "Finance"},
    ]

    result = group_by_department(employees)

    assert employees[0]["department"] == next(iter(result))