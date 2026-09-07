"""
test_layered_architecture.py - Pytest suite for domain models, repositories, and services.
"""

import os
import sys
import pytest

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domain.models import Customer, Product, Order, OrderStatus, Invoice
from domain.exceptions import ValidationError, InvalidOrderStateError, EntityNotFoundError
from repositories.memory import InMemoryOrderRepository
from repositories.file import JsonFileOrderRepository
from services.order_service import OrderService


# ---------------------------------------------------------------------------
# Domain Model Tests
# ---------------------------------------------------------------------------
def test_customer_validation():
    with pytest.raises(ValidationError, match="Invalid email address"):
        Customer(1, "Test User", "invalid-email-address")

    with pytest.raises(ValidationError, match="Customer name cannot be empty"):
        Customer(1, "   ", "user@example.com")

    with pytest.raises(ValidationError, match="Customer ID must be > 0"):
        Customer(-5, "Test User", "user@example.com")


def test_product_validation():
    with pytest.raises(ValidationError, match="Product price must be strictly positive"):
        Product("SKU-1", "Widget", -10.00)

    with pytest.raises(ValidationError, match="Product price must be strictly positive"):
        Product("SKU-1", "Widget", 0.00)

    with pytest.raises(ValidationError, match="Product SKU cannot be empty"):
        Product("", "Widget", 10.00)


def test_order_state_invariants():
    cust = Customer(1, "Jane Doe", "jane@example.com")
    prod = Product("SKU-A", "Item A", 20.00)
    order = Order("ORD-001", cust)

    # Cannot confirm empty order
    with pytest.raises(InvalidOrderStateError, match="Cannot confirm order with no items"):
        order.confirm()

    order.add_item(prod, 2)
    assert order.total == 40.00

    order.confirm()
    assert order.status == OrderStatus.CONFIRMED

    # Cannot add item to confirmed order
    with pytest.raises(InvalidOrderStateError, match="Cannot add items to an order in CONFIRMED"):
        order.add_item(prod, 1)

    # Cannot ship before payment
    with pytest.raises(InvalidOrderStateError, match="Order must be PAID before shipping"):
        order.ship()

    order.mark_paid()
    assert order.status == OrderStatus.PAID

    order.ship()
    assert order.status == OrderStatus.SHIPPED

    # Cannot cancel shipped order
    with pytest.raises(InvalidOrderStateError, match="Cannot cancel an order that has already been shipped"):
        order.cancel()


# ---------------------------------------------------------------------------
# Repository Tests (Parameterized across InMemory and File-based)
# ---------------------------------------------------------------------------
@pytest.fixture(params=["memory", "file"])
def repository(request, tmp_path):
    if request.param == "memory":
        return InMemoryOrderRepository()
    else:
        file_path = str(tmp_path / "test_repo.json")
        return JsonFileOrderRepository(file_path=file_path)


def test_repository_crud(repository):
    cust = Customer(10, "Repo User", "repo@example.com")
    prod = Product("SKU-X", "Gadget", 50.00)
    order = Order("ORD-CRUD-1", cust)
    order.add_item(prod, 1)

    # Save
    repository.save(order)

    # Retrieve
    retrieved = repository.get_by_id("ORD-CRUD-1")
    assert retrieved is not None
    assert retrieved.order_id == "ORD-CRUD-1"
    assert retrieved.customer.name == "Repo User"
    assert len(retrieved.items) == 1
    assert retrieved.total == 50.00

    # List
    all_orders = repository.list_all()
    assert len(all_orders) == 1

    # Delete
    assert repository.delete("ORD-CRUD-1") is True
    assert repository.get_by_id("ORD-CRUD-1") is None
    assert repository.delete("NON-EXISTENT") is False


# ---------------------------------------------------------------------------
# OrderService Tests
# ---------------------------------------------------------------------------
def test_order_service_workflow(tmp_path):
    repo = JsonFileOrderRepository(file_path=str(tmp_path / "service_orders.json"))
    service = OrderService(repo)

    cust = Customer(50, "Service Cust", "svc@example.com")
    prod = Product("SKU-SRV", "Server Rack", 1200.00)

    # Create & retrieve
    order = service.create_order("ORD-SVC-10", cust)
    assert order.status == OrderStatus.DRAFT

    service.add_product("ORD-SVC-10", prod, 2)
    service.apply_discount("ORD-SVC-10", 200.00)

    reloaded = service.get_order("ORD-SVC-10")
    assert reloaded.subtotal == 2400.00
    assert reloaded.total == 2200.00

    # Confirm & Invoice
    service.confirm_order("ORD-SVC-10")
    invoice = service.generate_invoice("ORD-SVC-10", "INV-SVC-10")
    assert invoice.is_paid is False

    service.pay_invoice(invoice)
    assert invoice.is_paid is True
    assert service.get_order("ORD-SVC-10").status == OrderStatus.PAID

    # Ship
    service.ship_order("ORD-SVC-10")
    assert service.get_order("ORD-SVC-10").status == OrderStatus.SHIPPED


def test_order_service_entity_not_found():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)

    with pytest.raises(EntityNotFoundError):
        service.get_order("UNKNOWN_ID")
