from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_mint_migration import (
    PulsightInternalCoreDomainAggregatorMintMigration,
)
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/migrations".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                PulsightInternalCoreDomainAggregatorMintMigration.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

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
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
]:
    """List Mint Migrations

     Returns bonding-curve → AMM graduation events (PumpFun → PumpSwap, Raydium Launchpad → CPMM, Meteora
    DBC → DAMM v2, etc.) for a single mint.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintMigration]]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
    | None
):
    """List Mint Migrations

     Returns bonding-curve → AMM graduation events (PumpFun → PumpSwap, Raydium Launchpad → CPMM, Meteora
    DBC → DAMM v2, etc.) for a single mint.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintMigration]
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
]:
    """List Mint Migrations

     Returns bonding-curve → AMM graduation events (PumpFun → PumpSwap, Raydium Launchpad → CPMM, Meteora
    DBC → DAMM v2, etc.) for a single mint.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintMigration]]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintMigration]
    | None
):
    """List Mint Migrations

     Returns bonding-curve → AMM graduation events (PumpFun → PumpSwap, Raydium Launchpad → CPMM, Meteora
    DBC → DAMM v2, etc.) for a single mint.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintMigration]
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
