# Functions, Scope, and Reusability

> **Module 01: Python Fundamentals | Topic 04**



## 1. Learning Outcomes

- **Design Functions:** Write small, single-purpose, pure functions with clear return values.
- **Arguments:** Use positional, keyword, default, *args, and **kwargs effectively.
- **Scope Resolution:** Apply the LEGB (Local, Enclosing, Global, Built-in) rule correctly.
- **Documentation:** Document parameters and returns with standard docstrings.

## 2. Key Syntax & Concepts


### Defining Functions & Arguments

```python
def calculate_discount(price: float, discount_pct: float = 10.0) -> float:
    """Calculate price after discount.
    
    Args:
        price: Original item price.
        discount_pct: Discount percentage (default 10.0).
    Returns:
        Final price after applying discount.
    """
    if price < 0:
        raise ValueError('Price cannot be negative')
    return round(price * (1 - discount_pct / 100), 2)
```


### Flexible Parameters: *args and **kwargs

```python
def log_event(event_type, *details, **metadata):
    print(f'Event: {event_type}')
    print(f'Details: {details}')    # tuple
    print(f'Meta: {metadata}')       # dict

log_event('LOGIN', 'User 10', 'Success', ip='192.168.1.1', status=200)
```


## 3. Common Mistakes & Gotchas

- **The Mutable Default Argument Bug:** NEVER use a mutable default like `def append_to(item, target=[])`. The list persists across function calls! Use `target=None` and initialize inside:
```python
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

- **Shadowing Built-ins:** Avoid naming parameters `list`, `str`, `id`, `sum`, or `type`.

## 4. Practice Tasks & Self-Check

- **Task 1:** Build a math utility module with pure functions: calculate_mean, calculate_median, and clamp_value.
- **Q1:** What does the LEGB rule stand for in Python scope resolution?
