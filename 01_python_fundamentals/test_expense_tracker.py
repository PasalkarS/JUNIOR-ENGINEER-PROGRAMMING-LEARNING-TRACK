"""
test_expense_tracker.py - Pytest suite for Expense Tracker and CSV Parsing logic.
"""

import os
import pytest
from expense_tracker import Expense, ExpenseTracker


def test_expense_valid_creation():
    exp = Expense(1, "2026-09-01", "Food", 24.50, "Lunch buffet")
    assert exp.expense_id == 1
    assert exp.date_str == "2026-09-01"
    assert exp.category == "Food"
    assert exp.amount == 24.50
    assert exp.description == "Lunch buffet"


def test_expense_invalid_amount():
    with pytest.raises(ValueError, match="Amount must be positive"):
        Expense(1, "2026-09-01", "Food", -10.0, "Negative amount")

    with pytest.raises(ValueError, match="Amount must be positive"):
        Expense(1, "2026-09-01", "Food", 0, "Zero amount")

    with pytest.raises(ValueError, match="Amount must be a valid number"):
        Expense(1, "2026-09-01", "Food", "not_a_number", "Bad type")


def test_expense_invalid_date():
    with pytest.raises(ValueError, match="Invalid date format"):
        Expense(1, "01-09-2026", "Food", 15.0, "Wrong format")

    with pytest.raises(ValueError, match="Invalid date format"):
        Expense(1, "2026/09/01", "Food", 15.0, "Slashes")


def test_parse_empty_csv(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("", encoding="utf-8")

    items, errors = ExpenseTracker.parse_csv_file(str(empty_file))
    assert items == []
    assert errors == []


def test_parse_missing_file(tmp_path):
    missing_file = tmp_path / "does_not_exist.csv"
    items, errors = ExpenseTracker.parse_csv_file(str(missing_file))
    assert items == []
    assert len(errors) == 1
    assert "File not found" in errors[0]


def test_parse_valid_csv_with_header(tmp_path):
    csv_file = tmp_path / "valid.csv"
    content = (
        "id,date,category,amount,description\n"
        "1,2026-09-01,Food,15.50,Sandwich\n"
        "2,2026-09-02,Transport,4.25,Train fare\n"
    )
    csv_file.write_text(content, encoding="utf-8")

    items, errors = ExpenseTracker.parse_csv_file(str(csv_file))
    assert len(errors) == 0
    assert len(items) == 2
    assert items[0].amount == 15.50
    assert items[1].category == "Transport"


def test_parse_malformed_rows_resilience(tmp_path):
    """Verify corrupted/malformed rows are skipped while valid rows are retained."""
    csv_file = tmp_path / "corrupt.csv"
    content = (
        "id,date,category,amount,description\n"
        "1,2026-09-01,Food,12.00,Good row 1\n"
        "bad_row_too_short\n"                      # Malformed: fewer than 3 cols
        "2,2026-09-02,Food,INVALID_AMT,Bad amount\n" # Malformed: invalid float
        "3,NOT_A_DATE,Food,20.00,Bad date\n"       # Malformed: invalid date
        "4,2026-09-03,Entertainment,-50.00,Neg\n"  # Malformed: negative amt
        "5,2026-09-04,Utilities,85.00,Electricity\n" # Good row 2
    )
    csv_file.write_text(content, encoding="utf-8")

    items, errors = ExpenseTracker.parse_csv_file(str(csv_file))
    # Should have extracted exactly 2 valid items (Good row 1, Good row 2)
    assert len(items) == 2
    assert items[0].description == "Good row 1"
    assert items[1].description == "Electricity"
    # 4 invalid rows caught and documented
    assert len(errors) == 4


def test_monthly_summary(tmp_path):
    tracker_file = tmp_path / "tracker.csv"
    tracker = ExpenseTracker(data_path=str(tracker_file))

    tracker.add(50.0, "Food", "Groceries", date_str="2026-09-01")
    tracker.add(20.0, "Food", "Coffee & Snacks", date_str="2026-09-05")
    tracker.add(30.0, "Transport", "Gas", date_str="2026-09-10")
    tracker.add(100.0, "Utilities", "Internet bill", date_str="2026-08-15")

    # Full summary
    summary = tracker.monthly_summary()
    assert summary["grand_total"] == 200.0
    assert summary["total_count"] == 4
    assert summary["monthly_totals"]["2026-09"] == 100.0
    assert summary["monthly_totals"]["2026-08"] == 100.0
    assert summary["by_category"]["2026-09"]["Food"] == 70.0

    # Filtered by month
    sep_summary = tracker.monthly_summary(month="2026-09")
    assert sep_summary["grand_total"] == 100.0
    assert sep_summary["total_count"] == 3


def test_add_and_delete(tmp_path):
    tracker_file = tmp_path / "tracker.csv"
    tracker = ExpenseTracker(data_path=str(tracker_file))

    e1 = tracker.add(10.0, "Food", "Snack")
    e2 = tracker.add(25.0, "Transport", "Bus pass")
    assert len(tracker.expenses) == 2

    # Delete existing
    assert tracker.delete(e1.expense_id) is True
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].expense_id == e2.expense_id

    # Delete non-existing
    assert tracker.delete(9999) is False
