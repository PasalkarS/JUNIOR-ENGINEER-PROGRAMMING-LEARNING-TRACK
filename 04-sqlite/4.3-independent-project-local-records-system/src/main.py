import database
import repository
import services
import reports


def display_products():
    products = repository.get_all_products()

    print("\nProduct List:")

    if not products:
        print("No products found.")
        return

    for product in products:
        print(
            "ID:", product[0],
            "| Name:", product[1],
            "| Category:", product[2],
            "| Quantity:", product[3],
            "| Price: ₹", product[4]
        )


def display_categories():
    categories = repository.get_categories()

    print("\nCategories:")

    for category in categories:
        print(category[0], "-", category[1])


def main():
    database.initialize_database()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Add Product")
        print("4. View Products")
        print("5. Search Products")
        print("6. Filter Products by Category")
        print("7. Update Product")
        print("8. Delete Product")
        print("9. Show Inventory Value")
        print("10. Show Low Stock")
        print("11. Show Category Report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                category_name = input("Enter category name: ").strip()

                if not category_name:
                    raise ValueError("Category name cannot be empty.")

                category_id = repository.add_category(category_name)
                print("Category added. ID:", category_id)

            elif choice == "2":
                display_categories()

            elif choice == "3":
                display_categories()

                product_name = input("Enter product name: ")
                category_id = int(input("Enter category ID: "))
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))

                product_id = services.add_new_product(
                    product_name,
                    category_id,
                    quantity,
                    price
                )

                print("Product added. ID:", product_id)

            elif choice == "4":
                display_products()

            elif choice == "5":
                search_text = input("Enter product name to search: ")
                products = repository.search_products(search_text)

                for product in products:
                    print(product)

                if not products:
                    print("No matching products found.")

            elif choice == "6":
                display_categories()
                category_id = int(input("Enter category ID: "))

                products = repository.filter_products_by_category(
                    category_id
                )

                for product in products:
                    print(product)

                if not products:
                    print("No products found in this category.")

            elif choice == "7":
                product_id = int(input("Enter product ID: "))
                product_name = input("Enter new product name: ")
                display_categories()
                category_id = int(input("Enter category ID: "))
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))

                services.update_existing_product(
                    product_id,
                    product_name,
                    category_id,
                    quantity,
                    price
                )

                print("Product updated successfully.")

            elif choice == "8":
                product_id = int(input("Enter product ID: "))
                services.remove_product(product_id)
                print("Product deleted successfully.")

            elif choice == "9":
                reports.show_inventory_value()

            elif choice == "10":
                threshold = int(input("Enter low-stock threshold: "))
                reports.show_low_stock(threshold)

            elif choice == "11":
                reports.show_category_report()

            elif choice == "0":
                print("Exiting Inventory Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print("Invalid input:", error)

        except Exception as error:
            print("Operation failed:", error)


if __name__ == "__main__":
    main()
