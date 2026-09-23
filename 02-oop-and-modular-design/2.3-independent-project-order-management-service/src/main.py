"""
CLI Demonstration for Order Management Service.
"""
from models import Customer, Product
from repositories import InMemoryProductRepository, InMemoryOrderRepository
from services import NotificationService, OrderService

def bootstrap():
    prod_repo = InMemoryProductRepository()
    prod_repo.save(Product("LAP-01", "MacBook Pro M3", 1999.00, 5))
    prod_repo.save(Product("MOU-01", "Logitech MX Master", 99.00, 20))
    prod_repo.save(Product("KEY-01", "Keychron K2", 89.00, 15))

    order_repo = InMemoryOrderRepository()
    notifier = NotificationService()
    service = OrderService(prod_repo, order_repo, notifier)

    print("=== Order Management Service Initialized ===")
    print("Available Catalog:")
    for p in prod_repo.list_all():
        print(f" - [{p.sku}] {p.name}: ${p.price:.2f} (Stock: {p.stock})")

    cust = Customer("C-101", "Sarah Connor", "sarah@resistance.org")
    print(f"\nCreating order for {cust.name}...")
    order = service.create_order(cust, [("LAP-01", 1), ("MOU-01", 2)])
    print(f"Order Created: #{order.order_id} | Total: ${order.total_amount:.2f} | Status: {order.status}")

    print("\nProcessing Payment...")
    service.pay_order(order.order_id)
    print(f"Order Status after payment: {order.status}")

    print("\nShipping Order...")
    service.ship_order(order.order_id)
    print(f"Order Status after shipping: {order.status}")

if __name__ == "__main__":
    bootstrap()
