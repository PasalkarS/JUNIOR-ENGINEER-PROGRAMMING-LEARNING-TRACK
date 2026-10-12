from database_connection import create_table
from inventory_repository import (
    add_product,
    get_all_products,
    get_product,
    update_product,
    delete_product
)


create_table()

# CREATE
product_id = add_product("Keyboard", 15, 799.00)
print("Product added with ID:", product_id)

# READ ALL
print("\nAll Products:")
products = get_all_products()

for product in products:
    print(product)

# READ ONE
print("\nSelected Product:")
product = get_product(product_id)
print(product)

# UPDATE
updated = update_product(product_id, "Gaming Keyboard", 20, 999.00)

if updated:
    print("\nProduct updated successfully.")
else:
    print("\nProduct not found.")

print(get_product(product_id))

# DELETE
deleted = delete_product(product_id)

if deleted:
    print("\nProduct deleted successfully.")
else:
    print("\nProduct not found.")

print("\nRemaining Products:")
for product in get_all_products():
    print(product)
