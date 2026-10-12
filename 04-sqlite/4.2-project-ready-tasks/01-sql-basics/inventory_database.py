import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    price REAL NOT NULL CHECK (price >= 0),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
)
""")

cursor.execute(
    "INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
    ("Electronics",)
)

cursor.execute(
    "INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
    ("Stationery",)
)

cursor.execute(
    "INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
    ("Furniture",)
)

cursor.execute(
    "SELECT category_id FROM categories WHERE category_name = ?",
    ("Electronics",)
)
electronics_id = cursor.fetchone()[0]

cursor.execute(
    "SELECT category_id FROM categories WHERE category_name = ?",
    ("Stationery",)
)
stationery_id = cursor.fetchone()[0]

cursor.execute(
    "SELECT category_id FROM categories WHERE category_name = ?",
    ("Furniture",)
)
furniture_id = cursor.fetchone()[0]

cursor.execute(
    "INSERT INTO products (product_name, category_id, quantity, price) "
    "VALUES (?, ?, ?, ?)",
    ("Keyboard", electronics_id, 15, 799.00)
)

cursor.execute(
    "INSERT INTO products (product_name, category_id, quantity, price) "
    "VALUES (?, ?, ?, ?)",
    ("Notebook", stationery_id, 50, 60.00)
)

cursor.execute(
    "INSERT INTO products (product_name, category_id, quantity, price) "
    "VALUES (?, ?, ?, ?)",
    ("Office Chair", furniture_id, 8, 4500.00)
)

connection.commit()

print("All Products:")
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

for product in products:
    print(product)

print("\nProducts with low stock:")
cursor.execute(
    "SELECT product_name, quantity FROM products WHERE quantity < ?",
    (20,)
)

low_stock_products = cursor.fetchall()

for product in low_stock_products:
    print(product)

cursor.execute(
    "UPDATE products SET quantity = ? WHERE product_name = ?",
    (40, "Keyboard")
)

connection.commit()

print("\nUpdated Products:")
cursor.execute("SELECT * FROM products")

for product in cursor.fetchall():
    print(product)

connection.close()

