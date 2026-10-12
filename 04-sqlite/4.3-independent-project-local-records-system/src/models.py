
class Product:
    def __init__(
        self,
        product_name,
        category_id,
        quantity,
        price,
        product_id=None
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.quantity = quantity
        self.price = price

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Category ID:", self.category_id)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
