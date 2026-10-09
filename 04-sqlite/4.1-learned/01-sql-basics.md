1 SQL Basics
1. Introduction to SQL

What it is

SQL (Structured Query Language) is used to create, manage, and retrieve data from relational databases.

Important Points

SQL works with data stored in tables.
It supports creating, reading, updating, and deleting records.
SQLite uses SQL to manage local databases.
SQL commands can be executed manually or through Python.
2. Introduction to Relational Databases

What it is

A relational database stores related information in tables that can be connected using keys.

Important Points

A database can contain multiple tables.
Tables store different types of information.
Relationships connect records across tables.
SQLite stores its database in a local file.
3. Tables, Rows, and Columns

What it is

A table organizes information into rows and columns.

Important Points

A row represents one record.
A column represents one attribute.
Each column has a name and data type.
A database can contain multiple related tables.

Example

id	name	price
1	Laptop	50000
2	Mouse	500
4. Data Types in SQLite

What it is

Data types describe the kind of values stored in a column.

Important Points

NULL represents a missing or unknown value.
INTEGER stores whole numbers.
REAL stores floating-point numbers.
TEXT stores text.
BLOB stores binary data.
SQLite also uses type affinity, so column declarations do not always strictly restrict stored values.

Basic Syntax

CREATE TABLE products (
    id INTEGER,
    name TEXT,
    price REAL,
    stock INTEGER
);
5. Creating Tables

What it is

The CREATE TABLE statement creates a new table in a database.

Important Points

Every table needs a name.
Columns are defined inside parentheses.
Each column has a name and declared type.
Constraints can be added to protect data quality.
Use IF NOT EXISTS to avoid an error if the table already exists.

Basic Syntax

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL
);
6. Primary Keys

What it is

A primary key uniquely identifies each record in a table.

Important Points

Primary key values must be unique.
A primary key cannot be NULL.
A table has one primary key, which can contain one or multiple columns.
IDs are commonly used as primary keys.
In SQLite, INTEGER PRIMARY KEY normally aliases the rowid.

Basic Syntax

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
7. Inserting Records — INSERT

What it is

INSERT adds new records to a table.

Important Points

Specify the table name.
Specify the columns receiving values.
Values must match the intended columns.
Text values are written inside quotes.
Omitting an automatically generated ID allows SQLite to assign one.

Basic Syntax

INSERT INTO products (name, price)
VALUES ('Laptop', 50000);
8. Retrieving Records — SELECT

What it is

SELECT retrieves data from a table.

Important Points

SELECT * retrieves all columns.
Specify column names to retrieve only selected data.
FROM identifies the table.
Queries do not change the stored records.

Basic Syntax

SELECT * FROM products;

SELECT name, price
FROM products;
9. Filtering Records — WHERE

What it is

WHERE selects records that match a condition.

Important Points

Use comparison operators such as =, !=, >, <, >=, and <=.
Multiple conditions can be combined.
Text comparisons usually require quotes.
Use IS NULL to find missing values.

Basic Syntax

SELECT *
FROM products
WHERE price > 1000;
10. Sorting Records — ORDER BY

What it is

ORDER BY sorts query results by one or more columns.

Important Points

ASC sorts in ascending order.
DESC sorts in descending order.
Ascending order is the default.
Multiple columns can be used for sorting.

Basic Syntax

SELECT *
FROM products
ORDER BY price DESC;
11. Updating Records — UPDATE

What it is

UPDATE changes existing records in a table.

Important Points

SET specifies the new values.
WHERE identifies the records to change.
Without WHERE, all records may be updated.
Check the condition carefully before executing an update.

Basic Syntax

UPDATE products
SET price = 55000
WHERE id = 1;
12. Deleting Records — DELETE

What it is

DELETE removes records from a table.

Important Points

WHERE identifies which records to remove.
Without WHERE, all records in the table may be deleted.
Deleting a record can affect related records depending on foreign-key rules.
Use conditions carefully.

Basic Syntax

DELETE FROM products
WHERE id = 1;
13. Using Conditions — AND, OR, NOT

What it is

Logical operators combine or reverse conditions in a query.

Important Points

AND requires all conditions to be true.
OR requires at least one condition to be true.
NOT reverses a condition.
Parentheses can make complex conditions easier to understand.

Basic Syntax

SELECT *
FROM products
WHERE price > 1000 AND stock > 0;
14. Aggregate Functions

What it is

Aggregate functions calculate a single result from multiple records.

Important Points

COUNT() counts records or non-NULL values.
SUM() calculates a total.
AVG() calculates an average.
MIN() finds the smallest value.
MAX() finds the largest value.
Most aggregate functions ignore NULL values.

Basic Syntax

SELECT COUNT(*) FROM products;

SELECT SUM(price) FROM products;

SELECT AVG(price) FROM products;
15. Grouping Records — GROUP BY and HAVING

What it is

GROUP BY groups records with matching values, while HAVING filters the resulting groups.

Important Points

Use GROUP BY for category-wise summaries.
Combine grouping with aggregate functions.
WHERE filters rows before grouping.
HAVING filters groups after aggregation.

Basic Syntax

SELECT category, COUNT(*) AS total
FROM products
GROUP BY category
HAVING COUNT(*) > 1;
16. Joining Tables

What it is

A JOIN combines related records from multiple tables.

Important Points

INNER JOIN returns matching records from both tables.
LEFT JOIN returns all records from the left table and matching records from the right.
Unmatched right-side values in a LEFT JOIN appear as NULL.
Join conditions commonly use primary and foreign keys.

Basic Syntax

SELECT orders.id, customers.name
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.id;
17. Relationships Between Tables

What it is

Relationships describe how records in different tables are connected.

Important Points

One-to-one: one record relates to one record.
One-to-many: one record relates to multiple records.
Many-to-many: multiple records relate to multiple records.
Foreign keys represent relationships.
Many-to-many relationships usually require a junction table.

Example

customers
---------
id
name

orders
------
id
customer_id
total

One customer can have multiple orders.

18. Creating and Managing an Inventory Database

What it is

An inventory database stores information about products and their available stock.

Important Points

Store product names, prices, and stock quantities.
Use unique IDs to identify products.
Validate prices and quantities.
Update stock when inventory changes.
Use queries to search and summarize products.

Basic Syntax

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL CHECK(price >= 0),
    stock INTEGER CHECK(stock >= 0)
);
19. Executing SQL Manually and Through Python

What it is

SQL can be executed using a database tool or through a Python program.

Important Points

Manual execution is useful for learning and inspecting data.
Python can automate database operations.
SQL statements remain mostly the same in both cases.
Python's sqlite3 module connects the application to SQLite.
