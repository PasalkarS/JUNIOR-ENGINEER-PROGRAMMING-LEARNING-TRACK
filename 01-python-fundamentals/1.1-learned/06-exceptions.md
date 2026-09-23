# 06 — Exceptions Handling

## 1. What Exceptions Are

### What it is

An exception is an error that occurs while a Python program is running.
Python can handle exceptions so the program does not stop unexpectedly.

### Important Points

* Exceptions happen during program execution.
* Different errors produce different exceptions.
* Exceptions can be handled using `try` and `except`.
* Handling exceptions helps make programs more reliable.

---

## 2. Common Exceptions

### What it is

Python has many built-in exceptions for common types of errors.

### Important Points

* `ValueError` — invalid value.
* `TypeError` — incorrect data type.
* `ZeroDivisionError` — division by zero.
* `IndexError` — invalid list or sequence index.
* `KeyError` — missing dictionary key.
* `FileNotFoundError` — file does not exist.

### Basic Syntax

```python
number = int("hello")
```

This produces a `ValueError`.

---

## 3. `try`

### What it is

The `try` block contains code that might cause an exception.

### Important Points

* Python first executes the code inside `try`.
* If an exception occurs, Python looks for a matching `except`.
* Code after the exception inside the `try` block is not executed.
* Use `try` only around code that may actually fail.

### Basic Syntax

```python
try:
    number = int(input("Enter a number: "))
```

---

## 4. `except`

### What it is

The `except` block handles an exception that occurs in the `try` block.

### Important Points

* It prevents the program from stopping unexpectedly.
* You can handle specific exceptions.
* Multiple `except` blocks can be used.
* Avoid using a broad `except` when a specific exception is known.

### Basic Syntax

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
```

---

## 5. `else`

### What it is

The `else` block runs when no exception occurs in the `try` block.

### Important Points

* `else` runs only when `try` succeeds.
* It is useful for code that should run after successful execution.
* It keeps success logic separate from error-handling logic.

### Basic Syntax

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print("Number:", number)
```

---

## 6. `finally`

### What it is

The `finally` block runs whether an exception occurs or not.

### Important Points

* It is commonly used for cleanup.
* It runs after `try` and `except`/`else`.
* It can be used to close resources.
* It normally runs even when an exception occurs.

### Basic Syntax

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Finished")
```

---

## 7. Raising Exceptions

### What it is

The `raise` keyword is used to create an exception manually.

### Important Points

* `raise` stops normal execution.
* It can be used when a condition is invalid.
* You can raise built-in exceptions.
* It is useful for enforcing rules in a program.

### Basic Syntax

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## 8. Custom Exceptions

### What it is

A custom exception is a user-defined exception created for a specific situation.

### Important Points

* Custom exceptions are created using a class.
* They normally inherit from `Exception`.
* They make errors more meaningful.
* They are useful in larger programs.

### Basic Syntax

```python
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Invalid age")
```

---

## 9. Validation

### What it is

Validation checks whether input or data meets the required rules before using it.

### Important Points

* Check user input before processing it.
* Validate data type, range, and required values.
* Invalid data should produce a clear message.
* Validation helps prevent unexpected errors.

### Basic Syntax

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age must be positive")
```

---

## 10. Defensive Programming

### What it is

Defensive programming means writing code that safely handles incorrect, unexpected, or invalid situations.

### Important Points

* Do not assume that input will always be correct.
* Validate important data.
* Handle expected exceptions.
* Give clear error messages.
* Keep the program from failing unnecessarily.

### Basic Syntax

```python
try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Number cannot be negative")

    print("Number:", number)

except ValueError as error:
    print("Error:", error)
```
