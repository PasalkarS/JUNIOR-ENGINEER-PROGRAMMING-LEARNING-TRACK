-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE
);

-- Create suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    phone TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    supplier_id INTEGER,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    price REAL NOT NULL CHECK (price >= 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id),

    FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)
);

-- Create an index for faster category searches
CREATE INDEX IF NOT EXISTS idx_products_category
ON products(category_id);

-- Create an index for faster product name searches
CREATE INDEX IF NOT EXISTS idx_products_name
ON products(product_name);

-- Insert sample categories
INSERT INTO categories (category_name)
VALUES
    ('Electronics'),
    ('Stationery'),
    ('Furniture');

-- Insert sample suppliers
INSERT INTO suppliers (supplier_name, phone)
VALUES
    ('Tech Supplies', '9876543210'),
    ('Office Mart', '9876501234');

-- Insert sample products
INSERT INTO products (
    product_name,
    category_id,
    supplier_id,
    quantity,
    price
)
VALUES
    ('Keyboard', 1, 1, 15, 799.00),
    ('Notebook', 2, 2, 50, 60.00),
    ('Office Chair', 3, 2, 8, 4500.00);

-- Display products with category and supplier information
SELECT
    products.product_id,
    products.product_name,
    categories.category_name,
    suppliers.supplier_name,
    products.quantity,
    products.price,
    products.created_at
FROM products
JOIN categories
    ON products.category_id = categories.category_id
LEFT JOIN suppliers
    ON products.supplier_id = suppliers.supplier_id;
