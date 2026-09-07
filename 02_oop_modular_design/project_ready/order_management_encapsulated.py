"""
order_management_encapsulated.py - Project Ready Level: Encapsulation & Invariants.

Enforces strict encapsulation, defensive data copying, domain validation,
and explicit state machine transitions preventing invalid states.
"""

from enum import Enum
from datetime import datetime
import re
from typing import List, Tuple


class OrderStatus(Enum):
    DRAFT = "DRAFT"
    CONFIRMED = "CONFIRMED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


class DomainValidationError(ValueError):
    """Raised when an entity attribute fails domain validation."""
    pass


class InvalidOrderStateError(RuntimeError):
    """Raised when an operation violates order state machine invariants."""
    pass


class Customer:
    """Represents a customer with validated identity and encapsulated state."""

    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __init__(self, customer_id: int, name: str, email: str):
        if customer_id <= 0:
            raise DomainValidationError(f"Customer ID must be a positive integer, got {customer_id}.")
        self._customer_id = customer_id
        self._name = ""
        self._email = ""
        self.name = name
        self.email = email

    @property
    def customer_id(self) -> int:
        return self._customer_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str) -> None:
        cleaned = val.strip() if isinstance(val, str) else ""
        if not cleaned:
            raise DomainValidationError("Customer name cannot be empty.")
        self._name = cleaned

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, val: str) -> None:
        cleaned = val.strip() if isinstance(val, str) else ""
        if not self.EMAIL_REGEX.match(cleaned):
            raise DomainValidationError(f"Invalid email address format: '{val}'.")
        self._email = cleaned

    def __repr__(self) -> str:
        return f"Customer(id={self._customer_id}, name='{self._name}', email='{self._email}')"


class Product:
    """Represents a catalog product with positive price constraints."""

    def __init__(self, sku: str, name: str, unit_price: float):
        cleaned_sku = sku.strip().upper() if isinstance(sku, str) else ""
        if not cleaned_sku:
            raise DomainValidationError("Product SKU cannot be empty.")
        self._sku = cleaned_sku

        cleaned_name = name.strip() if isinstance(name, str) else ""
        if not cleaned_name:
            raise DomainValidationError("Product name cannot be empty.")
        self._name = cleaned_name

        self._unit_price = 0.0
        self.unit_price = unit_price

    @property
    def sku(self) -> str:
        return self._sku

    @property
    def name(self) -> str:
        return self._name

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, val: float) -> None:
        try:
            amt = float(val)
        except (ValueError, TypeError):
            raise DomainValidationError(f"Price must be numeric, got {val}.")
        if amt <= 0.0:
            raise DomainValidationError(f"Product price must be strictly positive (> 0), got {amt}.")
        self._unit_price = round(amt, 2)

    def __repr__(self) -> str:
        return f"Product(sku='{self._sku}', name='{self._name}', price={self._unit_price})"


