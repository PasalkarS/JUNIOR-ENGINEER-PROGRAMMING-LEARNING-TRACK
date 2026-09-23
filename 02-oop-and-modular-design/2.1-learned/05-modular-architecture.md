# Modular Architecture & Separation of Concerns

> **Module 02: OOP and Modular Design | Topic 05**



## 1. Learning Outcomes

- **Package Architecture:** Structure Python packages cleanly with modules and `__init__.py` files.
- **Layered Design:** Separate models, repositories, business services, and user interfaces.
- **Circular Imports:** Identify and prevent circular dependency cycles in Python.
- **Dependency Flow:** Keep dependencies flowing in one direction (UI -> Service -> Repository -> Model).

## 2. The Standard 4-Layer Architecture


| Layer | Responsibility | Allowed Dependencies |
| --- | --- | --- |
| Models (Domain) | Data definitions and business rules (e.g. Order, Customer) | None (Pure domain) |
| Repositories | Persistence abstraction (saving / reading files/DB) | Models |
| Services | Business workflows, transactions, validations | Repositories, Models |
| Interface / CLI | User interactions, menus, command parsing | Services, Models |



## 3. Common Mistakes & Gotchas

- **Circular Import Pitfall:** Module A imports B, and B imports A. Resolve by moving shared types into a `models.py` or importing inside methods if necessary.
- **Mixing Business Logic with I/O:** Putting `input()` or `print()` calls inside repository or domain classes ruins testability and reusability.

## 4. Practice Tasks & Self-Check

- **Task 1:** Refactor a monolithic single-file script into models.py, repository.py, and service.py.
- **Q1:** Why should models never import repositories or CLI controllers?
