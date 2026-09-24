# Session State & Role-Based Access Control (RBAC)

> **Module 09: Authentication & Security | Topic 03**

## 1. Learning Outcomes
- **Authentication vs Authorization:** Distinguish WHO a user is (AuthN) from WHAT they can do (AuthZ).
- **Session Tokens:** Generate cryptographically secure session identifiers (`secrets.token_urlsafe`).
- **Session Expiration:** Enforce absolute and idle session timeouts.
- **Role-Based Guards:** Restrict sensitive operations to defined user roles (Admin, Editor, Viewer).

## 2. Key Syntax & Concepts

### Simple RBAC Authorization Decorator
```python
from functools import wraps
from typing import Callable

class User:
    def __init__(self, username: str, roles: list[str]):
        self.username = username
        self.roles = set(roles)

def require_role(required_role: str):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(current_user: User, *args, **kwargs):
            if required_role not in current_user.roles:
                raise PermissionError(
                    f"Access Denied: User '{current_user.username}' lacks role '{required_role}'"
                )
            return func(current_user, *args, **kwargs)
        return wrapper
    return decorator

# Usage
@require_role("ADMIN")
def delete_database_record(current_user: User, record_id: str):
    print(f"Record {record_id} deleted by {current_user.username}")
```

## 3. Common Mistakes & Gotchas
- **Relying on Client-Side Role Flags:** Never trust roles stored in localStorage or un-signed client cookies without backend verification.
- **Predictable Session Tokens:** Generating session IDs with `random.randint()` allows attackers to guess active session IDs. Always use `secrets.token_urlsafe()`.

## 4. Practice Tasks
- **Task 1:** Build a session manager that issues 32-byte tokens and expires sessions after 15 minutes of inactivity.

## 5. Self-Check Questions
- **Q1:** What is the difference between Authentication and Authorization?
- **Q2:** Why should `secrets` module be used instead of `random` for token generation?
