from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_dashboard_stats import (
    InternalAdaptersPrimaryHttpHandlerDashboardStats,
)
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/strategies/dashboard",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = InternalAdaptersPrimaryHttpHandlerDashboardStats.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Strategy Dashboard Stats

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerDashboardStats | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Strategy Dashboard Stats

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerDashboardStats | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Strategy Dashboard Stats

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerDashboardStats | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerDashboardStats
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Strategy Dashboard Stats

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerDashboardStats | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
