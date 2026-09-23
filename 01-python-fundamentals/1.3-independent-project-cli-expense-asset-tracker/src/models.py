"""
Data models for Expense and Asset records.
Uses clean dictionary representation for beginner clarity.
"""
from datetime import datetime

def create_expense(expense_id: int, date: str, category: str, amount: float, description: str) -> dict:
    return {
        "id": expense_id,
        "date": date,
        "category": category.strip().title(),
        "amount": round(float(amount), 2),
        "description": description.strip(),
    }

def create_asset(asset_id: int, name: str, category: str, value: float, acquisition_date: str) -> dict:
    return {
        "id": asset_id,
        "name": name.strip(),
        "category": category.strip().title(),
        "value": round(float(value), 2),
        "acquisition_date": acquisition_date,
    }
