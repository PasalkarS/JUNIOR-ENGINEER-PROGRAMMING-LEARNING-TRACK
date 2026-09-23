# Encapsulation & State Validation

> **Module 02: OOP and Modular Design | Topic 02**



## 1. Learning Outcomes

- **Data Protection:** Protect internal object state from illegal direct modifications.
- **Properties:** Use `@property` and `@setter` to provide clean validation.
- **Conventions:** Understand protected (`_single_underscore`) vs private (`__double_underscore`) naming.
- **Invariants:** Maintain domain rules across the entire lifecycle of an object.

## 2. Key Syntax & Concepts

```python
class Employee:
    def __init__(self, emp_id: str, salary: float):
        self.emp_id = emp_id
        self._salary = salary  # Internal state

    @property
    def salary(self) -> float:
        """Getter method for salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Setter method enforcing business validation."""
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self._salary = value
```


## 3. Common Mistakes & Gotchas

- **Overusing Double Underscores:** `__name` invokes Python name mangling (`_Class__name`). In Python, single underscore `_name` is standard convention for internal attributes.
- **Infinite Recursion in Setter:** Assigning `self.salary = value` inside `salary.setter` causes infinite recursion. Always assign to `self._salary`.

## 4. Practice Tasks & Self-Check

- **Task 1:** Create a Product entity with a validated `price` (> 0) and `discount` (0-100%).
- **Q1:** Why are Python properties preferred over Java-style `getSalary()` and `setSalary()`?
