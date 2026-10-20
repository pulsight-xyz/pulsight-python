from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/legs/export/declared-quotes",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download the quotes launch venues declared

     Streams, as Parquet (zstd), every mint a pool of a venue that names its base — PumpSwap, the pump
    bonding curve, Raydium LaunchLab, Meteora DBC — quotes in, with the earliest first swap of such a
    pool the ledger saw: mint_id (u64 ledger id), mint (base58) and first_slot. A pool counts by its
    merged ledger row, when it names a quote and its base is neither that quote nor a money mint (WSOL
    or a ledger dollar). The set only grows, except where a backfill dates a declaration earlier. Free,
    and refused like the parts (400, 403, 429) before streaming.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download the quotes launch venues declared

     Streams, as Parquet (zstd), every mint a pool of a venue that names its base — PumpSwap, the pump
    bonding curve, Raydium LaunchLab, Meteora DBC — quotes in, with the earliest first swap of such a
    pool the ledger saw: mint_id (u64 ledger id), mint (base58) and first_slot. A pool counts by its
    merged ledger row, when it names a quote and its base is neither that quote nor a money mint (WSOL
    or a ledger dollar). The set only grows, except where a backfill dates a declaration earlier. Free,
    and refused like the parts (400, 403, 429) before streaming.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
