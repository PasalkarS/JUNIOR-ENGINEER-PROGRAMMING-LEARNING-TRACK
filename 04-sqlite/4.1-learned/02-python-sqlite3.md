# 2 — Python sqlite3

## 1. Introduction to Python sqlite3

* `sqlite3` is a built-in Python module used to work with SQLite databases.
* It allows Python programs to store, retrieve, update, and delete data.
* No separate database server or external package is required.

**Important points**

* SQLite stores data in a database file.
* Python uses `sqlite3` to communicate with the database.
* SQL commands are executed through Python.
* The database can keep data even after the program closes.

## 2. Connecting to a Database

The `connect()` function creates a connection to an SQLite database.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")
```

**Important points**

* `sqlite3.connect()` opens or creates a database.
* `inventory.db` is the database file.
* If the file does not exist, SQLite creates it.
* The connection is used to communicate with the database.

## 3. Creating a Database File

SQLite automatically creates a database file when a connection is made to a new file path.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")

print("Database created successfully")

connection.close()
```

**Important points**

* The database file stores tables and their data.
* The file is created in the current working directory unless a path is specified.
* Existing database files can be opened again.
* Closing the connection releases the database resource.

## 4. Creating Tables Using Python

The `CREATE TABLE` statement creates a table inside the database.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL,
    quantity INTEGER
)
""")

connection.commit()
connection.close()
```

**Important points**

* A cursor executes SQL statements.
* `CREATE TABLE IF NOT EXISTS` creates the table only if it does not already exist.
* `INTEGER PRIMARY KEY` identifies each product.
* `TEXT`, `REAL`, and `INTEGER` represent common SQLite data types.
* `commit()` saves the changes.

## 5. Connections and Cursors

A connection manages the interaction between Python and the database. A cursor executes SQL statements and retrieves query results.

**Basic syntax**

```python
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
```

**Important points**

* A connection is created using `sqlite3.connect()`.
* A cursor is created using `connection.cursor()`.
* SQL commands are executed using `cursor.execute()`.
* Query results can be retrieved using fetch methods.
* A connection can have multiple cursors.

## 6. Executing SQL Statements

The `execute()` method runs an SQL statement through Python.

**Basic syntax**

```python
cursor.execute("SELECT * FROM products")
```

**Important points**

* `execute()` runs one SQL statement.
* SQL commands can create tables or modify data.
* SELECT statements return query results.
* Fetch methods are used to read the returned results.
* Use parameterized queries when inserting user-provided values.

## 7. Retrieving Records — fetchone(), fetchmany(), fetchall()

These methods retrieve rows returned by a query.

**Basic syntax**

```python
cursor.execute("SELECT * FROM products")

one_product = cursor.fetchone()
some_products = cursor.fetchmany(3)
all_products = cursor.fetchall()
```

**Important points**

* `fetchone()` retrieves the next row.
* `fetchmany(3)` retrieves up to three rows.
* `fetchall()` retrieves all remaining rows.
* A query must be executed before fetching its results.
* Each fetch method advances the cursor through the result set.
* If no rows remain, `fetchone()` returns `None`.

## 8. Parameterized Queries

Parameterized queries safely pass values into SQL statements instead of joining values directly into SQL strings.

**Basic syntax**

```python
product_name = "Keyboard"
price = 1200

cursor.execute(
    "INSERT INTO products (product_name, price) VALUES (?, ?)",
    (product_name, price)
)
```

**Important points**

* Use `?` as a placeholder for each value.
* Pass the values separately as a tuple or sequence.
* Use `(product_name,)` when passing a tuple containing one value.
* Parameterized queries help protect against SQL injection.
* Do not build SQL statements by concatenating user input.

## 9. Inserting Records — INSERT

The `INSERT` statement adds new records to a table.

**Basic syntax**

```python
cursor.execute(
    "INSERT INTO products (product_name, price, quantity) VALUES (?, ?, ?)",
    ("Mouse", 500, 10)
)

connection.commit()
```

**Important points**

* `INSERT INTO` specifies the table.
* Column names identify where values should be stored.
* Values are supplied using placeholders.
* `commit()` saves the inserted record.
* A primary key can be generated automatically when using `INTEGER PRIMARY KEY` and omitting that column.

## 10. Retrieving Records — SELECT

The `SELECT` statement reads records from a table.

**Basic syntax**

```python
cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)
```

**Important points**

* `SELECT` retrieves data.
* `*` selects all columns.
* Specific columns can be selected by name.
* `fetchall()` retrieves all remaining matching rows.
* `WHERE` can be used to filter the results.

## 11. Updating Records — UPDATE

The `UPDATE` statement changes existing records.

**Basic syntax**

```python
cursor.execute(
    "UPDATE products SET price = ? WHERE product_id = ?",
    (1500, 1)
)

connection.commit()
```

**Important points**

* `UPDATE` specifies the table to modify.
* `SET` specifies the columns and new values.
* `WHERE` identifies which records should change.
* Without a `WHERE` clause, every row in the table may be updated.
* Use parameterized queries for values.

## 12. Deleting Records — DELETE

The `DELETE` statement removes records from a table.

**Basic syntax**

```python
cursor.execute(
    "DELETE FROM products WHERE product_id = ?",
    (1,)
)

connection.commit()
```

**Important points**

* `DELETE FROM` specifies the table.
* `WHERE` identifies the records to remove.
* Without a `WHERE` clause, all rows in the table may be deleted.
* Deleting a record does not normally remove the table itself.
* Check the condition carefully before executing a delete operation.

## 13. Reading Rows as Dictionaries — sqlite3.Row

By default, SQLite returns query rows as tuples. Setting `row_factory` to `sqlite3.Row` allows values to be accessed by column name.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("SELECT * FROM products")

product = cursor.fetchone()

if product is not None:
    print(product["product_name"])
    print(product["price"])
```

**Important points**

* Set `connection.row_factory` before fetching query results.
* `sqlite3.Row` supports access by column name and position.
* `product["product_name"]` is easier to read than using a numeric index.
* Check whether a row is `None` before accessing its values.
* `sqlite3.Row` is row-like; it is not a regular dictionary.

## 14. Handling Database Errors

Database operations can fail because of invalid SQL, constraint violations, or other database problems.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")

try:
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO products (product_name, price, quantity) VALUES (?, ?, ?)",
        ("Monitor", 9000, 5)
    )

    connection.commit()
    print("Product added successfully")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    connection.close()
```

**Important points**

* `try` contains operations that may fail.
* `except sqlite3.Error` handles SQLite-related errors.
* `rollback()` undoes uncommitted changes in the current transaction.
* `finally` runs whether an error occurs or not.
* `close()` releases the database connection.
* Handle errors without hiding useful information during debugging.

## 15. Closing Database Resources

Database connections should be closed when they are no longer needed.

**Basic syntax**

```python
connection = sqlite3.connect("inventory.db")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    print(cursor.fetchall())

finally:
    connection.close()
```

**Important points**

* `connection.close()` closes the connection.
* Closing connections helps release resources.
* Use `try/finally` when you need to ensure cleanup.
* Do not attempt further database operations using a closed connection.
* A `with connection:` block manages transactions but does not automatically close the connection.

## 16. Transactions in Python

A transaction groups database operations so they can be committed together or rolled back when necessary.

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

except sqlite3.Error:
    connection.rollback()
    print("Transaction failed")

finally:
    connection.close()
```

**Important points**

* `commit()` saves the changes in a transaction.
* `rollback()` undoes uncommitted changes.
* Related operations should be grouped into one transaction when they must succeed together.
* If an operation fails, rollback can prevent partial changes from being saved.
* Transactions are important for operations such as order creation and stock updates.

## 17. CRUD Operations Using sqlite3

CRUD stands for Create, Read, Update, and Delete. These are the four basic operations used to manage records.

**Important points**

* **Create:** Add a new record using `INSERT`.
* **Read:** Retrieve records using `SELECT`.
* **Update:** Modify records using `UPDATE`.
* **Delete:** Remove records using `DELETE`.
* Use parameterized queries for values.
* Commit changes when they need to be saved.

## 18. Repository Pattern

The repository pattern separates database operations from the main application logic.

**What it is**

A repository is a class or module responsible for communicating with the database.

**Important points**

* The repository contains database-related operations.
* The application calls repository methods instead of writing SQL everywhere.
* Common methods include `add_product()`, `get_product()`, `update_product()`, and `delete_product()`.
* This structure makes code easier to maintain and test.
* Database logic stays separate from business logic.

**Example structure**

```text
inventory_app/
    main.py
    database.py
    product_repository.py
```

* `main.py` handles application flow.
* `database.py` handles database connections and initialization.
* `product_repository.py` contains product-related database operations.

## 19. Separating Database and Application Logic

Separating responsibilities keeps a project organized and easier to maintain.

**Important points**

* Database code handles connections and SQL queries.
* Repository code manages records.
* Application code handles user input and application flow.
* Validation checks whether input values are acceptable.
* Keeping these responsibilities separate reduces duplicated code.

**Example flow**

```text
User Input
    ↓
Application Logic
    ↓
Repository
    ↓
SQLite Database
```

## 20. Important sqlite3 Best Practices

* Use parameterized queries instead of string concatenation.
* Close database connections when finished.
* Use transactions for related database operations.
* Use `commit()` to save changes.
* Use `rollback()` when a transaction fails.
* Handle database errors with appropriate exception handling.
* Use primary keys to identify records.
* Use `sqlite3.Row` when accessing columns by name is helpful.
* Keep database operations separate from application logic.
* Never assume a query returned a row; handle empty results.
* Use `WHERE` carefully in UPDATE and DELETE statements.
* Use `CREATE TABLE IF NOT EXISTS` when initializing tables that may already exist.
