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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pubkey: str,
    *,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/top-holders".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                PulsightInternalCoreDomainAggregatorMintTraderRow.from_dict(
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
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
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
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
]:
    """List Mint Top Holders

     Current holders (token_balance > 0) of one mint from `trader_token_stats`. sort ∈
    {balance,holding_pnl,recent} (default balance). Paged via offset.

    Args:
        pubkey (str):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintTraderRow]]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
    | None
):
    """List Mint Top Holders

     Current holders (token_balance > 0) of one mint from `trader_token_stats`. sort ∈
    {balance,holding_pnl,recent} (default balance). Paged via offset.

    Args:
        pubkey (str):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
]:
    """List Mint Top Holders

     Current holders (token_balance > 0) of one mint from `trader_token_stats`. sort ∈
    {balance,holding_pnl,recent} (default balance). Paged via offset.

    Args:
        pubkey (str):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintTraderRow]]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
    | None
):
    """List Mint Top Holders

     Current holders (token_balance > 0) of one mint from `trader_token_stats`. sort ∈
    {balance,holding_pnl,recent} (default balance). Paged via offset.

    Args:
        pubkey (str):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintTraderRow]
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
