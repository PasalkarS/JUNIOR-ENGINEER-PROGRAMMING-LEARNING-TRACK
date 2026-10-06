
from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def get_all(self):
        pass


class MemoryRepository(OrderRepository):
    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)

    def get_all(self):
        return self.orders


class MockRepository(OrderRepository):
    def __init__(self):
        self.saved_orders = []

    def save(self, order):
        print("Mock save:", order)
        self.saved_orders.append(order)

    def get_all(self):
        return self.saved_orders


class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def create_order(self, product, amount):
        if not product:
            raise ValueError("Product is required")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        order = {
            "product": product,
            "amount": amount
        }

        self.repository.save(order)
        print("Order created")


memory_repository = MemoryRepository()
service = OrderService(memory_repository)

service.create_order("Laptop", 50000)
service.create_order("Mouse", 1000)

print("Saved orders:", memory_repository.get_all())

print("\nTesting with mock repository:")

mock_repository = MockRepository()
test_service = OrderService(mock_repository)

test_service.create_order("Keyboard", 1500)
print("Mock orders:", mock_repository.get_all())


"""
Order created
Order created
Saved orders: [{'product': 'Laptop', 'amount': 50000}, {'product': 'Mouse', 'amount': 1000}]

Testing with mock repository:
Mock save: {'product': 'Keyboard', 'amount': 1500}
Order created
Mock orders: [{'product': 'Keyboard', 'amount': 1500}]

"""
