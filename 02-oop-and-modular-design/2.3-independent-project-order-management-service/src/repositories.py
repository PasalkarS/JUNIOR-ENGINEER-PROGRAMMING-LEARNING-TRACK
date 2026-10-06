
from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def find_by_id(self, order_id):
        pass

    @abstractmethod
    def find_all(self):
        pass


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def save(self, order):
        self.orders[order.order_id] = order

    def find_by_id(self, order_id):
        return self.orders.get(order_id)

    def find_all(self):
        return list(self.orders.values())
