# Strings, Text Parsing, and File I/O

> **Module 01: Python Fundamentals | Topic 05**



## 1. Learning Outcomes

- **String Manipulation:** Clean, slice, strip, split, and reformat text strings reliably.
- **Context Managers:** Use `with open(...)` to prevent file resource leaks.
- **CSV Processing:** Read and write structured tabular data with the built-in `csv` module.
- **Pathlib:** Manipulate cross-platform file paths cleanly using `pathlib.Path`.

## 2. Key Syntax & Methods


### String Operations

```python
raw_record = '  AAPL, Apple Inc, 185.50 \n'
clean = raw_record.strip()           # 'AAPL, Apple Inc, 185.50'
parts = [p.strip() for p in clean.split(',')]  # ['AAPL', 'Apple Inc', '185.50']
joined = ' | '.join(parts)           # 'AAPL | Apple Inc | 185.50'
```


### Safe File Handling with `with open`

```python
from pathlib import Path

file_path = Path('data') / 'sample.txt'

# Writing safely
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('Line 1\nLine 2\n')

# Reading line by line (memory efficient)
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
```


### CSV Module Essentials

```python
import csv

# Reading as dictionaries
with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['role'])
```


## 3. Common Mistakes & Gotchas

- **Forgetting encoding='utf-8':** On Windows, default encoding can be cp1252, causing UnicodeDecodeError. Always specify encoding='utf-8'.
- **Opening Without Context Manager:** Using `f = open()` without `.close()` locks files in memory and risks corruption.

## 4. Practice Tasks & Self-Check

- **Task 1:** Build a log file parser that reads an Apache/Nginx-style log and counts HTTP status codes (200, 404, 500).
- **Q1:** Why is `with open(...)` preferred over `open()` and `close()`?
