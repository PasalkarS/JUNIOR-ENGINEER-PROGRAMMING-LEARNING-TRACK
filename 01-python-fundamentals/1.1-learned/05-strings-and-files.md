# 05 — Strings and Files

## 1. String Indexing

### What it is

String indexing is used to access individual characters from a string.

### Important Points

* Indexing starts from `0`.
* The first character has index `0`.
* Negative indexing starts from the end.
* Strings are immutable, so individual characters cannot be changed directly.

### Basic Syntax

```python
text = "Python"

print(text[0])
print(text[-1])
```

---

## 2. String Slicing

### What it is

Slicing is used to get a part of a string.

### Important Points

* Slicing uses `[start:stop]`.
* The `stop` index is not included.
* A step can also be provided.
* Slicing does not change the original string.

### Basic Syntax

```python
text = "Python"

print(text[0:3])
print(text[::2])
```

---

## 3. String Methods

### What it is

String methods are built-in functions used to work with strings.

### Important Points

* Methods are called using `.`.
* Common methods include `upper()`, `lower()`, `strip()`, and `replace()`.
* Most string methods return a new string.
* Strings themselves are not changed.

### Basic Syntax

```python
text = "hello"

print(text.upper())
print(text.lower())
```

---

## 4. String Formatting

### What it is

String formatting is used to insert values into text in a readable way.

### Important Points

* It makes output easier to create and read.
* Python supports different formatting methods.
* F-strings are the commonly used modern approach.
* Values can be inserted directly into strings.

### Basic Syntax

```python
name = "Sam"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

---

## 5. F-Strings

### What it is

F-strings allow variables and expressions to be placed directly inside a string.

### Important Points

* Start the string with `f`.
* Variables are written inside `{}`.
* Expressions can also be used inside `{}`.
* F-strings are simple and readable.

### Basic Syntax

```python
name = "Sam"
age = 25

message = f"{name} is {age} years old."
print(message)
```

---

## 6. Splitting

### What it is

`split()` divides a string into smaller parts and returns them as a list.

### Important Points

* By default, it splits using whitespace.
* A specific separator can be provided.
* The result is a list.
* It is useful for processing text.

### Basic Syntax

```python
text = "apple,banana,orange"

items = text.split(",")
print(items)
```

---

## 7. Joining

### What it is

`join()` combines multiple strings into one string.

### Important Points

* It is called on the separator string.
* The values being joined should be strings.
* It is commonly used with lists.
* It is useful for creating formatted text.

### Basic Syntax

```python
items = ["apple", "banana", "orange"]

text = ", ".join(items)
print(text)
```

---

## 8. Searching

### What it is

Searching is used to check whether specific text exists inside a string.

### Important Points

* The `in` operator checks if text exists.
* `find()` returns the position of matching text.
* `find()` returns `-1` when the text is not found.
* Searching is case-sensitive.

### Basic Syntax

```python
text = "Hello Python"

print("Python" in text)
print(text.find("Python"))
```

---

## 9. Replacing

### What it is

`replace()` is used to replace one part of a string with another.

### Important Points

* It returns a new string.
* The original string remains unchanged.
* It can replace one or multiple occurrences.
* It is useful for cleaning or modifying text.

### Basic Syntax

```python
text = "I like Java"

new_text = text.replace("Java", "Python")
print(new_text)
```

---

## 10. Stripping

### What it is

Stripping removes unwanted characters, usually spaces, from the beginning and end of a string.

### Important Points

* `strip()` removes characters from both sides.
* `lstrip()` removes from the left.
* `rstrip()` removes from the right.
* It is commonly used when cleaning user input.

### Basic Syntax

```python
text = "  Hello Python  "

print(text.strip())
```

---

## 11. Parsing Text

### What it is

Parsing text means breaking text into useful pieces so a program can process it.

### Important Points

* `split()` can separate text into parts.
* String methods can clean the data.
* Parsed values can be converted to other types.
* Parsing is commonly used when processing files or user input.

### Basic Syntax

```python
text = "Sam,25,Pune"

data = text.split(",")

name = data[0]
age = int(data[1])
city = data[2]
```

---

## 12. Reading Files

### What it is

Reading a file means opening a file and getting its contents into a Python program.

### Important Points

* Use `open()` to open a file.
* `"r"` means read mode.
* `read()` reads the file contents.
* `readline()` reads one line.
* `readlines()` reads lines into a list.

### Basic Syntax

```python
file = open("data.txt", "r")

content = file.read()
print(content)

file.close()
```

---

## 13. Writing Files

### What it is

Writing a file means storing text or other information in a file.

### Important Points

* `"w"` opens a file in write mode.
* Write mode can overwrite existing content.
* `write()` adds text to the file.
* `"a"` can be used to append content.
* The file should be properly closed after use.

### Basic Syntax

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

---

## 14. `with open(...)`

### What it is

`with open(...)` is the recommended way to work with files because Python automatically closes the file.

### Important Points

* It creates a file context.
* The file is automatically closed after the block.
* It reduces the chance of leaving files open.
* It can be used for both reading and writing.

### Basic Syntax

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 15. File Paths

### What it is

A file path tells Python where a file or folder is located.

### Important Points

* A relative path starts from the current working directory.
* An absolute path gives the complete location.
* Use `/` or `pathlib` for working with paths.
* Avoid hard-coding paths when possible.

### Basic Syntax

```python
from pathlib import Path

file_path = Path("data") / "data.txt"

print(file_path)
```

---

## 16. Text Files

### What it is

A text file stores information as readable characters.

### Important Points

* Common text files include `.txt`, `.log`, and `.csv`.
* Text files contain characters and lines.
* Python can read and write text files.
* Encoding such as UTF-8 can be specified.

### Basic Syntax

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

---

## 17. CSV Basics

### What it is

CSV stands for **Comma-Separated Values**. It is a simple format used to store tabular data.

### Important Points

* Data is usually organized into rows and columns.
* Each row represents a record.
* Commas commonly separate values.
* The first row often contains column names.
* Python provides the `csv` module for working with CSV files.

### Basic Syntax

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```
