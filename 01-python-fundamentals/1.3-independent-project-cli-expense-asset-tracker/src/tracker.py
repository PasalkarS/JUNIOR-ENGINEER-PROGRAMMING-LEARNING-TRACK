"""
CLI Entry Point for Expense and Asset Tracker.
"""
import sys
from pathlib import Path
from models import create_expense, create_asset
from validation import validate_amount, validate_date, validate_text, ValidationError
from storage import load_expenses, save_expenses, load_assets, save_assets
from reports import calculate_expense_summary, calculate_asset_summary, calculate_net_worth_overview

DATA_DIR = Path(__file__).parent.parent / "data"
EXPENSES_FILE = DATA_DIR / "expenses.csv"
ASSETS_FILE = DATA_DIR / "assets.csv"

def display_menu():
    print("\n==========================================")
    print("   CLI EXPENSE & ASSET TRACKER")
    print("==========================================")
    print(" 1. Add Expense")
    print(" 2. List Expenses")
    print(" 3. Add Asset")
    print(" 4. List Assets")
    print(" 5. Search Records")
    print(" 6. Financial Summary & Net Worth")
    print(" 7. Exit")
    print("==========================================")

def run_cli():
    expenses = load_expenses(EXPENSES_FILE)
    assets = load_assets(ASSETS_FILE)
    print(f"Loaded {len(expenses)} expense(s) and {len(assets)} asset(s).")

    while True:
        display_menu()
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            try:
                cat = validate_text(input("Category (e.g., Food, Travel, Rent): "), "Category")
                amt = validate_amount(input("Amount: "))
                desc = validate_text(input("Description: "), "Description")
                dt = validate_date(input("Date (YYYY-MM-DD, press Enter for today): "))
                next_id = max([e["id"] for e in expenses], default=0) + 1
                new_exp = create_expense(next_id, dt, cat, amt, desc)
                expenses.append(new_exp)
                save_expenses(expenses, EXPENSES_FILE)
                print(f"[SUCCESS] Added Expense #{next_id}: ${amt:.2f} ({cat})")
            except ValidationError as err:
                print(f"[ERROR] {err}")

        elif choice == "2":
            if not expenses:
                print("No expenses recorded.")
            else:
                print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
                print("-" * 60)
                for e in expenses:
                    print(f"{e['id']:<5} {e['date']:<12} {e['category']:<15} ${e['amount']:>9.2f} {e['description']}")

        elif choice == "3":
            try:
                name = validate_text(input("Asset Name: "), "Asset Name")
                cat = validate_text(input("Category (e.g., Equipment, Vehicle, Real Estate): "), "Category")
                val = validate_amount(input("Estimated Value: "))
                dt = validate_date(input("Acquisition Date (YYYY-MM-DD, press Enter for today): "))
                next_id = max([a["id"] for a in assets], default=0) + 1
                new_ast = create_asset(next_id, name, cat, val, dt)
                assets.append(new_ast)
                save_assets(assets, ASSETS_FILE)
                print(f"[SUCCESS] Added Asset #{next_id}: {name} - ${val:.2f}")
            except ValidationError as err:
                print(f"[ERROR] {err}")

        elif choice == "4":
            if not assets:
                print("No assets recorded.")
            else:
                print(f"\n{'ID':<5} {'Name':<20} {'Category':<15} {'Value':>12} {'Acquired'}")
                print("-" * 65)
                for a in assets:
                    print(f"{a['id']:<5} {a['name']:<20} {a['category']:<15} ${a['value']:>11.2f} {a['acquisition_date']}")

        elif choice == "5":
            query = input("Search query (matches category or description): ").strip().lower()
            matching_exp = [e for e in expenses if query in e['category'].lower() or query in e['description'].lower()]
            print(f"Found {len(matching_exp)} matching expense(s):")
            for e in matching_exp:
                print(f" - [{e['date']}] {e['category']}: ${e['amount']:.2f} ({e['description']})")

        elif choice == "6":
            overview = calculate_net_worth_overview(expenses, assets)
            exp_summary = calculate_expense_summary(expenses)
            ast_summary = calculate_asset_summary(assets)
            print("\n--- Financial Overview ---")
            print(f"Total Asset Valuation:  ${overview['total_assets']:,.2f}")
            print(f"Total Expenses Logged:  ${overview['total_expenses']:,.2f}")
            print(f"Net Asset Balance:      ${overview['net_balance']:,.2f}")
            print("\nExpenses by Category:")
            for cat, total in exp_summary["by_category"].items():
                print(f"  * {cat:<15}: ${total:,.2f}")

        elif choice == "7":
            print("Exiting Tracker. All data saved. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1 through 7.")

if __name__ == "__main__":
    run_cli()
