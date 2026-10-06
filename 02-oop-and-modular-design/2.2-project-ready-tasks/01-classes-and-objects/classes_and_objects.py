class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_customer(self):
        print("Customer:", self.name)
        print("Email:", self.email)


class Product:
    store_name = "Simple Store"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price_with_tax(self):
        return self.price * 1.18

    @classmethod
    def show_store(cls):
        print("Store:", cls.store_name)

    @staticmethod
    def is_valid_price(price):
        return price > 0


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity

    def show_order(self):
        print("Order Customer:", self.customer.name)
        print("Product:", self.product.name)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total())


class Invoice:
    def __init__(self, order):
        self.order = order

    def show_invoice(self):
        print("\n----- INVOICE -----")
        print("Customer:", self.order.customer.name)
        print("Product:", self.order.product.name)
        print("Amount:", self.order.calculate_total())
        print("-------------------")


customer1 = Customer("Rahul", "rahul@example.com")
product1 = Product("Keyboard", 1500)

if Product.is_valid_price(product1.price):
    order1 = Order(customer1, product1, 2)

    customer1.show_customer()
    Product.show_store()
    print("Price with tax:", product1.price_with_tax)

    order1.show_order()

    invoice1 = Invoice(order1)
    invoice1.show_invoice()


"""
Customer: Rahul
Email: rahul@example.com
Store: Simple Store
Price with tax: 1770.0
Order Customer: Rahul
Product: Keyboard
Quantity: 2
Total: 3000

----- INVOICE -----
Customer: Rahul
Product: Keyboard
Amount: 3000
-------------------
"""
