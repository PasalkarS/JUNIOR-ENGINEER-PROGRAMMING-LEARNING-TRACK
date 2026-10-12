# 4 — Mocking

## 1. Introduction to Mocking

Mocking is a testing technique used to replace a real dependency with a fake object during a test.

A dependency is something a function or component relies on, such as an API, database, file system, or external service.

Mocking allows tests to check how code behaves without depending on the real external resource.

### Example

Imagine a program that retrieves customer information from an external API. Instead of making a real API request during every test, a mock can return predefined customer data.

### Important Points

- Mocking replaces dependencies during tests.
- It helps tests run faster and more reliably.
- It avoids unnecessary calls to external services.
- It allows specific success and failure scenarios to be tested.
- It is especially useful when a dependency is slow, costly, or difficult to access.

## 2. Why Mocking Is Needed

Some functions depend on resources outside the program. These dependencies can make unit tests slow or unpredictable.

Examples include:

- External APIs
- Databases
- File systems
- Email services
- Payment gateways
- Message queues

Mocking allows the code to be tested without accessing these resources directly.

### Important Points

- External services may be unavailable during testing.
- Network requests can fail or produce inconsistent results.
- Real dependencies may require credentials or special configuration.
- Mocking provides controlled responses for testing different situations.
- Mocking does not replace the need for integration tests with real dependencies.

## 3. Introduction to `unittest.mock`

Python provides the built-in `unittest.mock` module for creating mock objects.

It can be used with pytest even though pytest is a separate testing framework.

One commonly used class is `Mock`, which can simulate an object or dependency.

### Example

```python
from unittest.mock import Mock

payment_service = Mock()

payment_service.process_payment.return_value = "Success"

result = payment_service.process_payment(500)

assert result == "Success"
```

### Important Points

- `Mock` creates an object that can simulate methods and attributes.
- `return_value` defines the value returned when a mock is called.
- Mock objects can record how they were called.
- They help isolate the code being tested from its dependencies.

## 4. Mocking a Function

A function that depends on another function can be tested by replacing the dependency with a mock.

For example, a service might retrieve a user's name from another function.

### Application Code

```python
def get_user_name(user_id):
    return "Amit"

def display_user(user_id):
    name = get_user_name(user_id)
    return "User: " + name
```

### Test Using a Mock

```python
from unittest.mock import Mock

def test_display_user():
    get_user_name = Mock(return_value="Riya")

    name = get_user_name(1)

    assert name == "Riya"
    get_user_name.assert_called_once_with(1)
```

This example demonstrates a mocked function independently. In a real test, the mock must replace the dependency used by the application code.

### Important Points

- Mock the dependency that the code under test actually uses.
- Define the expected return value.
- Verify the result produced by the code.
- Check how the dependency was called when that interaction matters.

## 5. Using `patch()`

The `patch()` function temporarily replaces an object with a mock during a test.

It is useful when the application imports or references a dependency that needs to be replaced.

### Application Code — `user_service.py`

```python
def get_user_name(user_id):
    return "Amit"

def display_user(user_id):
    name = get_user_name(user_id)
    return "User: " + name
```

### Test Code — `test_user_service.py`

```python
from unittest.mock import patch
from user_service import display_user

def test_display_user():
    with patch("user_service.get_user_name") as mock_get_user:
        mock_get_user.return_value = "Riya"

        result = display_user(1)

        assert result == "User: Riya"
        mock_get_user.assert_called_once_with(1)
```

### Important Points

- `patch()` replaces the specified object temporarily.
- The replacement is automatically restored when the context manager exits.
- Patch the name where the code under test looks up the dependency.
- The string passed to `patch()` must refer to the correct module and object.
- Incorrect patch targets are a common reason for mocking tests to fail.

## 6. Mocking External APIs

External API calls often depend on network access and remote systems.

Mocking allows API-dependent code to be tested using controlled responses.

### Application Code — `weather_service.py`

```python
import requests

def get_weather(city):
    response = requests.get(
        "https://example.com/weather",
        params={"city": city}
    )

    response.raise_for_status()
    return response.json()
```

### Test Code

```python
from unittest.mock import Mock, patch
from weather_service import get_weather

def test_get_weather():
    with patch("weather_service.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {
            "city": "Pune",
            "temperature": 30
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_weather("Pune")

        assert result["city"] == "Pune"
        assert result["temperature"] == 30
        mock_get.assert_called_once()
```

### Important Points

- No real HTTP request is made in this test.
- The mock response provides predictable data.
- Tests can simulate successful responses and failures.
- Mocking an API does not verify that the real API is available or returns the same response format.
- Real API behavior should be checked separately when necessary.

## 7. Mocking Exceptions and Failures

