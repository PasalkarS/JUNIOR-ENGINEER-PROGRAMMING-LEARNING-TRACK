"""
CSV file persistence for expenses and assets.
"""
import csv
from pathlib import Path
from models import create_expense, create_asset

EXPENSE_HEADERS = ["id", "date", "category", "amount", "description"]
ASSET_HEADERS = ["id", "name", "category", "value", "acquisition_date"]

def load_expenses(filepath: str | Path) -> list[dict]:
    p = Path(filepath)
    if not p.exists() or p.stat().st_size == 0:
        return []
    expenses = []
    with open(p, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                expenses.append(create_expense(
                    int(row["id"]), row["date"], row["category"],
                    float(row["amount"]), row["description"]
                ))
            except (ValueError, KeyError):
                continue
    return expenses

def save_expenses(expenses: list[dict], filepath: str | Path) -> None:
    p = Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=EXPENSE_HEADERS)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def load_assets(filepath: str | Path) -> list[dict]:
    p = Path(filepath)
    if not p.exists() or p.stat().st_size == 0:
        return []
    assets = []
    with open(p, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                assets.append(create_asset(
                    int(row["id"]), row["name"], row["category"],
                    float(row["value"]), row["acquisition_date"]
                ))
            except (ValueError, KeyError):
                continue
    return assets

def save_assets(assets: list[dict], filepath: str | Path) -> None:
    p = Path(filepath)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ASSET_HEADERS)
        writer.writeheader()
        for ast in assets:
            writer.writerow(ast)
