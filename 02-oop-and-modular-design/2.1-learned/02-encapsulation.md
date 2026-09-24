# 02 — Encapsulation

## 1. Public Attributes

### What it is

Public attributes can be accessed directly from outside the class.

### Important Points

* Public attributes normally have no special naming convention.
* They can be read or changed directly.
* They are simple to use.
* Example: `student.name`

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Sam")

print(student.name)
student.name = "Alex"
```

---

## 2. Naming Conventions

### What it is

Naming conventions are rules used to make class attributes and methods easier to understand.

### Important Points

* Normal attributes use names like `name` or `age`.
* A single underscore `_name` indicates an internal/protected-style attribute.
* Double underscore `__name` triggers name mangling.
* Naming conventions communicate how an attribute is intended to be used.

### Basic Syntax

```python
class Student:
    def __init__(self):
        self.name = "Sam"
        self._age = 25
        self.__password = "1234"
```

---

## 3. Protected-Style Attributes

### What it is

An attribute beginning with `_` is treated as an internal or protected-style attribute by convention.

### Important Points

* Python does not strictly enforce protected access.
* `_name` tells other programmers that the attribute is intended for internal use.
* It can still be accessed from outside the class.
* It is commonly used when subclasses may need access.

### Basic Syntax

```python
class Student:
    def __init__(self):
        self._age = 25

student = Student()

print(student._age)
```

---

## 4. Private Name Mangling

### What it is

An attribute beginning with `__` uses Python's name-mangling mechanism to make direct accidental access harder.

### Important Points

* `__name` is changed internally by Python.
* It helps avoid accidental access or name conflicts.
* It is not true security or strict privacy.
* It is mainly useful for protecting internal implementation details.

### Basic Syntax

```python
class Student:
    def __init__(self):
        self.__age = 25

student = Student()
```

---

## 5. Properties

### What it is

A property allows a method to be accessed like an attribute.

### Important Points

* Properties are created using `@property`.
* They allow controlled access to object data.
* Validation can be added before returning or changing values.
* They help keep the class interface simple.

### Basic Syntax

```python
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

---

## 6. Getters and Setters

### What it is

Getters are used to read values, while setters are used to change values in a controlled way.

### Important Points

* A getter returns an attribute value.
* A setter changes an attribute value.
* Setters can validate new values.
* In Python, properties are commonly used for getters and setters.

### Basic Syntax

```python
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

---

## 7. Validation

### What it is

Validation checks whether a value is valid before storing it in an object.

### Important Points

* Validation can be performed inside setters.
* Invalid values can raise exceptions.
* It prevents objects from containing incorrect data.
* Validation rules should match the requirements of the class.

### Basic Syntax

```python
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

---

## 8. Controlling Object State

### What it is

Controlling object state means deciding how an object's data can be read or changed.

### Important Points

* Do not allow invalid values into important attributes.
* Use properties when controlled access is needed.
* Use validation before changing object data.
* Internal attributes can be hidden behind methods or properties.
* Encapsulation keeps an object's data and rules together.

### Basic Syntax

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
```
