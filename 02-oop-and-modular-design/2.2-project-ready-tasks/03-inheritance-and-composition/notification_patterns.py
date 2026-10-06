
# Inheritance

class Notification:
    def send(self, message):
        print("Sending notification:", message)


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)


# Composition

class Payment:
    def pay(self, amount):
        print("Payment successful:", amount)


class Order:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount


class OrderService:
    def __init__(self, payment, notification):
        self.payment = payment
        self.notification = notification

    def place_order(self, order):
        print("Order placed:", order.product)
        self.payment.pay(order.amount)
        self.notification.send("Your order is confirmed")


class Report:
    def create_report(self, order):
        print("\n----- REPORT -----")
        print("Product:", order.product)
        print("Amount:", order.amount)


email = EmailNotification()
sms = SMSNotification()

email.send("Welcome to our store")
sms.send("Your order is ready")

payment = Payment()
order = Order("Laptop", 50000)

service = OrderService(payment, email)
service.place_order(order)

report = Report()
report.create_report(order)

"""
Email: Welcome to our store
SMS: Your order is ready
Order placed: Laptop
Payment successful: 50000
Email: Your order is confirmed

----- REPORT -----
Product: Laptop
Amount: 50000
"""
