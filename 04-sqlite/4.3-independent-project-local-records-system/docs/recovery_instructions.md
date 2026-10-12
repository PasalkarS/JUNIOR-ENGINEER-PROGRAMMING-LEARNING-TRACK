# Recovery Instructions

## Initialize the Database

From the project root, run:

```bash
python src/main.py
```

The database and tables are created automatically if they do not exist.

## Database Location

The database is stored at:

`data/inventory.db`

## Back Up the Database

1. Exit the application.
2. Copy `data/inventory.db` to a safe backup location.
3. Keep the backup separate from the original database.

## Restore the Database

1. Exit the application.
2. Keep a copy of the damaged database if you need to investigate it.
3. Replace `data/inventory.db` with a valid backup.
4. Run `python src/main.py`.

If no backup exists, running the application creates an empty database schema, but it cannot restore lost inventory records.
