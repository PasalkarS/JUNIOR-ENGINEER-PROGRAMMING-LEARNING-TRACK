# 3 — Schema Design

## 1. Introduction to Database Schema Design

* A database schema defines how data is organized inside a database.
* It describes tables, columns, data types, keys, constraints, and relationships.
* Good schema design helps keep data organized, accurate, and easy to maintain.

**Important points**

* Identify the information the application needs to store.
* Create separate tables for different types of entities.
* Choose suitable data types for columns.
* Define primary keys and foreign keys.
* Avoid unnecessary duplication of data.
* Plan relationships between tables before writing queries.

## 2. Identifying Entities and Tables

An entity is something about which an application stores information. Each main entity usually has its own table.

**Example**

An inventory application may contain these entities:

* Products
* Categories
* Suppliers
* Orders
* Order Items

**Important points**

* A product table stores product information.
* A category table stores category information.
* A supplier table stores supplier information.
* An order table stores order details.
* An order items table stores products belonging to each order.
* Separate tables help organize related information.

## 3. Choosing Columns and Data Types

Columns define the individual pieces of information stored in a table. Each column should have a suitable data type.

**Common SQLite data types**

| Data type | Purpose                  | Example                 |
| --------- | ------------------------ | ----------------------- |
| `INTEGER` | Whole numbers            | Quantity, ID            |
| `REAL`    | Decimal numbers          | Price, measurement      |
| `TEXT`    | Text values              | Name, email             |
| `BLOB`    | Binary data              | Image or file data      |
| `NULL`    | Missing or unknown value | Unavailable information |

**Important points**

* Use `INTEGER` for whole numbers and identifiers.
* Use `TEXT` for names, descriptions, and email addresses.
* Use `REAL` for measurements that require decimal values.
* SQLite uses dynamic typing, so declared column types do not always restrict stored values as strictly as in some other databases.
* Choose clear and meaningful column names.
* Avoid storing unrelated information in one column.

## 4. Primary Keys

A primary key uniquely identifies each record in a table.

**Basic syntax**

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL
);
```

**Important points**

* Every table should normally have a primary key.
* A primary key must uniquely identify each row.
* A primary key cannot contain `NULL`.
* `INTEGER PRIMARY KEY` in SQLite aliases the rowid and can automatically generate an identifier when one is not provided.
* Use primary keys to identify records reliably.
* Do not use a product name as a primary key if the name can change or repeat.

## 5. Foreign Keys

A foreign key connects a record in one table to a record in another table.

**Basic syntax**

```sql
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
```

**Important points**

* A foreign key refers to a key in another table.
* It helps maintain relationships between tables.
* A product can refer to a category using `category_id`.
* Foreign key values must refer to an existing parent record, unless the foreign key value is `NULL` and the relationship permits it.
* SQLite foreign-key enforcement should be enabled for each connection using `PRAGMA foreign_keys = ON`.

## 6. Relationships Between Tables

Relationships describe how records in different tables are connected.

### One-to-One Relationship

One record in a table is associated with one record in another table.

**Example:** A user and their unique profile.

### One-to-Many Relationship

One record in a table can be associated with many records in another table.

**Example:** One category can contain many products.

### Many-to-Many Relationship

Many records in one table can be associated with many records in another table.

**Example:** Many orders can contain many products.

**Important points**

* One-to-one relationships often use a foreign key with a `UNIQUE` constraint.
* One-to-many relationships usually store the foreign key on the “many” side.
* Many-to-many relationships usually require a junction table.
* Correct relationships reduce duplicated data.
* Foreign keys help maintain referential integrity.

## 7. Junction Tables

A junction table connects two tables in a many-to-many relationship.

**Basic syntax**

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
);

CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**Important points**

* `student_courses` connects students and courses.
* Each row represents one student enrolled in one course.
* The combined primary key prevents duplicate student-course pairs.
* A junction table can contain additional details, such as enrollment date.
* This structure avoids storing multiple course IDs in a single column.

## 8. Database Normalization

Normalization is the process of organizing data to reduce unnecessary duplication and prevent data inconsistencies.

**Important points**

* Store each type of information in an appropriate table.
* Avoid repeating the same details across many records.
* Use primary and foreign keys to connect related data.
* Separate data when it represents a different entity.
* Normalization makes updates and maintenance more reliable.

### First Normal Form (1NF)

* Each column should contain a single value for each row.
* Avoid storing multiple values in one column.
* Each row should be identifiable.

### Second Normal Form (2NF)

* The table should satisfy 1NF.
* Every non-key column should depend on the entire primary key, not just part of a composite key.

### Third Normal Form (3NF)

* The table should satisfy 2NF.
* Non-key columns should depend on the key rather than on other non-key columns.

## 9. Avoiding Data Duplication

Data duplication happens when the same information is stored repeatedly without a good reason.

**Example**

Instead of storing the category name repeatedly in every product record, store categories in a separate table and reference them using `category_id`.

**Important points**

* Repeated data takes up additional space.
* Updating duplicated information can cause inconsistencies.
* Separate tables can store information that is shared by multiple records.
* Use foreign keys to connect related records.
* Some duplication may be intentional for reporting or performance, but it should be a deliberate decision.

## 10. Constraints

Constraints are rules that control what data can be stored in a table.

**Common constraints**

* `PRIMARY KEY` — uniquely identifies each record.
* `FOREIGN KEY` — maintains relationships between tables.
* `NOT NULL` — prevents a column from storing `NULL`.
* `UNIQUE` — prevents duplicate values in a column or column combination.
* `CHECK` — validates a condition.
* `DEFAULT` — supplies a default value when one is not provided.

**Basic syntax**

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0
);
```

