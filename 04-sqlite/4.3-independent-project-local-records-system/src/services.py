import repository


def add_new_product(product_name, category_id, quantity, price):
    product_name = product_name.strip()

    if product_name == "":
        raise ValueError("Product name cannot be empty.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    if category_id <= 0:
        raise ValueError("Select a valid category.")

    return repository.add_product(
        product_name,
        category_id,
        quantity,
        price
    )


def update_existing_product(
    product_id,
    product_name,
    category_id,
    quantity,
    price
):
    if product_id <= 0:
        raise ValueError("Invalid product ID.")

    if product_name.strip() == "":
        raise ValueError("Product name cannot be empty.")

    if category_id <= 0:
        raise ValueError("Select a valid category.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    updated = repository.update_product(
        product_id,
        product_name.strip(),
        category_id,
        quantity,
        price
    )

    if not updated:
        raise ValueError("Product not found.")

    return updated


def remove_product(product_id):
    if product_id <= 0:
        raise ValueError("Invalid product ID.")

    deleted = repository.delete_product(product_id)

    if not deleted:
        raise ValueError("Product not found.")

    return deleted
