# Inheritance, Polymorphism, and Composition

> **Module 02: OOP and Modular Design | Topic 03**



## 1. Learning Outcomes

- **Inheritance Hierarchy:** Derive subclasses using `super().__init__()` properly.
- **Polymorphism:** Write client code that works across multiple interchangeable subclasses.
- **Composition over Inheritance:** Favor 'has-a' delegation over rigid 'is-a' inheritance.
- **LSP Adherence:** Ensure derived classes honor contracts established by parent classes.

## 2. Comparison: Is-A vs Has-A


| Relationship | Pattern | Example | When to Use |
| --- | --- | --- | --- |
| Is-A (Inheritance) | Subclass extends base class | CheckingAccount is a BankAccount | Strict behavioral subtype; shared core mechanism |
| Has-A (Composition) | Class holds instance of another | Order has an Invoice and Payment | Flexible assembly, modular swapping, loose coupling |



## 3. Key Syntax

```python
# Composition example: PaymentProcessor delegates to a gateway
class StripeGateway:
    def charge(self, amount: float) -> bool:
        return True

class CheckoutService:
    def __init__(self, gateway):
        self.gateway = gateway  # Composition: injected dependency

    def checkout(self, amount: float):
        return self.gateway.charge(amount)
```


## 4. Common Mistakes & Gotchas

- **Deep Inheritance Trees:** Hierarchy trees with 4+ levels create brittle code. Flatten using composition.
- **Forgetting super():** Overriding `__init__` without calling `super().__init__(...)` leaves base class attributes uninitialized.

## 5. Practice Tasks & Self-Check

- **Task 1:** Implement an alert notification system using composition: NotificationService holds a list of delivery channels (Email, SMS).
- **Q1:** Why is composition generally considered more maintainable than multiple inheritance?