**Important points**

* Constraints help prevent invalid data.
* `NOT NULL` is useful for required information.
* `UNIQUE` can prevent duplicate email addresses or codes.
* `CHECK` can enforce rules such as non-negative prices.
* `DEFAULT` supplies a value when a column is omitted.
* Constraints should reflect the actual requirements of the application.

## 11. Referential Integrity

Referential integrity means that relationships between records remain valid.

**Example**

A product should not refer to a category that does not exist.

**Important points**

* Foreign keys help maintain referential integrity.
* Foreign-key enforcement must be enabled on SQLite connections.
* Invalid references should be rejected.
* Deleting a parent record can affect related records.
* `ON DELETE CASCADE` can automatically delete related child records when the parent is deleted.
* Choose deletion rules carefully to avoid removing data unintentionally.

## 12. Indexes

An index helps SQLite find records more efficiently without scanning every row in many situations.

**Basic syntax**

```sql
CREATE INDEX idx_products_name
ON products(product_name);
```

**Important points**

* Indexes can improve searches and joins.
* Columns frequently used in `WHERE`, `JOIN`, or sorting operations may benefit from indexes.
* Indexes require additional storage.
* Inserts, updates, and deletes can become slower because indexes also need maintenance.
* Avoid creating unnecessary indexes.
* Use `EXPLAIN QUERY PLAN` to inspect how SQLite executes a query.

## 13. Unique and Composite Indexes

A unique index prevents duplicate indexed values. A composite index contains more than one column.

**Basic syntax**

```sql
CREATE UNIQUE INDEX idx_products_code
ON products(product_code);
```

```sql
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);
```

**Important points**

* A unique index prevents duplicate non-`NULL` values in the indexed key.
* A composite index can help queries that filter or sort by its leading columns.
* The order of columns in a composite index matters.
* A unique constraint is often a clearer way to express uniqueness as part of a table's design.
* Choose indexes based on actual query patterns.

## 14. Timestamps

Timestamps record when a record was created or last updated.

**Basic syntax**

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT
);
```

**Important points**

* `created_at` stores when the record was created.
* `updated_at` can store when the record was last changed.
* SQLite does not have a dedicated date/time storage class.
* Dates and times can be stored as `TEXT`, `REAL`, or `INTEGER`.
* `CURRENT_TIMESTAMP` supplies a UTC timestamp formatted as text.
* An `updated_at` column does not update automatically just because a row changes; application logic or a trigger must update it.

## 15. Naming Conventions

Naming conventions make a database easier to understand and maintain.

**Important points**

* Use meaningful table names, such as `products` and `orders`.
* Use clear column names, such as `product_id` and `order_date`.
* Use consistent naming throughout the database.
* Avoid spaces and confusing abbreviations in identifiers.
* Use names that describe the information stored.
* Follow one consistent style, such as `snake_case`.

## 16. Designing a Multi-Table Schema

A multi-table schema stores different entities in separate tables and connects them through keys.

**Example: Inventory and Orders Database**

```sql
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**Important points**

* Categories group related products.
* Products reference their categories.
* Orders store order-level information.
* Order items connect orders and products.
* `order_items` allows one order to contain multiple products.
* `unit_price` records the price used for that order item, even if the product's current price changes later.
* Foreign-key enforcement must be enabled on the connection.

## 17. Database Migrations

A migration is a controlled change to a database schema as an application develops.

**Examples**

* Adding a new column.
* Creating a new table.
* Adding an index.
* Changing how data is stored.

**Important points**

* Applications often need schema changes after their first release.
* Migrations document and apply these changes in a controlled order.
* Existing data must be considered when changing a schema.
* Back up important data before risky changes.
* Test migrations against a copy of the database.
* Avoid manually changing production databases without tracking the changes.

## 18. Schema Versioning

Schema versioning records which version of the database structure is currently installed.

**Basic syntax**

```sql
PRAGMA user_version = 1;
```

To read the version:

```sql
PRAGMA user_version;
```

**Important points**

* SQLite's `user_version` stores an application-defined integer.
* It can help an application identify which migrations need to run.
* Increase the version when a migration changes the schema.
* Version numbers do not automatically perform migrations.
* Application code must check the version and apply the required changes.

## 19. Database Initialization

Database initialization prepares the database before the application uses it.

**Important points**

* Create the required tables.
* Define primary keys, foreign keys, and constraints.
* Create necessary indexes.
* Enable foreign-key enforcement for each connection.
* Apply any required migrations.
* Make initialization safe to run more than once where appropriate.

**Basic syntax**

```python
import sqlite3

connection = sqlite3.connect("inventory.db")
connection.execute("PRAGMA foreign_keys = ON")

connection.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0)
)
""")

connection.commit()
connection.close()
```

## 20. Important Schema Design Best Practices

* Identify entities before creating tables.
* Give each table a clear purpose.
* Use primary keys to identify records.
* Use foreign keys to define relationships.
* Normalize data to reduce unnecessary duplication.
* Apply constraints to protect data quality.
* Enable foreign-key enforcement on SQLite connections.
* Add indexes based on actual query requirements.
* Store timestamps consistently.
* Use clear and consistent names.
* Plan migrations for future schema changes.
* Document important relationships and design decisions.
* Test the schema with valid and invalid data before using it in an application.
