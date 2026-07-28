from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_sol_price_response import (
    InternalAdaptersPrimaryHttpHandlerSolPriceResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/sol-price",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
    | None
):
    if response.status_code == 200:
        response_200 = InternalAdaptersPrimaryHttpHandlerSolPriceResponse.from_dict(
            response.json()
        )

        return response_200

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
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
]:
    """Get the SOL/USD reference rate

     Returns USD per 1 SOL — the same volume-weighted WSOL/USDC reference the token catalog prices market
    caps and USD candles with, so displayed figures agree with computed ones. `sol_usd` is `null` when
    the reference is unavailable (cold analytics store, or no WSOL/USDC trade in the lookback window);
    it is never `0`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerSolPriceResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
    | None
):
    """Get the SOL/USD reference rate

     Returns USD per 1 SOL — the same volume-weighted WSOL/USDC reference the token catalog prices market
    caps and USD candles with, so displayed figures agree with computed ones. `sol_usd` is `null` when
    the reference is unavailable (cold analytics store, or no WSOL/USDC trade in the lookback window);
    it is never `0`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
]:
    """Get the SOL/USD reference rate

     Returns USD per 1 SOL — the same volume-weighted WSOL/USDC reference the token catalog prices market
    caps and USD candles with, so displayed figures agree with computed ones. `sol_usd` is `null` when
    the reference is unavailable (cold analytics store, or no WSOL/USDC trade in the lookback window);
    it is never `0`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerSolPriceResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
    | None
):
    """Get the SOL/USD reference rate

     Returns USD per 1 SOL — the same volume-weighted WSOL/USDC reference the token catalog prices market
    caps and USD candles with, so displayed figures agree with computed ones. `sol_usd` is `null` when
    the reference is unavailable (cold analytics store, or no WSOL/USDC trade in the lookback window);
    it is never `0`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerSolPriceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
