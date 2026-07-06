"""Authenticated httpx client builder for the Pulsight API.

The generated ``pulsight_api_client`` package handles request/response
models; this layer adds api-token auth and 429 retry. Map responses to
typed errors with ``pulsight.raise_for_response``. See README for wiring
the generated client.
"""
from __future__ import annotations

import time

import httpx

from .errors import retry_after

DEFAULT_BASE_URL = "https://pulsight.xyz"


class _AuthAndRetryTransport(httpx.BaseTransport):
    """Injects the api token on every request and retries idempotent
    (GET/HEAD) requests on 429, honouring Retry-After."""

    def __init__(self, token: str, retries: int, inner: httpx.BaseTransport) -> None:
        self._token = token
        self._retries = retries
        self._inner = inner

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        # The wire uses the Authorization header; docs call it an "api token".
        request.headers["Authorization"] = f"Bearer {self._token}"
        attempts = 1 + (self._retries if request.method in ("GET", "HEAD") else 0)

        response = self._inner.handle_request(request)
        for attempt in range(1, attempts):
            if response.status_code != 429:
                return response
            response.read()
            response.close()
            wait = retry_after(response) or min(2 ** attempt * 0.2, 5.0)
            time.sleep(wait)
            response = self._inner.handle_request(request)
        return response


def build_client(
    token: str,
    base_url: str = DEFAULT_BASE_URL,
    retries: int = 2,
    timeout: float = 30.0,
) -> httpx.Client:
    """Build an authenticated httpx.Client to hand to the generated
    AuthenticatedClient (see README)."""
    transport = _AuthAndRetryTransport(token, retries, httpx.HTTPTransport())
    return httpx.Client(base_url=base_url, transport=transport, timeout=timeout)