A dependency may fail because of a network issue, invalid response, or service error.

Mocks can simulate these failures without causing an actual failure in the external system.

### Example

```python
from unittest.mock import Mock

def test_api_failure():
    api_service = Mock()
    api_service.get_data.side_effect = ConnectionError(
        "Connection failed"
    )

    try:
        api_service.get_data()
        assert False, "Expected ConnectionError"
    except ConnectionError:
        assert True
```

In pytest, `pytest.raises()` provides a clearer way to test exceptions.

```python
import pytest
from unittest.mock import Mock

def test_api_failure():
    api_service = Mock()
    api_service.get_data.side_effect = ConnectionError

    with pytest.raises(ConnectionError):
        api_service.get_data()
```

### Important Points

- `side_effect` can make a mock raise an exception.
- It can also provide different results on successive calls.
- Failure scenarios help verify that the application handles errors correctly.
- Test the application's error-handling behavior, not just that the mock raises an exception.

## 8. Mock Return Values and Side Effects

Mocks support two useful properties: `return_value` and `side_effect`.

| Property | Purpose |
|---|---|
| `return_value` | Specifies what a mock returns when called |
| `side_effect` | Specifies an exception or behavior that occurs when called |

### Example Using `return_value`

```python
from unittest.mock import Mock

service = Mock()
service.get_status.return_value = "Active"

assert service.get_status() == "Active"
```

### Example Using `side_effect`

```python
from unittest.mock import Mock

service = Mock()
service.get_status.side_effect = ValueError("Invalid status")
```

### Important Points

- Use `return_value` for predictable responses.
- Use `side_effect` to simulate failures or varying responses.
- Configure mocks to represent realistic scenarios.
- Avoid adding unnecessary mock behavior that makes tests difficult to understand.

## 9. Verifying Mock Calls

Mocks can record how they were used. This helps verify whether the code called a dependency with the correct arguments.

Common methods include:

- `assert_called()`
- `assert_called_once()`
- `assert_called_with()`
- `assert_called_once_with()`
- `assert_not_called()`

### Example

```python
from unittest.mock import Mock

notification_service = Mock()

notification_service.send("Test message")

notification_service.send.assert_called_once_with(
    "Test message"
)
```

### Important Points

- Use call assertions when interactions are part of the expected behavior.
- `assert_called_once_with()` checks both the number of calls and the arguments.
- `assert_not_called()` verifies that a dependency was not used.
- Do not verify every internal call unnecessarily; focus on interactions that matter to the behavior being tested.

## 10. Mocking Files and Databases

File operations and database access can be external dependencies for a unit test.

Mocking can help test the application's logic without creating real files or connecting to a real database.

However, mocked tests do not verify actual file handling, SQL execution, schema constraints, or transaction behavior.

### Important Points

- Mock file or database dependencies when testing business logic in isolation.
- Use temporary files when actual file behavior needs to be tested.
- Use a test database for database integration tests.
- Keep the mocked behavior consistent with the real dependency's expected interface.
- Test real resource behavior separately when it matters.

## 11. What Should Be Mocked?

Mock dependencies that are outside the specific unit of code being tested when their real behavior would make the test unreliable, slow, or difficult to control.

Common examples:

- External APIs
- Email and notification services
- Payment gateways
- Remote storage
- Expensive or unpredictable external operations

The main logic being tested should generally remain real.

For example, when testing an order service, the order service itself should run normally, while the payment gateway may be mocked.

### Important Points

- Mock external boundaries rather than the behavior you want to verify.
- Use real simple calculations and business rules in unit tests.
- Avoid mocking every function or object.
- Excessive mocking can make tests pass even when the actual application behavior is incorrect.
- Use integration tests to verify that real components work together.

## 12. What Should Not Be Mocked?

Not every dependency needs to be mocked.

Avoid mocking a component when doing so removes the behavior the test is intended to verify.

Examples:

- Do not mock the function whose calculation you are testing.
- Do not mock simple in-memory operations without a clear reason.
- Do not rely exclusively on mocked database calls to verify SQL queries.
- Do not assume mocked API responses prove compatibility with the real API.

### Important Points

- Keep the unit under test real.
- Mock only the dependencies needed to isolate that unit.
- Prefer simple test data over unnecessary mock objects.
- Use real components when their actual interaction is the subject of the test.

## 13. Common Mocking Mistakes

- Patching the wrong module or object.
- Mocking the function being tested instead of its dependency.
- Forgetting to configure the expected return value.
- Verifying irrelevant internal calls.
- Mocking too many dependencies.
- Making mock responses unrealistic.
- Treating mocked tests as proof that an external service works.
- Ignoring error-handling scenarios.
- Testing only interactions without checking the final result.

