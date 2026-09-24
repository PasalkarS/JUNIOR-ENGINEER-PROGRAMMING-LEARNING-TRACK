# 03 — Inheritance and Composition

## 1. Inheritance

### What it is

Inheritance allows one class to reuse attributes and methods from another class.

### Important Points

* The existing class is called the parent/base class.
* The new class is called the child/derived class.
* A child class can add its own features.
* It helps reduce duplicate code.

### Basic Syntax

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


dog = Dog()
dog.eat()
```

---

## 2. Parent and Child Classes

### What it is

A parent class contains common functionality, while a child class can inherit and extend it.

### Important Points

* Parent classes provide reusable behavior.
* Child classes inherit from the parent.
* A child can have additional attributes and methods.
* A child can also change inherited behavior.

### Basic Syntax

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")
```

---

## 3. Method Overriding

### What it is

Method overriding means a child class provides its own version of a method inherited from the parent.

### Important Points

* The child uses the same method name as the parent.
* The child's method replaces the inherited version when called on the child object.
* It allows different classes to behave differently.
* Overriding is commonly used with polymorphism.

### Basic Syntax

```python
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()
```

---

## 4. `super()`

### What it is

`super()` is used to access methods or functionality from the parent class.

### Important Points

* It is commonly used inside child classes.
* `super().__init__()` calls the parent's constructor.
* It avoids directly writing the parent class name.
* It is useful when extending parent behavior.

### Basic Syntax

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

## 5. Polymorphism

### What it is

Polymorphism means different objects can use the same method name but provide different behavior.

### Important Points

* The same method can work differently for different objects.
* It allows code to work with different object types.
* Method overriding is one common way to achieve polymorphism.
* It makes code more flexible.

### Basic Syntax

```python
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()
```

---

## 6. Composition

### What it is

Composition means creating a class that contains an object of another class.

### Important Points

* It represents a **has-a** relationship.
* One object uses another object to perform a task.
* Components are usually created and managed by the containing object.
* It helps build larger objects from smaller classes.

### Basic Syntax

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

---

## 7. Aggregation

### What it is

Aggregation is a **has-a** relationship where one object uses another object that can exist independently.

### Important Points

* The objects have separate lifecycles.
* The contained object can exist without the containing object.
* Objects can be shared between different objects.
* It is a weaker relationship than composition.

### Basic Syntax

```python
class Teacher:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Sam")
school = School(teacher)
```

---

## 8. Inheritance vs Composition

### What it is

Inheritance represents an **is-a** relationship, while composition represents a **has-a** relationship.

### Important Points

* **Inheritance:** a child class is a type of parent class.
* **Composition:** a class contains or uses another object.
* Inheritance focuses on reusing and extending class behavior.
* Composition focuses on combining objects.
* Composition often provides more flexibility when components may change independently.

### Basic Syntax

```python
# Inheritance: Dog is an Animal

class Animal:
    pass

class Dog(Animal):
    pass


# Composition: Car has an Engine

class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
```
