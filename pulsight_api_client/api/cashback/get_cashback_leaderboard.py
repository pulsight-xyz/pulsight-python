from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_cashback_board_page import (
    PulsightInternalCoreDomainAggregatorCashbackBoardPage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    f: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params["sort_by"] = sort_by

    params["direction"] = direction

    params["limit"] = limit

    params["offset"] = offset

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cashback/leaderboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorCashbackBoardPage.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
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
    window: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    f: list[str] | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
]:
    """Pump cashback leaderboard

     Wallets ranked by pump cashback over a window. Accepts the same composable `f=` filter clauses as
    /api/traders (repeated `f=key|op|value`), plus cashback-specific sorts. Lifetime claimed figures are
    retention-bounded sums over the 75-day claim ledger (they undercount once rows age out, never
    invent).

    Args:
        window (str | Unset):
        sort_by (str | Unset):
        direction (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        f (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackBoardPage]
    """

    kwargs = _get_kwargs(
        window=window,
        sort_by=sort_by,
        direction=direction,
        limit=limit,
        offset=offset,
        f=f,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    f: list[str] | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
    | None
):
    """Pump cashback leaderboard

     Wallets ranked by pump cashback over a window. Accepts the same composable `f=` filter clauses as
    /api/traders (repeated `f=key|op|value`), plus cashback-specific sorts. Lifetime claimed figures are
    retention-bounded sums over the 75-day claim ledger (they undercount once rows age out, never
    invent).

    Args:
        window (str | Unset):
        sort_by (str | Unset):
        direction (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        f (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackBoardPage
    """

    return sync_detailed(
        client=client,
        window=window,
        sort_by=sort_by,
        direction=direction,
        limit=limit,
        offset=offset,
        f=f,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    f: list[str] | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
]:
    """Pump cashback leaderboard

     Wallets ranked by pump cashback over a window. Accepts the same composable `f=` filter clauses as
    /api/traders (repeated `f=key|op|value`), plus cashback-specific sorts. Lifetime claimed figures are
    retention-bounded sums over the 75-day claim ledger (they undercount once rows age out, never
    invent).

    Args:
        window (str | Unset):
        sort_by (str | Unset):
        direction (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        f (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackBoardPage]
    """

    kwargs = _get_kwargs(
        window=window,
        sort_by=sort_by,
        direction=direction,
        limit=limit,
        offset=offset,
        f=f,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    f: list[str] | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackBoardPage
    | None
):
    """Pump cashback leaderboard

     Wallets ranked by pump cashback over a window. Accepts the same composable `f=` filter clauses as
    /api/traders (repeated `f=key|op|value`), plus cashback-specific sorts. Lifetime claimed figures are
    retention-bounded sums over the 75-day claim ledger (they undercount once rows age out, never
    invent).

    Args:
        window (str | Unset):
        sort_by (str | Unset):
        direction (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        f (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackBoardPage
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            sort_by=sort_by,
            direction=direction,
            limit=limit,
            offset=offset,
            f=f,
        )
    ).parsed
