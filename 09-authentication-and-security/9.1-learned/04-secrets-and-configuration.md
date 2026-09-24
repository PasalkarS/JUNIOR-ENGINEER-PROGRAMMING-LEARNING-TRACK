# Secrets Management & Environment Configuration

> **Module 09: Authentication & Security | Topic 04**

## 1. Learning Outcomes
- **Zero Secrets in Code:** Eliminate API keys, database passwords, and private tokens from source repositories.
- **Environment Variables:** Load configuration via `os.environ` and `.env` files.
- **The Twelve-Factor Config Rule:** Store configuration in the environment, separating code from secrets.
- **Safe Logging:** Redact and mask sensitive tokens before writing application logs.

## 2. Key Syntax & Concepts

### Safe Configuration Ingestion
```python
import os
from pathlib import Path

class AppConfig:
    def __init__(self):
        self.db_host = os.environ.get("DB_HOST", "localhost")
        self.db_port = int(os.environ.get("DB_PORT", "5432"))
        
        # Mandatory secret: fail fast if missing
        api_key = os.environ.get("PAYMENT_API_KEY")
        if not api_key:
            raise EnvironmentError("Critical: PAYMENT_API_KEY environment variable is not set!")
        self.api_key = api_key

    def safe_repr(self) -> str:
        # Mask sensitive key for safe logging
        masked_key = self.api_key[:4] + "..." + self.api_key[-4:]
        return f"Config(host={self.db_host}, port={self.db_port}, api_key={masked_key})"
```

## 3. Common Mistakes & Gotchas
- **Committing `.env` to Git:** Never commit `.env` files containing secrets. Add `.env` to `.gitignore` and supply `.env.example` with dummy values.
- **Logging Authorization Headers:** Printing raw request headers to logs inadvertently stores customer bearer tokens in log files.

## 4. Practice Tasks
- **Task 1:** Create an `.env.example` template and a Python config loader that validates all required variables exist on startup.

## 5. Self-Check Questions
- **Q1:** Why is storing secrets in environment variables safer than hardcoding them in source files?
- **Q2:** What is the purpose of an `.env.example` file?
