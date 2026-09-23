# CLI Expense & Asset Tracker

A modular command-line application for tracking personal or small business expenses and physical/digital capital assets.

## Features

- **Expense Tracking**: Log expenses with dates, categories, and amounts.
- **Asset Valuation**: Record assets and monitor capital portfolio valuation.
- **Data Validation**: Strict input parsing enforcing positive numbers and ISO dates (`YYYY-MM-DD`).
- **CSV Persistence**: Automatically saves and loads records to `data/expenses.csv` and `data/assets.csv`.
- **Financial Reporting**: Category-wise breakdowns, monthly totals, and net worth balance.
- **Search & Filter**: Keyword search across all transactions.

## Directory Structure

```text
1.3-independent-project-cli-expense-asset-tracker/
├── README.md
├── src/
│   ├── models.py       # Data creation factories
│   ├── storage.py      # CSV file persistence
│   ├── validation.py   # Input validators and custom errors
│   ├── reports.py      # Aggregation and net worth math
│   └── tracker.py      # CLI menu loop
├── tests/
│   └── test_tracker.py # Automated pytest test suite
├── data/
│   ├── expenses.csv    # Sample expenses
│   └── assets.csv      # Sample assets
└── docs/
    ├── architecture.md # Architectural design decisions
    └── user_guide.md   # Step-by-step usage guide
```

## Setup & Running

Run the tracker from this directory:

```bash
python src/tracker.py
```

## Running Automated Tests

```bash
pytest tests/ -v
```

## Design Decisions

- **Dictionary Entities**: Kept data structures as simple dicts to adhere strictly to Module 01 Python Fundamentals scope.
- **Pure Functions**: Separated calculation logic (`reports.py`) from presentation (`tracker.py`) to enable effortless unit testing.
