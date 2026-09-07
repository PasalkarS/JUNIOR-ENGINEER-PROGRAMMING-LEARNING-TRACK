"""Domain-specific exception hierarchy."""


class DomainException(Exception):
    """Base exception for all domain logic violations."""
    pass


class ValidationError(DomainException):
    """Raised when domain object validation fails."""
    pass


class InvalidOrderStateError(DomainException):
    """Raised when an illegal order lifecycle transition is attempted."""
    pass


class EntityNotFoundError(DomainException):
    """Raised when an expected entity does not exist."""
    pass
