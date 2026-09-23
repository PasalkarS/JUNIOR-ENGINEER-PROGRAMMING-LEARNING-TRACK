# 03 — Collections

## 1. Lists

### What it is

A list is an ordered and changeable collection used to store multiple values.

### Important Points

* Lists are created using `[]`.
* Lists can contain different data types.
* Lists allow duplicate values.
* List items can be changed, added, or removed.
* List items are accessed using an index.

### Basic Syntax

```python
fruits = ["apple", "banana", "orange"]
```

---

## 2. Tuples

### What it is

A tuple is an ordered collection that cannot be changed after it is created.

### Important Points

* Tuples are created using `()`.
* Tuples allow duplicate values.
* Tuple items can be accessed using an index.
* Tuples are immutable.
* Useful for values that should not be changed.

### Basic Syntax

```python
colors = ("red", "green", "blue")
```

---

## 3. Sets

### What it is

A set is an unordered collection that stores unique values.

### Important Points

* Sets are created using `{}`.
* Duplicate values are automatically removed.
* Sets do not use indexes.
* Sets can be changed after creation.
* Useful when unique values are required.

### Basic Syntax

```python
numbers = {1, 2, 3, 4}
```

---

## 4. Dictionaries

### What it is

A dictionary stores data as key-value pairs.

### Important Points

* Dictionaries are created using `{}`.
* Each value is accessed using its key.
* Keys must be unique.
* Values can be of different data types.
* Dictionaries can be changed after creation.

### Basic Syntax

```python
student = {
    "name": "Sam",
    "age": 25
}
```

---

## 5. Indexing

### What it is

Indexing is used to access an individual item from an ordered collection.

### Important Points

* Indexing starts from `0`.
* `0` represents the first item.
* Negative indexes can access items from the end.
* Lists, tuples, and strings support indexing.
* Dictionaries use keys instead of indexes.

### Basic Syntax

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])
```

---

## 6. Slicing

### What it is

Slicing is used to get a part of a sequence.

### Important Points

* Slicing uses `[start:stop]`.
* The `stop` index is not included.
* A step can also be provided.
* Lists, tuples, and strings support slicing.

### Basic Syntax

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])
```

---

## 7. Iteration

### What it is

Iteration means going through the items of a collection one by one.

### Important Points

* `for` loops are commonly used for iteration.
* Lists, tuples, sets, dictionaries, and strings can be iterated.
* Each iteration processes one item.
* Dictionaries can be iterated through keys, values, or key-value pairs.

### Basic Syntax

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

---

## 8. Nested Collections

### What it is

A nested collection is a collection stored inside another collection.

### Important Points

* A list can contain other lists.
* A dictionary can contain lists or other dictionaries.
* Nested collections are useful for representing structured data.
* Multiple levels of nesting are possible.

### Basic Syntax

```python
students = [
    ["Sam", 25],
    ["John", 22]
]
```

---

## 9. List Comprehensions

### What it is

A list comprehension is a short way to create a new list using a loop.

### Important Points

* It creates a list in a single line.
* It can include a condition.
* It is commonly used for simple transformations.
* It should be kept simple and readable.

### Basic Syntax

```python
numbers = [1, 2, 3, 4]

squares = [number * number for number in numbers]
```

---

## 10. Dictionary Comprehensions

### What it is

A dictionary comprehension is a short way to create a dictionary using an expression and a loop.

### Important Points

* Creates key-value pairs in a single line.
* Can include a condition.
* Useful for creating dictionaries from existing data.
* Uses `{key: value for item in collection}` syntax.

### Basic Syntax

```python
numbers = [1, 2, 3]

squares = {number: number * number for number in numbers}
```

---

## 11. Set Comprehensions

### What it is

A set comprehension is a short way to create a set using a loop.

### Important Points

* Creates a set in a single line.
* Duplicate values are automatically removed.
* Can include a condition.
* Uses `{expression for item in collection}` syntax.

### Basic Syntax

```python
numbers = [1, 2, 2, 3]

squares = {number * number for number in numbers}
```

---

## 12. Mutability

### What it is

Mutability means an object can be changed after it is created.

### Important Points

* Lists are mutable.
* Dictionaries are mutable.
* Sets are mutable.
* Mutable objects can be modified without creating a new object.
* Changes to a mutable object can affect other references to the same object.

### Basic Syntax

```python
numbers = [1, 2, 3]
numbers[0] = 10
```

---

## 13. Immutability

### What it is

Immutability means an object cannot be changed after it is created.

### Important Points

* Tuples are immutable.
* Strings are immutable.
* An immutable object cannot be modified directly.
* A new object must be created when a different value is needed.
* Immutability can help prevent accidental changes.

### Basic Syntax

```python
name = "Sam"
```

---

## 14. Copying

### What it is

Copying means creating another collection based on an existing collection.

### Important Points

* Assignment does not create a new copy.
* `copy()` can create a shallow copy of a collection.
* Changes to a shallow copy's top-level items do not affect the original.
* Nested objects can still be shared in a shallow copy.

### Basic Syntax

```python
numbers = [1, 2, 3]
new_numbers = numbers.copy()
```

---

## 15. Shallow Copy vs Deep Copy

### What it is

A shallow copy copies the outer collection, while a deep copy also copies nested objects.

### Important Points

* Shallow copy can be created using `copy.copy()` or `copy()`.
* Deep copy can be created using `copy.deepcopy()`.
* Shallow copies may share nested objects.
* Deep copies create separate nested objects.
* Deep copying is useful when nested data must be completely independent.

### Basic Syntax

```python
import copy

new_list = copy.copy(original_list)
deep_list = copy.deepcopy(original_list)
```

---

## 16. Choosing the Correct Collection

### What it is

Different collections are designed for different types of data and operations.

### Important Points

* **List** → ordered data that may need to change.
* **Tuple** → ordered data that should not change.
* **Set** → unique values and set operations.
* **Dictionary** → data that needs key-value access.
* Choose the collection based on how the data will be stored and used.

### Basic Syntax

```python
names = ["Sam", "John"]              # List
coordinates = (10, 20)              # Tuple
unique_numbers = {1, 2, 3}          # Set
student = {"name": "Sam", "age": 25} # Dictionary
```

---

## 17. Basic Time-Complexity Intuition

### What it is

Time complexity gives a basic idea of how the time required for an operation changes as the amount of data increases.

### Important Points

* Lists are generally fast for accessing an item by index: **O(1)**.
* Searching for an item in a list is generally **O(n)**.
* Sets are generally very fast for checking whether a value exists: **O(1)** on average.
* Dictionaries are generally very fast for key lookup: **O(1)** on average.
* `O(n)` means the work generally grows with the number of items.
* `O(1)` means the operation generally takes constant time regardless of collection size.
