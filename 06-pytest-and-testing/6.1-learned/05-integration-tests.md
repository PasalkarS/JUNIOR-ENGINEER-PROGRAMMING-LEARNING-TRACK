# 5 — Integration Tests

## 1. Introduction to Integration Testing

Integration testing checks whether two or more components of an application work correctly together.

Unlike unit testing, which focuses on individual functions or components, integration testing focuses on the interactions between them.

For example, an application may contain a service, a repository, and a database. An integration test checks whether the service can use the repository to store and retrieve data correctly.

### Important Points

- Tests interactions between multiple components.
- Helps identify errors that individual unit tests may not detect.
- Verifies that components exchange data correctly.
- Can involve databases, files, APIs, and other resources.
- Usually takes longer to run than unit tests.

## 2. Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
|---|---|
| Tests a small unit of code | Tests interactions between components |
| Usually isolates dependencies | Often uses real components and controlled resources |
| Commonly uses mocks | May use real databases, repositories, or services |
| Usually fast | May take longer |
| Finds errors in individual logic | Finds errors in component interactions |

### Example

Consider an order management application.

- A unit test checks whether an order total is calculated correctly.
- An integration test checks whether an order can be created, saved to a database, and retrieved correctly.

Both types of testing are important because they identify different kinds of problems.

## 3. Testing Component Interactions

An application often has multiple layers that work together.

For example:

- **Service layer:** Contains application or business logic.
- **Repository layer:** Handles data access.
- **Database layer:** Stores persistent information.

An integration test checks whether these layers communicate correctly.

### Example

When a customer creates an order, the application may need to:

1. Receive the order details.
2. Process the order through a service.
3. Save the order through a repository.
4. Store the order in a database.
5. Retrieve the saved order.

An integration test can verify that the complete interaction works as expected.

### Important Points

- Test realistic interactions between components.
- Check that data is passed correctly between layers.
- Verify that saved data can be retrieved.
- Test important error conditions at component boundaries.
- Keep tests focused on a clear integration behavior.

## 4. Testing Repositories

A repository is a component responsible for accessing and managing stored data.

Repository integration tests commonly use a real test database to verify that database operations work correctly.

Typical operations include:

- Creating a record.
- Retrieving a record.
- Updating a record.
- Deleting a record.
- Searching or filtering records.

### Example

Suppose an application stores products in a database. A repository may provide methods to save and retrieve products.

An integration test should verify that a product saved through the repository can be retrieved with the correct values.

### Important Points

- Test actual database operations when verifying repository integration.
- Verify that stored values match the original data.
- Test missing records and invalid operations where relevant.
- Check that database constraints behave as expected.
- Use a separate test database rather than modifying production data.

## 5. Using SQLite for Integration Tests

SQLite is useful for local integration tests because it can create a lightweight database without requiring a separate database server.

Python provides SQLite support through the built-in `sqlite3` module.

A database created with `":memory:"` exists only in memory and is useful for isolated tests.

### Example

```python id="s4l1nb"
import sqlite3

def test_database_insert_and_read():
    connection = sqlite3.connect(":memory:")

    connection.execute(
        "CREATE TABLE products (id INTEGER, name TEXT)"
    )

    connection.execute(
        "INSERT INTO products VALUES (?, ?)",
        (1, "Keyboard")
    )

    connection.commit()

    result = connection.execute(
        "SELECT name FROM products WHERE id = ?",
        (1,)
    ).fetchone()

    assert result == ("Keyboard",)

    connection.close()
```

### Important Points

- `sqlite3.connect(":memory:")` creates an in-memory database.
- SQL statements create the table and insert the record.
- Parameterized queries help prevent SQL injection.
- `fetchone()` retrieves one matching row.
- Assertions verify the actual database result.
- The connection should be closed after the test.

## 6. Preparing Test Resources

Integration tests often require resources such as databases, temporary directories, files, or test configurations.

These resources should be prepared before the test and cleaned up afterward.

Pytest fixtures are commonly used to manage this setup and cleanup.

### Example

```python id="c4t9np"
import sqlite3
import pytest

@pytest.fixture
def database():
    connection = sqlite3.connect(":memory:")

    connection.execute(
        "CREATE TABLE users (id INTEGER, name TEXT)"
    )

    yield connection

    connection.close()

def test_insert_user(database):
    database.execute(
        "INSERT INTO users VALUES (?, ?)",
        (1, "Riya")
    )

    result = database.execute(
        "SELECT name FROM users WHERE id = ?",
        (1,)
    ).fetchone()

    assert result == ("Riya",)
```

