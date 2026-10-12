
from database import get_connection


def add_product(product_name, category_id, quantity, price):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO products
            (product_name, category_id, quantity, price)
            VALUES (?, ?, ?, ?)
            """,
            (product_name, category_id, quantity, price)
        )

        connection.commit()
        return cursor.lastrowid

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT products.product_id,
               products.product_name,
               categories.category_name,
               products.quantity,
               products.price
        FROM products
        JOIN categories
        ON products.category_id = categories.category_id
        ORDER BY products.product_id
    """)

    products = cursor.fetchall()
    connection.close()

    return products


def search_products(search_text):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_id, product_name, category_id, quantity, price
        FROM products
        WHERE product_name LIKE ?
        ORDER BY product_name
    """, ("%" + search_text + "%",))

    products = cursor.fetchall()
    connection.close()

    return products


def filter_products_by_category(category_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_id, product_name, category_id, quantity, price
        FROM products
        WHERE category_id = ?
        ORDER BY product_name
    """, (category_id,))

    products = cursor.fetchall()
    connection.close()

    return products


def update_product(product_id, product_name, category_id, quantity, price):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE products
            SET product_name = ?,
                category_id = ?,
                quantity = ?,
                price = ?
            WHERE product_id = ?
        """, (product_name, category_id, quantity, price, product_id))

        connection.commit()
        return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id = ?",
        (product_id,)
    )

    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()

    return deleted


def get_categories():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category_id, category_name
        FROM categories
        ORDER BY category_name
    """)

    categories = cursor.fetchall()
    connection.close()

    return categories


def add_category(category_name):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO categories (category_name) VALUES (?)",
            (category_name,)
        )

        connection.commit()
        return cursor.lastrowid

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
