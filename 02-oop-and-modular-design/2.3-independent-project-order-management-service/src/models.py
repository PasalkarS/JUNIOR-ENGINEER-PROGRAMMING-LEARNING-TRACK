class Order:
    def __init__(self, order_id, customer, product, quantity, price):
        if not order_id:
            raise ValueError("Order ID is required")

        if not customer:
            raise ValueError("Customer name is required")

        if not product:
            raise ValueError("Product name is required")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if price <= 0:
            raise ValueError("Price must be greater than zero")

        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price

    def show_order(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Product:", self.product)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total:", self.calculate_total())
