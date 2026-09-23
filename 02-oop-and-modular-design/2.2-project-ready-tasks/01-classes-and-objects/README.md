# 01 — Classes and Objects

## Objective
Model a cohesive e-commerce invoicing domain with `Customer`, `Product`, `OrderItem`, and `Invoice` classes.

## Requirements
- Define constructors with explicit parameter typing.
- Implement readable `__str__` and computed properties (`subtotal`, `tax`, `total`).
- Ensure `OrderItem` calculates its line-item cost from the referenced `Product`.

## Constraints & Edge Cases
- Order quantities must be strictly positive (> 0).
- Floating-point calculations must be rounded cleanly to 2 decimal places.

## How to Run
```bash
python order_domain_models.py
```
