# 07 — Standard Library

## 1. `math`

### What it is

The `math` module provides mathematical functions and constants for common calculations.

### Important Points

* Use `import math` to use the module.
* Provides functions like `sqrt()`, `ceil()`, and `floor()`.
* Provides constants such as `pi`.
* Useful for mathematical calculations.

### Basic Syntax

```python
import math

print(math.sqrt(25))
print(math.pi)
```

---

## 2. `statistics`

### What it is

The `statistics` module provides functions for working with numerical data.

### Important Points

* Use `import statistics`.
* `mean()` calculates the average.
* `median()` finds the middle value.
* `mode()` finds the most common value.
* Useful for basic data analysis.

### Basic Syntax

```python
import statistics

numbers = [10, 20, 30, 40, 50]

print(statistics.mean(numbers))
print(statistics.median(numbers))
```

---

## 3. `datetime`

### What it is

The `datetime` module is used to work with dates and times.

### Important Points

* Can get the current date and time.
* Can create specific dates and times.
* Supports date and time calculations.
* Useful for timestamps and scheduling.

### Basic Syntax

```python
from datetime import datetime

now = datetime.now()

print(now)
```

---

## 4. `pathlib`

### What it is

The `pathlib` module provides an easy way to work with files and folder paths.

### Important Points

* Use `Path` to create and work with paths.
* Works with files and directories.
* Can check whether a path exists.
* Can create, rename, and remove paths.
* Often easier to use than manually building path strings.

### Basic Syntax

```python
from pathlib import Path

file_path = Path("data.txt")

print(file_path.exists())
```

---

## 5. `os`

### What it is

The `os` module allows Python to interact with the operating system.

### Important Points

* Can work with files and directories.
* Can get environment variables.
* Can get the current working directory.
* Provides operating-system-related functions.
* `pathlib` is often preferred for modern path handling.

### Basic Syntax

```python
import os

print(os.getcwd())
```

---

## 6. `sys`

### What it is

The `sys` module provides access to Python interpreter and system-related information.

### Important Points

* Can access command-line arguments.
* Provides information about the Python environment.
* `sys.argv` contains command-line arguments.
* `sys.exit()` can stop a program.

### Basic Syntax

```python
import sys

print(sys.version)
```

---

## 7. `json`

### What it is

The `json` module is used to work with JSON data.

### Important Points

* JSON is commonly used for storing and exchanging data.
* `json.loads()` converts JSON text into Python data.
* `json.dumps()` converts Python data into JSON text.
* JSON commonly uses objects, arrays, strings, numbers, and booleans.
* JSON files can also be read and written.

### Basic Syntax

```python
import json

data = {"name": "Sam", "age": 25}

json_data = json.dumps(data)

print(json_data)
```

---

## 8. `csv`

### What it is

The `csv` module is used to read and write CSV files.

### Important Points

* CSV stores data in rows and columns.
* Values are commonly separated by commas.
* `csv.reader()` reads CSV data.
* `csv.writer()` writes CSV data.
* Useful for simple tabular data.

### Basic Syntax

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## 9. `collections`

### What it is

The `collections` module provides specialized data structures that extend Python's basic collections.

### Important Points

* `Counter` counts items.
* `defaultdict` provides default values for missing keys.
* `deque` provides an efficient double-ended queue.
* These tools are useful when normal lists or dictionaries are not enough.

### Basic Syntax

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

count = Counter(numbers)

print(count)
```

---

## 10. `random`

### What it is

The `random` module is used to generate pseudo-random values.

### Important Points

* `random.randint()` generates a random integer in a range.
* `random.choice()` selects a random item.
* `random.shuffle()` changes the order of a list.
* Useful for simulations, games, and testing.
* It is not suitable for security-sensitive random values.

### Basic Syntax

```python
import random

number = random.randint(1, 10)

print(number)
```
