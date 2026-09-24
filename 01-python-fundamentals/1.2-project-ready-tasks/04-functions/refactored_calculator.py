from math_utils import add, subtract, multiply, divide


def calculator(num1, num2):
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

calculator(number1, number2)
