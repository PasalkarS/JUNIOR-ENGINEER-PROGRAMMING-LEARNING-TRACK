# 1 — Test Basics

## 1. Introduction to Software Testing

### What it is
Software testing is the process of checking whether a program works as expected. It helps identify bugs, incorrect results, and unexpected behavior.

### Important Points
- Testing helps identify problems before software is released.
- Tests verify whether a program produces the expected results.
- Testing helps prevent existing functionality from breaking after code changes.
- Automated tests can be run repeatedly.
- Testing is a regular part of software development.

## 2. Introduction to pytest

### What it is
`pytest` is a Python testing framework used to write and execute automated tests. It provides simple assertions, automatic test discovery, fixtures, and detailed failure reports.

### Important Points
- Tests are written using Python functions.
- Test functions usually begin with `test_`.
- Test files usually begin with `test_` or end with `_test.py`.
- The `assert` statement checks expected results.
- pytest automatically discovers and runs tests.
- pytest supports unit tests, integration tests, fixtures, and parametrization.

### Installing pytest

```bash
pip install pytest
```

Check the installed version:

```bash
pytest --version
```

### Running Tests

Run all tests:

```bash
pytest
```

Run pytest using Python:

```bash
python -m pytest
```

Run tests with detailed output:

```bash
pytest -v
```

## 3. Test File and Function Naming

### What it is
pytest uses naming conventions to identify files and functions containing tests.

### Important Points
- Test files commonly start with `test_`.
- Test functions must start with `test_` to be discovered by default.
- Test names should describe the behavior being checked.
- Test files should be organized according to application functionality.
- Tests should be small and focused.

### Example Project Structure

```text
project/
├── calculator.py
└── tests/
    └── test_calculator.py
```

### Application File: `calculator.py`

```python
def add(num1, num2):
    return num1 + num2
```

### Test File: `test_calculator.py`

```python
from calculator import add

def test_add():
    result = add(10, 20)
    assert result == 30
```

The test calls `add()` and checks whether the returned value is correct.

## 4. Test Discovery

### What it is
Test discovery is the process by which pytest automatically finds test files, functions, and test classes.

### Important Points
- pytest searches for files using its naming conventions.
- Test functions normally start with `test_`.
- Test classes normally start with `Test`.
- Test methods inside test classes normally start with `test_`.
- Tests can be executed individually or as a complete suite.

### Running a Specific Test File

```bash
pytest tests/test_calculator.py
```

### Running a Specific Test Function

```bash
pytest tests/test_calculator.py::test_add
```

### Understanding Test Results

| Result | Meaning |
|---|---|
| `PASSED` | The test completed successfully. |
| `FAILED` | An assertion or another check failed. |
| `ERROR` | An error occurred during test setup or execution. |
| `SKIPPED` | The test was intentionally skipped. |

## 5. Assertions

### What it is
An assertion checks whether a condition is true. In testing, assertions compare actual results with expected results.

### Important Points
- Use `assert` to verify expected behavior.
- If the condition is true, the assertion passes.
- If the condition is false, the test fails.
- Assertions should check meaningful results.
- pytest provides detailed information when assertions fail.

### Basic Syntax

```python
assert condition
```

### Comparing Values

```python
def test_add():
    result = 10 + 20
    assert result == 30
```

### Checking Boolean Conditions

```python
def test_positive_number():
    number = 10
    assert number > 0
```

### Checking Strings

```python
def test_greeting():
    message = "Hello"
    assert message == "Hello"
```

### Checking Lists

```python
def test_product_list():
    products = ["Laptop", "Mouse", "Keyboard"]
    assert len(products) == 3
```

### Checking Membership

```python
def test_product_exists():
    products = ["Laptop", "Mouse", "Keyboard"]
    assert "Mouse" in products
```

## 6. Fixtures

### What it is
A fixture provides data, objects, or resources that a test needs. Fixtures help prepare the test environment and reduce repeated setup code.

### Important Points
- Fixtures are created using the `@pytest.fixture` decorator.
- A test requests a fixture through a function parameter.
- pytest automatically supplies the fixture value.
- Fixtures can provide sample data or prepare resources.
- Fixtures can also handle cleanup after tests.

### Example

```python
import pytest

@pytest.fixture
def product_price():
    return 500

def test_product_price(product_price):
    assert product_price == 500
```

### How It Works
1. The fixture provides the value `500`.
2. The test requests the fixture using its name.
3. pytest supplies the value to the test.
4. The assertion checks the result.

## 7. Setup and Teardown

### What it is
Setup prepares the data or resources needed before a test runs. Teardown cleans up resources after the test finishes.

### Important Points
- Setup prepares the test environment.
- Teardown removes temporary data or releases resources.
- Cleanup prevents tests from affecting one another.
- Fixtures can manage setup and teardown.
- The `yield` statement separates setup from cleanup in a fixture.

### Example

```python
import pytest

@pytest.fixture
def sample_products():
    products = ["Laptop", "Mouse"]

    yield products

    products.clear()

def test_product_count(sample_products):
    assert len(sample_products) == 2
```

The code before `yield` prepares the data. The code after `yield` runs during fixture cleanup after the test finishes.

## 8. Test Organization

### What it is
Test organization means arranging test files and functions so that tests are easy to find, understand, and maintain.

### Important Points
- Keep application code separate from test code.
- Group tests by module or functionality.
- Use descriptive test names.
- Avoid unnecessary duplication.
- Keep tests independent whenever possible.
- Place related tests in the same file or directory.

### Example Project Structure

```text
inventory_project/
├── inventory.py
├── validators.py
└── tests/
    ├── test_inventory.py
    └── test_validators.py
```

- `inventory.py` contains inventory-related functionality.
- `validators.py` contains input validation functions.
- `test_inventory.py` tests inventory behavior.
- `test_validators.py` tests validation behavior.

## 9. Writing Readable Tests

### What it is
Readable tests clearly explain what behavior is being checked and what result is expected.

### Important Points
- Use descriptive function names.
- Keep tests short and focused.
- Use meaningful variable names.
- Make expected results easy to identify.
- Avoid testing unrelated behaviors in one test.
- Write tests that communicate the intended behavior.

### Example

```python
def test_total_price():
    price = 100
    quantity = 3

    total = price * quantity

    assert total == 300
```

The function name and assertion clearly describe the expected behavior.

## 10. Common Testing Mistakes

### What it is
Testing mistakes can make tests unreliable, difficult to understand, or less useful for identifying defects.

### Important Points
- Using filenames that pytest does not discover.
- Forgetting the `test_` prefix in test functions.
- Writing assertions that do not verify expected behavior.
- Testing only successful inputs.
- Making tests depend on one another.
- Using unclear test names.
- Ignoring failed tests.
- Changing expected values just to make tests pass.
- Assuming passing tests prove that the entire program is bug-free.


