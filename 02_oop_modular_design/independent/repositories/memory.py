"""In-memory implementation of OrderRepository (ideal for unit tests and ephemeral caching)."""

from typing import Dict, List, Optional
from domain.models import Order
from .base import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    """Stores orders in an in-memory dictionary keyed by order_id."""

    def __init__(self):
        self._storage: Dict[str, Order] = {}

    def get_by_id(self, order_id: str) -> Optional[Order]:
        return self._storage.get(order_id)

    def list_all(self) -> List[Order]:
        return list(self._storage.values())

    def save(self, order: Order) -> None:
        self._storage[order.order_id] = order

    def delete(self, order_id: str) -> bool:
        if order_id in self._storage:
            del self._storage[order_id]
            return True
        return False

    def clear(self) -> None:
        """Utility for test suites."""
        self._storage.clear()
