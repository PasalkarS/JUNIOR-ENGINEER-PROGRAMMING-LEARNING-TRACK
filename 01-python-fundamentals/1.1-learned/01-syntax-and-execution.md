# Syntax, Types, and Execution Flow

> **Module 01: Python Fundamentals | Topic 01**



## 1. Learning Outcomes

- **Execute Scripts:** Run Python scripts via CLI and understand interpreter mechanics.
- **Core Types:** Identify and convert int, float, str, bool, and None types.
- **Operators & Precedence:** Use arithmetic, comparison, and logical operators correctly.
- **Entry Points:** Safely structure Python files using `if __name__ == '__main__':`.

## 2. Key Syntax & Concepts


### Variables and Naming Conventions

Python uses dynamic typing. Variable names follow PEP 8 snake_case (e.g., total_amount, user_id). Avoid uppercase initials or camelCase for variables.

```python
age = 25              # int
price = 19.99         # float
user_name = 'Alice'   # str
is_active = True      # bool
result = None         # NoneType
```


### Type Checking and Conversion

Check types with type() or isinstance(). Explicit conversion prevents TypeError:

```python
raw_input = '42'
clean_number = int(raw_input)         # '42' -> 42
ratio = float('3.14')                # '3.14' -> 3.14
is_valid = isinstance(clean_number, int)  # True
```


### Operators and Expressions


| Category | Operators | Example / Notes |
| --- | --- | --- |
| Arithmetic | +, -, *, /, //, %, ** | 10 // 3 = 3 (floor div), 10 % 3 = 1 (modulo), 2 ** 3 = 8 |
| Comparison | ==, !=, <, >, <=, >= | Values comparison. Use 'is' only for identity (e.g., x is None) |
| Logical | and, or, not | Short-circuit evaluation applies |
| Assignment | =, +=, -=, *= | x += 1 increments in place |



### Script Execution & Entry Point

When a Python file is run directly, Python sets the special variable __name__ to '__main__'. When imported as a module, __name__ is set to the module name.

```python
def main():
    print('Application started.')

if __name__ == '__main__':
    main()
```


## 3. Common Mistakes & Gotchas

- **String Concatenation Trap:** 'User' + 42 throws TypeError. Use f-strings: f'User {42}'.
- **Floating Point Imprecision:** 0.1 + 0.2 != 0.3 (evaluates to 0.30000000000000004). For money, use round() or the decimal module.
- **Equality vs Identity:** Use '==' for value equality (a == b) and 'is' for singleton checks (res is None).

## 4. Practice Tasks

- **Task 1:** Write a script that prompts for item name, quantity, and unit price, computes subtotal and 8% tax, and prints an itemized bill.
- **Task 2:** Write a temperature converter verifying input types and printing results formatted to 2 decimal places.

## 5. Self-Check Questions

- **Q1:** What is the difference between '/' and '//' in Python?
- **Q2:** Why should you guard executable code with `if __name__ == '__main__':`?
- **Q3:** What does isinstance(x, (int, float)) return if x = 4.5?
