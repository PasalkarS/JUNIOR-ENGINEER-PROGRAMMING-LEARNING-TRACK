# Modular Calculator with Functions
# Refactors procedural calculator into clean, testable functions.

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Division by zero is not permitted.")
    return x / y

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate(op: str, num1: float, num2: float) -> float:
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: '{op}'")
    return OPERATIONS[op](num1, num2)

if __name__ == "__main__":
    print("10 + 5 =", calculate("+", 10, 5))
    print("10 / 2 =", calculate("/", 10, 2))
    print("7 * 8  =", calculate("*", 7, 8))
