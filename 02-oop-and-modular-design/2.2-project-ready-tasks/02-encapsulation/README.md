# 02 — Encapsulation & State Validation

## Objective
Implement protected state management and property validation to prevent illegal transitions in a financial `BankAccount`.

## Key Concepts
- `_balance` and `_is_frozen` attributes are protected from direct mutation.
- `@property` exposes safe read access.
- Explicit methods enforce boundary checks before altering object state.

## How to Run
```bash
python validated_bank_account.py
```
