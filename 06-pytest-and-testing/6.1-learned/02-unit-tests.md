# Unit Testing & Boundary Analysis

> **Module 06: Pytest & Testing | Topic 02**

## 1. Learning Outcomes
- **Testing Pure Functions:** Isolate business logic from database, network, and disk I/O.
- **Boundary Value Analysis:** Test minimum, maximum, zero, and boundary transition values.
- **Testing Exceptions:** Use `pytest.raises()` to verify that invalid inputs trigger expected errors.
- **Deterministic Tests:** Ensure tests produce identical results on every execution regardless of order or time.

## 2. Key Syntax & Concepts

### Testing Expected Exceptions with `pytest.raises`
```python
import pytest

def calculate_discount(price: float, discount_pct: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not 0 <= discount_pct <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    return round(price * (1 - discount_pct / 100), 2)

def test_valid_discount():
    assert calculate_discount(100.0, 20.0) == 80.0

def test_negative_price_raises_error():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_discount(-50.0, 10.0)

def test_boundary_zero_and_hundred_discount():
    assert calculate_discount(50.0, 0.0) == 50.0
    assert calculate_discount(50.0, 100.0) == 0.0
```

## 3. Common Mistakes & Gotchas
- **Testing Implementation Instead of Behavior:** Don't assert private internal variables; assert public return values and state.
- **Flaky Tests:** Avoid dependencies on `datetime.now()` or random numbers without fixed seeds.

## 4. Practice Tasks
- **Task 1:** Write boundary tests for a password validation rule requiring length >= 8 characters.

## 5. Self-Check Questions
- **Q1:** What does `match="pattern"` inside `pytest.raises` verify?
- **Q2:** Why are boundary tests more likely to catch bugs than average-case tests?
