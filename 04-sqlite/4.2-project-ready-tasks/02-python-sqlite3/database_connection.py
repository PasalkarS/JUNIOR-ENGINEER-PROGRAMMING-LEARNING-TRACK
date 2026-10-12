import sqlite3


def connect_database():
    connection = sqlite3.connect("inventory.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity >= 0),
            price REAL NOT NULL CHECK (price >= 0)
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    print("Database and products table created successfully.")
