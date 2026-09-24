# 05 — Modular Architecture

## 1. Modules

### What it is

A module is a Python file containing code such as functions, classes, and variables.
Modules help organize code into separate files.

### Important Points

* A Python file with `.py` is a module.
* A module can contain related functionality.
* Modules can be imported into other files.
* Splitting code into modules makes programs easier to maintain.

### Basic Syntax

```python
# math_utils.py

def add(a, b):
    return a + b
```

---

## 2. Packages

### What it is

A package is a folder containing related Python modules.

### Important Points

* Packages help organize larger projects.
* A package can contain multiple modules.
* Packages can contain sub-packages.
* Python code can import modules from packages.

### Basic Syntax

```text
project/
│
├── main.py
└── utils/
    ├── __init__.py
    └── math_utils.py
```

```python
from utils.math_utils import add
```

---

## 3. Imports

### What it is

Imports allow code from another module or package to be used in the current file.

### Important Points

* `import` loads a module.
* `from ... import ...` imports specific items.
* Imports allow code reuse.
* Keep imports clear and organized.

### Basic Syntax

```python
import math

print(math.sqrt(25))
```

```python
from math import sqrt

print(sqrt(25))
```

---

## 4. Separation of Concerns

### What it is

Separation of concerns means dividing a program into parts where each part has a specific responsibility.

### Important Points

* Each module or class should have a clear purpose.
* Avoid putting all code in one file.
* Separate user interface, business logic, and data access.
* Makes code easier to test and maintain.

### Basic Syntax

```text
main.py          → program flow
services.py      → business logic
repositories.py  → data access
models.py        → data structures
```

---

## 5. Layers

### What it is

Layers divide an application into different levels, with each level having a specific responsibility.

### Important Points

* Common layers are presentation, service, and data access.
* Each layer should focus on its own responsibility.
* One layer can use another layer.
* Layers make larger applications easier to organize.

### Basic Syntax

```text
Application
    ↓
Service Layer
    ↓
Repository Layer
    ↓
Database / File
```

---

## 6. Service Classes

### What it is

A service class contains business logic or operations that an application needs to perform.

### Important Points

* Services focus on what the application needs to do.
* They can use repositories to access data.
* They should not contain unnecessary database details.
* Service classes help keep business logic organized.

### Basic Syntax

```python
class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.find_user(user_id)
```

---

## 7. Repositories

### What it is

A repository handles access to stored data such as a database or file.

### Important Points

* Repositories handle data access.
* They can contain operations such as `find()`, `save()`, or `delete()`.
* Business logic should normally stay outside the repository.
* A repository can hide database details from other parts of the application.

### Basic Syntax

```python
class UserRepository:
    def find_user(self, user_id):
        # Get user from database
        pass
```

---

## 8. Models

### What it is

Models represent the data or objects used by an application.

### Important Points

* Models define the structure of data.
* They can be created using classes.
* Models may contain attributes and methods.
* They help keep data organized.

### Basic Syntax

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 9. Utilities

### What it is

Utility modules contain small reusable functions that can be used in different parts of a program.

### Important Points

* Utilities should contain general-purpose functionality.
* They should not contain application-specific business logic.
* Common examples include formatting, validation, and date helpers.
* Keep utility functions simple and reusable.

### Basic Syntax

```python
# utils.py

def format_name(name):
    return name.strip().title()
```

---

## 10. Dependency Relationships

### What it is

A dependency relationship means one part of a program needs another part to perform its work.

### Important Points

* A service may depend on a repository.
* A repository may depend on a database.
* Dependencies should have clear directions.
* Avoid unnecessary dependencies between modules.
* Passing dependencies into classes can make code easier to test.

### Basic Syntax

```python
class UserService:
    def __init__(self, repository):
        self.repository = repository
```

Here, `UserService` depends on `repository`.

---

## 11. Avoiding Circular Imports

### What it is

A circular import happens when two or more modules directly or indirectly import each other.

### Important Points

* `module_a` imports `module_b`.
* `module_b` imports `module_a`.
* Circular imports can cause import errors and confusing behavior.
* Keep dependencies flowing in one direction.
* Move shared code into a separate module when necessary.

### Basic Syntax

```text
# Avoid

module_a.py
    ↓ imports
module_b.py
    ↓ imports
module_a.py
```

A better structure is:

```text
module_a.py ──→ common.py
module_b.py ──→ common.py
```
