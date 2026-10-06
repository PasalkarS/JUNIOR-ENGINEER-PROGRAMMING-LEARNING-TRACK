
# Design Decisions

## 1. Separate the Application into Layers

The project separates models, repositories, services, and
the application entry point.

This makes the code easier to understand and maintain.

## 2. Use an Order Class

The Order class stores order information and calculates
the total price.

It also validates important order details to prevent
invalid objects from being created.

## 3. Use a Repository Interface

The OrderRepository abstract class defines the operations
that a repository must support.

The service depends on this interface rather than directly
depending on a specific storage implementation.

## 4. Use In-Memory Storage

The InMemoryOrderRepository stores orders in a dictionary.

This is simple for a learning project and does not require
a database setup.

The data is lost when the application stops.

## 5. Use Dependency Injection

OrderService receives the repository through its constructor.

This makes it possible to replace the repository without
changing the service's business logic.

## 6. Validate Order Details

The Order model checks that the order ID, customer,
product, quantity, and price are valid.

The service also prevents duplicate order IDs.

## 7. Use Unit Tests

The test file checks successful operations and expected
errors.

Tests help identify problems when the code changes.

## 8. Keep the Design Simple

The project uses only the Python standard library.

Additional layers, databases, and frameworks can be added
when the requirements become more complex.
