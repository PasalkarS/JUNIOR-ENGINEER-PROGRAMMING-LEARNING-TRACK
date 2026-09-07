# Python Fundamentals — My Study Notes

These are my personal takeaway notes as I went through the core mechanics of Python. No academic textbook jargon, just how things actually behave under the hood.

---

## 1. Variables & Data Types

In Python, a variable isn't a "box" holding data—it's a **name tag** pointing to an object in memory.

```python
x = [1, 2, 3]
y = x          # y points to the exact same list in memory!
y.append(4)
print(x)       # [1, 2, 3, 4] — x changed too because both pointed to the same object.
```

### Mutability Rule of Thumb
- **Immutable** (cannot change in place): `int`, `float`, `str`, `bool`, `tuple`. When you "modify" a string, Python actually creates a brand-new string behind the scenes.
- **Mutable** (can be updated in place): `list`, `dict`, `set`. Be careful passing lists or dicts as default arguments in functions—they persist across function calls!

```python
# The classic default arg trap:
def add_item(item, basket=[]):   # BAD: basket is created once at definition time
    basket.append(item)
    return basket

# Correct way:
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
```

---

## 2. Expressions vs. Statements

It took me a second to separate these cleanly:

- **Expression**: Anything that evaluates to a value.
  - `5 + 10` evaluates to `15`
  - `"hello".upper()` evaluates to `"HELLO"`
  - `x > 0 and y < 10` evaluates to a boolean
- **Statement**: An instruction that does something or controls flow, but doesn't produce a value you can assign.
  - `if x > 5:`, `for item in items:`, `import math`, `return value`

Why this matters: You can only pass expressions where a value is expected (like function arguments, list comprehensions, or inside f-strings).

---

## 3. Imports & Modules

When Python sees `import foo`:
1. It checks `sys.modules` to see if `foo` was already imported (cached).
2. If not, it searches the directories in `sys.path` (starting with the current working directory, then the standard library, then installed virtualenv packages).
3. It compiles and executes `foo.py` from top to bottom once, creating its namespace.

### Best Practices I'm Sticking To:
- Use absolute imports over relative imports when possible.
- Avoid wildcard imports (`from math import *`) because they pollute the namespace and make it impossible to tell where a function came from.
- Guard runnable code with `if __name__ == "__main__":` so that importing the file as a module doesn't accidentally execute interactive loops or CLI logic.

---

## 4. Execution Flow & Error Handling

Python executes code top-to-bottom, line-by-line, until it encounters a control flow statement or an exception:

1. **Branching (`if` / `elif` / `else`)**: Evaluates truthiness lazily. In `A and B`, if `A` is false, Python never even evaluates `B`.
2. **Loops (`for` / `while`)**: `for` iterates over iterables (generators, lists, dict keys). `break` exits the loop; `continue` skips to the next iteration. Python also has `for ... else` which runs only if the loop finished *without* hitting a `break`.
3. **Exception Handling**:
   - `try`: Code that might fail. Keep this block as small as possible.
   - `except SpecificError as e`: Always catch specific exceptions (never bare `except:`).
   - `else`: Runs only if *no* exception occurred in `try`.
   - `finally`: Always runs (great for closing files, sockets, or database connections).

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("data.txt does not exist!")
except PermissionError:
    print("No permission to read data.txt.")
else:
    print(f"Read {len(content)} characters successfully.")
```
