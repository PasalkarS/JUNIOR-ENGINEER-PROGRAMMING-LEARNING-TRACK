```sql
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    price REAL NOT NULL CHECK (price >= 0),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories (category_name)
VALUES
    ('Electronics'),
    ('Stationery'),
    ('Furniture');

INSERT INTO products (product_name, category_id, quantity, price)
VALUES
    ('Keyboard', 1, 15, 799.00),
    ('Mouse', 1, 25, 399.00),
    ('Notebook', 2, 50, 60.00),
    ('Office Chair', 3, 8, 4500.00);
```
