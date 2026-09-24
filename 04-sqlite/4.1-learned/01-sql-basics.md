# Relational Databases & SQL Basics

> **Module 04: SQLite | Topic 01**

## 1. Learning Outcomes
- **Core Concepts:** Understand relational tables, primary keys, and foreign key constraints.
- **DML Operations:** Execute SELECT, INSERT, UPDATE, and DELETE queries confidently.
- **Filtering & Aggregating:** Use WHERE, ORDER BY, GROUP BY, and aggregate functions (COUNT, SUM, AVG).
- **Table Joins:** Query related data using INNER JOIN and LEFT JOIN.

## 2. Key Syntax & Concepts

### Creating Tables & Constraints
```sql
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dept_id INTEGER,
    salary REAL NOT NULL,
    hired_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

### Essential DML Queries
```sql
-- Insert
INSERT INTO employees (name, dept_id, salary) VALUES ('Alice Smith', 1, 75000.0);

-- Query with Filter & Join
SELECT e.name, d.dept_name, e.salary
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary >= 60000.0
ORDER BY e.salary DESC;

-- Aggregation with Group By
SELECT d.dept_name, COUNT(e.emp_id) as headcount, AVG(e.salary) as avg_sal
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

## 3. Common Mistakes & Gotchas
- **Missing WHERE on UPDATE/DELETE:** Omitting `WHERE` mutates or deletes all rows across the entire table.
- **NULL Comparisons:** Comparing with `col = NULL` always evaluates to false. Use `col IS NULL` or `col IS NOT NULL`.

## 4. Practice Tasks
- **Task 1:** Create an inventory table with columns `sku`, `name`, `unit_price`, and `stock_qty`. Write queries to insert 5 items and select items with low stock (< 5 units).

## 5. Self-Check Questions
- **Q1:** What is the fundamental difference between `INNER JOIN` and `LEFT JOIN`?
- **Q2:** Why should primary keys generally be immutable integers rather than arbitrary strings?
