# Classes, Objects, and Instance Mechanics

> **Module 02: OOP and Modular Design | Topic 01**



## 1. Learning Outcomes

- **Object Modeling:** Define classes that represent real-world entities cleanly.
- **Constructors & Self:** Use `__init__` and understand `self` as the instance reference.
- **Class vs Instance State:** Distinguish shared class variables from instance-specific fields.
- **Dunder Representation:** Implement `__str__` for humans and `__repr__` for debugging.

## 2. Key Syntax & Concepts


### Defining a Class and State

```python
class BankAccount:
    # Class attribute (shared by all instances)
    BANK_CODE = 'CORP_01'

    def __init__(self, account_id: str, holder_name: str, balance: float = 0.0):
        # Instance attributes (unique to each object)
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def __str__(self) -> str:
        return f'Account {self.account_id} ({self.holder_name}): ${self.balance:.2f}'

    def __repr__(self) -> str:
        return f'BankAccount(id={self.account_id!r}, balance={self.balance})'
```


## 3. Common Mistakes & Gotchas

- **Mutable Class Attributes Bug:** Defining a list as a class attribute (`items = []` at class level) shares that single list across EVERY instance created!
- **Missing self:** Forgetting `self.` when assigning inside `__init__` creates a temporary local variable that vanishes upon exit.

## 4. Practice Tasks & Self-Check

- **Task 1:** Create an Item class with SKU, name, unit_price, and a method to calculate total price given quantity.
- **Q1:** When is __repr__ invoked versus __str__?
