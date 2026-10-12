# 2 — Unit Tests

## 1. What Is Unit Testing?

Unit testing is the process of testing a small, individual part of a program to check whether it works correctly.

A unit is usually a function, method, or small piece of logic.

**Example:** If a function calculates the total price of products, a unit test checks whether it returns the correct total.

### Important Points
- Tests one small part of the program at a time.
- Helps identify errors early.
- Makes code easier to maintain.
- Tests expected behavior rather than internal implementation details.
- Unit tests should be fast and independent.

## 2. Testing Pure Functions

A pure function returns the same output when given the same input and does not change anything outside the function.

### Example

```python
def add_numbers(a, b):
    return a + b
```

### Unit Test

```python
def test_add_numbers():
    assert add_numbers(5, 3) == 8
```

### Important Points
- A pure function is easy to test because its output depends only on its inputs.
- Tests should check different valid inputs.
- Functions that depend on files, databases, or APIs may require additional testing techniques.

## 3. Testing Expected Behavior

Tests should verify what a function is supposed to do.

For example, a discount calculator should return the correct discounted price.

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)
```

```python
def test_calculate_discount():
    assert calculate_discount(1000, 10) == 900
```

### Important Points
- Check the expected output for a given input.
- Use clear test names that describe the behavior being tested.
- Test meaningful scenarios instead of writing tests only to increase the test count.

## 4. Testing Boundary Conditions

Boundary conditions are values at the limits of the accepted input range.

Errors often occur when a program handles values at these limits.

For example, a function that checks whether someone is eligible to vote may need to handle the minimum eligible age.

```python
def is_eligible_to_vote(age):
    return age >= 18
```

```python
def test_below_eligible_age():
    assert is_eligible_to_vote(17) == False

def test_at_eligible_age():
    assert is_eligible_to_vote(18) == True

def test_above_eligible_age():
    assert is_eligible_to_vote(19) == True
```

### Important Points
- Test values below the boundary.
- Test the exact boundary value.
- Test values above the boundary.
- Include zero, empty values, or maximum values when relevant to the function.

## 5. Testing Invalid Inputs

Invalid inputs are values that a function should reject or handle safely.

For example, a function that divides two numbers should not allow division by zero.

```python
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

### Testing Exceptions with pytest

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
```

### Important Points
- Test inputs that violate the function's requirements.
- Check whether the expected exception is raised.
- Avoid allowing invalid inputs to produce misleading results.
- Use `pytest.raises()` to verify that an exception occurs.

## 6. Testing Different Input Types

Functions may receive different types of input, such as integers, strings, lists, or `None`.

Tests should cover the input types the function is expected to support.

Example:

```python
def get_name_length(name):
    return len(name)
```

```python
def test_get_name_length():
    assert get_name_length("Python") == 6

def test_empty_name():
    assert get_name_length("") == 0
```

If a function accepts only strings, tests should also verify how it handles unsupported input types when that behavior is defined.

### Important Points
- Test normal inputs.
- Test empty inputs.
- Test supported data types.
- Test unsupported types when relevant.
- Do not assume every function must accept every possible input type.

## 7. Testing Deterministic Behavior

A deterministic function produces the same result when given the same input under the same conditions.

Unit tests should generally be deterministic so that they pass consistently.

Example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

```python
def test_calculate_total():
    assert calculate_total(100, 3) == 300
```

### Important Points
- The same inputs should produce predictable outputs.
- Avoid relying on random values unless randomness is controlled.
- Avoid depending on the current time or external services in ordinary unit tests.
- Use controlled test data to make results repeatable.

## 8. Testing Functions That Return Different Results

A function may return different results depending on its input or conditions.

Each important outcome should be tested.

Example:

```python
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
```

```python
def test_positive_number():
    assert check_number(5) == "Positive"

def test_negative_number():
    assert check_number(-5) == "Negative"

def test_zero():
    assert check_number(0) == "Zero"
```

### Important Points
- Test every meaningful branch of the function.
- Include cases for `if`, `elif`, and `else` when present.
- Check that each branch produces the expected result.

## 9. Test Coverage

Test coverage measures how much of the code is executed while tests run.

Common types include:

- **Line coverage:** Measures which lines of code are executed.
- **Branch coverage:** Measures which decision paths are executed.
- **Function coverage:** Measures which functions are called by tests.

Coverage can be measured using the `pytest-cov` plugin.

Install it:

```bash
pip install pytest-cov
```

Run tests with coverage:

```bash
pytest --cov=.
```

Generate a detailed terminal report:

```bash
pytest --cov=. --cov-report=term-missing
```

### Important Points
- High coverage does not automatically mean the code is tested well.
- A test can execute a line without checking whether its result is correct.
- Focus on meaningful assertions and important behavior.
- Use coverage reports to identify areas that may need more tests.

## 10. Testing Without Depending on Implementation Details

Tests should focus on what a function does, not unnecessarily on how it does it.

For example, if a function calculates a total, test the returned total rather than requiring the function to use a particular variable name or internal calculation sequence.

### Important Points
- Test observable behavior.
- Avoid tying tests to internal variable names.
- Avoid checking private implementation details unless there is a specific reason.
- Well-designed tests should continue to work when internal code is refactored without changing its behavior.

## 11. Common Unit Testing Mistakes

- Testing only normal inputs and ignoring edge cases.
- Writing tests without meaningful assertions.
- Testing multiple unrelated behaviors in one test.
- Depending on external services unnecessarily.
- Using unclear test names.
- Ignoring invalid input scenarios.
- Assuming high coverage guarantees correctness.
- Writing tests that depend on the execution order of other tests.

