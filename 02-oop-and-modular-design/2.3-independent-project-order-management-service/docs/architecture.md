
# Order Management Service Architecture

## Overview

The Order Management Service is a simple Python application
that creates, stores, and retrieves customer orders.

The project uses three main layers.

## 1. Models Layer

File: `src/models.py`

The Order class stores order details, validates the data,
calculates the total price, and displays order information.

## 2. Repository Layer

File: `src/repositories.py`

The repository defines methods for saving and retrieving orders.

The InMemoryOrderRepository class stores orders in a Python
dictionary. The data is available only while the program runs.

## 3. Service Layer

File: `src/services.py`

The OrderService class handles business logic.

It creates orders, prevents duplicate order IDs, retrieves
individual orders, and returns all stored orders.

## 4. Application Layer

File: `src/main.py`

The main file displays the menu, accepts user input,
calls the service, and displays results.

## Request Flow

1. The user enters order details in main.py.
2. The service checks for duplicate order IDs.
3. The Order model validates the order details.
4. The repository stores the order.
5. The application displays the result.

## Testing

The tests use an in-memory repository to check the service
without requiring a database.

## Benefits

- Each class has a clear responsibility.
- Business logic is separated from storage.
- The repository can be replaced with another implementation.
- Unit tests can run without an external database.
