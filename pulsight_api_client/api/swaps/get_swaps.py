from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_trade import (
    PulsightInternalCoreDomainAggregatorTrade,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mint: str | Unset = UNSET,
    trader: str | Unset = UNSET,
    pool: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    before_ts: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["mint"] = mint

    params["trader"] = trader

    params["pool"] = pool

    params["from"] = from_

    params["to"] = to

    params["from_ts"] = from_ts

    params["to_ts"] = to_ts

    params["before_ts"] = before_ts

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/swaps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorTrade]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PulsightInternalCoreDomainAggregatorTrade.from_dict(
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
    | list[PulsightInternalCoreDomainAggregatorTrade]
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
    mint: str | Unset = UNSET,
    trader: str | Unset = UNSET,
    pool: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    before_ts: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorTrade]
]:
    """List Swaps

     Returns the ledger's trade rows filtered by `mint` and/or one-or-more `trader` params (AND-combined;
    at least one required). `trader` may be repeated (trader=a&trader=b) or comma-separated. `pool`
    narrows to one or more markets by the trade's primary pool and accepts the same repeated/comma-
    separated forms, OR-combined — pass the whole set when a token's market spans several pools (a
    graduated token's bonding curve plus the pool it migrated to). Every money field is a `{sol, usd}`
    pair fixed at execution (lamports and micro-USD; null = unpriced). A quote-registry mint (SOL, USDC,
    USDT, USD1) lists the legs whose base it is, keyed by the leg, with no realized PnL. All time params
    are optional; with none supplied the latest rows are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest rows strictly
    older than the cursor — no lower bound, so pagination crosses activity gaps).

    Args:
        mint (str | Unset):
        trader (str | Unset):
        pool (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        before_ts (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorTrade]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        trader=trader,
        pool=pool,
        from_=from_,
        to=to,
        from_ts=from_ts,
        to_ts=to_ts,
        before_ts=before_ts,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mint: str | Unset = UNSET,
    trader: str | Unset = UNSET,
    pool: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    before_ts: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorTrade]
    | None
):
    """List Swaps

     Returns the ledger's trade rows filtered by `mint` and/or one-or-more `trader` params (AND-combined;
    at least one required). `trader` may be repeated (trader=a&trader=b) or comma-separated. `pool`
    narrows to one or more markets by the trade's primary pool and accepts the same repeated/comma-
    separated forms, OR-combined — pass the whole set when a token's market spans several pools (a
    graduated token's bonding curve plus the pool it migrated to). Every money field is a `{sol, usd}`
    pair fixed at execution (lamports and micro-USD; null = unpriced). A quote-registry mint (SOL, USDC,
    USDT, USD1) lists the legs whose base it is, keyed by the leg, with no realized PnL. All time params
    are optional; with none supplied the latest rows are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest rows strictly
    older than the cursor — no lower bound, so pagination crosses activity gaps).

    Args:
        mint (str | Unset):
        trader (str | Unset):
        pool (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        before_ts (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorTrade]
    """

    return sync_detailed(
        client=client,
        mint=mint,
        trader=trader,
        pool=pool,
        from_=from_,
        to=to,
        from_ts=from_ts,
        to_ts=to_ts,
        before_ts=before_ts,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mint: str | Unset = UNSET,
    trader: str | Unset = UNSET,
    pool: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    before_ts: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorTrade]
]:
    """List Swaps

     Returns the ledger's trade rows filtered by `mint` and/or one-or-more `trader` params (AND-combined;
    at least one required). `trader` may be repeated (trader=a&trader=b) or comma-separated. `pool`
    narrows to one or more markets by the trade's primary pool and accepts the same repeated/comma-
    separated forms, OR-combined — pass the whole set when a token's market spans several pools (a
    graduated token's bonding curve plus the pool it migrated to). Every money field is a `{sol, usd}`
    pair fixed at execution (lamports and micro-USD; null = unpriced). A quote-registry mint (SOL, USDC,
    USDT, USD1) lists the legs whose base it is, keyed by the leg, with no realized PnL. All time params
    are optional; with none supplied the latest rows are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest rows strictly
    older than the cursor — no lower bound, so pagination crosses activity gaps).

    Args:
        mint (str | Unset):
        trader (str | Unset):
        pool (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        before_ts (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorTrade]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        trader=trader,
        pool=pool,
        from_=from_,
        to=to,
        from_ts=from_ts,
        to_ts=to_ts,
        before_ts=before_ts,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mint: str | Unset = UNSET,
    trader: str | Unset = UNSET,
    pool: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    before_ts: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorTrade]
    | None
):
    """List Swaps

     Returns the ledger's trade rows filtered by `mint` and/or one-or-more `trader` params (AND-combined;
    at least one required). `trader` may be repeated (trader=a&trader=b) or comma-separated. `pool`
    narrows to one or more markets by the trade's primary pool and accepts the same repeated/comma-
    separated forms, OR-combined — pass the whole set when a token's market spans several pools (a
    graduated token's bonding curve plus the pool it migrated to). Every money field is a `{sol, usd}`
    pair fixed at execution (lamports and micro-USD; null = unpriced). A quote-registry mint (SOL, USDC,
    USDT, USD1) lists the legs whose base it is, keyed by the leg, with no realized PnL. All time params
    are optional; with none supplied the latest rows are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest rows strictly
    older than the cursor — no lower bound, so pagination crosses activity gaps).

    Args:
        mint (str | Unset):
        trader (str | Unset):
        pool (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        before_ts (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorTrade]
    """

    return (
        await asyncio_detailed(
            client=client,
            mint=mint,
            trader=trader,
            pool=pool,
            from_=from_,
            to=to,
            from_ts=from_ts,
            to_ts=to_ts,
            before_ts=before_ts,
            limit=limit,
        )
    ).parsed
