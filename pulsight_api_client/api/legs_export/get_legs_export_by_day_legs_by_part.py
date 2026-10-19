from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    day: str,
    part: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/legs/export/{day}/legs/{part}".format(
            day=quote(str(day), safe=""),
            part=quote(str(part), safe=""),
        ),
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
    day: str,
    part: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download one part of a day's DEX legs

     Streams, as Parquet (zstd), every DEX leg of the UTC day, on every venue the ledger records, whose
    pool_id modulo the catalog's parts equals `part`, sorted by pool_id, slot, tx_index, ix_index. A
    pool's legs are in the same part every day. Columns: pool_id, mint_id, quote_mint_id (u64 ledger
    ids), dex, ts_ms, slot, tx_index, ix_index, trader (32 raw bytes), is_buy (the base side),
    base_amount, quote_amount, base_reserve_pre, quote_reserve_pre, base_reserve_post,
    quote_reserve_post (raw units), value_sol (lamports), swap_fee_bps (0 = unknown), flags. A request
    refused before streaming (400, 403, 429) is not charged, and one the server fails to deliver is
    refunded.

    Args:
        day (str):
        part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
        part=part,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    day: str,
    part: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download one part of a day's DEX legs

     Streams, as Parquet (zstd), every DEX leg of the UTC day, on every venue the ledger records, whose
    pool_id modulo the catalog's parts equals `part`, sorted by pool_id, slot, tx_index, ix_index. A
    pool's legs are in the same part every day. Columns: pool_id, mint_id, quote_mint_id (u64 ledger
    ids), dex, ts_ms, slot, tx_index, ix_index, trader (32 raw bytes), is_buy (the base side),
    base_amount, quote_amount, base_reserve_pre, quote_reserve_pre, base_reserve_post,
    quote_reserve_post (raw units), value_sol (lamports), swap_fee_bps (0 = unknown), flags. A request
    refused before streaming (400, 403, 429) is not charged, and one the server fails to deliver is
    refunded.

    Args:
        day (str):
        part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
        part=part,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
