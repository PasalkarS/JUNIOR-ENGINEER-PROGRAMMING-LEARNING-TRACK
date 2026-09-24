# 01 — Classes and Objects

## 1. Classes

### What it is

A class is a blueprint used to create objects.
It defines the data and behavior that objects can have.

### Important Points

* Classes are created using the `class` keyword.
* A class can contain attributes and methods.
* One class can create many objects.
* Class names usually use `PascalCase`.

### Basic Syntax

```python
class Student:
    pass
```

---

## 2. Objects

### What it is

An object is an instance of a class.
It is created from the class blueprint.

### Important Points

* Objects are created by calling a class.
* Each object can have its own data.
* Multiple objects can be created from one class.
* Objects can access the class's methods and attributes.

### Basic Syntax

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

---

## 3. Attributes

### What it is

Attributes are variables that store data related to an object or class.

### Important Points

* Attributes describe an object's data.
* They are accessed using the `.` operator.
* Attributes can belong to an object or to the class.
* Example attributes can be `name`, `age`, or `salary`.

### Basic Syntax

```python
student.name = "Sam"

print(student.name)
```

---

## 4. Methods

### What it is

A method is a function defined inside a class.
It usually performs an action related to an object.

### Important Points

* Methods are defined inside a class.
* Instance methods normally use `self`.
* Methods can access object attributes.
* Methods are called using the object.

### Basic Syntax

```python
class Student:
    def greet(self):
        print("Hello")

student = Student()
student.greet()
```

---

## 5. Constructors

### What it is

A constructor is used to initialize an object when it is created.

### Important Points

* Python commonly uses `__init__()` for initialization.
* It runs automatically when an object is created.
* It can receive values from the object creation.
* It is commonly used to set initial attributes.

---

## 6. `__init__`

### What it is

`__init__()` is a special method that runs automatically when a new object is created.

### Important Points

* It is used to initialize object data.
* It normally takes `self` as the first parameter.
* Other parameters can be used to receive values.
* It is called automatically when creating the object.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Sam")

print(student.name)
```

---

## 7. Instance Attributes

### What it is

Instance attributes are attributes that belong to a specific object.

### Important Points

* They are usually created using `self`.
* Different objects can have different values.
* They are commonly initialized inside `__init__()`.
* Each object has its own instance attributes.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Sam")
student2 = Student("Alex")

print(student1.name)
print(student2.name)
```

---

## 8. Class Attributes

### What it is

A class attribute belongs to the class and is shared by objects unless an object provides its own value.

### Important Points

* It is defined inside the class but outside methods.
* It is shared by instances.
* It can be accessed using the class name.
* It is useful for values common to all objects.

### Basic Syntax

```python
class Student:
    school = "ABC School"

student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)
```

---

## 9. Instance Methods

### What it is

An instance method is a method that works with a particular object.

### Important Points

* The first parameter is normally `self`.
* `self` refers to the current object.
* Instance methods can access instance attributes.
* They are called using an object.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

student = Student("Sam")
student.greet()
```

---

## 10. `self`

### What it is

`self` refers to the current object inside an instance method.

### Important Points

* It allows a method to access object attributes.
* It is normally the first parameter of an instance method.
* `self.name` refers to the current object's `name`.
* Python passes the object automatically when the method is called.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
```

---

## 11. Object Lifecycle

### What it is

The object lifecycle describes what happens from creating an object to when it is no longer used.

### Important Points

* An object is created from a class.
* `__init__()` initializes the object.
* The object can be used by calling its methods.
* Python manages object memory automatically.
* An object is removed when it is no longer needed and can be garbage-collected.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Sam")
student.show_name()
```

---

## 12. `__str__`

### What it is

`__str__()` defines the readable string representation of an object.

### Important Points

* It is called when `str()` is used.
* It is also used by `print()`.
* It should return a string.
* It is mainly intended for a user-friendly representation.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

student = Student("Sam")

print(student)
```

---

## 13. `__repr__`

### What it is

`__repr__()` defines a more detailed representation of an object, mainly useful for developers and debugging.

### Important Points

* It is called by `repr()`.
* It should return a string.
* It is useful when inspecting objects.
* A class can define both `__str__()` and `__repr__()`.

### Basic Syntax

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name='{self.name}')"

student = Student("Sam")

print(repr(student))
```
