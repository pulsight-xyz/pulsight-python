from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_trader_filter import (
    PulsightInternalCoreDomainTraderFilter,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/trader-filters/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PulsightInternalCoreDomainTraderFilter.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 500:
        response_500 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
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
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
]:
    """List Trader Filters

     Returns all saved filter presets belonging to the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderFilter]]
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
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
    | None
):
    """List Trader Filters

     Returns all saved filter presets belonging to the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderFilter]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
]:
    """List Trader Filters

     Returns all saved filter presets belonging to the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderFilter]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderFilter]
    | None
):
    """List Trader Filters

     Returns all saved filter presets belonging to the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderFilter]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
