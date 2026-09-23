# Order Management Service

A modular, test-driven e-commerce order management service built in Python adhering to SOLID principles and clean layer separation.

## Architecture

- **Domain Models**: `Customer`, `Product`, `OrderItem`, and `Order` with state transitions.
- **Repositories**: Abstract contracts (`IProductRepository`, `IOrderRepository`) and in-memory implementations.
- **Business Services**: `OrderService` managing multi-item orders, stock checks, and status flows.
- **Notifications**: Decoupled `NotificationService` triggered on domain events.

## Directory Structure

```text
2.3-independent-project-order-management-service/
├── README.md
├── src/
│   ├── models.py       # Domain entities & OrderStatus enum
│   ├── repositories.py # Abstract & concrete storage contracts
│   ├── services.py     # Business logic & notifications
│   └── main.py         # Entry point demonstration
├── tests/
│   └── test_order_service.py # Pytest test suite
└── docs/
    ├── architecture.md       # Layer diagrams
    └── design_decisions.md   # Architectural tradeoffs
```

## Running the Project

```bash
python src/main.py
```

## Running Automated Tests

```bash
pytest tests/ -v
```
