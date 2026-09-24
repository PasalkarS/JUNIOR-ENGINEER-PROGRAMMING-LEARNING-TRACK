# Mocking HTTP Services & Contract Testing

> **Module 07: REST API Integration | Topic 05**

## 1. Learning Outcomes
- **Isolated Testing:** Test client code without depending on live external networks or APIs.
- **Mocking Responses:** Use `unittest.mock` or `responses` library to intercept HTTP calls.
- **Testing Edge Cases:** Simulate HTTP 500 server crashes, 401 auth failures, and timeouts deterministically.
- **Schema Contracts:** Verify expected dictionary schema contracts against client parser logic.

## 2. Key Syntax & Concepts

### Mocking requests using `unittest.mock.patch`
```python
from unittest.mock import patch, Mock
import pytest

def get_exchange_rate(base_currency: str) -> float:
    # Client function under test
    resp = requests.get(f"https://api.fx.com/rate?base={base_currency}", timeout=3.0)
    resp.raise_for_status()
    return resp.json()["rate"]

@patch("requests.get")
def test_exchange_rate_success(mock_get):
    # Setup mock response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"base": "USD", "rate": 1.25}
    mock_get.return_value = mock_resp

    rate = get_exchange_rate("USD")
    assert rate == 1.25
    mock_get.assert_called_once()
```

## 3. Common Mistakes & Gotchas
- **Hitting Live Endpoints in CI/CD:** Live API tests fail unexpectedly when networks fluctuate or rate limits expire. Keep unit test suites 100% mocked.
- **Not Testing Timeout Handling:** Always write a test that verifies your client catches `requests.Timeout` cleanly.

## 4. Practice Tasks
- **Task 1:** Write a test that mocks a `requests.Timeout` exception and verifies your function returns a graceful fallback value.

## 5. Self-Check Questions
- **Q1:** Why is testing with mocked responses faster and more reliable than hitting test API servers?
- **Q2:** How can contract drift between mock and actual API be detected over time?
