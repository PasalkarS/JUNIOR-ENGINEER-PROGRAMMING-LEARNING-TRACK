"""
Simple Unit Converter
Beginner-friendly script to convert length, weight, and temperature.
"""

def km_to_miles(km):
    if km < 0:
        raise ValueError("Distance cannot be negative.")
    return km * 0.621371

def miles_to_km(miles):
    if miles < 0:
        raise ValueError("Distance cannot be negative.")
    return miles / 0.621371

def kg_to_lbs(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462

def lbs_to_kg(lbs):
    if lbs < 0:
        raise ValueError("Weight cannot be negative.")
    return lbs / 2.20462

def celsius_to_fahrenheit(c):
    if c < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 °C).")
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    if f < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67 °F).")
    return (f - 32) * 5/9

def main():
    while True:
        print("\n--- Simple Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. Exit")

        choice = input("Select an option (1-7): ").strip()

        if choice == "7":
            print("Exiting converter. Goodbye!")
            break

        if choice not in [str(i) for i in range(1, 7)]:
            print("Invalid choice! Please choose 1 to 7.")
            continue

        try:
            val = float(input("Enter value to convert: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        try:
            if choice == "1":
                print(f"{val} km = {km_to_miles(val):.2f} miles")
            elif choice == "2":
                print(f"{val} miles = {miles_to_km(val):.2f} km")
            elif choice == "3":
                print(f"{val} kg = {kg_to_lbs(val):.2f} lbs")
            elif choice == "4":
                print(f"{val} lbs = {lbs_to_kg(val):.2f} kg")
            elif choice == "5":
                print(f"{val} °C = {celsius_to_fahrenheit(val):.2f} °F")
            elif choice == "6":
                print(f"{val} °F = {fahrenheit_to_celsius(val):.2f} °C")
        except ValueError as e:
            print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
