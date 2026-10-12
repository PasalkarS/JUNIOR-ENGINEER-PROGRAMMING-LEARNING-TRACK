from database import get_connection


def show_inventory_value():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(quantity * price)
        FROM products
    """)

    result = cursor.fetchone()
    connection.close()

    total_value = result[0] if result[0] is not None else 0

    print("Total Inventory Value: ₹", round(total_value, 2))


def show_low_stock(threshold=10):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_id, product_name, quantity
        FROM products
        WHERE quantity <= ?
        ORDER BY quantity
    """, (threshold,))

    products = cursor.fetchall()
    connection.close()

    print("\nLow Stock Products:")

    if not products:
        print("No low-stock products found.")
        return

    for product in products:
        print(
            "ID:", product[0],
            "| Name:", product[1],
            "| Quantity:", product[2]
        )


def show_category_report():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT categories.category_name,
               COUNT(products.product_id),
               COALESCE(SUM(products.quantity * products.price), 0)
        FROM categories
        LEFT JOIN products
        ON categories.category_id = products.category_id
        GROUP BY categories.category_id, categories.category_name
        ORDER BY categories.category_name
    """)

    report = cursor.fetchall()
    connection.close()

    print("\nCategory Report:")

    for category in report:
        print(
            "Category:", category[0],
            "| Products:", category[1],
            "| Inventory Value: ₹", round(category[2], 2)
        )
