# Expense Tracker CLI — Independent Challenge

This is my standalone solution for the Module 01 Independent Challenge. It's a command-line expense tracker designed to record, categorize, summarize, and import/export expense data using standard Python without external database dependencies.

---

## Design Choices & Rationale

1. **Why CSV as the Storage Format?**
   - For an early-stage CLI tool, CSV is human-readable, simple to inspect with Excel/text editors, and requires zero setup or external services.
   - It also gave me a great surface to practice file handling, dialect management, and parsing edge cases in Python's standard `csv` module.

2. **Decoupled Data Modeling (`Expense` vs `ExpenseTracker`)**:
   - The `Expense` class acts as a domain entity responsible for validating its own attributes (non-negative amount, strict `YYYY-MM-DD` date formatting, category standardization).
   - The `ExpenseTracker` manages collection-level operations (adding, deleting, monthly grouping, and persistence).

3. **Handling Edge Cases & Corrupted Inputs**:
   - **Empty Files**: If the user points to an empty CSV file (0 bytes or header only), the parser detects this gracefully and returns an empty list without throwing an unhandled exception or crashing.
   - **Malformed Rows**: When reading external CSV files, rows can have missing columns, non-numeric amounts, or corrupted dates. Instead of failing the entire import, `parse_csv_file()` logs a clear warning per bad row, skips only that row, and preserves all valid records.
   - **Invalid User Inputs**: Interactive commands validate numbers and dates upfront, offering meaningful error messages rather than raw Python tracebacks.

---

## How to Run

### 1. Add an Expense
```bash
python expense_tracker.py add -a 45.50 -c Food -d "Team lunch"
python expense_tracker.py add -a 120.00 -c Utilities -d "Internet bill" --date 2026-09-01
```

### 2. List Expenses
```bash
# List all
python expense_tracker.py list

# Filter by category or month
python expense_tracker.py list -c Food
python expense_tracker.py list -m 2026-09
```

### 3. Monthly Summary Breakdown
```bash
python expense_tracker.py summary
python expense_tracker.py summary -m 2026-09
```

### 4. Delete an Expense
```bash
python expense_tracker.py delete 1
```

### 5. Export and Import CSV
```bash
python expense_tracker.py export backup_expenses.csv
python expense_tracker.py import backup_expenses.csv
```

---

## Running the Tests

A comprehensive pytest suite is included in `test_expense_tracker.py` covering creation, validation, monthly aggregations, and edge cases (corrupted rows, empty files):

```bash
pytest test_expense_tracker.py -v
```
