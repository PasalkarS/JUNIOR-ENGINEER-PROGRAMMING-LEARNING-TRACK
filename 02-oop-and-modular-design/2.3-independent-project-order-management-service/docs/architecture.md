# Order Management Service Architecture

## Layered Design Overview

The application demonstrates clean junior-level OOP and modular architecture:

```
[Presentation / CLI]
       |
       v
[OrderService] <---> [NotificationService]
       |
       v
[Repositories (IOrderRepository, IProductRepository)]
       |
       v
[Domain Models (Customer, Product, Order, OrderItem)]
```

## Responsibilities

1. **Domain Models (`models.py`)**: Hold domain data, calculate line totals, manage order lifecycle state.
2. **Repositories (`repositories.py`)**: Abstract persistence storage behind interfaces (`IProductRepository`, `IOrderRepository`).
3. **Services (`services.py`)**: Coordinates inventory checks, order creation, notifications, and stock rollbacks.
