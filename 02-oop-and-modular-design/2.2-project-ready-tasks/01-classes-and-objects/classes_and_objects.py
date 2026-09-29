# Topic 5.1: Classes and Objects
# Task: Model Customer, Product, Order and Invoice


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def show_customer(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Email:", self.email)


class Product:
    total_products = 0

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self._price = price
        Product.total_products += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative")

    def show_product(self):
        print("Product ID:", self.product_id)
        print("Product:", self.name)
        print("Price:", self.price)

    @classmethod
    def show_total_products(cls):
        print("Total Products:", cls.total_products)

    @staticmethod
    def is_valid_price(price):
        return price >= 0


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total = total + product.price

        return total

    def show_order(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer.name)

        print("Products:")

        for product in self.products:
            print("-", product.name, "₹", product.price)


class Invoice:
    def __init__(self, invoice_id, order):
        self.invoice_id = invoice_id
        self.order = order

    def show_invoice(self):
        print("Invoice ID:", self.invoice_id)
        print("Customer:", self.order.customer.name)
        print("Total Amount: ₹", self.order.calculate_total())


# Create Customer
customer1 = Customer(101, "Sam", "sam@example.com")


# Create Products
product1 = Product(1, "Laptop", 50000)
product2 = Product(2, "Mouse", 1000)
product3 = Product(3, "Keyboard", 2000)


# Create Order
order1 = Order(1001, customer1)

order1.add_product(product1)
order1.add_product(product2)
order1.add_product(product3)


# Create Invoice
invoice1 = Invoice(5001, order1)


# Display Customer
customer1.show_customer()

print()


# Display Products
product1.show_product()

print()

product2.show_product()

print()

product3.show_product()

print()


# Display Order
order1.show_order()

print()


# Display Invoice
invoice1.show_invoice()

print()


# Class Method
Product.show_total_products()

print()


# Static Method
print("Is ₹500 a valid price?", Product.is_valid_price(500))
print("Is ₹-100 a valid price?", Product.is_valid_price(-100))

print()


# Property
product2.price = 1200

print("Updated Mouse Price:", product2.price)
