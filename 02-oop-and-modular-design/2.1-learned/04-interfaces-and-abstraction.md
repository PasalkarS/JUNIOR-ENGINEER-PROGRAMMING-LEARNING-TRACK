# 04 — Interfaces and Abstraction

## 1. Abstraction

### What it is

Abstraction means hiding unnecessary implementation details and showing only the important parts of an object.

### Important Points

* Focuses on **what** an object does instead of **how** it does it.
* Reduces unnecessary complexity.
* Makes code easier to understand.
* Abstract classes can be used to define common behavior.

---

## 2. Abstract Base Classes

### What it is

An abstract base class (ABC) is a class designed to be inherited by other classes.

### Important Points

* Python provides ABCs through the `abc` module.
* An abstract class cannot normally be instantiated directly.
* It can define methods that child classes must implement.
* ABCs provide a common structure for related classes.

### Basic Syntax

```python id="h5q1xj"
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

---

## 3. `abc`

### What it is

`abc` is a Python standard-library module used to create abstract base classes.

### Important Points

* `ABC` is used as a base class.
* `abstractmethod` marks a method as required.
* A class can contain both normal and abstract methods.
* It helps enforce a common design between classes.

### Basic Syntax

```python id="j9m5cz"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

## 4. Abstract Methods

### What it is

An abstract method is a method that child classes are expected to implement.

### Important Points

* It is marked using `@abstractmethod`.
* The abstract class does not provide the required implementation.
* A concrete child class must implement it.
* Objects cannot normally be created from a class with unimplemented abstract methods.

### Basic Syntax

```python id="p0j8xw"
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()
```

---

## 5. Interfaces as a Design Concept

### What it is

An interface is a design idea that defines what operations a class should provide without focusing on their implementation.

### Important Points

* It defines a common set of methods.
* Different classes can implement those methods differently.
* Python does not have a separate `interface` keyword like some languages.
* Abstract base classes can be used to create interface-like designs.

### Basic Syntax

```python id="l5gq6h"
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

---

## 6. Polymorphic Implementations

### What it is

Polymorphic implementations allow different classes to implement the same interface or abstract method in their own way.

### Important Points

* Different classes can use the same method name.
* Each class can provide different behavior.
* Code can work with the common interface instead of specific classes.
* This makes code easier to extend.

### Basic Syntax

```python id="wq5t9x"
class CardPayment:
    def pay(self, amount):
        print("Paid by card:", amount)


class CashPayment:
    def pay(self, amount):
        print("Paid by cash:", amount)


payments = [CardPayment(), CashPayment()]

for payment in payments:
    payment.pay(100)
```

---

## 7. Dependency Inversion

### What it is

Dependency inversion means high-level code should depend on an abstract interface rather than directly depending on a specific implementation.

### Important Points

* Avoid tightly connecting one class to one specific implementation.
* Depend on a common interface or abstract class.
* Different implementations can be replaced easily.
* This makes code more flexible and easier to maintain.

### Basic Syntax

```python id="m8k2pc"
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)


class App:
    def __init__(self, notification):
        self.notification = notification

    def notify(self):
        self.notification.send("Hello")


app = App(EmailNotification())
app.notify()
```

