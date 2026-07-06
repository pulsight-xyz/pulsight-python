"""pulsight — official Python client for the Pulsight API.

The handwritten ergonomic layer (auth, typed errors, retry) lives here; the
generated protocol core is the sibling ``pulsight_api_client`` package
(emitted by ``make sdk-python``, never hand-edited).
"""
from .client import DEFAULT_BASE_URL, build_client
from .errors import (
    APIError,
    CreditExhaustedError,
    MissingScopeError,
    PulsightError,
    RateLimitedError,
    credits_remaining,
    raise_for_response,
)

__all__ = [
    "build_client",
    "DEFAULT_BASE_URL",
    "PulsightError",
    "CreditExhaustedError",
    "RateLimitedError",
    "MissingScopeError",
    "APIError",
    "credits_remaining",
    "raise_for_response",
]
__version__ = "0.0.0"
