from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_program_daily_series import (
    PulsightInternalCoreDomainAggregatorProgramDailySeries,
)
from ...types import Response


def _get_kwargs(
    program_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/programs/{program_id}/daily".format(
            program_id=quote(str(program_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorProgramDailySeries.from_dict(
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
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    program_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
]:
    """Program daily stats

     One program's per-day activity over the trailing 3 months: landed txs by kind (swap/arb/other),
    unique users, SOL-projected volume for both attribution roles, the raw arb + fee revenue components
    (the client folds them by the program's resolved category), and the failed side (failed
    swaps/arbs/other, landed no-CPI probes, fees burned). Days with no activity are absent. Also carries
    the derived per-window figures ("7d"/"30d"/"3m" — volume both roles, users, category-gated revenue,
    landed/failed txs, success/spam/non-swap rates), computed with the same formulas as the leaderboard
    rows.

    Args:
        program_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramDailySeries]
    """

    kwargs = _get_kwargs(
        program_id=program_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    program_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
    | None
):
    """Program daily stats

     One program's per-day activity over the trailing 3 months: landed txs by kind (swap/arb/other),
    unique users, SOL-projected volume for both attribution roles, the raw arb + fee revenue components
    (the client folds them by the program's resolved category), and the failed side (failed
    swaps/arbs/other, landed no-CPI probes, fees burned). Days with no activity are absent. Also carries
    the derived per-window figures ("7d"/"30d"/"3m" — volume both roles, users, category-gated revenue,
    landed/failed txs, success/spam/non-swap rates), computed with the same formulas as the leaderboard
    rows.

    Args:
        program_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramDailySeries
    """

    return sync_detailed(
        program_id=program_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    program_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
]:
    """Program daily stats

     One program's per-day activity over the trailing 3 months: landed txs by kind (swap/arb/other),
    unique users, SOL-projected volume for both attribution roles, the raw arb + fee revenue components
    (the client folds them by the program's resolved category), and the failed side (failed
    swaps/arbs/other, landed no-CPI probes, fees burned). Days with no activity are absent. Also carries
    the derived per-window figures ("7d"/"30d"/"3m" — volume both roles, users, category-gated revenue,
    landed/failed txs, success/spam/non-swap rates), computed with the same formulas as the leaderboard
    rows.

    Args:
        program_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramDailySeries]
    """

    kwargs = _get_kwargs(
        program_id=program_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    program_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorProgramDailySeries
    | None
):
    """Program daily stats

     One program's per-day activity over the trailing 3 months: landed txs by kind (swap/arb/other),
    unique users, SOL-projected volume for both attribution roles, the raw arb + fee revenue components
    (the client folds them by the program's resolved category), and the failed side (failed
    swaps/arbs/other, landed no-CPI probes, fees burned). Days with no activity are absent. Also carries
    the derived per-window figures ("7d"/"30d"/"3m" — volume both roles, users, category-gated revenue,
    landed/failed txs, success/spam/non-swap rates), computed with the same formulas as the leaderboard
    rows.

    Args:
        program_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorProgramDailySeries
    """

    return (
        await asyncio_detailed(
            program_id=program_id,
            client=client,
        )
    ).parsed
