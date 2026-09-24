# 06 — Design Principles

## 1. Single Responsibility Principle (SRP)

### What it is

A class or function should have one main responsibility or one clear job.

### Important Points

* Keep each class focused on one task.
* Avoid putting unrelated functionality together.
* Smaller responsibilities make code easier to understand.
* Makes testing and maintenance easier.

---

## 2. Open/Closed Principle (OCP)

### What it is

Code should be open for adding new functionality but should not need frequent changes to existing working code.

### Important Points

* New features should be easy to add.
* Avoid changing the same code repeatedly for new requirements.
* Separate different behaviors when possible.
* Helps reduce the chance of breaking existing functionality.

---

## 3. Liskov Substitution Principle (LSP)

### What it is

A child class should be able to replace its parent class without causing unexpected problems.

### Important Points

* Use inheritance only when the relationship makes sense.
* Child classes should follow the expected behavior of the parent.
* A child class should not remove important behavior expected from the parent.
* If inheritance does not fit, composition may be a better choice.

---

## 4. Interface Segregation Principle (ISP)

### What it is

A class should not be forced to depend on methods or functionality that it does not need.

### Important Points

* Keep interfaces small and focused.
* Group related functionality together.
* Avoid creating one large interface for unrelated operations.
* Classes should use only the functionality they actually need.

---

## 5. Dependency Inversion Principle (DIP)

### What it is

High-level code should depend on general interfaces or abstractions instead of directly depending on specific implementations.

### Important Points

* Avoid tightly connecting classes.
* Pass dependencies into classes when possible.
* Different implementations should be replaceable.
* Makes code easier to change and test.

---

## 6. DRY — Don't Repeat Yourself

### What it is

DRY means avoiding unnecessary repetition of the same code or logic.

### Important Points

* Put repeated logic into reusable functions or classes.
* Avoid copying the same code into multiple places.
* Changes become easier when logic exists in one place.
* Do not remove every small repetition if doing so makes the code more complicated.

---

## 7. KISS — Keep It Simple

### What it is

KISS means keeping code as simple as possible while still solving the problem correctly.

### Important Points

* Prefer simple solutions over unnecessary complexity.
* Use clear names for variables, functions, and classes.
* Avoid features that are not required.
* Simple code is easier to understand and maintain.

---

## 8. Separation of Concerns

### What it is

Separation of concerns means keeping different responsibilities in separate parts of a program.

### Important Points

* Keep user-interface logic separate from business logic.
* Keep database or file operations separate from business logic.
* Use different functions, classes, or modules for different responsibilities.
* Makes code easier to understand, test, and modify.
