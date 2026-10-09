# 4 — Transactions

## 1. Introduction to Database Transactions

* A transaction is a group of database operations treated as one unit of work.
* Transactions help ensure that related changes are saved together.
* If an operation fails, uncommitted changes can be rolled back.

**Important points**

* A transaction can contain one or more SQL operations.
* `COMMIT` saves the changes made in a transaction.
* `ROLLBACK` undoes uncommitted changes.
* Transactions help prevent incomplete database updates.
* They are useful for payments, orders, and inventory updates.

## 2. Understanding Atomicity

Atomicity means that a transaction is completed fully or not applied at all.

**Example**

When transferring money between two accounts:

* Money is deducted from the first account.
* Money is added to the second account.
* Both operations must succeed together.
* If either operation fails, the transaction should be rolled back.

**Important points**

* A transaction should not leave the database in a partially updated state.
* Related operations should belong to the same transaction.
* Rollback undoes changes that have not been committed.
* Atomicity is one of the ACID properties of database transactions.

## 3. ACID Properties

ACID describes four important properties of reliable database transactions.

### Atomicity

* All operations in a transaction succeed together.
* If the transaction fails, uncommitted changes are rolled back.

### Consistency

* A transaction moves the database from one valid state to another.
* Database constraints and application rules should remain satisfied.

### Isolation

* Concurrent transactions should not interfere with each other in ways that produce invalid results.
* SQLite controls database access to help maintain consistency during concurrent operations.

### Durability

* Once a transaction is successfully committed, its changes are intended to persist even after the application closes or restarts.
* Durability depends on the database and storage configuration working correctly.

## 4. COMMIT

`COMMIT` saves the changes made during a transaction.

**Basic syntax**

```sql
BEGIN;

UPDATE products
SET quantity = quantity - 2
WHERE product_id = 1;

COMMIT;
```

**Important points**

* `BEGIN` starts an explicit transaction.
* SQL statements inside the transaction make changes.
* `COMMIT` makes the transaction's changes permanent.
* Committed changes cannot normally be undone using a later `ROLLBACK`.
* Use a transaction when multiple operations must succeed together.

## 5. ROLLBACK

`ROLLBACK` cancels the changes made in the current uncommitted transaction.

**Basic syntax**

```sql
BEGIN;

UPDATE products
SET quantity = quantity - 2
WHERE product_id = 1;

ROLLBACK;
```

**Important points**

* `ROLLBACK` undoes uncommitted changes in the current transaction.
* It is useful when an operation fails.
* It helps prevent partial updates.
* It does not undo changes from a transaction that has already been committed.
* Always handle failures at the correct transaction boundary.

## 6. Transactions in Python sqlite3

Python's `sqlite3` module supports transactions through a database connection.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")

try:
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
        (2, 1)
    )

    connection.commit()
    print("Transaction completed")

except sqlite3.Error as error:
    connection.rollback()
    print("Transaction failed:", error)

finally:
    connection.close()
```

**Important points**

* `connection.commit()` saves the transaction's changes.
* `connection.rollback()` undoes uncommitted changes.
* Use `try` and `except` to handle database errors.
* Close the connection when the work is finished.
* Check whether an operation affected the expected number of rows.
* SQLite transaction behavior depends on the connection's transaction settings.

## 7. Automatic and Explicit Transaction Handling

Python's `sqlite3` supports different ways to manage transactions.

### Explicit Transaction Handling

You start and manage the transaction yourself.

```python
connection.execute("BEGIN")

try:
    connection.execute(
        "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
        (1, 1)
    )

    connection.commit()

except sqlite3.Error:
    connection.rollback()
    raise
```

### Using a Connection Context Manager

A connection context manager can automatically commit or roll back a transaction.

```python
import sqlite3

connection = sqlite3.connect("inventory.db")

try:
    with connection:
        connection.execute(
            "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
            (1, 1)
        )

finally:
    connection.close()
```

**Important points**

* Explicit transaction handling gives direct control over transaction boundaries.
* The connection context manager commits on successful completion of the block.
* If an exception occurs, the context manager rolls back an active transaction.
* `with connection:` does not automatically close the connection.
* Avoid mixing transaction-management methods without understanding the connection's settings.

## 8. Grouping Multiple Operations into One Transaction

When multiple operations depend on each other, they should usually be grouped into one transaction.

**Example**

An order may require the application to:

* Create an order record.
* Add the order's items.
* Reduce product quantities.
* Save all related changes together.

**Important points**

* All related operations should succeed together.
* If one operation fails, the transaction should be rolled back.
* Do not commit after every individual operation when the operations must be atomic as a group.
* Validate inputs before making changes where possible.
* Keep transactions focused and avoid holding them open longer than necessary.

## 9. Error Handling During Transactions

Errors can occur because of invalid data, constraint violations, missing records, or database problems.

**Important points**

* Place transaction operations inside a `try` block.
* Catch appropriate exceptions.
* Roll back uncommitted changes after a transaction failure.
* Do not silently ignore errors.
* Report useful error information for debugging.
* Re-raise exceptions when the calling code needs to know the operation failed.

**Basic syntax**

```python
try:
    connection.execute(
        "UPDATE products SET quantity = quantity - ? WHERE product_id = ?",
        (2, 1)
    )

    connection.commit()

