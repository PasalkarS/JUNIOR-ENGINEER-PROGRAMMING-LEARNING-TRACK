# Integration Testing & End-to-End Verification

> **Module 06: Pytest & Testing | Topic 05**

## 1. Learning Outcomes
- **Integration Scope:** Verify interactions across real boundaries (Database + Repository + Service).
- **Test Environments:** Spin up isolated SQLite databases or temporary file systems for integration testing.
- **Distinguishing Failures:** Separate database connection errors from domain calculation bugs.
- **Test Pyramid:** Balance fast, abundant unit tests with focused, essential integration tests.

## 2. Key Syntax & Concepts

### Database Integration Test
```python
import pytest
import sqlite3
from pathlib import Path

@pytest.fixture
def db_conn(tmp_path):
    db_file = tmp_path / "integration_test.db"
    conn = sqlite3.connect(db_file)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);")
    conn.commit()
    yield conn
    conn.close()

def test_user_repository_integration(db_conn):
    repo = SqliteUserRepository(db_conn)
    repo.save({"id": 1, "name": "Alice"})
    
    loaded = repo.get(1)
    assert loaded["name"] == "Alice"
```

## 3. Common Mistakes & Gotchas
- **Shared State Pollution:** Tests writing to the same database file without resetting between runs cause order-dependent failures.
- **Slow Test Suites:** Too many integration tests make test suites sluggish. Reserve integration tests for critical cross-boundary workflows.

## 4. Practice Tasks
- **Task 1:** Build an end-to-end integration test that writes a CSV, runs the data cleaning transformer, and verifies the SQLite output table.

## 5. Self-Check Questions
- **Q1:** What distinguishes a unit test from an integration test?
- **Q2:** Why does `yield` inside a pytest fixture represent the boundary between setup and teardown?
