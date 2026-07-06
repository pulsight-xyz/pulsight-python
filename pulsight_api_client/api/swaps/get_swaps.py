from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_swap_event_row import (
    InternalAdaptersPrimaryHttpHandlerSwapEventRow,
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                InternalAdaptersPrimaryHttpHandlerSwapEventRow.from_dict(
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
]:
    """List Swaps

     Returns swaps filtered by `mint` and/or one-or-more `trader` params (AND-combined; at least one
    required). `trader` may be repeated (trader=a&trader=b) or comma-separated. All time params are
    optional; with none supplied the latest swaps are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest swaps strictly
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
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]]
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
    | None
):
    """List Swaps

     Returns swaps filtered by `mint` and/or one-or-more `trader` params (AND-combined; at least one
    required). `trader` may be repeated (trader=a&trader=b) or comma-separated. All time params are
    optional; with none supplied the latest swaps are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest swaps strictly
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
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
]:
    """List Swaps

     Returns swaps filtered by `mint` and/or one-or-more `trader` params (AND-combined; at least one
    required). `trader` may be repeated (trader=a&trader=b) or comma-separated. All time params are
    optional; with none supplied the latest swaps are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest swaps strictly
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
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]]
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
    | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
    | None
):
    """List Swaps

     Returns swaps filtered by `mint` and/or one-or-more `trader` params (AND-combined; at least one
    required). `trader` may be repeated (trader=a&trader=b) or comma-separated. All time params are
    optional; with none supplied the latest swaps are returned regardless of age. Supports RFC3339
    from/to, Unix epoch from_ts/to_ts, and cursor-based before_ts (returns the latest swaps strictly
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
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerSwapEventRow]
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
