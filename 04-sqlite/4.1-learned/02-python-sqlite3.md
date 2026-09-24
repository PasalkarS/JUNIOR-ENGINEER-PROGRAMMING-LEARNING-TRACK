# Python sqlite3 & Parameterized Queries

> **Module 04: SQLite | Topic 02**

## 1. Learning Outcomes
- **Connection Mechanics:** Connect to SQLite databases using the standard library `sqlite3` module.
- **Cursor Lifecycle:** Execute queries and fetch records with `fetchone()`, `fetchall()`, and `row_factory`.
- **SQL Injection Defense:** Always use parameterized placeholders (`?`) instead of f-strings.
- **Row Mapping:** Map database rows directly to Python dictionaries or domain objects.

## 2. Key Syntax & Concepts

### Safe Database Connection & Parameterization
```python
import sqlite3
from pathlib import Path

def get_connection(db_path: str = "app.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    # Enable dictionary-like row access
    conn.row_factory = sqlite3.Row
    # Enforce foreign key constraints in SQLite
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# SAFE: Parameterized Query using ? placeholders
def find_user_by_email(conn: sqlite3.Connection, email: str) -> dict | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE email = ?;", (email,))
    row = cursor.fetchone()
    return dict(row) if row else None
```

### The SQL Injection Vulnerability (Never Do This!)
```python
# VULNERABLE: Direct string formatting allows malicious SQL execution
user_input = "test@example.com' OR '1'='1"
# cursor.execute(f"SELECT * FROM users WHERE email = '{user_input}';")  <-- COMPROMISED!
```

## 3. Common Mistakes & Gotchas
- **Single Item Tuple Trap:** When passing one parameter to `execute()`, remember the trailing comma: `(val,)`. Passing `(val)` unpacks characters of a string.
- **Forgetting Foreign Keys PRAGMA:** SQLite disables foreign key enforcement by default for backwards compatibility. Always run `PRAGMA foreign_keys = ON;`.

## 4. Practice Tasks
- **Task 1:** Write a Python function `save_product(conn, name, price, stock)` that inserts a record and returns the newly generated auto-increment ID (`cursor.lastrowid`).

## 5. Self-Check Questions
- **Q1:** Why does using `?` placeholders eliminate SQL injection risks?
- **Q2:** What does `conn.row_factory = sqlite3.Row` enable?
