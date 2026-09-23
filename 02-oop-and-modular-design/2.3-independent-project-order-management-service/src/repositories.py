"""
Data persistence repositories using Python dictionaries.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from models import Product, Order

class IProductRepository(ABC):
    @abstractmethod
    def get_by_sku(self, sku: str) -> Optional[Product]:
        pass

    @abstractmethod
    def save(self, product: Product) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass

class InMemoryProductRepository(IProductRepository):
    def __init__(self):
        self._products: Dict[str, Product] = {}

    def get_by_sku(self, sku: str) -> Optional[Product]:
        return self._products.get(sku)

    def save(self, product: Product) -> None:
        self._products[product.sku] = product

    def list_all(self) -> List[Product]:
        return list(self._products.values())

class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        pass

class InMemoryOrderRepository(IOrderRepository):
    def __init__(self):
        self._orders: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._orders[order.order_id] = order

    def get_by_id(self, order_id: str) -> Optional[Order]:
        return self._orders.get(order_id)

    def list_all(self) -> List[Order]:
        return list(self._orders.values())
