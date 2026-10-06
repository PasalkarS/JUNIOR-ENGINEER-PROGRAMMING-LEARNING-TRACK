
from repositories import InMemoryOrderRepository
from services import OrderService


def main():
    repository = InMemoryOrderRepository()
    service = OrderService(repository)

    while True:
        print("\n===== ORDER MANAGEMENT =====")
        print("1. Create Order")
        print("2. View Order")
        print("3. View All Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                order_id = input("Enter order ID: ")
                customer = input("Enter customer name: ")
                product = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))

                order = service.create_order(
                    order_id,
                    customer,
                    product,
                    quantity,
                    price
                )

                print("\nOrder created successfully!")
                order.show_order()

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            order_id = input("Enter order ID: ")

            try:
                order = service.get_order(order_id)
                order.show_order()
            except ValueError as error:
                print("Error:", error)

        elif choice == "3":
            orders = service.get_all_orders()

            if not orders:
                print("No orders found")
            else:
                for order in orders:
                    print("-------------------")
                    order.show_order()

        elif choice == "4":
            print("Exiting Order Management System")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
