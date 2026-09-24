# Python Standard Logging & Structured Logs

> **Module 11: Debugging & Logging | Topic 03**

## 1. Learning Outcomes
- **Why Logging > `print()`:** Use the standard `logging` library for configurable levels, timestamps, and log destinations.
- **The 5 Standard Levels:** DEBUG, INFO, WARNING, ERROR, and CRITICAL.
- **Exception Logging:** Capture full stack traces automatically using `logger.exception()`.
- **Security in Logs:** Prevent passwords, API keys, and sensitive PII from leaking into log files.

## 2. Key Syntax & Concepts

### Production Logging Configuration
```python
import logging
from pathlib import Path

# Create dedicated logger instance
logger = logging.getLogger("OrderService")
logger.setLevel(logging.INFO)

# Formatter including timestamp, level, logger name, and message
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File Handler
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Usage
logger.info("Service initialized successfully.")

try:
    result = 10 / 0
except ZeroDivisionError:
    # logger.exception automatically appends full traceback!
    logger.exception("Calculation failed due to zero division")
```

## 3. Common Mistakes & Gotchas
- **Using `root` Logger:** Calling `logging.info()` configures root logger. Use `logging.getLogger(__name__)` for granular per-module control.
- **Logging Passwords:** Never write `logger.info(f"User login attempt with password: {pwd}")`. Mask credentials.

## 4. Practice Tasks
- **Task 1:** Configure a logger that writes WARNING and above to `errors.log` while printing all INFO messages to the terminal.

## 5. Self-Check Questions
- **Q1:** What is the advantage of `logger.exception()` over `logger.error()` inside an `except` block?
- **Q2:** Arrange the 5 standard logging levels in ascending order of severity.
