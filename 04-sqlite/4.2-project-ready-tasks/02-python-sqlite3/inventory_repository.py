from database_connection import connect_database


def add_product(product_name, quantity, price):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO products (product_name, quantity, price)
        VALUES (?, ?, ?)
        """,
        (product_name, quantity, price)
    )

    connection.commit()
    product_id = cursor.lastrowid
    connection.close()

    return product_id


def get_all_products():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()
    return products


def get_product(product_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_id = ?",
        (product_id,)
    )

    product = cursor.fetchone()
    connection.close()

    return product


def update_product(product_id, product_name, quantity, price):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET product_name = ?, quantity = ?, price = ?
        WHERE product_id = ?
        """,
        (product_name, quantity, price, product_id)
    )

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return updated


def delete_product(product_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id = ?",
        (product_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted
