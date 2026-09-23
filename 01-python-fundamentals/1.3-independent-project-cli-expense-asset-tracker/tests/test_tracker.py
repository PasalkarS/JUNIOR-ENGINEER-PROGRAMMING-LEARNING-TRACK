"""
Unit tests for CLI Expense and Asset Tracker.
"""
import pytest
from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path in sys.path:
    sys.path.remove(src_path)
sys.path.insert(0, src_path)

for mod in ["models", "validation", "storage", "reports"]:
    sys.modules.pop(mod, None)

from models import create_expense, create_asset
from validation import validate_amount, validate_date, validate_text, ValidationError
from storage import load_expenses, save_expenses, load_assets, save_assets
from reports import calculate_expense_summary, calculate_asset_summary, calculate_net_worth_overview

def test_models():
    exp = create_expense(1, "2026-09-01", "food", 15.5, "Lunch")
    assert exp["category"] == "Food"
    assert exp["amount"] == 15.50

    ast = create_asset(1, "Laptop", "tech", 1200.0, "2026-01-01")
    assert ast["name"] == "Laptop"
    assert ast["value"] == 1200.0

def test_validation():
    assert validate_amount("45.50") == 45.50
    with pytest.raises(ValidationError):
        validate_amount("-10")
    with pytest.raises(ValidationError):
        validate_amount("abc")

    assert validate_date("2026-09-20") == "2026-09-20"
    with pytest.raises(ValidationError):
        validate_date("not-a-date")

    assert validate_text("  Valid Text  ", "field") == "Valid Text"
    with pytest.raises(ValidationError):
        validate_text("   ", "field")

def test_storage(tmp_path):
    exp_file = tmp_path / "exp.csv"
    expenses = [create_expense(1, "2026-09-01", "Food", 20.0, "Lunch")]
    save_expenses(expenses, exp_file)
    loaded = load_expenses(exp_file)
    assert len(loaded) == 1
    assert loaded[0]["amount"] == 20.0

def test_reports():
    expenses = [
        create_expense(1, "2026-09-01", "Food", 30.0, "Groceries"),
        create_expense(2, "2026-09-05", "Food", 20.0, "Dinner"),
        create_expense(3, "2026-09-10", "Transport", 50.0, "Fuel"),
    ]
    assets = [
        create_asset(1, "Car", "Vehicle", 5000.0, "2025-01-01"),
    ]
    exp_sum = calculate_expense_summary(expenses)
    assert exp_sum["total_expenses"] == 100.0
    assert exp_sum["by_category"]["Food"] == 50.0

    ast_sum = calculate_asset_summary(assets)
    assert ast_sum["total_asset_value"] == 5000.0

    overview = calculate_net_worth_overview(expenses, assets)
    assert overview["net_balance"] == 4900.0
