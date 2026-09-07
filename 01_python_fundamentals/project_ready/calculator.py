"""
calculator.py - A menu-driven CLI calculator with robust input validation.

Supports basic arithmetic and power/modulo operations, gracefully handling
non-numeric inputs, division-by-zero, and out-of-range menu selections.
"""

import sys
import argparse


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero. Please supply a non-zero denominator.")
    return a / b


def power(a: float, b: float) -> float:
    if a == 0 and b < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power.")
    if b > 10000:
        raise OverflowError("Exponent is too large to safely compute.")
    return a ** b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulo with a zero divisor.")
    return a % b


OPERATIONS = {
    "1": ("Addition (+)", add),
    "2": ("Subtraction (-)", subtract),
    "3": ("Multiplication (*)", multiply),
    "4": ("Division (/)", divide),
    "5": ("Power (^)", power),
    "6": ("Modulo (%)", modulo),
}


def get_float_input(prompt: str) -> float:
    """Prompt the user for a number, continuously retrying if input is invalid."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  [Error] '{raw}' is not a valid number. Please enter a valid integer or float.")


def interactive_menu() -> None:
    """Run the interactive calculator loop."""
    print("=" * 45)
    print("        CLI Modular Calculator")
    print("=" * 45)

    while True:
        print("\nSelect an operation:")
        for key, (label, _) in OPERATIONS.items():
            print(f"  [{key}] {label}")
        print("  [q] Quit")

        choice = input("\nEnter choice [1-6, q]: ").strip().lower()

        if choice in ("q", "quit", "exit"):
            print("\nExiting calculator. Have a great day!")
            break

        if choice not in OPERATIONS:
            print(f"  [Error] '{choice}' is not a valid choice. Choose between 1 and 6, or 'q' to exit.")
            continue

        label, func = OPERATIONS[choice]
        print(f"\nSelected: {label}")

        num1 = get_float_input("  Enter first number:  ")
        num2 = get_float_input("  Enter second number: ")

        try:
            result = func(num1, num2)
            # Format integer outputs without trailing decimal zeros
            formatted = f"{int(result)}" if result.is_integer() else f"{result:.6g}"
            print(f"  -> Result: {formatted}")
        except ZeroDivisionError as e:
            print(f"  [Math Error] {e}")
        except OverflowError as e:
            print(f"  [Overflow Error] {e}")
        except Exception as e:
            print(f"  [Unexpected Error] {e}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CLI Calculator - Standalone or Menu Driven",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--op", choices=["add", "sub", "mul", "div", "pow", "mod"], help="Operation to execute directly")
    parser.add_argument("-a", type=float, help="First operand")
    parser.add_argument("-b", type=float, help="Second operand")

    args = parser.parse_args()

    # If flags are passed, run direct non-interactive calculation
    if args.op:
        if args.a is None or args.b is None:
            print("[Error] Both -a and -b operands are required when using --op.")
            sys.exit(1)

        mapping = {
            "add": add,
            "sub": subtract,
            "mul": multiply,
            "div": divide,
            "pow": power,
            "mod": modulo,
        }
        try:
            res = mapping[args.op](args.a, args.b)
            print(res)
        except ZeroDivisionError as e:
            print(f"[Math Error] {e}", file=sys.stderr)
            sys.exit(2)
        except Exception as e:
            print(f"[Error] {e}", file=sys.stderr)
            sys.exit(1)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
