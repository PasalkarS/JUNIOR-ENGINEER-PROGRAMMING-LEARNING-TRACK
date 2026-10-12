# 3 — Fixtures & Parametrization

## 1. Introduction to Fixtures

A fixture is a function that prepares the data or resources required by a test.

In `pytest`, fixtures are created using the `@pytest.fixture` decorator. They help avoid repeating the same setup code across multiple tests.

### Example

```python
import pytest

@pytest.fixture
def sample_numbers():
    return [10, 20, 30]

def test_list_length(sample_numbers):
    assert len(sample_numbers) == 3

def test_list_sum(sample_numbers):
    assert sum(sample_numbers) == 60
```

### Important Points

- Fixtures provide reusable test data or resources.
- They are defined using `@pytest.fixture`.
- A test requests a fixture by using its name as a function parameter.
- Pytest automatically runs the fixture and passes its result to the test.
- Fixtures reduce code duplication and make tests easier to maintain.

## 2. Why Fixtures Are Useful

Without fixtures, the same preparation code may need to be repeated in multiple tests.

Fixtures allow common setup logic to be written once and reused wherever required.

### Example Without a Fixture

```python
def test_first_item():
    numbers = [10, 20, 30]
    assert numbers[0] == 10

def test_last_item():
    numbers = [10, 20, 30]
    assert numbers[-1] == 30
```

### Example With a Fixture

```python
import pytest

@pytest.fixture
def numbers():
    return [10, 20, 30]

def test_first_item(numbers):
    assert numbers[0] == 10

def test_last_item(numbers):
    assert numbers[-1] == 30
```

### Important Points

- Shared setup belongs in fixtures when it improves clarity.
- Fixtures help keep test functions focused on the behavior being tested.
- Fixtures can return strings, numbers, lists, dictionaries, objects, or other resources.
- Avoid creating fixtures for trivial setup when they make the code harder to understand.

## 3. Fixture Scope

Fixture scope determines how often a fixture is created during a test run.

Pytest supports several fixture scopes.

| Scope | Description |
|---|---|
| `function` | Runs once for each test function; this is the default |
| `class` | Runs once for each test class |
| `module` | Runs once for each test module |
| `package` | Runs once for each package |
| `session` | Runs once for the entire test session |

### Example

```python
import pytest

@pytest.fixture(scope="function")
def sample_data():
    return [1, 2, 3]

def test_first_value(sample_data):
    assert sample_data[0] == 1

def test_data_length(sample_data):
    assert len(sample_data) == 3
```

Here, the fixture is created separately for each test function.

### Important Points

- Use `function` scope when tests need fresh, independent data.
- Use broader scopes when expensive setup can safely be shared.
- Broader scopes may cause tests to share state.
- Choose a scope based on the resource's lifetime and the need for test isolation.

## 4. Setup and Teardown Using Fixtures

**Setup** prepares the resources required by a test.

**Teardown** cleans up those resources after the test has finished.

Pytest fixtures can use `yield` to separate setup from teardown.

### Example

```python
import pytest

@pytest.fixture
def sample_resource():
    print("Setting up resource")
    resource = {"status": "ready"}

    yield resource

    print("Cleaning up resource")

def test_resource_status(sample_resource):
    assert sample_resource["status"] == "ready"
```

The code before `yield` performs setup. The code after `yield` performs cleanup.

### Important Points

- Use `yield` when a fixture needs cleanup after a test.
- Cleanup code runs after the test finishes, including when the test fails.
- Teardown is useful for closing files, database connections, or other resources.
- Avoid leaving temporary resources open after tests complete.

## 5. Using Fixtures for Test Data

Fixtures can provide consistent sample data for testing functions.

### Example

```python
import pytest

@pytest.fixture
def employee():
    return {
        "name": "Amit",
        "salary": 30000,
        "department": "QA"
    }

def test_employee_name(employee):
    assert employee["name"] == "Amit"

def test_employee_salary(employee):
    assert employee["salary"] == 30000
```

### Important Points

