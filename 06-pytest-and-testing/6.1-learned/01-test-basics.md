# Testing Foundations & Pytest Discovery

> **Module 06: Pytest & Testing | Topic 01**

## 1. Learning Outcomes
- **The Value of Testing:** Understand automated verification over manual repetitive testing.
- **Test Discovery:** Structure test files (`test_*.py`), functions (`def test_*()`), and test suites.
- **Plain Assertions:** Leverage Python's native `assert` statement with rich pytest failure diffs.
- **Running Pytest:** Execute tests with `-v` (verbose), `-q` (quiet), `-k` (keyword filter), and `--tb=short`.

## 2. Key Syntax & Structure

### Minimal Test File Structure
```python
# test_math_operations.py

def add(a: float, b: float) -> float:
    return a + b

def test_add_positive_numbers():
    assert add(2.0, 3.5) == 5.5

def test_add_negative_numbers():
    assert add(-4.0, 1.0) == -3.0
```

### CLI Execution Flags
```bash
# Run all discovered tests verbosely
pytest -v

# Run tests matching a name pattern
pytest -k "add"

# Stop immediately upon first test failure
pytest -x

# Show print statements inside passing tests
pytest -s
```

## 3. Common Mistakes & Gotchas
- **Naming Files Incorrectly:** Naming test files without `test_` prefix (e.g., `tests.py`) prevents pytest discovery.
- **Testing Multiple Unrelated Behaviors in One Test:** If the first assertion fails, subsequent assertions are skipped. Keep tests focused.

## 4. Practice Tasks
- **Task 1:** Write 3 unit tests verifying a string slugify function (`"Hello World" -> "hello-world"`).

## 5. Self-Check Questions
- **Q1:** How does pytest find test functions automatically?
- **Q2:** Why is plain `assert expr` in pytest superior to unittest's `self.assertEqual()`?
