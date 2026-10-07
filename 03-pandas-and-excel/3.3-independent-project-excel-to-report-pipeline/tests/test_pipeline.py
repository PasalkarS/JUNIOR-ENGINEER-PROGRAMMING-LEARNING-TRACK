import unittest
import pandas as pd

from cleaner import clean_sales_data
from validator import validate_sales_data
from transformer import (
    transform_sales_data,
    create_monthly_summary
)


class TestPipeline(unittest.TestCase):

    def setUp(self):

        self.sales = pd.DataFrame({
            "Sale_ID": [1, 2, 3],
            "Customer": [
                "Rahul",
                "Priya",
                "Amit"
            ],
            "Product_ID": [
                "P1",
                "P2",
                "P1"
            ],
            "Quantity": [2, 1, 3],
            "Price": [1000, 2000, 1000],
            "Sale_Date": [
                "2026-01-10",
                "2026-01-15",
                "2026-02-05"
            ]
        })

        self.products = pd.DataFrame({
            "Product_ID": [
                "P1",
                "P2"
            ],
            "Product_Name": [
                "Mouse",
                "Keyboard"
            ],
            "Category": [
                "Accessories",
                "Accessories"
            ]
        })

    def test_validation(self):

        errors = validate_sales_data(
            self.sales
        )

        self.assertEqual(errors, [])

    def test_cleaning(self):

        cleaned = clean_sales_data(
            self.sales
        )

        self.assertEqual(
            len(cleaned),
            3
        )

    def test_total_calculation(self):

        result = transform_sales_data(
            self.sales,
            self.products
        )

        self.assertEqual(
            result.iloc[0]["Total"],
            2000
        )

    def test_monthly_summary(self):

        result = transform_sales_data(
            self.sales,
            self.products
        )

        summary = create_monthly_summary(
            result
        )

        self.assertEqual(
            len(summary),
            2
        )

    def test_invalid_quantity(self):

        bad_sales = self.sales.copy()

        bad_sales.loc[0, "Quantity"] = -1

        errors = validate_sales_data(
            bad_sales
        )

        self.assertTrue(
            len(errors) > 0
        )


if __name__ == "__main__":
    unittest.main()
