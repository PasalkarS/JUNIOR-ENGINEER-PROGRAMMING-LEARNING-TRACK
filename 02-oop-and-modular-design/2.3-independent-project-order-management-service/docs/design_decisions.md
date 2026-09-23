# Design Decisions

- **Dependency Inversion**: `OrderService` accepts abstract repositories via constructor injection, enabling trivial in-memory mocking during tests.
- **Stock Guard**: Orders cannot be placed if inventory is deficient. Cancellation restores reserved inventory.
- **State Machine**: Order status progresses strictly along allowed paths: `PENDING -> PAID -> SHIPPED` or `PENDING/PAID -> CANCELLED`.
