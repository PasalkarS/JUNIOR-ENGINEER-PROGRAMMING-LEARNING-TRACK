import unittest
from unittest.mock import patch

import services


class TestInventoryServices(unittest.TestCase):

    @patch("services.repository.add_product")
    def test_add_product(self, mock_add_product):
        mock_add_product.return_value = 1

        product_id = services.add_new_product(
            "Keyboard", 1, 10, 799.00
        )

        self.assertEqual(product_id, 1)

    def test_empty_product_name(self):
        with self.assertRaises(ValueError):
            services.add_new_product("", 1, 10, 799.00)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            services.add_new_product("Keyboard", 1, -5, 799.00)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            services.add_new_product("Keyboard", 1, 10, -100)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            services.add_new_product("Keyboard", 0, 10, 799.00)


if __name__ == "__main__":
    unittest.main()
