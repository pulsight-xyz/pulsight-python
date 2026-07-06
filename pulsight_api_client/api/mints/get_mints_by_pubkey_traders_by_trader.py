from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_mint_trader_row import (
    PulsightInternalCoreDomainAggregatorMintTraderRow,
)
from ...types import Response


def _get_kwargs(
    pubkey: str,
    trader: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/traders/{trader}".format(
            pubkey=quote(str(pubkey), safe=""),
            trader=quote(str(trader), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintTraderRow
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorMintTraderRow.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 404:
        response_404 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_404

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
    | PulsightInternalCoreDomainAggregatorMintTraderRow
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    trader: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintTraderRow
]:
    """Get Mint Trader Stats

     Single per-(trader, mint) stats row (same shape as a top-traders row) from `trader_token_stats`. 404
    when the trader never traded the mint.

    Args:
        pubkey (str):
        trader (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintTraderRow]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        trader=trader,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    trader: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintTraderRow
    | None
):
    """Get Mint Trader Stats

     Single per-(trader, mint) stats row (same shape as a top-traders row) from `trader_token_stats`. 404
    when the trader never traded the mint.

    Args:
        pubkey (str):
        trader (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintTraderRow
    """

    return sync_detailed(
        pubkey=pubkey,
        trader=trader,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    trader: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintTraderRow
]:
    """Get Mint Trader Stats

     Single per-(trader, mint) stats row (same shape as a top-traders row) from `trader_token_stats`. 404
    when the trader never traded the mint.

    Args:
        pubkey (str):
        trader (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintTraderRow]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        trader=trader,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    trader: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintTraderRow
    | None
):
    """Get Mint Trader Stats

     Single per-(trader, mint) stats row (same shape as a top-traders row) from `trader_token_stats`. 404
    when the trader never traded the mint.

    Args:
        pubkey (str):
        trader (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintTraderRow
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            trader=trader,
            client=client,
        )
    ).parsed
