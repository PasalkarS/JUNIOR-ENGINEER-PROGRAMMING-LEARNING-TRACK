# 02. OOP & Modular Design

Object-oriented programming principles, class architecture, encapsulation, inheritance, and clean module separation.

## Progress
- [x] Learned
- [x] Project Ready
- [x] Independent

---

## Module Levels Breakdown

1. **[Learned](learned/order_management_basic.py)**: Basic class definitions for `Customer`, `Product`, `OrderItem`, `Order`, and `Invoice` demonstrating constructors, object references, and string representations.
2. **[Project Ready](project_ready/order_management_encapsulated.py)**: Added defensive encapsulation with properties, state machine validation (`DRAFT` → `CONFIRMED` → `PAID` → `SHIPPED`), price/email constraints, and defensive copying of order items.
3. **[Independent](independent/)**: Refactored into a full layered architecture (`domain/`, `repositories/`, `services/`) featuring an abstract `OrderRepository` interface with `InMemoryOrderRepository` and `JsonFileOrderRepository` implementations, fully tested with pytest.

---

## Composition vs. Inheritance Choices

- **Composition ("Has-A")**:
  - `Order` aggregates `OrderItem`s and associates with `Customer`. An order is not a customer, so inheritance would lead to bloated, coupled classes.
  - `Invoice` references an `Order` rather than subclassing it, preventing inappropriate mutations to the underlying order through the invoice handle.
  - `OrderService` accepts an abstract `OrderRepository` via dependency injection. Composing the service with its repository allows swapping persistence layers (memory vs. disk vs. database) with zero changes to business logic.
- **Inheritance ("Is-A")**:
  - Reserved strictly for polymorphic interfaces (`OrderRepository(ABC)`) and exception hierarchies (`DomainException` → `ValidationError`, `InvalidOrderStateError`).
- **Rule of Thumb**: Favor composition for flexibility and loose coupling; use inheritance strictly for behavior contracts and taxonomies.
