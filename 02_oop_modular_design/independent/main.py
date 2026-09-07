"""
main.py - Driver demonstration of the Layered Architecture with Swappable Repositories.
"""

import sys
import os

# Ensure local packages can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from domain.models import Customer, Product
from repositories.memory import InMemoryOrderRepository
from repositories.file import JsonFileOrderRepository
from services.order_service import OrderService


def run_workflow(repo_name: str, service: OrderService) -> None:
    print(f"\n{'=' * 60}")
    print(f"  Running Order Lifecycle with: {repo_name}")
    print(f"{'=' * 60}")

    # 1. Setup entities
    customer = Customer(101, "Alice Cooper", "alice.cooper@example.com")
    laptop = Product("SKU-PRO-15", "Dell XPS 15", 1750.00)
    keyboard = Product("SKU-KEY-01", "Keychron K2", 95.00)

    # 2. Create Order via Service
    order_id = f"ORD-{repo_name.lower()[:3]}-001"
    print(f"-> Creating order '{order_id}' for {customer.name}...")
    service.create_order(order_id, customer)

    # 3. Add items and discount
    service.add_product(order_id, laptop, 1)
    service.add_product(order_id, keyboard, 2)
    service.apply_discount(order_id, 40.00)

    order = service.get_order(order_id)
    print(f"   Subtotal: ${order.subtotal:.2f} | Discount: -${order.discount:.2f} | Total: ${order.total:.2f}")

    # 4. Confirm Order
    print(f"-> Confirming order '{order_id}'...")
    service.confirm_order(order_id)

    # 5. Generate & Pay Invoice
    invoice = service.generate_invoice(order_id, f"INV-{order_id}")
    print(f"-> Paying invoice '{invoice.invoice_id}'...")
    service.pay_invoice(invoice)

    # 6. Ship Order
    print(f"-> Shipping order '{order_id}'...")
    service.ship_order(order_id)

    final_order = service.get_order(order_id)
    print(f"-> Final Order Status in Repository: {final_order.status.value}")
    print(f"[Done] Workflow completed successfully with {repo_name}!\n")


def main() -> None:
    # 1. Run using InMemoryOrderRepository
    in_memory_repo = InMemoryOrderRepository()
    memory_service = OrderService(in_memory_repo)
    run_workflow("InMemoryOrderRepository", memory_service)

    # 2. Run using JsonFileOrderRepository
    test_json_file = "demo_orders.json"
    file_repo = JsonFileOrderRepository(file_path=test_json_file)
    file_service = OrderService(file_repo)
    run_workflow("JsonFileOrderRepository", file_service)

    # Clean up demo json file
    if os.path.exists(test_json_file):
        os.remove(test_json_file)


if __name__ == "__main__":
    main()
