
from models import Order


class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def create_order(self, order_id, customer, product, quantity, price):
        if self.repository.find_by_id(order_id):
            raise ValueError("Order ID already exists")

        order = Order(
            order_id,
            customer,
            product,
            quantity,
            price
        )

        self.repository.save(order)

        return order

    def get_order(self, order_id):
        order = self.repository.find_by_id(order_id)

        if order is None:
            raise ValueError("Order not found")

        return order

    def get_all_orders(self):
        return self.repository.find_all()