class OrderItem:
    """Encapsulates a product reference and quantity with immutable attributes."""

    def __init__(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise DomainValidationError("OrderItem requires a valid Product instance.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise DomainValidationError(f"Quantity must be a positive integer >= 1, got {quantity}.")

        self._product = product
        self._quantity = quantity
        self._unit_price_at_purchase = product.unit_price

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def unit_price(self) -> float:
        return self._unit_price_at_purchase

    @property
    def subtotal(self) -> float:
        return round(self._unit_price_at_purchase * self._quantity, 2)

    def __repr__(self) -> str:
        return f"OrderItem(sku='{self._product.sku}', qty={self._quantity}, subtotal={self.subtotal})"


class Order:
    """
    Manages order lifecycle, protecting invariants via state machine.
    Callers cannot mutate internal items directly.
    """

    def __init__(self, order_id: str, customer: Customer):
        if not order_id or not str(order_id).strip():
            raise DomainValidationError("Order ID cannot be empty.")
        if not isinstance(customer, Customer):
            raise DomainValidationError("Order must be associated with a valid Customer.")

        self._order_id = str(order_id).strip()
        self._customer = customer
        self._items: List[OrderItem] = []
        self._status = OrderStatus.DRAFT
        self._created_at = datetime.now()
        self._discount = 0.0

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def status(self) -> OrderStatus:
        return self._status

    @property
    def items(self) -> Tuple[OrderItem, ...]:
        """Defensive copy: returns immutable tuple preventing external list mutation."""
        return tuple(self._items)

    @property
    def discount(self) -> float:
        return self._discount

    def apply_discount(self, amount: float) -> None:
        self._assert_state(OrderStatus.DRAFT, "Cannot modify discount on non-draft orders.")
        if amount < 0:
            raise DomainValidationError("Discount cannot be negative.")
        if amount > self.subtotal:
            raise DomainValidationError(f"Discount (${amount:.2f}) cannot exceed subtotal (${self.subtotal:.2f}).")
        self._discount = round(amount, 2)

    @property
    def subtotal(self) -> float:
        return round(sum(i.subtotal for i in self._items), 2)

    @property
    def total(self) -> float:
        return round(max(0.0, self.subtotal - self._discount), 2)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        self._assert_state(OrderStatus.DRAFT, "Cannot add items to a finalized order.")
        # If product already in order, merge quantities
        for idx, existing in enumerate(self._items):
            if existing.product.sku == product.sku:
                new_qty = existing.quantity + quantity
                self._items[idx] = OrderItem(product, new_qty)
                return
        self._items.append(OrderItem(product, quantity))

    def remove_item(self, sku: str) -> None:
        self._assert_state(OrderStatus.DRAFT, "Cannot remove items from a finalized order.")
        initial_len = len(self._items)
        self._items = [i for i in self._items if i.product.sku != sku]
        if len(self._items) == initial_len:
            raise DomainValidationError(f"Cannot remove SKU '{sku}': not found in order.")

    def confirm(self) -> None:
        self._assert_state(OrderStatus.DRAFT, "Only DRAFT orders can be confirmed.")
        if not self._items:
            raise InvalidOrderStateError("Cannot confirm an empty order with no items.")
        self._status = OrderStatus.CONFIRMED

    def mark_paid(self) -> None:
        self._assert_state(OrderStatus.CONFIRMED, "Only CONFIRMED orders can be marked PAID.")
        self._status = OrderStatus.PAID

    def ship(self) -> None:
        self._assert_state(OrderStatus.PAID, "Only PAID orders can be shipped.")
        self._status = OrderStatus.SHIPPED

    def cancel(self) -> None:
        if self._status == OrderStatus.SHIPPED:
            raise InvalidOrderStateError("Cannot cancel an order that has already been shipped.")
        if self._status == OrderStatus.CANCELLED:
            raise InvalidOrderStateError("Order is already cancelled.")
        self._status = OrderStatus.CANCELLED

    def _assert_state(self, expected: OrderStatus, msg: str) -> None:
        if self._status != expected:
            raise InvalidOrderStateError(f"{msg} (Current state: {self._status.value})")

    def __repr__(self) -> str:
        return f"Order(id='{self._order_id}', status={self._status.value}, total=${self.total:.2f})"


class Invoice:
    """Represents a finalized, immutable billing record tied to an order."""

    def __init__(self, invoice_id: str, order: Order):
        if not invoice_id or not str(invoice_id).strip():
            raise DomainValidationError("Invoice ID cannot be empty.")
        if not isinstance(order, Order):
            raise DomainValidationError("Invoice requires a valid Order instance.")
        if order.status == OrderStatus.DRAFT:
            raise InvalidOrderStateError("Cannot invoice an order in DRAFT state. Order must be confirmed first.")
        if order.status == OrderStatus.CANCELLED:
            raise InvalidOrderStateError("Cannot invoice a CANCELLED order.")

        self._invoice_id = str(invoice_id).strip()
        self._order = order
        self._issued_at = datetime.now()
        self._paid_at: datetime | None = None

    @property
    def invoice_id(self) -> str:
        return self._invoice_id

    @property
    def is_paid(self) -> bool:
        return self._paid_at is not None

    def mark_paid(self) -> None:
        if self.is_paid:
            raise InvalidOrderStateError("Invoice is already paid.")
        self._order.mark_paid()
        self._paid_at = datetime.now()

    def generate_summary(self) -> str:
        lines = [
            "=" * 50,
            f"INVOICE #{self._invoice_id}",
            f"Date:     {self._issued_at.strftime('%Y-%m-%d %H:%M')}",
            f"Customer: {self._order.customer.name} ({self._order.customer.email})",
            f"Status:   {'PAID on ' + self._paid_at.strftime('%Y-%m-%d %H:%M') if self.is_paid else 'UNPAID'}",
            "-" * 50,
            "Line Items:",
        ]
        for item in self._order.items:
            lines.append(f"  - [{item.product.sku}] {item.product.name:<18} {item.quantity:>2}x @ ${item.unit_price:.2f} = ${item.subtotal:.2f}")
        lines.append("-" * 50)
        lines.append(f"Subtotal: ${self._order.subtotal:.2f}")
        if self._order.discount > 0:
            lines.append(f"Discount: -${self._order.discount:.2f}")
        lines.append(f"Total:    ${self._order.total:.2f}")
        lines.append("=" * 50)
        return "\n".join(lines)


if __name__ == "__main__":
    # Test defensive invariants
    customer = Customer(1, "Bob Martin", "bob@clean-code.com")
    laptop = Product("SKU-LAPTOP", "ThinkPad X1", 1499.00)
    mouse = Product("SKU-MOUSE", "Logitech MX", 99.00)

    order = Order("ORD-2026-001", customer)
    order.add_item(laptop, 1)
    order.add_item(mouse, 2)
    order.apply_discount(50.00)
    order.confirm()

    invoice = Invoice("INV-1001", order)
    invoice.mark_paid()
    print(invoice.generate_summary())
