# Layered Order Management System — Independent Level

This module demonstrates a production-grade, layered architecture refactor of our Order Management domain. It isolates business rules from infrastructure and persistence using domain-driven design principles, dependency inversion, and the repository pattern.

---

## Architecture Overview

```
independent/
├── domain/                  # Core Business Domain (Zero External Dependencies)
│   ├── models.py            # Customer, Product, OrderItem, Order, Invoice
│   └── exceptions.py        # Domain-specific hierarchy (ValidationError, InvalidOrderStateError)
├── repositories/            # Data Access & Storage Layer
│   ├── base.py              # Abstract OrderRepository contract (ABC)
│   ├── memory.py            # InMemoryOrderRepository (ephemeral / fast test fixtures)
│   └── file.py              # JsonFileOrderRepository (disk persistence with atomic file writes)
├── services/                # Application Orchestration Layer
│   └── order_service.py     # OrderService coordinates workflow via OrderRepository
├── tests/                   # Automated Pytest Suite
│   └── test_layered_architecture.py
└── main.py                  # Runnable driver showcasing swappable repositories
```

---

## Design Rationale: Composition vs. Inheritance

A common beginner trap in object-oriented design is creating deep inheritance hierarchies (e.g., `Order` inheriting from `Customer`, or `Invoice` inheriting from `Order`). In this project, I deliberately followed the rule: **"Favor object composition over class inheritance."**

### 1. Where Composition Was Chosen (and Why)

- **`Order` HAS `Customer` and `OrderItem`s**:
  - *Why not inheritance?* An order is not a kind of customer, and an order is not a product. An order *aggregates* items and *associates* with a customer.
  - *Benefits*: Customers and Products can exist independently in the system. Changing customer attributes doesn't break order calculation logic.
- **`Invoice` HAS an `Order`**:
  - *Why not inherit?* An invoice is a distinct billing snapshot of an order at a point in time. Inheriting would expose internal order mutation methods (`add_item`, `cancel`) on the invoice object, violating encapsulation.
- **`OrderService` HAS an `OrderRepository` (Dependency Injection)**:
  - *Why?* The business logic in `OrderService` should never know or care whether data is stored in memory, written to a `.json` file, or saved to a remote database. By composing `OrderService` with an abstract repository, we can swap storage backends with zero lines of business code modified.

### 2. Where Inheritance Was Deliberately Chosen

- **Interface Contracts (`OrderRepository(ABC)`)**:
  - Used `abc.ABC` and `@abstractmethod` so that `InMemoryOrderRepository` and `JsonFileOrderRepository` inherit the contract. This guarantees that any repository implementation adheres to Liskov Substitution Principle (LSP).
- **Domain Exceptions**:
  - `DomainException(Exception)` forms the root for `ValidationError`, `InvalidOrderStateError`, and `EntityNotFoundError`. This allows callers to catch all domain errors with a single `except DomainException:` or inspect granular exceptions individually.

---

## Key OOP & Software Engineering Patterns Applied

1. **Information Hiding & Defensive Encapsulation**:
   - Private attributes (`_items`, `_status`, `_unit_price`) protect invariants.
   - Property getters return defensive copies (e.g., `tuple(self._items)`) so external callers cannot bypass state machine validation by directly modifying the list.

2. **State Machine Invariants**:
   - Orders transition predictably: `DRAFT` → `CONFIRMED` → `PAID` → `SHIPPED` (or `CANCELLED`).
   - Finalized orders cannot accept new items; shipped orders cannot be cancelled; draft orders cannot be invoiced.

3. **Storage Independence**:
   - `OrderService` accepts any implementation of `OrderRepository`. Running unit tests with `InMemoryOrderRepository` is lightning fast and requires zero filesystem cleanup.

---

## How to Run

### Run the Demo Workflow
```bash
python main.py
```

### Run the Pytest Suite
```bash
pytest tests/ -v
```
