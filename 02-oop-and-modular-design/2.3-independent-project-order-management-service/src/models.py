"""
Domain models for the Order Management System.
"""
from dataclasses import dataclass
from enum import Enum
from typing import List

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"

@dataclass
class Customer:
    customer_id: str
    name: str
    email: str

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Customer name cannot be empty.")
        if "@" not in self.email:
            raise ValueError("Customer email must contain '@'.")

@dataclass
class Product:
    sku: str
    name: str
    price: float
    stock: int

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Product price must be greater than zero.")
        if self.stock < 0:
            raise ValueError("Product stock cannot be negative.")

class OrderItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.product = product
        self.quantity = quantity

    @property
    def line_total(self) -> float:
        return round(self.product.price * self.quantity, 2)

    def to_dict(self) -> dict:
        return {
            "sku": self.product.sku,
            "name": self.product.name,
            "unit_price": self.product.price,
            "quantity": self.quantity,
            "line_total": self.line_total,
        }

class Order:
    def __init__(self, order_id: str, customer: Customer, items: List[OrderItem]):
        if not items:
            raise ValueError("An order must contain at least one item.")
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = OrderStatus.PENDING

    @property
    def total_amount(self) -> float:
        return round(sum(item.line_total for item in self.items), 2)

    def mark_as_paid(self) -> None:
        if self.status != OrderStatus.PENDING:
            raise ValueError(f"Cannot pay an order with status '{self.status}'.")
        self.status = OrderStatus.PAID

    def mark_as_shipped(self) -> None:
        if self.status != OrderStatus.PAID:
            raise ValueError(f"Cannot ship an unpaid order with status '{self.status}'.")
        self.status = OrderStatus.SHIPPED

    def cancel(self) -> None:
        if self.status == OrderStatus.SHIPPED:
            raise ValueError("Cannot cancel an order that has already shipped.")
        self.status = OrderStatus.CANCELLED
