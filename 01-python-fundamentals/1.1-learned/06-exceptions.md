# Exception Handling & Defensive Programming

> **Module 01: Python Fundamentals | Topic 06**



## 1. Learning Outcomes

- **Try-Except Blocks:** Catch and recover from expected operational exceptions gracefully.
- **Else & Finally:** Use `else` for success path and `finally` for guaranteed cleanup.
- **Raising Errors:** Raise built-in and custom domain exceptions with informative messages.
- **Defensive Programming:** Validate inputs at public boundaries before execution.

## 2. Key Syntax & Structure

```python
def parse_positive_int(text: str) -> int:
    try:
        val = int(text)
    except ValueError as e:
        raise ValueError(f'Invalid integer string: {text}') from e
    else:
        if val <= 0:
            raise ValueError(f'Value must be positive, got {val}')
        return val
    finally:
        # Runs under all conditions (cleanup actions)
        pass
```


### Creating Custom Exceptions

```python
class ValidationError(Exception):
    """Raised when input data fails domain business rules."""
    pass

class InsufficientFundsError(ValidationError):
    """Raised when account balance is lower than withdrawal."""
    pass
```


## 3. Common Mistakes & Gotchas

- **Bare Except Trap:** NEVER write `except:`. It catches SystemExit and KeyboardInterrupt (Ctrl+C), making the program un-killable. Always catch specific exceptions: `except (ValueError, KeyError):`.
- **Swallowing Errors Silently:** Writing `except Exception: pass` hides bugs completely and makes debugging nearly impossible.

## 4. Practice Tasks & Self-Check

- **Task 1:** Create a safe user input utility function that loops until valid numeric input is provided.
- **Q1:** When does the `else` block in a try-except structure execute?
