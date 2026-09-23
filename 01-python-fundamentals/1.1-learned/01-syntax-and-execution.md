
# 01 — Syntax and Execution

## 1. Python Syntax

### What it is

Python syntax is the set of rules used to write Python code.

### Important Points

* Python syntax is simple and easy to read.
* Python is case-sensitive.
* Indentation is important in Python.
* Most statements do not need `;` at the end.
* Incorrect syntax gives a `SyntaxError`.

### Basic Syntax

```python
print("Hello World")
```

---

## 2. Variables

### What it is

A variable is a name used to store a value.

### Important Points

* Variables are created using `=`.
* Python automatically identifies the data type.
* The value of a variable can be changed.
* Variables can store different types of data.

### Basic Syntax

```python
name = "Sam"
age = 25
```

---

## 3. Naming Conventions

### What it is

Naming conventions are rules used to give meaningful names to variables and other objects.

### Important Points

* Use meaningful and readable names.
* Use `snake_case` for variables and functions.
* A name cannot start with a number.
* Names can contain letters, numbers, and `_`.
* Python variable names are case-sensitive.

### Basic Syntax

```python
first_name = "Sam"
total_marks = 90
```

---

## 4. Python Built-in Types

### What it is

Built-in types are data types already provided by Python for storing different kinds of values.

### Important Points

* `int` → whole numbers
* `float` → decimal numbers
* `str` → text
* `bool` → `True` or `False`
* `NoneType` → represents no value

### Basic Syntax

```python
age = 25
price = 10.5
name = "Sam"
is_valid = True
result = None
```

---

## 5. Integers

### What it is

An integer (`int`) is a whole number without a decimal point.

### Important Points

* Can be positive, negative, or zero.
* Used for counting and whole-number calculations.
* Integers can be used with arithmetic operators.
* Examples: `10`, `-5`, `0`.

### Basic Syntax

```python
age = 25
temperature = -5
```

---

## 6. Floats

### What it is

A float (`float`) is a number that contains a decimal point.

### Important Points

* Used for decimal values.
* Can be positive or negative.
* Arithmetic operations can produce float values.
* Examples: `10.5`, `3.14`, `-2.5`.

### Basic Syntax

```python
price = 99.50
temperature = -2.5
```

---

## 7. Strings

### What it is

A string (`str`) is a sequence of characters used to store text.

### Important Points

* Strings are written inside quotes.
* Single quotes (`' '`) or double quotes (`" "`) can be used.
* Strings can contain letters, numbers, and symbols.
* Strings can be joined using `+`.

### Basic Syntax

```python
name = "Sam"
message = 'Hello'
```

---

## 8. Booleans

### What it is

A boolean (`bool`) represents one of two values: `True` or `False`.

### Important Points

* `True` and `False` are boolean values.
* They must start with a capital letter.
* Booleans are commonly used in conditions.
* Comparisons usually return a boolean value.

### Basic Syntax

```python
is_logged_in = True
is_available = False
```

---

## 9. None

### What it is

`None` represents the absence of a value.

### Important Points

* `None` is a special Python value.
* Its type is `NoneType`.
* It is different from `0`, `False`, and an empty string.
* It is often used when a value is not available.

### Basic Syntax

```python
result = None
```

---

## 10. Type Checking

### What it is

Type checking is used to find the data type of a value or variable.

### Important Points

* `type()` is used to check the type.
* It can identify types such as `int`, `float`, and `str`.
* `isinstance()` can also be used to check a type.
* Type checking is useful when working with different types of data.

### Basic Syntax

```python
age = 25

print(type(age))
```

---

## 11. Type Conversion

### What it is

Type conversion means changing a value from one data type to another.

### Important Points

* `int()` converts a value to an integer.
* `float()` converts a value to a float.
* `str()` converts a value to a string.
* `bool()` converts a value to a boolean.
* The value must be suitable for the target type.

### Basic Syntax

```python
age = int("25")
price = float("10.5")
number = str(100)
```

---

## 12. Expressions

### What it is

An expression is a combination of values, variables, and operators that produces a result.

### Important Points

* Expressions are evaluated by Python.
* They can contain variables and operators.
* Arithmetic expressions produce values.
* Comparison expressions return `True` or `False`.

### Basic Syntax

```python
total = 10 + 5
result = age > 18
```

---

## 13. Arithmetic Operators

### What it is

Arithmetic operators are used to perform mathematical calculations.

### Important Points

* `+` → addition
* `-` → subtraction
* `*` → multiplication
* `/` → division
* `//` → floor division
* `%` → remainder
* `**` → power

### Basic Syntax

```python
addition = 10 + 5
multiplication = 10 * 2
division = 10 / 2
```

---

## 14. Comparison Operators

### What it is

