"""File-based implementation of OrderRepository using JSON serialization."""

import os
import json
from typing import Dict, List, Optional
from domain.models import Order
from .base import OrderRepository


class JsonFileOrderRepository(OrderRepository):
    """Persists orders into a JSON file, surviving process restarts."""

    def __init__(self, file_path: str = "orders.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        if not os.path.exists(self.file_path):
            directory = os.path.dirname(self.file_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            self._write_raw({})

    def _read_raw(self) -> Dict[str, dict]:
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return {}
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}

    def _write_raw(self, data: Dict[str, dict]) -> None:
        temp_path = f"{self.file_path}.tmp"
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        # Atomic replace
        os.replace(temp_path, self.file_path)

    def get_by_id(self, order_id: str) -> Optional[Order]:
        raw = self._read_raw()
        item = raw.get(order_id)
        if item:
            return Order.from_dict(item)
        return None

    def list_all(self) -> List[Order]:
        raw = self._read_raw()
        return [Order.from_dict(d) for d in raw.values()]

    def save(self, order: Order) -> None:
        raw = self._read_raw()
        raw[order.order_id] = order.to_dict()
        self._write_raw(raw)

    def delete(self, order_id: str) -> bool:
        raw = self._read_raw()
        if order_id in raw:
            del raw[order_id]
            self._write_raw(raw)
            return True
        return False
