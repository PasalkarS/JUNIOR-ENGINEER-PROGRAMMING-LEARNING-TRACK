# Mocking External Dependencies & Monkeypatching

> **Module 06: Pytest & Testing | Topic 04**

## 1. Learning Outcomes
- **Why Mock:** Avoid hitting live external APIs, credit card gateways, or file servers during unit tests.
- **unittest.mock:** Replace objects and methods with `Mock` and `patch`.
- **Verifying Invocations:** Assert call counts and parameter arguments with `assert_called_once_with()`.
- **When NOT to Mock:** Avoid mocking internal business logic or simple domain objects.

## 2. Key Syntax & Concepts

### Mocking an External Email Service
```python
from unittest.mock import Mock, patch

class OrderService:
    def __init__(self, mailer):
        self.mailer = mailer

    def complete_order(self, customer_email: str, order_id: str):
        # Process order logic...
        self.mailer.send_email(customer_email, f"Order #{order_id} confirmed!")
        return True

def test_order_completion_triggers_email():
    # 1. Create mock dependency
    mock_mailer = Mock()
    service = OrderService(mailer=mock_mailer)

    # 2. Execute action
    result = service.complete_order("bob@example.com", "ORD-99")

    # 3. Assert behavior
    assert result is True
    mock_mailer.send_email.assert_called_once_with(
        "bob@example.com", "Order #ORD-99 confirmed!"
    )
```

## 3. Common Mistakes & Gotchas
- **Over-Mocking:** Mocking everything leaves you testing that your mocks work, rather than your actual code.
- **Mocking What You Don't Own:** Prefer wrapping third-party APIs in a small internal adapter class and mock that adapter.

## 4. Practice Tasks
- **Task 1:** Use `unittest.mock.patch` to simulate an HTTP 500 error from `requests.get` and verify your client retry handler.

## 5. Self-Check Questions
- **Q1:** What happens if an un-mocked unit test calls a paid third-party SMS API?
- **Q2:** What does `mock.assert_called_once()` verify?
