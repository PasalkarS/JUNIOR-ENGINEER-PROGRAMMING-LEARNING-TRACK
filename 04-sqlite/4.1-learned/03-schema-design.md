# Relational Schema Design & Normalization

> **Module 04: SQLite | Topic 03**

## 1. Learning Outcomes
- **Normalization Basics:** Eliminate data redundancy using 1NF, 2NF, and 3NF principles.
- **Integrity Constraints:** Enforce data accuracy with `NOT NULL`, `CHECK`, `UNIQUE`, and `FOREIGN KEY`.
- **Indexing Strategy:** Create targeted indexes on frequently filtered or joined columns.
- **Schema Migrations:** Understand versioned table schema evolution.

## 2. Key Syntax & Concepts

### Normalized Multi-Table Schema
```sql
-- Customers Table
CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- Orders Table
CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('PENDING', 'PAID', 'SHIPPED', 'CANCELLED')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items Table (Many-to-Many Bridge)
CREATE TABLE order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT NOT NULL,
    product_sku TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create Index for Foreign Key and Search acceleration
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_date ON orders(order_date);
```

## 3. Common Mistakes & Gotchas
- **Denormalizing Too Early:** Storing comma-separated lists of values inside a single column violates 1NF and prevents effective indexing or querying.
- **Over-Indexing:** Indexes accelerate reads (`SELECT`) but add write overhead on `INSERT`/`UPDATE`. Only index foreign keys and high-frequency filter columns.

## 4. Practice Tasks
- **Task 1:** Design a schema for a library system with `authors`, `books`, and `borrow_records`, including appropriate primary and foreign key constraints.

## 5. Self-Check Questions
- **Q1:** What does `ON DELETE CASCADE` do when a parent row is deleted?
- **Q2:** Why should status values have a `CHECK` constraint?
