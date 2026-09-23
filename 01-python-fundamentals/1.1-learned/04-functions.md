# 04 — Functions

## 1. Defining Functions

### What it is

A function is a reusable block of code that performs a specific task.
Functions help avoid writing the same code multiple times.

### Important Points

* Functions are created using the `def` keyword.
* A function can contain one or more statements.
* A function runs only when it is called.
* Functions can accept inputs and return outputs.
* Use meaningful function names.

### Basic Syntax

```python
def greet():
    print("Hello")

greet()
```

---

## 2. Parameters

### What it is

Parameters are variables written inside the function definition.
They receive values when the function is called.

### Important Points

* Parameters act as inputs to a function.
* A function can have multiple parameters.
* Parameters are available inside the function.
* Each parameter can have a different purpose.

### Basic Syntax

```python
def greet(name):
    print("Hello", name)

greet("Sam")
```

---

## 3. Return Values

### What it is

A return value is the result sent back by a function using `return`.

### Important Points

* `return` sends a value back to the caller.
* The returned value can be stored in a variable.
* `return` also stops the function.
* A function can return different types of values.

### Basic Syntax

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

## 4. Positional Arguments

### What it is

Positional arguments are passed to a function based on their position.

### Important Points

* The first value goes to the first parameter.
* The second value goes to the second parameter.
* The order matters.
* The number of arguments should match the parameters unless defaults or special arguments are used.

### Basic Syntax

```python
def greet(name, age):
    print(name, age)

greet("Sam", 25)
```

---

## 5. Keyword Arguments

### What it is

Keyword arguments pass values by using the parameter name.

### Important Points

* Parameter names are written when calling the function.
* The order does not matter.
* They make function calls easier to understand.
* Keyword arguments can be mixed with positional arguments in the correct order.

### Basic Syntax

```python
def greet(name, age):
    print(name, age)

greet(age=25, name="Sam")
```

---

## 6. Default Arguments

### What it is

A default argument has a value that is used when no value is provided.

### Important Points

* Default values are defined in the function definition.
* The caller can provide a different value.
* Default parameters are optional when calling the function.
* Parameters without defaults normally come before parameters with defaults.

### Basic Syntax

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Sam")
```

---

## 7. `*args`

### What it is

`*args` allows a function to accept any number of positional arguments.

### Important Points

* `args` is stored as a tuple.
* The `*` allows multiple positional values.
* The name `args` is a convention and can be changed.
* Useful when the number of inputs is unknown.

### Basic Syntax

```python
def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30)
```

---

## 8. `**kwargs`

### What it is

`**kwargs` allows a function to accept any number of keyword arguments.

### Important Points

* `kwargs` is stored as a dictionary.
* The `**` accepts multiple keyword values.
* The name `kwargs` is a convention.
* Useful when the number of named inputs is unknown.

### Basic Syntax

```python
def show_details(**kwargs):
    print(kwargs)

show_details(name="Sam", age=25)
```

---

## 9. Variable Scope

### What it is

Scope defines where a variable can be accessed in a program.

### Important Points

* A variable is available only within its scope.
* Variables created inside functions normally have local scope.
* Variables created outside functions can have global scope.
* Scope helps prevent unwanted changes to variables.

### Basic Syntax

```python
x = 10

def show():
    y = 20
    print(x)
    print(y)
```

---

## 10. Local Scope

### What it is

A local variable is created inside a function and is normally available only inside that function.

### Important Points

* Local variables belong to the function.
* They are created when the function runs.
* They cannot normally be accessed outside the function.
* Different functions can have local variables with the same name.

### Basic Syntax

```python
def calculate():
    result = 10 + 20
    print(result)

calculate()
```

---

## 11. Global Scope

### What it is

A global variable is created outside functions and can generally be accessed throughout the program.

### Important Points

* Global variables are defined outside functions.
* Functions can read global variables.
* Avoid using too many global variables.
* The `global` keyword can be used when modifying a global variable inside a function.

### Basic Syntax

```python
count = 10

def show():
    print(count)

show()
```

---

## 12. Pure Functions

### What it is

A pure function gives the same output for the same input and does not change outside data.

### Important Points

* It depends only on its inputs.
* It does not modify global or external data.
* It is easier to test and understand.
* Pure functions are useful for reusable code.

### Basic Syntax

```python
def add(a, b):
    return a + b
```

---

## 13. Reusable Functions

### What it is

A reusable function is designed to perform a task that can be used in different parts of a program.

### Important Points

* Keep each function focused on one task.
* Use parameters instead of hard-coded values.
* Return results when needed.
* Use meaningful names.
* Reusable functions reduce duplicate code.

### Basic Syntax

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5)
print(area)
```

---

## 14. Function Composition

### What it is

Function composition means using the result of one function as the input to another function.

### Important Points

* Functions can work together to complete a larger task.
* The output of one function becomes the input of another.
* It helps break complex tasks into smaller parts.
* Small functions are easier to reuse.

### Basic Syntax

```python
def double(number):
    return number * 2

def add_five(number):
    return number + 5

result = add_five(double(10))
print(result)
```

---

## 15. Docstrings

### What it is

A docstring is a description written inside a function to explain what it does.

### Important Points

* A docstring is written immediately after the function definition.
* It is usually written using triple quotes.
* It explains the purpose of the function.
* It can be viewed using `help()` or `__doc__`.

### Basic Syntax

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```
