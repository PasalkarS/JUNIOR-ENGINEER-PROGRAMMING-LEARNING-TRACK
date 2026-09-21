"""
Simple CLI Expense Tracker
A beginner-friendly tool to add, list, delete, summarize, and import/export expenses using CSV.
"""

import csv
import os
from datetime import datetime

DEFAULT_FILE = "expenses.csv"

def parse_row(row):
    """
    Parse a CSV row into an expense dictionary.
    Handles malformed rows by returning None.
    Expected row: [id, date, category, amount, description]
    """
    if not row or len(row) < 4:
        return None

    try:
        exp_id = int(row[0].strip())
        date = row[1].strip()
        category = row[2].strip()
        amount = float(row[3].strip())
        desc = row[4].strip() if len(row) > 4 else ""

        if amount <= 0:
            return None

        return {
            "id": exp_id,
            "date": date,
            "category": category,
            "amount": amount,
            "description": desc,
        }
    except (ValueError, IndexError):
        return None

def load_expenses(filepath=DEFAULT_FILE):
    """Load expenses from a CSV file. Skips empty files and malformed rows."""
    expenses = []
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return expenses

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skip header if present
            if row and row[0].lower() == "id":
                continue
            item = parse_row(row)
            if item:
                expenses.append(item)

    return expenses

def save_expenses(expenses, filepath=DEFAULT_FILE):
    """Save expenses list to a CSV file."""
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "date", "category", "amount", "description"])
        for e in expenses:
            writer.writerow([e["id"], e["date"], e["category"], e["amount"], e["description"]])

def add_expense(expenses, category, amount, description, date=None):
    """Add a new expense to the list."""
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if not category.strip():
        raise ValueError("Category cannot be empty.")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    next_id = max([e["id"] for e in expenses], default=0) + 1
    item = {
        "id": next_id,
        "date": date,
        "category": category.strip().capitalize(),
        "amount": round(amount, 2),
        "description": description.strip(),
    }
    expenses.append(item)
    return item

def delete_expense(expenses, expense_id):
    """Delete an expense by ID. Returns True if deleted, False otherwise."""
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            del expenses[i]
            return True
    return False

def get_monthly_summary(expenses):
    """Returns a dictionary with monthly totals and category breakdown."""
    summary = {}
    for e in expenses:
        month = e["date"][:7]  # e.g. "2026-09"
        cat = e["category"]
        amt = e["amount"]

        if month not in summary:
            summary[month] = {"total": 0.0, "by_category": {}}

        summary[month]["total"] += amt
        summary[month]["by_category"][cat] = summary[month]["by_category"].get(cat, 0.0) + amt

    return summary

def main():
    expenses = load_expenses()
    print("Welcome to Expense Tracker!")

    while True:
        print("\n--- Menu ---")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("7. Exit")

        choice = input("Enter option (1-7): ").strip()

        if choice == "1":
            try:
                cat = input("Enter category (e.g. Food, Travel, Bills): ").strip()
                amt = float(input("Enter amount ($): "))
                desc = input("Enter description: ").strip()
                item = add_expense(expenses, cat, amt, desc)
                save_expenses(expenses)
                print(f"Added: #{item['id']} {item['category']} - ${item['amount']:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nID  | Date       | Category    | Amount    | Description")
                print("-" * 55)
                for e in expenses:
                    print(f"{e['id']:<3} | {e['date']} | {e['category']:<11} | ${e['amount']:>7.2f} | {e['description']}")
                total = sum(e["amount"] for e in expenses)
                print("-" * 55)
                print(f"Total: ${total:.2f}")

        elif choice == "3":
            try:
                exp_id = int(input("Enter Expense ID to delete: "))
                if delete_expense(expenses, exp_id):
                    save_expenses(expenses)
                    print(f"Expense #{exp_id} deleted.")
                else:
                    print(f"Expense #{exp_id} not found.")
            except ValueError:
                print("Error: Please enter a valid number ID.")

        elif choice == "4":
            summary = get_monthly_summary(expenses)
            if not summary:
                print("No expenses to summarize.")
            else:
                print("\n--- Monthly Summary ---")
                for month, data in summary.items():
                    print(f"\nMonth: {month} (Total: ${data['total']:.2f})")
                    for cat, amt in data["by_category"].items():
                        print(f"  - {cat}: ${amt:.2f}")

        elif choice == "5":
            out_file = input("Enter destination CSV file (e.g. backup.csv): ").strip()
            if out_file:
                save_expenses(expenses, out_file)
                print(f"Exported {len(expenses)} expenses to '{out_file}'.")

        elif choice == "6":
            in_file = input("Enter source CSV file to import: ").strip()
            if os.path.exists(in_file):
                imported = load_expenses(in_file)
                for item in imported:
                    add_expense(expenses, item["category"], item["amount"], item["description"], item["date"])
                save_expenses(expenses)
                print(f"Imported {len(imported)} expenses from '{in_file}'.")
            else:
                print(f"File '{in_file}' not found.")

        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-7.")

if __name__ == "__main__":
    main()
