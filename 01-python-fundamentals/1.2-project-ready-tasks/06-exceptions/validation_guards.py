# Input Validation & Defensive Guards
# Demonstrates verifying input constraints and raising explicit errors.

class ValidationError(Exception):
    """Base exception for data validation errors."""
    pass

class NegativeValueError(ValidationError):
    """Raised when a numerical value is negative."""
    pass

def validate_age(age_val) -> int:
    try:
        val = int(age_val)
    except (TypeError, ValueError) as err:
        raise ValidationError(f"Age must be a valid integer, got {age_val!r}") from err

    if val < 0 or val > 120:
        raise ValidationError(f"Age must be between 0 and 120, got {val}")
    return val

def validate_email(email: str) -> str:
    if not isinstance(email, str) or "@" not in email or "." not in email:
        raise ValidationError(f"Invalid email address format: {email!r}")
    return email.strip().lower()

if __name__ == "__main__":
    # Test valid
    print("Valid age:", validate_age("25"))
    print("Valid email:", validate_email(" user@example.com "))

    # Test caught exception
    try:
        validate_age("-5")
    except ValidationError as e:
        print("[CAUGHT EXPECTED ERROR]:", e)
