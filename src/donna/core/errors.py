class DonnaError(Exception):
    """Base application error."""


class NotFoundError(DonnaError):
    """Raised when an entity cannot be found."""


class PermissionDeniedError(DonnaError):
    """Raised when the current user may not perform an action."""
