"""
expense_tracker.py - Standalone CLI Expense Tracker.

Provides expense tracking capabilities:
  - Add, list, and delete expenses
  - Import / Export to CSV format
  - Monthly spending summary grouped by category
  - Resilient CSV parsing handling empty files, corrupted rows, and invalid inputs
"""

import sys
import os
import csv
import argparse
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional


DEFAULT_DATA_FILE = "expenses.csv"
VALID_CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Health", "Shopping", "Other"]


class Expense:
    """Represents a single validated expense item."""

    def __init__(self, expense_id: int, date_str: str, category: str, amount: float, description: str):
        self.expense_id = expense_id
        self.date_str = self._validate_date(date_str)
        self.category = self._validate_category(category)
        self.amount = self._validate_amount(amount)
        self.description = description.strip() or "No description"

    @staticmethod
    def _validate_date(date_str: str) -> str:
        s = date_str.strip()
        try:
            parsed = datetime.strptime(s, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format '{date_str}'. Must be YYYY-MM-DD.")

    @staticmethod
    def _validate_category(cat: str) -> str:
        c = cat.strip().capitalize()
        # Accept valid categories or default to Other
        for valid in VALID_CATEGORIES:
            if c.lower() == valid.lower():
                return valid
        return "Other"

    @staticmethod
    def _validate_amount(val: Any) -> float:
        try:
            amt = float(val)
        except (ValueError, TypeError):
            raise ValueError(f"Amount must be a valid number, got '{val}'.")

        if amt <= 0:
            raise ValueError(f"Amount must be positive and greater than zero, got '{amt}'.")
        return round(amt, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.expense_id,
            "date": self.date_str,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Expense":
        return cls(
            expense_id=int(d["id"]),
            date_str=str(d["date"]),
            category=str(d["category"]),
            amount=float(d["amount"]),
            description=str(d.get("description", "")),
        )


class ExpenseTracker:
    """Manages collection of expenses, persistence, and summary analytics."""

    def __init__(self, data_path: str = DEFAULT_DATA_FILE):
        self.data_path = data_path
        self.expenses: List[Expense] = []
        self._next_id = 1
        self.load()

    def add(self, amount: float, category: str, description: str, date_str: Optional[str] = None) -> Expense:
        if date_str is None or not date_str.strip():
            date_str = datetime.now().strftime("%Y-%m-%d")

        expense = Expense(self._next_id, date_str, category, amount, description)
        self.expenses.append(expense)
        self._next_id += 1
        self.save()
        return expense

    def delete(self, expense_id: int) -> bool:
        initial_len = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.expense_id != expense_id]
        if len(self.expenses) < initial_len:
            self.save()
            return True
        return False

    def list_expenses(self, category: Optional[str] = None, month: Optional[str] = None) -> List[Expense]:
        results = self.expenses
        if category:
            results = [e for e in results if e.category.lower() == category.strip().lower()]
        if month:
            # month format YYYY-MM
            results = [e for e in results if e.date_str.startswith(month.strip())]
        return sorted(results, key=lambda e: e.date_str, reverse=True)

    def monthly_summary(self, month: Optional[str] = None) -> Dict[str, Any]:
        """
        Aggregate spending by category and month.
        If month is provided (e.g. '2026-09'), summarizes that month.
        Otherwise summarizes all recorded months.
        """
        target_expenses = self.expenses
        if month:
            target_expenses = [e for e in target_expenses if e.date_str.startswith(month.strip())]

        breakdown: Dict[str, Dict[str, float]] = {}
        monthly_totals: Dict[str, float] = {}

        for e in target_expenses:
            m = e.date_str[:7]  # YYYY-MM
            monthly_totals[m] = monthly_totals.get(m, 0.0) + e.amount

            if m not in breakdown:
                breakdown[m] = {}
            breakdown[m][e.category] = breakdown[m].get(e.category, 0.0) + e.amount

        grand_total = sum(e.amount for e in target_expenses)
        return {
            "grand_total": round(grand_total, 2),
            "total_count": len(target_expenses),
            "monthly_totals": {k: round(v, 2) for k, v in monthly_totals.items()},
            "by_category": {m: {cat: round(amt, 2) for cat, amt in cats.items()} for m, cats in breakdown.items()},
        }

    # -----------------------------------------------------------------------
    # CSV Persistence & Parsing with Edge Case Handling
    # -----------------------------------------------------------------------
    def save(self, target_path: Optional[str] = None) -> None:
        path = target_path or self.data_path
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "date", "category", "amount", "description"])
            writer.writeheader()
            for e in self.expenses:
                writer.writerow(e.to_dict())

    def load(self, source_path: Optional[str] = None) -> Tuple[int, List[str]]:
        """
        Load expenses from CSV file.
        
        Returns:
            Tuple of (loaded_count, list_of_error_messages)
        """
        path = source_path or self.data_path
        if not os.path.exists(path):
            self.expenses = []
            self._next_id = 1
            return 0, []

        loaded, errors = self.parse_csv_file(path)
        self.expenses = loaded
        self._next_id = max([e.expense_id for e in self.expenses], default=0) + 1
        return len(self.expenses), errors

    @classmethod
    def parse_csv_file(cls, file_path: str) -> Tuple[List[Expense], List[str]]:
        """
        Parse CSV lines safely handling empty files, missing columns, and malformed rows.
        
        Returns:
            (valid_expenses, skipped_row_errors)
        """
        if not os.path.exists(file_path):
            return [], [f"File not found: {file_path}"]

        if os.path.getsize(file_path) == 0:
            return [], []

        valid_expenses: List[Expense] = []
        errors: List[str] = []

        with open(file_path, "r", newline="", encoding="utf-8") as f:
            # Check if file has header or content
            reader = csv.reader(f)
            try:
                first_row = next(reader)
            except StopIteration:
                # File is empty
                return [], []

            # Check if first row is header
            headers = [h.strip().lower() for h in first_row]
            has_header = "amount" in headers and ("date" in headers or "id" in headers)

            if not has_header:
                # Process the first row as data
                f.seek(0)
                reader = csv.reader(f)

            row_num = 1 if has_header else 0
            for row in reader:
                row_num += 1
                if not row or all(c.strip() == "" for c in row):
                    continue  # skip blank lines

                if len(row) < 3:
                    errors.append(f"Row {row_num}: Malformed row has fewer than 3 columns ({row})")
                    continue

                try:
                    # Support: [id, date, category, amount, desc] OR [date, category, amount, desc]
                    if len(row) >= 5:
                        exp_id = int(row[0].strip())
                        d_str = row[1].strip()
                        cat = row[2].strip()
                        amt = float(row[3].strip())
                        desc = row[4].strip()
                    elif len(row) == 4:
                        # date, category, amount, description
                        exp_id = len(valid_expenses) + 1
                        d_str = row[0].strip()
                        cat = row[1].strip()
                        amt = float(row[2].strip())
                        desc = row[3].strip()
                    else:
                        # 3 columns: date, category, amount
                        exp_id = len(valid_expenses) + 1
                        d_str = row[0].strip()
                        cat = row[1].strip()
                        amt = float(row[2].strip())
                        desc = ""

                    exp = Expense(exp_id, d_str, cat, amt, desc)
                    valid_expenses.append(exp)
                except Exception as e:
                    errors.append(f"Row {row_num}: Skipped invalid row ({row}): {e}")

        return valid_expenses, errors


