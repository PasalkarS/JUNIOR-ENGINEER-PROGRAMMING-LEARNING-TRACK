"""
Simple Tests for Expense Tracker - Beginner Friendly
Tests the core CSV parsing and expense logic.
"""

import os
import pytest
from expense_tracker import add_expense, delete_expense, parse_row, get_monthly_summary, load_expenses, save_expenses


def test_add_expense_basic():
    expenses = []
    item = add_expense(expenses, "Food", 25.50, "Lunch")
    assert item["category"] == "Food"
    assert item["amount"] == 25.50
    assert len(expenses) == 1


def test_add_expense_invalid_amount():
    expenses = []
    with pytest.raises(ValueError):
        add_expense(expenses, "Food", -10, "Bad amount")

    with pytest.raises(ValueError):
        add_expense(expenses, "Food", 0, "Zero amount")


def test_add_expense_empty_category():
    expenses = []
    with pytest.raises(ValueError):
        add_expense(expenses, "   ", 10.0, "No category")


def test_delete_expense():
    expenses = []
    add_expense(expenses, "Food", 10.0, "Coffee")
    add_expense(expenses, "Travel", 50.0, "Bus")

    assert delete_expense(expenses, 1) is True
    assert len(expenses) == 1

    # Deleting something that doesn't exist
    assert delete_expense(expenses, 999) is False


def test_parse_row_valid():
    row = ["1", "2026-09-01", "Food", "20.00", "Breakfast"]
    result = parse_row(row)
    assert result is not None
    assert result["amount"] == 20.00
    assert result["category"] == "Food"


def test_parse_row_too_short():
    # Too few columns - should return None, not crash
    row = ["1", "2026-09-01"]
    result = parse_row(row)
    assert result is None


def test_parse_row_bad_amount():
    # Non-numeric amount - should return None
    row = ["1", "2026-09-01", "Food", "not_a_number", "Lunch"]
    result = parse_row(row)
    assert result is None


def test_parse_row_negative_amount():
    # Negative amount - should return None
    row = ["1", "2026-09-01", "Food", "-5.00", "Invalid"]
    result = parse_row(row)
    assert result is None


def test_monthly_summary():
    expenses = []
    add_expense(expenses, "Food", 20.0, "Lunch", date="2026-09-01")
    add_expense(expenses, "Food", 15.0, "Dinner", date="2026-09-05")
    add_expense(expenses, "Travel", 40.0, "Bus pass", date="2026-09-10")

    summary = get_monthly_summary(expenses)
    assert "2026-09" in summary
    assert summary["2026-09"]["total"] == 75.0
    assert summary["2026-09"]["by_category"]["Food"] == 35.0
    assert summary["2026-09"]["by_category"]["Travel"] == 40.0


def test_empty_file_loads_cleanly(tmp_path):
    # Edge case: load from an empty file - should return empty list without crashing
    empty_file = str(tmp_path / "empty.csv")
    open(empty_file, "w").close()  # create empty file

    result = load_expenses(empty_file)
    assert result == []


def test_save_and_reload(tmp_path):
    filepath = str(tmp_path / "test_expenses.csv")
    expenses = []
    add_expense(expenses, "Food", 30.0, "Groceries", date="2026-09-01")
    add_expense(expenses, "Bills", 100.0, "Internet", date="2026-09-02")

    save_expenses(expenses, filepath)

    loaded = load_expenses(filepath)
    assert len(loaded) == 2
    assert loaded[0]["category"] == "Food"
    assert loaded[1]["amount"] == 100.0
