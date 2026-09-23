# Interfaces, Abstraction, and Contracts

> **Module 02: OOP and Modular Design | Topic 04**



## 1. Learning Outcomes

- **Abstract Base Classes:** Define explicit contracts using Python's `abc.ABC` and `@abstractmethod`.
- **Enforce Contracts:** Prevent instantiation of incomplete classes lacking required methods.
- **Loose Coupling:** Design services that depend on abstract interfaces rather than concrete implementations.
- **Interchangeability:** Swap storage or processing implementations without modifying client code.

## 2. Key Syntax & Concepts

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    """Abstract interface defining user persistence contract."""

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[dict]:
        pass

    @abstractmethod
    def save(self, user_data: dict) -> None:
        pass

# Concrete Implementation 1: In-Memory (for testing)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage = {}

    def get_by_id(self, user_id: str) -> Optional[dict]:
        return self._storage.get(user_id)

    def save(self, user_data: dict) -> None:
        self._storage[user_data['id']] = user_data
```


## 3. Common Mistakes & Gotchas

- **Instantiating Abstract Classes:** Attempting to create an object of a class with unimplemented `@abstractmethod` raises TypeError immediately at runtime.
- **Signature Mismatch:** Subclasses must match the parameter signature expected by the interface contract.

## 4. Practice Tasks & Self-Check

- **Task 1:** Create an abstract `PaymentGateway` interface and implement `CreditCardGateway` and `PayPalGateway`.
- **Q1:** What error occurs if a subclass fails to implement an `@abstractmethod`?