# ---------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------
def print_table(expenses: List[Expense]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount ($)':<12} | {'Description'}")
    print("-" * 65)
    for e in expenses:
        print(f"{e.expense_id:<5} | {e.date_str:<12} | {e.category:<15} | {e.amount:>10.2f}   | {e.description}")
    print("-" * 65)
    total = sum(e.amount for e in expenses)
    print(f"{'TOTAL':<36} | {total:>10.2f}   | ({len(expenses)} items)\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI Personal Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available actions")

    # Add
    p_add = subparsers.add_parser("add", help="Record a new expense")
    p_add.add_argument("-a", "--amount", type=float, required=True, help="Expense amount in dollars")
    p_add.add_argument("-c", "--category", required=True, help=f"Category: {', '.join(VALID_CATEGORIES)}")
    p_add.add_argument("-d", "--desc", default="General", help="Brief description")
    p_add.add_argument("--date", help="Date in YYYY-MM-DD (defaults to today)")

    # List
    p_list = subparsers.add_parser("list", help="List recorded expenses")
    p_list.add_argument("-c", "--category", help="Filter by category")
    p_list.add_argument("-m", "--month", help="Filter by month (YYYY-MM)")

    # Delete
    p_del = subparsers.add_parser("delete", help="Delete an expense by ID")
    p_del.add_argument("id", type=int, help="Expense ID to remove")

    # Summary
    p_sum = subparsers.add_parser("summary", help="Monthly spending breakdown")
    p_sum.add_argument("-m", "--month", help="Filter summary to specific month (YYYY-MM)")

    # Export
    p_exp = subparsers.add_parser("export", help="Export expenses to external CSV file")
    p_exp.add_argument("target", help="Destination file path (e.g. backup.csv)")

    # Import
    p_imp = subparsers.add_parser("import", help="Import expenses from external CSV file")
    p_imp.add_argument("source", help="Source CSV file path")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    tracker = ExpenseTracker()

    if args.command == "add":
        try:
            exp = tracker.add(args.amount, args.category, args.desc, args.date)
            print(f"[Success] Added expense #{exp.expense_id}: ${exp.amount:.2f} for {exp.category} on {exp.date_str}")
        except Exception as e:
            print(f"[Error] {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "list":
        items = tracker.list_expenses(category=args.category, month=args.month)
        print_table(items)

    elif args.command == "delete":
        if tracker.delete(args.id):
            print(f"[Success] Removed expense #{args.id}.")
        else:
            print(f"[Error] Expense with ID #{args.id} not found.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "summary":
        summary = tracker.monthly_summary(month=args.month)
        print("=" * 45)
        print("          Monthly Spending Summary")
        print("=" * 45)
        print(f"Total Recorded Items: {summary['total_count']}")
        print(f"Grand Total:          ${summary['grand_total']:.2f}\n")

        for m, total in summary["monthly_totals"].items():
            print(f"Month: {m} (Total: ${total:.2f})")
            cats = summary["by_category"].get(m, {})
            for cat, amt in cats.items():
                pct = (amt / total * 100) if total else 0
                print(f"  - {cat:<15}: ${amt:>8.2f} ({pct:5.1f}%)")
            print()

    elif args.command == "export":
        try:
            tracker.save(args.target)
            print(f"[Success] Exported {len(tracker.expenses)} expenses to '{args.target}'.")
        except Exception as e:
            print(f"[Error exporting] {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "import":
        try:
            imported, errors = ExpenseTracker.parse_csv_file(args.source)
            # Append to current tracker
            for item in imported:
                tracker.add(item.amount, item.category, item.description, item.date_str)

            print(f"[Success] Imported {len(imported)} expenses from '{args.source}'.")
            if errors:
                print(f"[Notice] {len(errors)} malformed rows were skipped:")
                for err in errors[:5]:
                    print(f"  * {err}")
                if len(errors) > 5:
                    print(f"  * ... and {len(errors) - 5} more.")
        except Exception as e:
            print(f"[Error importing] {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
