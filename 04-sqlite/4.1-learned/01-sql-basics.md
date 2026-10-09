# 1 — SQL Basics

## 1. Introduction to SQL

### What it is

SQL (Structured Query Language) is used to create, read, update, and delete data in relational databases.

### Important Points

* SQL is used to communicate with databases.
* It helps manage data stored in tables.
* SQL commands can retrieve or modify records.
* SQLite uses SQL to manage database information.

## 2. Introduction to Relational Databases

### What it is

A relational database stores data in tables that can be connected through relationships.

### Important Points

* A database can contain multiple tables.
* Each table stores a particular type of information.
* Tables contain rows and columns.
* Relationships connect related records across tables.
* SQLite stores database information in a local file.

## 3. Tables, Rows, and Columns

### What it is

A table organizes data into rows and columns.

### Important Points

* A **table** stores related information.
* A **row** represents one record.
* A **column** represents one attribute.
* Each column has a name and a declared data type.
* Each record can be identified using a unique ID.

### Example

```text
products
-------------------------
id    name       price
1     Laptop     50000
2     Mouse      500
3     Keyboard   1200
```

## 4. Data Types in SQLite

### What it is

Data types describe the kind of values a column is intended to store.

### Important Points

* `INTEGER` — whole numbers.
* `REAL` — floating-point numbers.
* `TEXT` — text values.
* `BLOB` — binary data.
* `NULL` — a missing or unknown value.
* SQLite uses type affinity, so declared types do not always strictly restrict the values stored.

### Basic Syntax

```sql
CREATE TABLE products (
    id INTEGER,
    name TEXT,
    price REAL,
    stock INTEGER
);
```

## 5. Creating Tables

### What it is

The `CREATE TABLE` statement creates a new table in a database.

### Important Points

* Every table needs a name.
* Columns are defined inside parentheses.
* Each column has a name and declared type.
* Constraints can be used to protect data quality.
* `IF NOT EXISTS` prevents an error if the table already exists.

### Basic Syntax

```sql
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL
);
```

## 6. Primary Keys

### What it is

A primary key uniquely identifies each record in a table.

### Important Points

* Primary key values must be unique.
* A primary key cannot contain `NULL`.
* A table has one primary key, which can consist of one or multiple columns.
* IDs are commonly used as primary keys.
* `INTEGER PRIMARY KEY` normally acts as the row ID in SQLite.

### Basic Syntax

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

## 7. Inserting Records — INSERT

### What it is

The `INSERT` statement adds new records to a table.

### Important Points

* Specify the table name.
* Specify the columns that will receive values.
* Values should match the intended columns.
* Text values are enclosed in single quotes.
* SQLite can automatically assign an ID when an appropriate integer primary key is omitted.

### Basic Syntax

```sql
INSERT INTO products (name, price)
VALUES ('Laptop', 50000);
```

### Inserting Multiple Records

```sql
INSERT INTO products (name, price)
VALUES
    ('Mouse', 500),
    ('Keyboard', 1200);
```

## 8. Retrieving Records — SELECT

### What it is

The `SELECT` statement retrieves data from a table.

### Important Points

* `SELECT *` retrieves all columns.
* Specify column names to retrieve only selected columns.
* `FROM` identifies the table.
* `SELECT` does not modify stored records.

### Basic Syntax

```sql
SELECT * FROM products;
```

### Selecting Specific Columns

```sql
SELECT name, price
FROM products;
```

## 9. Filtering Records — WHERE

### What it is

The `WHERE` clause selects records that match a specified condition.

### Important Points

* `=` checks equality.
* `!=` and `<>` check inequality.
* `>` and `<` compare values.
* `>=` and `<=` check greater-than-or-equal and less-than-or-equal conditions.
* `IS NULL` checks for missing values.
* `WHERE` can be used with `SELECT`, `UPDATE`, and `DELETE`.

### Basic Syntax

```sql
SELECT *
FROM products
WHERE price > 1000;
```

### Filtering Text Values

```sql
SELECT *
FROM products
WHERE name = 'Laptop';
```

## 10. Sorting Records — ORDER BY

### What it is

The `ORDER BY` clause sorts query results using one or more columns.

### Important Points

* `ASC` sorts in ascending order.
* `DESC` sorts in descending order.
* Ascending order is the default.
* Multiple columns can be used for sorting.

### Basic Syntax

```sql
SELECT *
FROM products
ORDER BY price ASC;
```

### Sorting in Descending Order

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

## 11. Updating Records — UPDATE

### What it is

The `UPDATE` statement modifies existing records in a table.

### Important Points

* `SET` specifies the new values.
* `WHERE` identifies the records to update.
* Without `WHERE`, all records may be updated.
* Always check the condition before executing an update.

### Basic Syntax

```sql
UPDATE products
SET price = 55000
WHERE id = 1;
```

## 12. Deleting Records — DELETE

### What it is

The `DELETE` statement removes records from a table.

### Important Points