except sqlite3.Error:
    connection.rollback()
    raise
```

## 10. Preventing Partial Updates

A partial update happens when some related database changes succeed but others fail.

**Example**

An order is created, but its product quantities are not updated because a later operation fails.

**Important points**

* Use a transaction for related changes.
* Commit only after all required operations succeed.
* Roll back if any operation fails.
* Check that required records exist.
* Use database constraints to protect important rules.
* Keep all operations that must succeed together within the same transaction.

## 11. Transaction Boundaries

A transaction boundary defines which database operations belong to one transaction.

**Important points**

* Start the transaction before the first related database change.
* Include all operations that must succeed together.
* Commit after all required operations finish successfully.
* Roll back when an operation fails.
* Do not combine unrelated work into a single long transaction without a reason.
* Decide transaction boundaries based on the application's business rules.

## 12. Bank Transfer Transaction Exercise

A bank transfer moves money from one account to another.

**Requirements**

* Create an accounts table.
* Store an account ID and account balance.
* Deduct money from the sender.
* Add money to the receiver.
* Ensure both updates succeed together.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("bank.db")

try:
    with connection:
        cursor = connection.cursor()

        sender_id = 1
        receiver_id = 2
        amount = 500

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        cursor.execute(
            "UPDATE accounts SET balance = balance - ? "
            "WHERE account_id = ? AND balance >= ?",
            (amount, sender_id, amount)
        )

        if cursor.rowcount != 1:
            raise ValueError("Sender not found or insufficient balance")

        cursor.execute(
            "UPDATE accounts SET balance = balance + ? "
            "WHERE account_id = ?",
            (amount, receiver_id)
        )

        if cursor.rowcount != 1:
            raise ValueError("Receiver not found")

    print("Transfer completed successfully")

except (sqlite3.Error, ValueError) as error:
    print("Transfer failed:", error)

finally:
    connection.close()
```

**Important points**

* The sender must have enough money.
* The transfer amount must be greater than zero.
* The receiver must exist.
* Both balance updates occur within the same transaction.
* An exception inside the connection context manager causes the transaction to roll back.
* The example assumes the `accounts` table already exists and has suitable constraints.

## 13. Order Transaction Exercise

An order transaction may involve creating an order, inserting order items, and updating inventory quantities.

**Important points**

* Validate the order before saving it.
* Create the order record.
* Insert each order item.
* Check that enough inventory exists before reducing stock.
* Update inventory quantities within the same transaction.
* Commit only when every required operation succeeds.
* Roll back all uncommitted changes if an operation fails.

**Example transaction flow**

```text
Start Transaction
        ↓
Create Order
        ↓
Insert Order Items
        ↓
Check and Update Stock
        ↓
All Operations Successful?
       / \
     Yes  No
      ↓    ↓
   Commit Rollback
      ↓    ↓
     End  End
```

## 14. Testing Transaction Success and Failure

Transactions should be tested under both successful and unsuccessful conditions.

**Successful transaction tests**

* Verify that all expected records are saved.
* Verify that balances or quantities are updated correctly.
* Verify that the transaction is committed.

**Failed transaction tests**

* Cause one operation to fail.
* Verify that earlier uncommitted changes are rolled back.
* Verify that the database has not been partially updated.
* Test missing records and invalid amounts.
* Test constraint violations.

**Important points**

* Test the database state before and after each operation.
* Use a temporary test database when possible.
* Do not rely only on printed success messages.
* Verify the actual stored values.

## 15. Maintaining Database Consistency

Consistency means that database rules remain satisfied before and after a transaction.

**Important points**

* Use constraints to prevent invalid values.
* Use foreign keys to protect relationships.
* Validate application input.
* Use transactions for related operations.
* Check affected row counts when an operation must update a specific record.
* Test failure scenarios as well as successful scenarios.

## 16. Important Transaction Best Practices

* Group related operations into one transaction.
* Commit only after all required operations succeed.
* Roll back when a transaction fails.
* Use parameterized SQL queries.
* Validate important input values.
* Check whether expected records were found or updated.
* Use database constraints to enforce important rules.
* Keep transaction boundaries clear.
* Avoid long-running transactions.
* Test both successful and failed operations.
* Never assume that a transaction succeeded without checking for errors.
