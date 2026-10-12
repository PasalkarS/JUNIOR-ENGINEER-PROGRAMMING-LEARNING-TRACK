import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import repository


class TestInventoryRepository(unittest.TestCase):

    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_directory.name) / "test.db"

        connection = sqlite3.connect(self.database_path)
        connection.execute("PRAGMA foreign_keys = ON")

        connection.execute("""
            CREATE TABLE categories (
                category_id INTEGER PRIMARY KEY,
                category_name TEXT NOT NULL UNIQUE
            )
        """)

        connection.execute("""
            CREATE TABLE products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                category_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                price REAL NOT NULL CHECK (price >= 0),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id)
                    REFERENCES categories(category_id)
            )
        """)

        connection.execute(
            "INSERT INTO categories VALUES (1, 'Electronics')"
        )
        connection.commit()
        connection.close()

        self.connection_patch = patch(
            "repository.get_connection",
            side_effect=self.get_test_connection
        )
        self.connection_patch.start()

    def get_test_connection(self):
        connection = sqlite3.connect(self.database_path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def tearDown(self):
        self.connection_patch.stop()
        self.temp_directory.cleanup()

    def test_add_and_get_product(self):
        product_id = repository.add_product(
            "Keyboard", 1, 10, 799.00
        )

        product = repository.search_products("Keyboard")

        self.assertEqual(len(product), 1)
        self.assertEqual(product[0][0], product_id)
        self.assertEqual(product[0][1], "Keyboard")

    def test_update_product(self):
        product_id = repository.add_product(
            "Mouse", 1, 5, 399.00
        )

        updated = repository.update_product(
            product_id, "Wireless Mouse", 1, 8, 599.00
        )

        self.assertTrue(updated)

        products = repository.search_products("Wireless Mouse")
        self.assertEqual(products[0][3], 8)

    def test_delete_product(self):
        product_id = repository.add_product(
            "Keyboard", 1, 10, 799.00
        )

        deleted = repository.delete_product(product_id)

        self.assertTrue(deleted)
        self.assertEqual(repository.get_all_products(), [])


if __name__ == "__main__":
    unittest.main()