* `WHERE` identifies the records to remove.
* Without `WHERE`, all records in the table may be deleted.
* Related records may be affected by foreign-key rules.
* Check the condition carefully before deleting data.

### Basic Syntax

```sql
DELETE FROM products
WHERE id = 1;
```

## 13. Using Conditions — AND, OR, NOT

### What it is

Logical operators combine conditions or reverse a condition in a SQL query.

### Important Points

* `AND` requires all conditions to be true.
* `OR` requires at least one condition to be true.
* `NOT` reverses a condition.
* Parentheses help group conditions clearly.

### Basic Syntax

```sql
SELECT *
FROM products
WHERE price > 1000 AND stock > 0;
```

### Using OR

```sql
SELECT *
FROM products
WHERE name = 'Laptop' OR name = 'Mouse';
```

### Using NOT

```sql
SELECT *
FROM products
WHERE NOT price > 1000;
```

## 14. Aggregate Functions

### What it is

Aggregate functions calculate a single result from multiple records.

### Important Points

* `COUNT()` counts records or non-NULL values.
* `SUM()` calculates a total.
* `AVG()` calculates an average.
* `MIN()` finds the smallest value.
* `MAX()` finds the largest value.
* Most aggregate functions ignore `NULL` values.

### Basic Syntax

```sql
SELECT COUNT(*)
FROM products;
```

### Calculating a Total

```sql
SELECT SUM(price)
FROM products;
```

### Calculating an Average

```sql
SELECT AVG(price)
FROM products;
```

## 15. Grouping Records — GROUP BY and HAVING

### What it is

`GROUP BY` groups records with matching values, while `HAVING` filters the resulting groups.

### Important Points

* `GROUP BY` is useful for category-wise summaries.
* It is commonly used with aggregate functions.
* `WHERE` filters individual rows before grouping.
* `HAVING` filters groups after aggregation.
* Grouped queries can calculate counts, totals, and averages.

### Basic Syntax

```sql
SELECT category, COUNT(*) AS total
FROM products
GROUP BY category;
```

### Using HAVING

```sql
SELECT category, COUNT(*) AS total
FROM products
GROUP BY category
HAVING COUNT(*) > 1;
```

## 16. Joining Tables — JOIN

### What it is

A `JOIN` combines related records from two or more tables.

### Important Points

* `INNER JOIN` returns records with matching values in both tables.
* `LEFT JOIN` returns all records from the left table and matching records from the right table.
* Unmatched columns from the right table contain `NULL`.
* Join conditions commonly use primary and foreign keys.
* Use table aliases to make queries easier to read.

### Example Tables

```text
customers
----------------
id    name
1     Sam
2     Alex

orders
-------------------------
id    customer_id    total
1     1              2000
2     1              500
```

### Basic Syntax

```sql
SELECT customers.name, orders.total
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;
```

### Using LEFT JOIN

```sql
SELECT customers.name, orders.total
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id;
```

## 17. Relationships Between Tables

### What it is

Relationships describe how records in different tables are connected.

### Important Points

* **One-to-one:** one record relates to at most one record in another table.
* **One-to-many:** one record relates to multiple records in another table.
* **Many-to-many:** multiple records relate to multiple records in another table.
* Foreign keys represent relationships between tables.
* Many-to-many relationships usually require a junction table.

### Example

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

## 18. Creating and Managing an Inventory Database

### What it is

An inventory database stores information about products, prices, and available stock.

### Important Points

* Each product should have a unique ID.
* Product names should be required where appropriate.
* Prices and stock quantities should be validated.
* Queries can search for products and summarize inventory.
* Updates should keep stock quantities accurate.

### Basic Syntax

```sql
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL CHECK(price >= 0),
    stock INTEGER CHECK(stock >= 0)
);
```

### Adding a Product

```sql
INSERT INTO products (name, price, stock)
VALUES ('Laptop', 50000, 10);
```

### Viewing Available Stock

```sql
SELECT name, stock
FROM products
WHERE stock > 0;
```

### Updating Stock

```sql
UPDATE products
SET stock = 8
WHERE id = 1;
```

## 19. Executing SQL Manually and Through Python

### What it is

SQL statements can be executed manually using a database tool or automatically through a Python program.

### Important Points

* Manual SQL execution is useful for learning and checking data.
* Python can automate database operations.
* SQL commands remain mostly the same in both approaches.
* Python's `sqlite3` module connects Python programs to SQLite databases.
* User-provided values should be passed through parameterized queries when using Python.

### Basic Syntax

```python
import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)

connection.close()
```

## 20. Important SQL Best Practices

### Important Points

* Use meaningful table and column names.
* Define primary keys for tables.
* Use foreign keys to maintain relationships.
* Use `WHERE` carefully with `UPDATE` and `DELETE`.
* Use constraints to prevent invalid data.
* Use `JOIN` to retrieve related information.
* Use aggregate functions for summaries.
* Use parameterized queries for user-provided values in Python.
* Keep queries readable and organized.
