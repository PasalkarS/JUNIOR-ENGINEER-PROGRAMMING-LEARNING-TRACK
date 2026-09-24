# Transactions & Atomic Operations

> **Module 04: SQLite | Topic 04**

## 1. Learning Outcomes
- **ACID Properties:** Understand Atomicity, Consistency, Isolation, and Durability.
- **Commit & Rollback:** Ensure all-or-nothing execution across multiple related statements.
- **Context Manager Handling:** Use Python's `with conn:` context manager for automatic commits and rollbacks.
- **Preventing Partial Updates:** Safeguard financial and inventory updates from partial write failures.

## 2. Key Syntax & Concepts

### Atomic Funds Transfer Example
```python
import sqlite3

def transfer_funds(conn: sqlite3.Connection, from_acc: int, to_acc: int, amount: float):
    # Using 'with conn:' automatically commits on success and rolls back on exception
    with conn:
        cursor = conn.cursor()
        
        # 1. Deduct from source
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?;",
            (amount, from_acc, amount)
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Insufficient funds or invalid account {from_acc}")
            
        # 2. Add to destination
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?;",
            (amount, to_acc)
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Target account {to_acc} does not exist.")
            
    print(f"Successfully transferred ${amount:.2f} from {from_acc} to {to_acc}.")
```

## 3. Common Mistakes & Gotchas
- **Manual Commit During Context Manager:** Don't call `conn.commit()` manually inside a `with conn:` block; the context manager manages the lifecycle automatically.
- **Database Locks:** Long-running transactions hold a write lock on the SQLite file, blocking other processes. Keep transaction blocks concise.

## 4. Practice Tasks
- **Task 1:** Write an order checkout function that inside a single transaction decrements product inventory and records an order entry.

## 5. Self-Check Questions
- **Q1:** What happens to pending database mutations if an unhandled Python exception occurs inside a `with conn:` block?
- **Q2:** What does the 'A' in ACID stand for and why is it critical?
