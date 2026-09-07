"""Domain models with strict encapsulation and serialization support."""

from enum import Enum
from datetime import datetime
import re
from typing import List, Tuple, Dict, Any
from .exceptions import ValidationError, InvalidOrderStateError


class OrderStatus(str, Enum):
    DRAFT = "DRAFT"
    CONFIRMED = "CONFIRMED"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


class Customer:
    """Represents a validated customer identity."""

    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

    def __init__(self, customer_id: int, name: str, email: str):
        if customer_id <= 0:
            raise ValidationError(f"Customer ID must be > 0, got {customer_id}.")
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
            raise ValidationError("Customer name cannot be empty.")
        self._name = cleaned

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, val: str) -> None:
        cleaned = val.strip() if isinstance(val, str) else ""
        if not self.EMAIL_REGEX.match(cleaned):
            raise ValidationError(f"Invalid email address: '{val}'.")
        self._email = cleaned

    def to_dict(self) -> Dict[str, Any]:
        return {
            "customer_id": self._customer_id,
            "name": self._name,
            "email": self._email,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        return cls(
            customer_id=data["customer_id"],
            name=data["name"],
            email=data["email"],
        )

    def __repr__(self) -> str:
        return f"Customer({self._customer_id}, '{self._name}')"


class Product:
    """Represents a product item."""

    def __init__(self, sku: str, name: str, unit_price: float):
        cleaned_sku = sku.strip().upper() if isinstance(sku, str) else ""
        if not cleaned_sku:
            raise ValidationError("Product SKU cannot be empty.")
        self._sku = cleaned_sku

        cleaned_name = name.strip() if isinstance(name, str) else ""
        if not cleaned_name:
            raise ValidationError("Product name cannot be empty.")
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
            raise ValidationError(f"Price must be numeric, got {val}.")
        if amt <= 0.0:
            raise ValidationError(f"Product price must be strictly positive (> 0), got {amt}.")
        self._unit_price = round(amt, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sku": self._sku,
            "name": self._name,
            "unit_price": self._unit_price,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            sku=data["sku"],
            name=data["name"],
            unit_price=data["unit_price"],
        )

    def __repr__(self) -> str:
        return f"Product('{self._sku}', '${self._unit_price:.2f}')"


class OrderItem:
    """Encapsulates line item snapshot at purchase."""

    def __init__(self, product: Product, quantity: int, unit_price_at_purchase: float | None = None):
        if not isinstance(product, Product):
            raise ValidationError("OrderItem product must be a Product instance.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValidationError(f"Quantity must be a positive integer, got {quantity}.")

        self._product = product
        self._quantity = quantity
        self._unit_price = round(unit_price_at_purchase if unit_price_at_purchase is not None else product.unit_price, 2)

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @property
    def subtotal(self) -> float:
        return round(self._unit_price * self._quantity, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "product": self._product.to_dict(),
            "quantity": self._quantity,
            "unit_price": self._unit_price,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OrderItem":
        prod = Product.from_dict(data["product"])
        return cls(
            product=prod,
            quantity=data["quantity"],
            unit_price_at_purchase=data.get("unit_price", prod.unit_price),
        )

    def __repr__(self) -> str:
        return f"OrderItem({self._product.sku}, qty={self._quantity})"


class Order:
    """Aggregate Root: Order encapsulates customer, line items, and lifecycle."""

    def __init__(
        self,
        order_id: str,
        customer: Customer,
        status: OrderStatus = OrderStatus.DRAFT,
        created_at: str | None = None,
        discount: float = 0.0,
    ):
        clean_id = str(order_id).strip()
        if not clean_id:
            raise ValidationError("Order ID cannot be empty.")
        if not isinstance(customer, Customer):
            raise ValidationError("Order requires a valid Customer instance.")

        self._order_id = clean_id
        self._customer = customer
        self._items: List[OrderItem] = []
        self._status = status if isinstance(status, OrderStatus) else OrderStatus(status)
        self._created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._discount = round(discount, 2)

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
    def created_at(self) -> str:
        return self._created_at

    @property
    def items(self) -> Tuple[OrderItem, ...]:
        return tuple(self._items)

    @property
    def discount(self) -> float:
        return self._discount

    @property
    def subtotal(self) -> float:
        return round(sum(i.subtotal for i in self._items), 2)

    @property
    def total(self) -> float:
        return round(max(0.0, self.subtotal - self._discount), 2)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        if self._status != OrderStatus.DRAFT:
            raise InvalidOrderStateError(f"Cannot add items to an order in {self._status.value} state.")

        for idx, existing in enumerate(self._items):
            if existing.product.sku == product.sku:
                new_qty = existing.quantity + quantity
                self._items[idx] = OrderItem(product, new_qty)
                return
        self._items.append(OrderItem(product, quantity))

    def apply_discount(self, amount: float) -> None:
        if self._status != OrderStatus.DRAFT:
            raise InvalidOrderStateError("Discounts can only be applied while order is in DRAFT.")
        if amount < 0:
            raise ValidationError("Discount cannot be negative.")
        if amount > self.subtotal:
            raise ValidationError(f"Discount (${amount:.2f}) cannot exceed subtotal (${self.subtotal:.2f}).")
        self._discount = round(amount, 2)

    def confirm(self) -> None:
        if self._status != OrderStatus.DRAFT:
            raise InvalidOrderStateError(f"Cannot confirm order in state {self._status.value}.")
        if not self._items:
            raise InvalidOrderStateError("Cannot confirm order with no items.")
        self._status = OrderStatus.CONFIRMED

    def mark_paid(self) -> None:
        if self._status != OrderStatus.CONFIRMED:
            raise InvalidOrderStateError(f"Order must be CONFIRMED before payment. Current: {self._status.value}")
        self._status = OrderStatus.PAID

    def ship(self) -> None:
        if self._status != OrderStatus.PAID:
            raise InvalidOrderStateError(f"Order must be PAID before shipping. Current: {self._status.value}")
        self._status = OrderStatus.SHIPPED

    def cancel(self) -> None:
        if self._status == OrderStatus.SHIPPED:
            raise InvalidOrderStateError("Cannot cancel an order that has already been shipped.")
        if self._status == OrderStatus.CANCELLED:
            raise InvalidOrderStateError("Order is already cancelled.")
        self._status = OrderStatus.CANCELLED

    def to_dict(self) -> Dict[str, Any]:
        return {
            "order_id": self._order_id,
            "customer": self._customer.to_dict(),
            "status": self._status.value,
            "created_at": self._created_at,
            "discount": self._discount,
            "items": [i.to_dict() for i in self._items],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Order":
        cust = Customer.from_dict(data["customer"])
        order = cls(
            order_id=data["order_id"],
            customer=cust,
            status=OrderStatus(data["status"]),
            created_at=data["created_at"],
            discount=data.get("discount", 0.0),
        )
        for item_data in data.get("items", []):
            order._items.append(OrderItem.from_dict(item_data))
        return order


class Invoice:
    """Represents a finalized billing statement for an order."""

    def __init__(self, invoice_id: str, order: Order, issued_at: str | None = None, is_paid: bool = False):
        if not invoice_id:
            raise ValidationError("Invoice ID cannot be empty.")
        if not isinstance(order, Order):
            raise ValidationError("Invoice requires a valid Order instance.")
        if order.status == OrderStatus.DRAFT:
            raise InvalidOrderStateError("Cannot create invoice for a DRAFT order. Order must be confirmed.")

        self.invoice_id = str(invoice_id).strip()
        self.order = order
        self.issued_at = issued_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_paid = is_paid

    def mark_paid(self) -> None:
        if self.is_paid:
            raise InvalidOrderStateError("Invoice is already paid.")
        self.order.mark_paid()
        self.is_paid = True

    def generate_summary(self) -> str:
        lines = [
            "=" * 50,
            f"INVOICE #{self.invoice_id}",
            f"Date:     {self.issued_at}",
            f"Customer: {self.order.customer.name} ({self.order.customer.email})",
            f"Status:   {'PAID' if self.is_paid else 'UNPAID'}",
            "-" * 50,
            "Items:",
        ]
        for item in self.order.items:
            lines.append(f"  - [{item.product.sku}] {item.product.name:<20} {item.quantity}x @ ${item.unit_price:.2f} = ${item.subtotal:.2f}")
        lines.append("-" * 50)
        lines.append(f"Subtotal: ${self.order.subtotal:.2f}")
        if self.order.discount > 0:
            lines.append(f"Discount: -${self.order.discount:.2f}")
        lines.append(f"Total:    ${self.order.total:.2f}")
        lines.append("=" * 50)
        return "\n".join(lines)
