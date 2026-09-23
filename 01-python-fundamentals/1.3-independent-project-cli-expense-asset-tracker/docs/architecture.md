# System Architecture

The CLI Expense & Asset Tracker is architected into 5 modular Python layers:

```
[tracker.py] (CLI Interaction / Presentation)
       |
       +---> [validation.py] (Input guards & business rules)
       |
       +---> [models.py] (Normalized dictionary entities)
       |
       +---> [storage.py] (CSV serialization & file I/O)
       |
       +---> [reports.py] (Aggregations, monthly totals, net worth)
```

## Layer Separation

1. `tracker.py`: Handles menu printing, user inputs, and displays cleanly formatted tables.
2. `validation.py`: Protects against corrupt data (negative values, malformed dates).
3. `models.py`: Encapsulates dictionary schemas for expenses and assets.
4. `storage.py`: Encapsulates file reading and writing using Python's `csv` module.
5. `reports.py`: Pure computational functions with zero I/O dependencies.
