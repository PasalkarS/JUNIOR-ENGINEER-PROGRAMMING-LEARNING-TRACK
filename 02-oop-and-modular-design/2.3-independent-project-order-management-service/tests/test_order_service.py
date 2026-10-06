
import unittest

from models import Order
from repositories import MockOrderRepository
from services import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.repository = MockOrderRepository()
        self.service = OrderService(self.repository)

    def test_create_order(self):
        order = self.service.create_order(
            "O1", "Rahul", "Laptop", 1, 50000
        )

        self.assertEqual(order.order_id, "O1")
        self.assertEqual(order.customer, "Rahul")

    def test_calculate_total(self):
        order = Order("O1", "Rahul", "Mouse", 2, 500)

        self.assertEqual(order.calculate_total(), 1000)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.service.create_order(
                "O1", "Rahul", "Mouse", 0, 500
            )

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            self.service.create_order(
                "O1", "Rahul", "Mouse", 1, -500
            )

    def test_duplicate_order_id(self):
        self.service.create_order(
            "O1", "Rahul", "Mouse", 1, 500
        )

        with self.assertRaises(ValueError):
            self.service.create_order(
                "O1", "Amit", "Keyboard", 1, 1000
            )

    def test_order_not_found(self):
        with self.assertRaises(ValueError):
            self.service.get_order("O99")

    def test_get_all_orders(self):
        self.service.create_order(
            "O1", "Rahul", "Mouse", 1, 500
        )
        self.service.create_order(
            "O2", "Amit", "Keyboard", 1, 1000
        )

        orders = self.service.get_all_orders()

        self.assertEqual(len(orders), 2)

    def test_repository_saves_order(self):
        self.service.create_order(
            "O1", "Rahul", "Mouse", 1, 500
        )

        saved_order = self.repository.find_by_id("O1")

        self.assertIsNotNone(saved_order)
        self.assertEqual(saved_order.product, "Mouse")


if __name__ == "__main__":
    unittest.main()
