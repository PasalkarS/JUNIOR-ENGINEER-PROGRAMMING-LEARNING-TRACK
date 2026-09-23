# Menu Loop
# Demonstrates a while loop with a clean exit sentinel condition.

def show_menu():
    print("\n--- Mini System Menu ---")
    print("1. View Status")
    print("2. Run Health Check")
    print("3. Exit")

def run():
    # Simulated automated input for demonstration / testability
    simulated_inputs = ["1", "2", "3"]
    input_index = 0

    while True:
        show_menu()
        if input_index < len(simulated_inputs):
            choice = simulated_inputs[input_index]
            input_index += 1
            print(f"User selected: {choice}")
        else:
            choice = "3"

        if choice == "1":
            print("[INFO]: All systems operational.")
        elif choice == "2":
            print("[CHECK]: Memory OK, Disk OK, Network OK.")
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    run()
