"""Abstract base repository contract for order persistence."""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models import Order


class OrderRepository(ABC):
    """
    Abstract interface for Order persistence.
    Decouples domain business rules from storage mechanisms.
    """

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by its unique identifier."""
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        """Retrieve all persisted orders."""
        pass

    @abstractmethod
    def save(self, order: Order) -> None:
        """Persist or update an order."""
        pass

    @abstractmethod
    def delete(self, order_id: str) -> bool:
        """Delete an order by ID. Returns True if found and removed."""
        pass