Comparison operators compare two values and return `True` or `False`.

### Important Points

* `==` → equal to
* `!=` → not equal to
* `>` → greater than
* `<` → less than
* `>=` → greater than or equal to
* `<=` → less than or equal to

### Basic Syntax

```python
age >= 18
```

---

## 15. Logical Operators

### What it is

Logical operators are used to combine or reverse conditions.

### Important Points

* `and` → both conditions must be true.
* `or` → at least one condition must be true.
* `not` → reverses the result.
* They are commonly used with conditional statements.

### Basic Syntax

```python
age >= 18 and age <= 60
```

---

## 16. Assignment Operators

### What it is

Assignment operators are used to assign or update values in variables.

### Important Points

* `=` → assigns a value.
* `+=` → adds and assigns.
* `-=` → subtracts and assigns.
* `*=` → multiplies and assigns.
* `/=` → divides and assigns.
* Other operators include `//=`, `%=`, and `**=`.

### Basic Syntax

```python
x = 10
x += 5
```

---

## 17. Operator Precedence

### What it is

Operator precedence determines the order in which operators are evaluated.

### Important Points

* Parentheses `()` are evaluated first.
* `**` has higher precedence than multiplication.
* `*`, `/`, `//`, and `%` are evaluated before `+` and `-`.
* Comparison operators are evaluated after arithmetic operators.
* Parentheses can be used to clearly control the order.

### Basic Syntax

```python
result = (10 + 5) * 2
```

---

## 18. Input

### What it is

Input allows a Python program to receive data from the user.

### Important Points

* `input()` is used to receive user input.
* `input()` returns the entered value as a string.
* Use `int()` or `float()` when numerical input is required.
* The program waits for the user to enter a value.

### Basic Syntax

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

---

## 19. Output

### What it is

Output is the information displayed by a Python program.

### Important Points

* `print()` is commonly used for output.
* It can display text, numbers, variables, and expressions.
* Multiple values can be printed together.
* `print()` normally moves to a new line after printing.

### Basic Syntax

```python
print("Hello")
print("Age:", age)
```

---

## 20. `print()`

### What it is

`print()` is a built-in Python function used to display information on the screen.

### Important Points

* Can print text, variables, and expressions.
* Multiple values can be printed using commas.
* `sep` controls the separator between values.
* `end` controls what is printed at the end.

### Basic Syntax

```python
print("Hello World")
print("Age:", 25)
```

---

## 21. Comments

### What it is

Comments are notes in the code that Python does not execute.

### Important Points

* Single-line comments start with `#`.
* Comments help explain code.
* Python ignores comments during execution.
* Comments should be short and useful.

### Basic Syntax

```python
# This is a comment
name = "Sam"
```

---

## 22. Indentation

### What it is

Indentation means spaces at the beginning of a line. Python uses indentation to define blocks of code.

### Important Points

* Indentation is required inside blocks such as `if`, loops, and functions.
* Incorrect indentation can cause an error.
* Use consistent indentation.
* The common standard is 4 spaces.

### Basic Syntax

```python
if age >= 18:
    print("Adult")
```

---

## 23. Script Execution

### What it is

Script execution means running a Python file containing Python code.

### Important Points

* Python files normally use the `.py` extension.
* The Python interpreter reads and executes the code.
* Code is generally executed from top to bottom.
* An error can stop the program from continuing.

### Basic Syntax

```text
python program.py
```

---

## 24. Python Interpreter Basics

### What it is

The Python interpreter is the program that reads and executes Python code.

### Important Points

* It can execute Python files.
* It can also run Python code interactively.
* Interactive mode is useful for testing small pieces of code.
* The interpreter shows errors when code cannot be executed.

### Basic Syntax

```text
>>> print("Hello")
Hello
```

---

## 25. Modules

### What it is

A module is a Python file containing reusable code such as variables, functions, or classes.

### Important Points

* Modules help organize code.
* A `.py` file can be used as a module.
* Modules can contain reusable functions and variables.
* Python also provides many built-in modules.

### Basic Syntax

```python
# calculator.py

def add(a, b):
    return a + b
```

---

## 26. Imports

### What it is

An import allows you to use code from another module in your program.

### Important Points

* `import` is used to import a module.
* `from ... import ...` can import specific items.
* Imported code can be reused in your program.
* Python provides many built-in modules.

### Basic Syntax

```python
import math

print(math.sqrt(25))
```

---

## 27. `if __name__ == "__main__":`

### What it is

It is used to run specific code only when a Python file is executed directly.

### Important Points

* `__name__` is a special Python variable.
* When a file is run directly, `__name__` is `"__main__"`.
* When the file is imported, this condition is normally false.
* It is commonly used as the starting point of a Python script.

### Basic Syntax

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()
```
