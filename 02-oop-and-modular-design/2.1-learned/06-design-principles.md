# Software Design Principles (SOLID, DRY, KISS)

> **Module 02: OOP and Modular Design | Topic 06**



## 1. Learning Outcomes

- **Single Responsibility:** Ensure every class has only one reason to change.
- **Open / Closed:** Design systems open for extension but closed for modification.
- **Dependency Inversion:** Inject dependencies rather than instantiating hardcoded concrete classes.
- **KISS & DRY:** Keep solutions simple and eliminate duplicate logic systematically.

## 2. SOLID Principles in Practice


| Principle | Meaning | Bad Example vs Improved Example |
| --- | --- | --- |
| SRP | Single Responsibility | Bad: Order class saves to CSV and sends emails. Good: Order holds state; OrderRepository saves; Mailer sends. |
| OCP | Open/Closed | Bad: if/elif checks for every new payment type. Good: Polymorphic PaymentMethod interface. |
| LSP | Liskov Substitution | Bad: Subclass throws NotImplementedError. Good: Subclass fulfills parent contract. |
| ISP | Interface Segregation | Bad: Huge interface with 20 methods. Good: Small focused interfaces. |
| DIP | Dependency Inversion | Bad: Service hardcodes `self.repo = SqlRepo()`. Good: Pass repo into `__init__`. |



## 3. Code Example: Dependency Inversion

```python
class OrderService:
    # Good: Dependency Injection allows swapping storage without touching this service!
    def __init__(self, repository, notification_service):
        self.repository = repository
        self.notification_service = notification_service

    def place_order(self, order):
        self.repository.save(order)
        self.notification_service.notify(order)
```


## 4. Practice Tasks & Self-Check

- **Task 1:** Take an all-in-one UserManager class and decompose it into User model, PasswordHasher, and UserRepository.
- **Q1:** What is the primary danger of violating the Single Responsibility Principle?
