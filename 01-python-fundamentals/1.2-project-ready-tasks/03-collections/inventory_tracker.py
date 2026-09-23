# Inventory Tracker
# Demonstrates dictionary manipulation, lookups, and updates.

inventory = {
    "SKU-001": {"name": "USB-C Cable", "price": 9.99, "stock": 15},
    "SKU-002": {"name": "Wireless Mouse", "price": 24.50, "stock": 3},
    "SKU-003": {"name": "Mechanical Keyboard", "price": 79.00, "stock": 8},
    "SKU-004": {"name": "Monitor Stand", "price": 35.00, "stock": 2},
}

def add_stock(sku, quantity):
    if sku in inventory:
        inventory[sku]["stock"] += quantity
        print(f"Updated {inventory[sku]['name']}: New stock = {inventory[sku]['stock']}")
    else:
        print(f"Error: SKU '{sku}' not found.")

def get_low_stock_items(threshold=5):
    # Dict comprehension for low stock alert
    return {sku: data for sku, data in inventory.items() if data["stock"] < threshold}

print("--- Current Low Stock Items (< 5) ---")
low = get_low_stock_items(5)
for sku, data in low.items():
    print(f"[{sku}] {data['name']} - Only {data['stock']} remaining!")

add_stock("SKU-002", 10)