- Use fixtures for common test data.
- Keep test data simple and understandable.
- Include only the fields required for the tests when practical.
- Avoid modifying shared mutable data in ways that affect other tests.
- The default function scope helps provide fresh fixture data to each test.

## 6. Introduction to Parametrization

Parametrization allows the same test function to run with multiple input values.

In pytest, `@pytest.mark.parametrize` is used to provide different inputs and their expected results.

It avoids writing separate test functions for every similar test case.

### Example

```python
import pytest

def add_numbers(a, b):
    return a + b

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 5, 10),
        (-2, 2, 0),
        (0, 0, 0)
    ]
)
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected
```

### Important Points

- `@pytest.mark.parametrize` defines multiple test cases.
- Each tuple provides values for the listed parameters.
- Pytest runs the test once for each set of values.
- Each case is reported separately.
- Parametrization is useful when testing the same behavior with different inputs.

## 7. Parametrizing Boundary Conditions

Parametrization is especially useful for testing boundary values.

### Example

```python
import pytest

def is_adult(age):
    return age >= 18

@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True),
        (0, False)
    ]
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected
```

### Important Points

- Include values below, at, and above important boundaries.
- Include typical values and edge cases.
- State the expected result for each input.
- Make each test case easy to understand.
- Parametrization does not replace the need to choose meaningful cases.

## 8. Parametrizing Invalid Inputs

Parametrization can also test inputs that should cause exceptions.

### Example

```python
import pytest

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@pytest.mark.parametrize(
    "a, b",
    [
        (10, 0),
        (5, 0),
        (-4, 0)
    ]
)
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError):
        divide_numbers(a, b)
```

### Important Points

- Multiple invalid inputs can be tested using one parametrized function.
- Use `pytest.raises()` to verify expected exceptions.
- Each invalid input should represent a meaningful scenario.
- Do not group unrelated behaviors into a single parametrized test.

## 9. Combining Fixtures and Parametrization

Fixtures and parametrization solve different problems and can be used together.

- **Fixtures** prepare data or resources.
- **Parametrization** supplies multiple sets of input values.

### Example

```python
import pytest

@pytest.fixture
def prices():
    return [100, 200, 300]

@pytest.mark.parametrize(
    "index, expected",
    [
        (0, 100),
        (1, 200),
        (2, 300)
    ]
)
def test_price_at_index(prices, index, expected):
    assert prices[index] == expected
```

### Important Points

- Use fixtures for reusable setup.
- Use parametrization for multiple variations of a test.
- A test can request a fixture and accept parametrized values at the same time.
- Keep the purpose of each fixture and parameter clear.

## 10. Organizing Fixtures in `conftest.py`

When multiple test files need the same fixtures, they can be placed in a file named `conftest.py`.

Pytest discovers fixtures defined in this file automatically, so test files do not need to import them directly.

### Example Structure

```text
project/
│
├── app.py
├── conftest.py
└── tests/
    ├── test_users.py
    └── test_orders.py
```

Example `conftest.py`:

```python
import pytest

@pytest.fixture
def sample_user():
    return {
        "name": "Amit",
        "role": "tester"
    }
```

A test file can use the fixture:

```python
def test_user_role(sample_user):
    assert sample_user["role"] == "tester"
```

### Important Points

- `conftest.py` is used for shared pytest fixtures and configuration.
- Fixtures in a `conftest.py` file are available to applicable tests in its directory and subdirectories.
- Do not import fixtures from `conftest.py` directly.
- Keep file-specific fixtures near the tests that use them.
- Avoid placing every fixture in one file if that makes the project difficult to navigate.

## 11. Common Mistakes

- Repeating setup code instead of using a suitable fixture.
- Using a fixture with an unnecessarily broad scope.
- Modifying shared data and causing tests to interfere with one another.
- Forgetting cleanup for resources that need it.
- Using parametrization for unrelated scenarios.
- Providing incorrect expected results.
- Creating too many fixtures for simple, one-off values.
- Making parameter names unclear.
- Assuming fixtures and parametrization serve the same purpose.

