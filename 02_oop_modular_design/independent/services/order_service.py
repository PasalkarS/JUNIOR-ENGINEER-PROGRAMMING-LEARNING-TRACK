"""
order_service.py - Layered Service orchestrating order operations.

Demonstrates Dependency Inversion: business logic depends on the abstract
OrderRepository interface, completely isolated from concrete storage details.
"""

from typing import List, Optional
from domain.models import Order, Customer, Product, Invoice
from domain.exceptions import EntityNotFoundError
from repositories.base import OrderRepository


class OrderService:
    """
    Application service that coordinates domain models with persistence.
    Injects an abstract OrderRepository interface.
    """

    def __init__(self, repository: OrderRepository):
        self._repo = repository

    def create_order(self, order_id: str, customer: Customer) -> Order:
        existing = self._repo.get_by_id(order_id)
        if existing:
            raise ValueError(f"Order with ID '{order_id}' already exists.")

        order = Order(order_id, customer)
        self._repo.save(order)
        return order

    def get_order(self, order_id: str) -> Order:
        order = self._repo.get_by_id(order_id)
        if not order:
            raise EntityNotFoundError(f"Order #{order_id} not found.")
        return order

    def add_product(self, order_id: str, product: Product, quantity: int = 1) -> Order:
        order = self.get_order(order_id)
        order.add_item(product, quantity)
        self._repo.save(order)
        return order

    def apply_discount(self, order_id: str, amount: float) -> Order:
        order = self.get_order(order_id)
        order.apply_discount(amount)
        self._repo.save(order)
        return order

    def confirm_order(self, order_id: str) -> Order:
        order = self.get_order(order_id)
        order.confirm()
        self._repo.save(order)
        return order

    def generate_invoice(self, order_id: str, invoice_id: str) -> Invoice:
        order = self.get_order(order_id)
        invoice = Invoice(invoice_id, order)
        return invoice

    def pay_invoice(self, invoice: Invoice) -> None:
        invoice.mark_paid()
        # Save updated order status back to repository
        self._repo.save(invoice.order)

    def ship_order(self, order_id: str) -> Order:
        order = self.get_order(order_id)
        order.ship()
        self._repo.save(order)
        return order

    def cancel_order(self, order_id: str) -> Order:
        order = self.get_order(order_id)
        order.cancel()
        self._repo.save(order)
        return order

    def list_orders(self) -> List[Order]:
        return self._repo.list_all()
