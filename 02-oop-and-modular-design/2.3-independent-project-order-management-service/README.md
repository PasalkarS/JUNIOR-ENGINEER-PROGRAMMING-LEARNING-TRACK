
# Order Management Service

## Overview

A beginner-friendly Python project that demonstrates
Object-Oriented Programming and Modular Architecture.

The application allows users to create orders, view an
individual order, and display all saved orders.

## Features

- Create customer orders
- Validate order details
- Calculate order totals
- Prevent duplicate order IDs
- Find orders by ID
- View all orders
- Run automated unit tests

## Technologies

- Python
- Object-Oriented Programming
- Abstract Base Classes
- Modular Architecture
- Python unittest

## Project Structure

```text
2.3-independent-project-order-management-service/
├── docs/
│   ├── architecture.md
│   └── design_decisions.md
├── src/
│   ├── main.py
│   ├── models.py
│   ├── repositories.py
│   └── services.py
├── tests/
│   └── test_order_service.py
└── README.md
```

## Requirements

Python 3.10 or later is recommended.

No external packages are required.

## How to Run

Open a terminal in the project root directory.

Run the application:

```bash
python src/main.py
```

## How to Run Tests

The application modules are inside the src directory.

On Windows Command Prompt:

```bat
set PYTHONPATH=src&& python -m unittest discover -s tests -v
```

On macOS or Linux:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Concepts Practiced

- Classes and objects
- Encapsulation and validation
- Abstract classes
- Repository pattern
- Service layer
- Dependency injection
- Separation of concerns
- Unit testing

## Limitations

Orders are stored in memory and are lost when the
application stops.

The application does not use a database or process
real payments.

## Future Improvements

- Add order update and delete operations
- Store orders in a JSON file or database
- Add customer and product management
- Add order status tracking
- Improve validation and error handling

## Learning Goal

Build and explain a small maintainable application
using domain models, service and repository layers,
validation, and automated tests.
