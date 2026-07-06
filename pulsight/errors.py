"""Typed errors for the Pulsight API wire contract.

These map the 402/429/403 responses to first-class exceptions so callers
branch on type instead of string-matching. Used by the handwritten client
layer; the generated core in ``pulsight_api_client`` is never hand-edited.
"""
from __future__ import annotations

from typing import Optional

import httpx


class PulsightError(Exception):
    """Base class for every Pulsight client error."""


class CreditExhaustedError(PulsightError):
    """HTTP 402 CREDIT_EXHAUSTED — the api credit pool is empty this cycle."""

    def __init__(self, pool: str) -> None:
        self.pool = pool
        super().__init__(f"credit pool {pool!r} exhausted (HTTP 402)")


class RateLimitedError(PulsightError):
    """HTTP 429 — too many requests."""

    def __init__(self, retry_after: float) -> None:
        self.retry_after = retry_after
        super().__init__(f"rate limited, retry after {retry_after}s (HTTP 429)")


class MissingScopeError(PulsightError):
    """HTTP 403 — the api token lacks a required scope."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(f"{message} (HTTP 403)")


class APIError(PulsightError):
    """Any other non-2xx response."""

    def __init__(self, status_code: int, body: str) -> None:
        self.status_code = status_code
        self.body = body
        super().__init__(f"unexpected status {status_code}: {body}")


def credits_remaining(response: httpx.Response) -> Optional[int]:
    """Remaining api credits from the X-Credits-Remaining header, or None."""
    raw = response.headers.get("X-Credits-Remaining")
    if raw is None:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def raise_for_response(response: httpx.Response) -> None:
    """Map a non-2xx response to a typed PulsightError (no-op on 2xx)."""
    if 200 <= response.status_code < 300:
        return
    if response.status_code == 402:
        pool = ""
        try:
            pool = response.json().get("pool", "")
        except ValueError:
            pass
        raise CreditExhaustedError(pool)
    if response.status_code == 429:
        raise RateLimitedError(retry_after(response))
    if response.status_code == 403:
        message = "forbidden"
        try:
            message = response.json().get("error", message)
        except ValueError:
            pass
        raise MissingScopeError(message)
    raise APIError(response.status_code, response.text)


def retry_after(response: httpx.Response) -> float:
    """Seconds from the Retry-After header (0.0 when absent/unparseable)."""
    raw = response.headers.get("Retry-After")
    if not raw:
        return 0.0
    try:
        return float(raw)
    except ValueError:
        return 0.0
