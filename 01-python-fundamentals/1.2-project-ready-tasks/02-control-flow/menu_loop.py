while True:
    print("\n1. Say Hello")
    print("2. Show Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        print("Welcome to Python!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
