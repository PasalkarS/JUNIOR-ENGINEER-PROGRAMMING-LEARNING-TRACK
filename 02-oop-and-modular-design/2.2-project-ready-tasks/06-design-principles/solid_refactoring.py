# Bad design: one class does everything

class BadOrderManager:
    def place_order(self, product, price):
        print("Saving order:", product)
        print("Price:", price)
        print("Sending email to customer")
        print("Creating report")


# Improved design

class Order:
    def __init__(self, product, price):
        self.product = product
        self.price = price


class OrderRepository:
    def save(self, order):
        print("Saving order:", order.product)


class EmailNotification:
    def send(self, message):
        print("Email sent:", message)


class OrderService:
    def __init__(self, repository, notification):
        self.repository = repository
        self.notification = notification

    def place_order(self, order):
        if not order.product:
            raise ValueError("Product is required")

        if order.price <= 0:
            raise ValueError("Price must be positive")

        self.repository.save(order)
        self.notification.send("Order confirmed")


# Create objects

order1 = Order("Laptop", 50000)

repository = OrderRepository()
notification = EmailNotification()

service = OrderService(repository, notification)
service.place_order(order1)

"""
Saving order: Laptop
Email sent: Order confirmed
"""