### Important Points

- Fixtures keep test setup reusable.
- Each test can receive its own database connection.
- Cleanup prevents resources from remaining open.
- Tests should not depend on records created by unrelated tests.
- A fresh test database helps keep tests independent and repeatable.

## 7. Testing Data Persistence

Persistence means that data is stored and can be retrieved later.

Integration tests can verify that an application's repository correctly saves, retrieves, updates, and deletes records.

### Important Points

- Verify that inserted records can be retrieved.
- Confirm that updates change the expected values.
- Confirm that deleted records are no longer available.
- Test duplicate records and constraints where relevant.
- Check that the repository handles missing records correctly.
- Verify that data types and relationships are handled as expected.

## 8. Testing Transactions and Rollbacks

A transaction groups database operations into a unit of work.

A successful transaction can be committed, while a failed transaction can be rolled back.

Integration tests can verify that database changes behave correctly when an operation succeeds or fails.

### Important Points

- Verify that successful operations are saved.
- Verify that failed operations do not leave unintended changes.
- Test rollback behavior when the application uses transactions.
- Check that database connections remain usable after errors.
- Avoid leaving test data behind in shared databases.

## 9. Testing Error Handling Between Components

Errors may occur when one component receives unexpected data or when a dependency fails.

Integration tests can check whether these errors are handled correctly across component boundaries.

Examples include:

- A repository cannot find a requested record.
- A database constraint rejects invalid data.
- A service receives an unexpected repository result.
- A file is missing when another component tries to read it.
- A remote service returns an error.

### Important Points

- Test important failure scenarios, not only successful operations.
- Verify that errors are handled or propagated as intended.
- Check that failed operations do not corrupt data.
- Avoid making tests depend on unpredictable external failures.
- Use controlled test resources to reproduce failure conditions.

## 10. Integration Testing with Mocks and Real Dependencies

Integration tests often use real components to verify their interactions, but not every dependency must be real.

For example, an order service and its repository may use a real test database, while an external payment gateway is mocked.

The correct choice depends on what the test needs to verify.

### Important Points

- Use real components for the interactions being tested.
- Use controlled test resources instead of production systems.
- Mock unrelated external services when necessary.
- Do not mock the exact interaction you are trying to verify.
- Test external integrations separately when their real behavior matters.

## 11. Test Isolation and Cleanup

Test isolation means that one test does not depend on another test's execution or results.

Integration tests need particular attention because they may create records, files, or other resources.

### Important Points

- Use separate test data for each test where practical.
- Reset or recreate databases when appropriate.
- Close database connections and files.
- Remove temporary files after testing.
- Avoid relying on test execution order.
- Ensure failed tests do not leave resources in an unexpected state.

## 12. Organizing Integration Tests

Integration tests should be organized so that they are easy to identify and maintain.

A project may separate unit and integration tests into different files or directories.

### Example Structure

```text id="9w8m4k"
project/
│
├── app.py
├── repositories.py
├── services.py
│
└── tests/
    ├── unit/
    │   ├── test_services.py
    │   └── test_validators.py
    │
    └── integration/
        ├── test_repository_database.py
        └── test_order_workflow.py
```

### Important Points

- Keep integration tests separate when it improves clarity.
- Use descriptive file and test names.
- Make any required test resources clear.
- Ensure integration tests can be run repeatedly.
- Keep tests focused on specific component interactions.

## 13. Running Integration Tests with pytest

Pytest can discover and run integration tests using the same commands used for other tests.

Run all tests:

```bash id="f6k9rq"
pytest
```

Run only the integration test directory:

```bash id="t4p3vs"
pytest tests/integration/
```

Run a specific integration test file:

```bash id="z9v5xq"
pytest tests/integration/test_repository_database.py
```

### Important Points

- Pytest does not require a separate testing framework for integration tests.
- Tests should follow pytest's discovery conventions.
- Integration tests may require additional setup or configuration.
- Keep test environments separate from production environments.

## 14. Common Integration Testing Mistakes

- Using a production database for testing.
- Sharing test data between tests unintentionally.
- Forgetting to close database connections.
- Testing only successful operations.
- Mocking the component interaction that needs to be verified.
- Depending on test execution order.
- Failing to clean up temporary resources.
- Writing tests that depend on unreliable network services.
- Assuming unit tests alone prove that all components work together.

