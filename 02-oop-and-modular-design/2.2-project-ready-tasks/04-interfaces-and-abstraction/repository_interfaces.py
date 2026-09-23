# Topic 04: Interfaces and Abstraction
# Abstract repository interface with two swappable implementations.

from abc import ABC, abstractmethod
from typing import Optional

class IUserRepository(ABC):
    """Contract defining user persistence operations."""

    @abstractmethod
    def add(self, user_id: str, user_data: dict) -> None:
        pass

    @abstractmethod
    def get(self, user_id: str) -> Optional[dict]:
        pass

    @abstractmethod
    def list_all(self) -> list[dict]:
        pass

# Implementation 1: In-Memory (ideal for unit testing)
class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._db = {}

    def add(self, user_id: str, user_data: dict) -> None:
        self._db[user_id] = user_data

    def get(self, user_id: str) -> Optional[dict]:
        return self._db.get(user_id)

    def list_all(self) -> list[dict]:
        return list(self._db.values())

# Implementation 2: Dictionary-backed Mock Database with logging
class AuditedUserRepository(IUserRepository):
    def __init__(self):
        self._db = {}
        self.audit_log = []

    def add(self, user_id: str, user_data: dict) -> None:
        self._db[user_id] = user_data
        self.audit_log.append(f"INSERT: user {user_id}")

    def get(self, user_id: str) -> Optional[dict]:
        self.audit_log.append(f"READ: user {user_id}")
        return self._db.get(user_id)

    def list_all(self) -> list[dict]:
        self.audit_log.append("LIST: all users")
        return list(self._db.values())

# Client Service depending strictly on the abstract interface
class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def register_user(self, user_id: str, name: str, email: str):
        self.repo.add(user_id, {"id": user_id, "name": name, "email": email})

    def find_user(self, user_id: str):
        return self.repo.get(user_id)

if __name__ == "__main__":
    # Test with Audited repo
    repo = AuditedUserRepository()
    service = UserService(repo)

    service.register_user("U101", "Alice", "alice@test.com")
    user = service.find_user("U101")
    print("Found User:", user)
    print("Audit Log:", repo.audit_log)
