"""
order_management_basic.py - Learned Level: Basic OOP Concepts.

Demonstrates core object-oriented programming concepts:
  - Class definition and __init__ constructors
  - Object relationships and collaboration
  - String representations (__str__ and __repr__)
  - Basic domain classes: Customer, Product, OrderItem, Order, Invoice
"""

from datetime import datetime
from typing import List


class Customer:
    """Represents a store customer."""

    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"Customer(id={self.customer_id}, name='{self.name}', email='{self.email}')"

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"


class Product:
    """Represents an item available in catalog."""

    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"Product(id='{self.product_id}', name='{self.name}', price={self.price})"

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


class OrderItem:
    """Represents a line item in an order."""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def line_total(self) -> float:
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        return f"OrderItem(product={self.product.name}, qty={self.quantity})"


class Order:
    """Represents an order placed by a customer containing order items."""

    def __init__(self, order_id: str, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.items: List[OrderItem] = []
        self.created_at = datetime.now()

    def add_product(self, product: Product, quantity: int = 1) -> None:
        self.items.append(OrderItem(product, quantity))

    def total(self) -> float:
        return sum(item.line_total() for item in self.items)

    def __repr__(self) -> str:
        return f"Order(id='{self.order_id}', customer='{self.customer.name}', items={len(self.items)})"


class Invoice:
    """Represents a billing invoice generated from an order."""

    def __init__(self, invoice_id: str, order: Order):
        self.invoice_id = invoice_id
        self.order = order
        self.issued_at = datetime.now()
        self.is_paid = False

    def mark_as_paid(self) -> None:
        self.is_paid = True

    def generate_summary(self) -> str:
        lines = [
            "=" * 45,
            f"INVOICE #{self.invoice_id}",
            f"Date:     {self.issued_at.strftime('%Y-%m-%d %H:%M')}",
            f"Customer: {self.order.customer}",
            f"Status:   {'PAID' if self.is_paid else 'UNPAID'}",
            "-" * 45,
            "Items:",
        ]
        for item in self.order.items:
            lines.append(f"  - {item.product.name:<20} x{item.quantity:<3} = ${item.line_total():.2f}")
        lines.append("-" * 45)
        lines.append(f"Total Due: ${self.order.total():.2f}")
        lines.append("=" * 45)
        return "\n".join(lines)


if __name__ == "__main__":
    # Quick standalone demonstration
    c1 = Customer(101, "Alice Chen", "alice@example.com")
    p1 = Product("SKU-100", "Wireless Mouse", 29.99)
    p2 = Product("SKU-200", "Mechanical Keyboard", 89.50)

    order = Order("ORD-001", c1)
    order.add_product(p1, 2)
    order.add_product(p2, 1)

    invoice = Invoice("INV-9001", order)
    print(invoice.generate_summary())
