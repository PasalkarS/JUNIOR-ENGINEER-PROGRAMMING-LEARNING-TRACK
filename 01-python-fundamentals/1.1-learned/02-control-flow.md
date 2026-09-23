# 02 — Control Flow

## 1. `if`

### What it is

`if` is used to execute a block of code when a condition is `True`.

### Important Points

* Checks whether a condition is true.
* Runs the code only when the condition is `True`.
* Uses `:` after the condition.
* The code inside `if` must be indented.

### Basic Syntax

```python
if condition:
    # code
```

---

## 2. `elif`

### What it is

`elif` means "else if" and is used to check another condition when the previous condition is `False`.

### Important Points

* Used after an `if` statement.
* Multiple `elif` statements can be used.
* Conditions are checked from top to bottom.
* Only the first `True` condition is executed.

### Basic Syntax

```python
if condition:
    # code
elif condition:
    # code
```

---

## 3. `else`

### What it is

`else` is used to execute code when all previous conditions are `False`.

### Important Points

* Does not have a condition.
* Must come after `if` or `elif`.
* Only one `else` can be used in a condition block.
* `else` is optional.

### Basic Syntax

```python
if condition:
    # code
else:
    # code
```

---

## 4. Nested Conditions

### What it is

A nested condition is an `if` statement placed inside another `if` statement.

### Important Points

* Used when one condition depends on another.
* The inner `if` is checked only when the outer condition is `True`.
* Proper indentation is required.
* Too many nested conditions can make code difficult to read.

### Basic Syntax

```python
if condition:
    if condition:
        # code
```

---

## 5. `for` Loop

### What it is

A `for` loop is used to repeat code for each item in a sequence or collection.

### Important Points

* Commonly used with lists, strings, and `range()`.
* Runs once for each item.
* The loop variable stores the current item.
* Stops after all items have been processed.

### Basic Syntax

```python
for item in collection:
    # code
```

---

## 6. `while` Loop

### What it is

A `while` loop repeats code as long as a condition is `True`.

### Important Points

* Checks the condition before each iteration.
* Stops when the condition becomes `False`.
* The condition should eventually become `False`.
* Useful when the number of repetitions is not known.

### Basic Syntax

```python
while condition:
    # code
```

---

## 7. `range()`

### What it is

`range()` generates a sequence of numbers and is commonly used with `for` loops.

### Important Points

* `range(stop)` starts from `0`.
* `range(start, stop)` starts from `start`.
* The `stop` value is not included.
* `range(start, stop, step)` allows a custom step.

### Basic Syntax

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

---

## 8. `break`

### What it is

`break` is used to immediately stop a loop.

### Important Points

* Stops the current loop.
* Works with both `for` and `while`.
* Execution continues with the code after the loop.
* Useful when the required result is found.

### Basic Syntax

```python
for item in collection:
    if condition:
        break
```

---

## 9. `continue`

### What it is

`continue` skips the current iteration and moves to the next iteration of the loop.

### Important Points

* Does not stop the entire loop.
* Only skips the current iteration.
* Works with both `for` and `while`.
* Useful when certain values need to be skipped.

### Basic Syntax

```python
for item in collection:
    if condition:
        continue
```

---

## 10. Conditional Expressions

### What it is

A conditional expression is a short way to write a simple `if-else` condition in one line.

### Important Points

* Also called a ternary expression.
* Used for simple conditions.
* Makes simple code shorter.
* Should not be used for complex conditions.

### Basic Syntax

```python
value = value_if_true if condition else value_if_false
```

---

## 11. Nested Loops

### What it is

A nested loop is a loop placed inside another loop.

### Important Points

* The inner loop runs completely for each iteration of the outer loop.
* Can be used with `for` and `while` loops.
* Commonly used for patterns, tables, and grids.
* Proper indentation is required.

### Basic Syntax

```python
for i in range(3):
    for j in range(3):
        # code
```
