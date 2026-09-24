# Reusable Fixtures & Parametrized Tests

> **Module 06: Pytest & Testing | Topic 03**

## 1. Learning Outcomes
- **Pytest Fixtures:** Provide consistent setup and teardown for test dependencies using `@pytest.fixture`.
- **Built-in Fixtures:** Use `tmp_path` for temporary file I/O and `monkeypatch` for environment variables.
- **Parametrized Testing:** Run a single test logic across multiple input/output pairs using `@pytest.mark.parametrize`.
- **Eliminating Repetition:** Keep test suites DRY without sacrificing legibility.

## 2. Key Syntax & Concepts

### Parametrized Test Cases
```python
import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("user@domain.com", True),
    ("valid.name+tag@sub.example.co", True),
    ("missing_at_symbol", False),
    ("@nodomain.com", False),
    ("", False),
])
def test_is_valid_email(input_str: str, expected: bool):
    assert is_valid_email(input_str) == expected
```

### Temporary Path Fixture (`tmp_path`)
```python
def test_file_persistence(tmp_path):
    # tmp_path is a unique pathlib.Path created automatically per test
    test_file = tmp_path / "test_data.csv"
    test_file.write_text("id,val\n1,100\n", encoding="utf-8")
    
    loaded = read_csv(test_file)
    assert len(loaded) == 1
    assert loaded[0]["val"] == "100"
```

## 3. Common Mistakes & Gotchas
- **Hardcoded File Paths:** Using relative paths like `data/test.csv` pollutes workspace and fails concurrently. Always use `tmp_path`.
- **Overly Complex Fixture Hierarchies:** Deeply nested fixtures obscure what data a test relies upon.

## 4. Practice Tasks
- **Task 1:** Write a fixture providing a pre-populated SQLite in-memory database and test record insertion against it.

## 5. Self-Check Questions
- **Q1:** What is the primary benefit of `@pytest.mark.parametrize` over looping inside a test function?
- **Q2:** Does `tmp_path` persist after the pytest session finishes?
