"""
Business logic and application services.
"""
from typing import List, Tuple
from models import Customer, Order, OrderItem, OrderStatus
from repositories import IProductRepository, IOrderRepository

class NotificationService:
    def __init__(self):
        self.sent_notifications: List[str] = []

    def notify_order_placed(self, order: Order):
        msg = f"[NOTIFICATION] Order #{order.order_id} placed for {order.customer.name}. Total: ${order.total_amount:.2f}"
        self.sent_notifications.append(msg)
        print(msg)

    def notify_order_status(self, order: Order):
        msg = f"[NOTIFICATION] Order #{order.order_id} updated to status '{order.status}'."
        self.sent_notifications.append(msg)
        print(msg)

class OrderService:
    def __init__(
        self,
        product_repo: IProductRepository,
        order_repo: IOrderRepository,
        notifier: NotificationService,
    ):
        self.product_repo = product_repo
        self.order_repo = order_repo
        self.notifier = notifier
        self._order_counter = 1000

    def create_order(self, customer: Customer, items_spec: List[Tuple[str, int]]) -> Order:
        """
        items_spec is a list of (sku, quantity) tuples.
        Validates stock, reserves stock, creates Order, and persists it.
        """
        order_items = []

        # 1. Validation & Stock Check
        for sku, qty in items_spec:
            product = self.product_repo.get_by_sku(sku)
            if not product:
                raise ValueError(f"Product with SKU '{sku}' not found.")
            if product.stock < qty:
                raise ValueError(f"Insufficient stock for '{product.name}': requested {qty}, available {product.stock}.")
            order_items.append((product, qty))

        # 2. Deduct Stock
        for product, qty in order_items:
            product.stock -= qty
            self.product_repo.save(product)

        # 3. Create & Save Order
        self._order_counter += 1
        order_id = f"ORD-{self._order_counter}"
        built_items = [OrderItem(p, q) for p, q in order_items]
        new_order = Order(order_id, customer, built_items)
        self.order_repo.save(new_order)

        # 4. Notify
        self.notifier.notify_order_placed(new_order)
        return new_order

    def pay_order(self, order_id: str) -> Order:
        order = self.order_repo.get_by_id(order_id)
        if not order:
            raise ValueError(f"Order '{order_id}' not found.")
        order.mark_as_paid()
        self.order_repo.save(order)
        self.notifier.notify_order_status(order)
        return order

    def ship_order(self, order_id: str) -> Order:
        order = self.order_repo.get_by_id(order_id)
        if not order:
            raise ValueError(f"Order '{order_id}' not found.")
        order.mark_as_shipped()
        self.order_repo.save(order)
        self.notifier.notify_order_status(order)
        return order

    def cancel_order(self, order_id: str) -> Order:
        order = self.order_repo.get_by_id(order_id)
        if not order:
            raise ValueError(f"Order '{order_id}' not found.")
        
        # Restore stock if cancelled
        for item in order.items:
            prod = self.product_repo.get_by_sku(item.product.sku)
            if prod:
                prod.stock += item.quantity
                self.product_repo.save(prod)

        order.cancel()
        self.order_repo.save(order)
        self.notifier.notify_order_status(order)
        return order
