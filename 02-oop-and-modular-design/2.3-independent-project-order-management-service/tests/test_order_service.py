"""
Automated unit tests for Order Management Service.
"""
import pytest
from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path in sys.path:
    sys.path.remove(src_path)
sys.path.insert(0, src_path)

for mod in ["models", "repositories", "services"]:
    sys.modules.pop(mod, None)

from models import Customer, Product, OrderStatus
from repositories import InMemoryProductRepository, InMemoryOrderRepository
from services import NotificationService, OrderService

@pytest.fixture
def test_setup():
    prod_repo = InMemoryProductRepository()
    prod_repo.save(Product("SKU-1", "Test Product 1", 50.0, 10))
    prod_repo.save(Product("SKU-2", "Test Product 2", 100.0, 2))

    order_repo = InMemoryOrderRepository()
    notifier = NotificationService()
    service = OrderService(prod_repo, order_repo, notifier)
    customer = Customer("C1", "John Tester", "tester@example.com")
    return service, prod_repo, order_repo, customer

def test_create_order_success(test_setup):
    service, prod_repo, order_repo, customer = test_setup
    order = service.create_order(customer, [("SKU-1", 2), ("SKU-2", 1)])

    assert order.total_amount == 200.0
    assert order.status == OrderStatus.PENDING
    assert prod_repo.get_by_sku("SKU-1").stock == 8
    assert prod_repo.get_by_sku("SKU-2").stock == 1
    assert len(order_repo.list_all()) == 1

def test_create_order_insufficient_stock(test_setup):
    service, prod_repo, order_repo, customer = test_setup
    with pytest.raises(ValueError, match="Insufficient stock"):
        service.create_order(customer, [("SKU-2", 5)])

def test_order_lifecycle_transitions(test_setup):
    service, prod_repo, order_repo, customer = test_setup
    order = service.create_order(customer, [("SKU-1", 1)])

    # Cannot ship before pay
    with pytest.raises(ValueError):
        service.ship_order(order.order_id)

    # Pay
    service.pay_order(order.order_id)
    assert order.status == OrderStatus.PAID

    # Ship
    service.ship_order(order.order_id)
    assert order.status == OrderStatus.SHIPPED

    # Cannot cancel shipped order
    with pytest.raises(ValueError):
        service.cancel_order(order.order_id)

def test_cancel_order_restores_stock(test_setup):
    service, prod_repo, order_repo, customer = test_setup
    order = service.create_order(customer, [("SKU-1", 3)])
    assert prod_repo.get_by_sku("SKU-1").stock == 7

    service.cancel_order(order.order_id)
    assert order.status == OrderStatus.CANCELLED
    assert prod_repo.get_by_sku("SKU-1").stock == 10
