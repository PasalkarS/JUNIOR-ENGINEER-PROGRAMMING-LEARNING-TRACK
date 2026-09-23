# Topic 01: Classes and Objects
# Domain modeling: Customer, Product, OrderItem, and Invoice

class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Customer({self.customer_id}: {self.name})"

class Product:
    def __init__(self, sku: str, title: str, unit_price: float):
        self.sku = sku
        self.title = title
        self.unit_price = unit_price

    def __str__(self) -> str:
        return f"Product({self.sku}: {self.title} @ ${self.unit_price:.2f})"

class OrderItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self) -> float:
        return round(self.product.unit_price * self.quantity, 2)

    def __str__(self) -> str:
        return f"{self.product.title} x {self.quantity} = ${self.subtotal:.2f}"

class Invoice:
    def __init__(self, invoice_id: str, customer: Customer, items: list[OrderItem], tax_rate: float = 0.08):
        self.invoice_id = invoice_id
        self.customer = customer
        self.items = items
        self.tax_rate = tax_rate

    @property
    def subtotal(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    @property
    def tax(self) -> float:
        return round(self.subtotal * self.tax_rate, 2)

    @property
    def total(self) -> float:
        return round(self.subtotal + self.tax, 2)

    def print_invoice(self):
        print("=" * 45)
        print(f"INVOICE #{self.invoice_id}")
        print(f"Billed To: {self.customer.name} ({self.customer.email})")
        print("-" * 45)
        for item in self.items:
            print(f" - {item}")
        print("-" * 45)
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Tax ({self.tax_rate*100:.1f}%): ${self.tax:.2f}")
        print(f"TOTAL:    ${self.total:.2f}")
        print("=" * 45)

if __name__ == "__main__":
    cust = Customer("C100", "Alice Smith", "alice@example.com")
    prod1 = Product("SKU-LAP", "Pro Laptop", 1200.0)
    prod2 = Product("SKU-MOU", "Ergo Mouse", 45.0)

    items = [OrderItem(prod1, 1), OrderItem(prod2, 2)]
    inv = Invoice("INV-2026-001", cust, items)
    inv.print_invoice()
