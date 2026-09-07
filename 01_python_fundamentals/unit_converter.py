"""
unit_converter.py - Standalone unit conversion utility for length, weight, and temperature.

Features clear modular conversion functions with type hints, input validation,
and deliberate physical constraint checks (e.g. non-negative lengths/weights,
and absolute-zero temperature boundaries).
"""

import sys
import argparse
from typing import Dict


# ---------------------------------------------------------------------------
# Length Conversions (Base unit: meters)
# ---------------------------------------------------------------------------
LENGTH_FACTORS: Dict[str, float] = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "ft": 0.3048,
    "in": 0.0254,
    "mi": 1609.344,
    "yd": 0.9144,
}


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert between length units.
    
    Raises:
        ValueError: If value is negative or unit is unrecognized.
    """
    if value < 0:
        raise ValueError(f"Length cannot be negative (got {value}). Physical dimensions must be >= 0.")

    u_from = from_unit.strip().lower()
    u_to = to_unit.strip().lower()

    if u_from not in LENGTH_FACTORS:
        raise ValueError(f"Unknown source length unit '{from_unit}'. Supported: {', '.join(LENGTH_FACTORS.keys())}")
    if u_to not in LENGTH_FACTORS:
        raise ValueError(f"Unknown target length unit '{to_unit}'. Supported: {', '.join(LENGTH_FACTORS.keys())}")

    # Convert to base (meters), then to target
    meters = value * LENGTH_FACTORS[u_from]
    return meters / LENGTH_FACTORS[u_to]


# ---------------------------------------------------------------------------
# Weight Conversions (Base unit: kilograms)
# ---------------------------------------------------------------------------
WEIGHT_FACTORS: Dict[str, float] = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.45359237,
    "oz": 0.028349523125,
    "ton": 1000.0,
}


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert between mass/weight units.
    
    Raises:
        ValueError: If value is negative or unit is unrecognized.
    """
    if value < 0:
        raise ValueError(f"Weight/mass cannot be negative (got {value}). Mass must be >= 0.")

    u_from = from_unit.strip().lower()
    u_to = to_unit.strip().lower()

    if u_from not in WEIGHT_FACTORS:
        raise ValueError(f"Unknown source weight unit '{from_unit}'. Supported: {', '.join(WEIGHT_FACTORS.keys())}")
    if u_to not in WEIGHT_FACTORS:
        raise ValueError(f"Unknown target weight unit '{to_unit}'. Supported: {', '.join(WEIGHT_FACTORS.keys())}")

    kg = value * WEIGHT_FACTORS[u_from]
    return kg / WEIGHT_FACTORS[u_to]


# ---------------------------------------------------------------------------
# Temperature Conversions (Base unit: Celsius)
# ---------------------------------------------------------------------------
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert between Celsius, Fahrenheit, and Kelvin with absolute zero verification.
    
    Raises:
        ValueError: If temperature is below absolute zero or unit is unrecognized.
    """
    u_from = from_unit.strip().upper()
    u_to = to_unit.strip().upper()

    valid_units = {"C", "F", "K"}
    if u_from not in valid_units:
        raise ValueError(f"Unknown temperature unit '{from_unit}'. Supported: C, F, K.")
    if u_to not in valid_units:
        raise ValueError(f"Unknown temperature unit '{to_unit}'. Supported: C, F, K.")

    # 1. Convert to Celsius and validate absolute zero (-273.15 °C)
    if u_from == "C":
        celsius = value
    elif u_from == "F":
        celsius = (value - 32.0) * (5.0 / 9.0)
    else:  # Kelvin
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError(
            f"Physical violation: {value} {u_from} evaluates to {celsius:.2f} °C, "
            f"which is below absolute zero (-273.15 °C / 0 K)."
        )

    # 2. Convert from Celsius to Target
    if u_to == "C":
        return celsius
    elif u_to == "F":
        return (celsius * 9.0 / 5.0) + 32.0
    else:  # Kelvin
        return celsius + 273.15


# ---------------------------------------------------------------------------
# Interactive Menu & CLI
# ---------------------------------------------------------------------------
def interactive_menu() -> None:
    print("=" * 50)
    print("           CLI Unit Converter")
    print("=" * 50)

    categories = {
        "1": ("Length", convert_length, "m, km, cm, mm, ft, in, mi, yd"),
        "2": ("Weight", convert_weight, "kg, g, mg, lb, oz, ton"),
        "3": ("Temperature", convert_temperature, "C, F, K"),
    }

    while True:
        print("\nSelect conversion category:")
        for k, (name, _, sample) in categories.items():
            print(f"  [{k}] {name} ({sample})")
        print("  [q] Quit")

        choice = input("\nChoice [1-3, q]: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        if choice not in categories:
            print(f"  [Error] Invalid choice '{choice}'.")
            continue

        cat_name, conv_func, units_hint = categories[choice]
        print(f"\n--- {cat_name} Conversion ---")
        print(f"Available units: {units_hint}")

        try:
            val_str = input("Enter value: ").strip()
            val = float(val_str)
            from_u = input("From unit: ").strip()
            to_u = input("To unit:   ").strip()

            result = conv_func(val, from_u, to_u)
            print(f"\n  -> {val} {from_u} = {result:.4f} {to_u}")
        except ValueError as e:
            print(f"\n  [Validation Error] {e}")
        except Exception as e:
            print(f"\n  [Unexpected Error] {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Length, Weight, or Temperature units.")
    parser.add_argument("--category", "-c", choices=["length", "weight", "temp"], help="Conversion category")
    parser.add_argument("--value", "-v", type=float, help="Numeric value to convert")
    parser.add_argument("--from-unit", "-f", help="Source unit (e.g. km, lb, C)")
    parser.add_argument("--to-unit", "-t", help="Target unit (e.g. mi, kg, F)")

    args = parser.parse_args()

    if args.category:
        if args.value is None or not args.from_unit or not args.to_unit:
            print("[Error] When --category is specified, --value, --from-unit, and --to-unit are all required.", file=sys.stderr)
            sys.exit(1)

        try:
            if args.category == "length":
                res = convert_length(args.value, args.from_unit, args.to_unit)
            elif args.category == "weight":
                res = convert_weight(args.value, args.from_unit, args.to_unit)
            else:
                res = convert_temperature(args.value, args.from_unit, args.to_unit)
            print(f"{res:.4f}")
        except ValueError as e:
            print(f"[Error] {e}", file=sys.stderr)
            sys.exit(2)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
