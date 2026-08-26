from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_program_board_page import (
    PulsightInternalCoreDomainAggregatorProgramBoardPage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    board: str | Unset = UNSET,
    window: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    search: str | Unset = UNSET,
    min_volume_sol: float | Unset = UNSET,
    max_volume_sol: float | Unset = UNSET,
    min_users: int | Unset = UNSET,
    max_users: int | Unset = UNSET,
    min_txs: int | Unset = UNSET,
    max_txs: int | Unset = UNSET,
    min_revenue_sol: float | Unset = UNSET,
    max_revenue_sol: float | Unset = UNSET,
    min_success_rate: float | Unset = UNSET,
    max_success_rate: float | Unset = UNSET,
    min_spam_rate: float | Unset = UNSET,
    max_spam_rate: float | Unset = UNSET,
    min_non_swap_rate: float | Unset = UNSET,
    max_non_swap_rate: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["board"] = board

    params["window"] = window

    params["sort"] = sort

    params["order"] = order

    params["limit"] = limit

    params["offset"] = offset

    params["search"] = search

    params["min_volume_sol"] = min_volume_sol

    params["max_volume_sol"] = max_volume_sol

    params["min_users"] = min_users

    params["max_users"] = max_users

    params["min_txs"] = min_txs

    params["max_txs"] = max_txs

    params["min_revenue_sol"] = min_revenue_sol

    params["max_revenue_sol"] = max_revenue_sol

    params["min_success_rate"] = min_success_rate

    params["max_success_rate"] = max_success_rate

    params["min_spam_rate"] = min_spam_rate

    params["max_spam_rate"] = max_spam_rate

    params["min_non_swap_rate"] = min_non_swap_rate

    params["max_non_swap_rate"] = max_non_swap_rate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/programs/leaderboard",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorProgramBoardPage.from_dict(
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
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
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
    board: str | Unset = UNSET,
    window: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    search: str | Unset = UNSET,
    min_volume_sol: float | Unset = UNSET,
    max_volume_sol: float | Unset = UNSET,
    min_users: int | Unset = UNSET,
    max_users: int | Unset = UNSET,
    min_txs: int | Unset = UNSET,
    max_txs: int | Unset = UNSET,
    min_revenue_sol: float | Unset = UNSET,
    max_revenue_sol: float | Unset = UNSET,
    min_success_rate: float | Unset = UNSET,
    max_success_rate: float | Unset = UNSET,
    min_spam_rate: float | Unset = UNSET,
    max_spam_rate: float | Unset = UNSET,
    min_non_swap_rate: float | Unset = UNSET,
    max_non_swap_rate: float | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
]:
    """Programs leaderboard

     On-chain programs ranked over a window: volume (SOL-projected; venue-executed for AMM-category
    programs, tx-level otherwise), unique users, revenue (category-gated: net arb extraction for
    arbitrage programs, decoded venue fees for AMMs, 0 = not measured for routers/unknowns), landed tx
    count, success / spam / non-swap rates, and a resolved category (admin identity > curated AMM seed >
    7d arb-share auto-rule > unknown). Numeric filters are flat query params; SOL values in whole SOL,
    rates in percent.

    Args:
        board (str | Unset):
        window (str | Unset):
        sort (str | Unset):
        order (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        search (str | Unset):
        min_volume_sol (float | Unset):
        max_volume_sol (float | Unset):
        min_users (int | Unset):
        max_users (int | Unset):
        min_txs (int | Unset):
        max_txs (int | Unset):
        min_revenue_sol (float | Unset):
        max_revenue_sol (float | Unset):
        min_success_rate (float | Unset):
        max_success_rate (float | Unset):
        min_spam_rate (float | Unset):
        max_spam_rate (float | Unset):
        min_non_swap_rate (float | Unset):
        max_non_swap_rate (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramBoardPage]
    """

    kwargs = _get_kwargs(
        board=board,
        window=window,
        sort=sort,
        order=order,
        limit=limit,
        offset=offset,
        search=search,
        min_volume_sol=min_volume_sol,
        max_volume_sol=max_volume_sol,
        min_users=min_users,
        max_users=max_users,
        min_txs=min_txs,
        max_txs=max_txs,
        min_revenue_sol=min_revenue_sol,
        max_revenue_sol=max_revenue_sol,
        min_success_rate=min_success_rate,
        max_success_rate=max_success_rate,
        min_spam_rate=min_spam_rate,
        max_spam_rate=max_spam_rate,
        min_non_swap_rate=min_non_swap_rate,
        max_non_swap_rate=max_non_swap_rate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    board: str | Unset = UNSET,
    window: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    search: str | Unset = UNSET,
    min_volume_sol: float | Unset = UNSET,
    max_volume_sol: float | Unset = UNSET,
    min_users: int | Unset = UNSET,
    max_users: int | Unset = UNSET,
    min_txs: int | Unset = UNSET,
    max_txs: int | Unset = UNSET,
    min_revenue_sol: float | Unset = UNSET,
    max_revenue_sol: float | Unset = UNSET,
    min_success_rate: float | Unset = UNSET,
    max_success_rate: float | Unset = UNSET,
    min_spam_rate: float | Unset = UNSET,
    max_spam_rate: float | Unset = UNSET,
    min_non_swap_rate: float | Unset = UNSET,
    max_non_swap_rate: float | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
    | None
):
    """Programs leaderboard

     On-chain programs ranked over a window: volume (SOL-projected; venue-executed for AMM-category
    programs, tx-level otherwise), unique users, revenue (category-gated: net arb extraction for
    arbitrage programs, decoded venue fees for AMMs, 0 = not measured for routers/unknowns), landed tx
    count, success / spam / non-swap rates, and a resolved category (admin identity > curated AMM seed >
    7d arb-share auto-rule > unknown). Numeric filters are flat query params; SOL values in whole SOL,
    rates in percent.

    Args:
        board (str | Unset):
        window (str | Unset):
        sort (str | Unset):
        order (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        search (str | Unset):
        min_volume_sol (float | Unset):
        max_volume_sol (float | Unset):
        min_users (int | Unset):
        max_users (int | Unset):
        min_txs (int | Unset):
        max_txs (int | Unset):
        min_revenue_sol (float | Unset):
        max_revenue_sol (float | Unset):
        min_success_rate (float | Unset):
        max_success_rate (float | Unset):
        min_spam_rate (float | Unset):
        max_spam_rate (float | Unset):
        min_non_swap_rate (float | Unset):
        max_non_swap_rate (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramBoardPage
    """

    return sync_detailed(
        client=client,
        board=board,
        window=window,
        sort=sort,
        order=order,
        limit=limit,
        offset=offset,
        search=search,
        min_volume_sol=min_volume_sol,
        max_volume_sol=max_volume_sol,
        min_users=min_users,
        max_users=max_users,
        min_txs=min_txs,
        max_txs=max_txs,
        min_revenue_sol=min_revenue_sol,
        max_revenue_sol=max_revenue_sol,
        min_success_rate=min_success_rate,
        max_success_rate=max_success_rate,
        min_spam_rate=min_spam_rate,
        max_spam_rate=max_spam_rate,
        min_non_swap_rate=min_non_swap_rate,
        max_non_swap_rate=max_non_swap_rate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    board: str | Unset = UNSET,
    window: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    search: str | Unset = UNSET,
    min_volume_sol: float | Unset = UNSET,
    max_volume_sol: float | Unset = UNSET,
    min_users: int | Unset = UNSET,
    max_users: int | Unset = UNSET,
    min_txs: int | Unset = UNSET,
    max_txs: int | Unset = UNSET,
    min_revenue_sol: float | Unset = UNSET,
    max_revenue_sol: float | Unset = UNSET,
    min_success_rate: float | Unset = UNSET,
    max_success_rate: float | Unset = UNSET,
    min_spam_rate: float | Unset = UNSET,
    max_spam_rate: float | Unset = UNSET,
    min_non_swap_rate: float | Unset = UNSET,
    max_non_swap_rate: float | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
]:
    """Programs leaderboard

     On-chain programs ranked over a window: volume (SOL-projected; venue-executed for AMM-category
    programs, tx-level otherwise), unique users, revenue (category-gated: net arb extraction for
    arbitrage programs, decoded venue fees for AMMs, 0 = not measured for routers/unknowns), landed tx
    count, success / spam / non-swap rates, and a resolved category (admin identity > curated AMM seed >
    7d arb-share auto-rule > unknown). Numeric filters are flat query params; SOL values in whole SOL,
    rates in percent.

    Args:
        board (str | Unset):
        window (str | Unset):
        sort (str | Unset):
        order (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        search (str | Unset):
        min_volume_sol (float | Unset):
        max_volume_sol (float | Unset):
        min_users (int | Unset):
        max_users (int | Unset):
        min_txs (int | Unset):
        max_txs (int | Unset):
        min_revenue_sol (float | Unset):
        max_revenue_sol (float | Unset):
        min_success_rate (float | Unset):
        max_success_rate (float | Unset):
        min_spam_rate (float | Unset):
        max_spam_rate (float | Unset):
        min_non_swap_rate (float | Unset):
        max_non_swap_rate (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramBoardPage]
    """

    kwargs = _get_kwargs(
        board=board,
        window=window,
        sort=sort,
        order=order,
        limit=limit,
        offset=offset,
        search=search,
        min_volume_sol=min_volume_sol,
        max_volume_sol=max_volume_sol,
        min_users=min_users,
        max_users=max_users,
        min_txs=min_txs,
        max_txs=max_txs,
        min_revenue_sol=min_revenue_sol,
        max_revenue_sol=max_revenue_sol,
        min_success_rate=min_success_rate,
        max_success_rate=max_success_rate,
        min_spam_rate=min_spam_rate,
        max_spam_rate=max_spam_rate,
        min_non_swap_rate=min_non_swap_rate,
        max_non_swap_rate=max_non_swap_rate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    board: str | Unset = UNSET,
    window: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    order: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    search: str | Unset = UNSET,
    min_volume_sol: float | Unset = UNSET,
    max_volume_sol: float | Unset = UNSET,
    min_users: int | Unset = UNSET,
    max_users: int | Unset = UNSET,
    min_txs: int | Unset = UNSET,
    max_txs: int | Unset = UNSET,
    min_revenue_sol: float | Unset = UNSET,
    max_revenue_sol: float | Unset = UNSET,
    min_success_rate: float | Unset = UNSET,
    max_success_rate: float | Unset = UNSET,
    min_spam_rate: float | Unset = UNSET,
    max_spam_rate: float | Unset = UNSET,
    min_non_swap_rate: float | Unset = UNSET,
    max_non_swap_rate: float | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramBoardPage
    | None
):
    """Programs leaderboard

     On-chain programs ranked over a window: volume (SOL-projected; venue-executed for AMM-category
    programs, tx-level otherwise), unique users, revenue (category-gated: net arb extraction for
    arbitrage programs, decoded venue fees for AMMs, 0 = not measured for routers/unknowns), landed tx
    count, success / spam / non-swap rates, and a resolved category (admin identity > curated AMM seed >
    7d arb-share auto-rule > unknown). Numeric filters are flat query params; SOL values in whole SOL,
    rates in percent.

    Args:
        board (str | Unset):
        window (str | Unset):
        sort (str | Unset):
        order (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        search (str | Unset):
        min_volume_sol (float | Unset):
        max_volume_sol (float | Unset):
        min_users (int | Unset):
        max_users (int | Unset):
        min_txs (int | Unset):
        max_txs (int | Unset):
        min_revenue_sol (float | Unset):
        max_revenue_sol (float | Unset):
        min_success_rate (float | Unset):
        max_success_rate (float | Unset):
        min_spam_rate (float | Unset):
        max_spam_rate (float | Unset):
        min_non_swap_rate (float | Unset):
        max_non_swap_rate (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramBoardPage
    """

    return (
        await asyncio_detailed(
            client=client,
            board=board,
            window=window,
            sort=sort,
            order=order,
            limit=limit,
            offset=offset,
            search=search,
            min_volume_sol=min_volume_sol,
            max_volume_sol=max_volume_sol,
            min_users=min_users,
            max_users=max_users,
            min_txs=min_txs,
            max_txs=max_txs,
            min_revenue_sol=min_revenue_sol,
            max_revenue_sol=max_revenue_sol,
            min_success_rate=min_success_rate,
            max_success_rate=max_success_rate,
            min_spam_rate=min_spam_rate,
            max_spam_rate=max_spam_rate,
            min_non_swap_rate=min_non_swap_rate,
            max_non_swap_rate=max_non_swap_rate,
        )
    ).parsed
