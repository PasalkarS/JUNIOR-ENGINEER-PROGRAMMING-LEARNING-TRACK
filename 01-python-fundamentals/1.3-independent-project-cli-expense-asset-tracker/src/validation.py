"""
Input validation utilities for expenses and assets.
"""
from datetime import datetime

class ValidationError(Exception):
    """Raised when record input fails validation."""
    pass

def validate_amount(amount_input) -> float:
    try:
        val = float(amount_input)
    except (TypeError, ValueError) as e:
        raise ValidationError(f"Amount must be a valid number, got {amount_input!r}") from e
    if val <= 0:
        raise ValidationError(f"Amount must be greater than zero, got {val}")
    return round(val, 2)

def validate_date(date_str: str) -> str:
    if not isinstance(date_str, str) or not date_str.strip():
        return datetime.now().strftime("%Y-%m-%d")
    date_str = date_str.strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError as e:
        raise ValidationError(f"Date must be in YYYY-MM-DD format, got {date_str!r}") from e

def validate_text(text: str, field_name: str) -> str:
    if not isinstance(text, str) or not text.strip():
        raise ValidationError(f"{field_name} cannot be empty.")
    return text.strip()
