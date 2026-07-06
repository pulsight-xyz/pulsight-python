from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_mint_row import (
    PulsightInternalCoreDomainAggregatorMintRow,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    dex: list[str] | Unset = UNSET,
    hours: int | Unset = UNSET,
    min_pool_sol: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params["search"] = search

    params["sort"] = sort

    json_dex: list[str] | Unset = UNSET
    if not isinstance(dex, Unset):
        json_dex = dex

    params["dex"] = json_dex

    params["hours"] = hours

    params["min_pool_sol"] = min_pool_sol

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PulsightInternalCoreDomainAggregatorMintRow.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 402:
        response_402 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_402

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
    | list[PulsightInternalCoreDomainAggregatorMintRow]
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
    window: str,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    dex: list[str] | Unset = UNSET,
    hours: int | Unset = UNSET,
    min_pool_sol: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintRow]
]:
    """List Active Mints

     Returns the active-mint catalog with windowed stats. The activity gate is
    `hourly_mint_trader_activity`; rows ordered by window-bound activity desc. By default the list hides
    low-liquidity (dust / drained-pool) mints — see `min_pool_sol`.

    Args:
        window (str):
        search (str | Unset):
        sort (str | Unset):
        dex (list[str] | Unset):
        hours (int | Unset):
        min_pool_sol (float | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintRow]]
    """

    kwargs = _get_kwargs(
        window=window,
        search=search,
        sort=sort,
        dex=dex,
        hours=hours,
        min_pool_sol=min_pool_sol,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    window: str,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    dex: list[str] | Unset = UNSET,
    hours: int | Unset = UNSET,
    min_pool_sol: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintRow]
    | None
):
    """List Active Mints

     Returns the active-mint catalog with windowed stats. The activity gate is
    `hourly_mint_trader_activity`; rows ordered by window-bound activity desc. By default the list hides
    low-liquidity (dust / drained-pool) mints — see `min_pool_sol`.

    Args:
        window (str):
        search (str | Unset):
        sort (str | Unset):
        dex (list[str] | Unset):
        hours (int | Unset):
        min_pool_sol (float | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintRow]
    """

    return sync_detailed(
        client=client,
        window=window,
        search=search,
        sort=sort,
        dex=dex,
        hours=hours,
        min_pool_sol=min_pool_sol,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    window: str,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    dex: list[str] | Unset = UNSET,
    hours: int | Unset = UNSET,
    min_pool_sol: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintRow]
]:
    """List Active Mints

     Returns the active-mint catalog with windowed stats. The activity gate is
    `hourly_mint_trader_activity`; rows ordered by window-bound activity desc. By default the list hides
    low-liquidity (dust / drained-pool) mints — see `min_pool_sol`.

    Args:
        window (str):
        search (str | Unset):
        sort (str | Unset):
        dex (list[str] | Unset):
        hours (int | Unset):
        min_pool_sol (float | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintRow]]
    """

    kwargs = _get_kwargs(
        window=window,
        search=search,
        sort=sort,
        dex=dex,
        hours=hours,
        min_pool_sol=min_pool_sol,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    window: str,
    search: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    dex: list[str] | Unset = UNSET,
    hours: int | Unset = UNSET,
    min_pool_sol: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorMintRow]
    | None
):
    """List Active Mints

     Returns the active-mint catalog with windowed stats. The activity gate is
    `hourly_mint_trader_activity`; rows ordered by window-bound activity desc. By default the list hides
    low-liquidity (dust / drained-pool) mints — see `min_pool_sol`.

    Args:
        window (str):
        search (str | Unset):
        sort (str | Unset):
        dex (list[str] | Unset):
        hours (int | Unset):
        min_pool_sol (float | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorMintRow]
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            search=search,
            sort=sort,
            dex=dex,
            hours=hours,
            min_pool_sol=min_pool_sol,
            limit=limit,
            offset=offset,
        )
    ).parsed
