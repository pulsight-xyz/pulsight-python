from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_paginated_pnls import (
    InternalAdaptersPrimaryHttpHandlerPaginatedPnls,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trader_id: str,
    *,
    token_search: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    sort_by: str | Unset = "last_active_timestamp",
    direction: str | Unset = "desc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["token_search"] = token_search

    params["limit"] = limit

    params["offset"] = offset

    params["sort_by"] = sort_by

    params["direction"] = direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{trader_id}/pnls".format(
            trader_id=quote(str(trader_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
    | None
):
    if response.status_code == 200:
        response_200 = InternalAdaptersPrimaryHttpHandlerPaginatedPnls.from_dict(
            response.json()
        )

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
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    token_search: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    sort_by: str | Unset = "last_active_timestamp",
    direction: str | Unset = "desc",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
]:
    """List Trader PnLs

     Retrieves per-token PnL statistics for a specific trader.

    Args:
        trader_id (str):
        token_search (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'last_active_timestamp'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedPnls]
    """

    kwargs = _get_kwargs(
        trader_id=trader_id,
        token_search=token_search,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    token_search: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    sort_by: str | Unset = "last_active_timestamp",
    direction: str | Unset = "desc",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
    | None
):
    """List Trader PnLs

     Retrieves per-token PnL statistics for a specific trader.

    Args:
        trader_id (str):
        token_search (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'last_active_timestamp'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
    """

    return sync_detailed(
        trader_id=trader_id,
        client=client,
        token_search=token_search,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    token_search: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    sort_by: str | Unset = "last_active_timestamp",
    direction: str | Unset = "desc",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
]:
    """List Trader PnLs

     Retrieves per-token PnL statistics for a specific trader.

    Args:
        trader_id (str):
        token_search (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'last_active_timestamp'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedPnls]
    """

    kwargs = _get_kwargs(
        trader_id=trader_id,
        token_search=token_search,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    token_search: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    sort_by: str | Unset = "last_active_timestamp",
    direction: str | Unset = "desc",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
    | None
):
    """List Trader PnLs

     Retrieves per-token PnL statistics for a specific trader.

    Args:
        trader_id (str):
        token_search (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'last_active_timestamp'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedPnls
    """

    return (
        await asyncio_detailed(
            trader_id=trader_id,
            client=client,
            token_search=token_search,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            direction=direction,
        )
    ).parsed
