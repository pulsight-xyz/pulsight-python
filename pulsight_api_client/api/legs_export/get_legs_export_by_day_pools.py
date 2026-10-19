from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    day: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/legs/export/{day}/pools".format(
            day=quote(str(day), safe=""),
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
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download the pools of a day's DEX legs

     Streams, as Parquet (zstd), every pool with a leg on the UTC day, on any venue: pool_id, pool
    (base58), dex, mint_id and mint (the base, base58), quote_mint_id and quote_mint (base58),
    first_slot (the pool's first swap the ledger saw, which may predate the 90-day history). A request
    refused before streaming (400, 403, 429) is not charged, and one the server fails to deliver is
    refunded.

    Args:
        day (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    day: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download the pools of a day's DEX legs

     Streams, as Parquet (zstd), every pool with a leg on the UTC day, on any venue: pool_id, pool
    (base58), dex, mint_id and mint (the base, base58), quote_mint_id and quote_mint (base58),
    first_slot (the pool's first swap the ledger saw, which may predate the 90-day history). A request
    refused before streaming (400, 403, 429) is not charged, and one the server fails to deliver is
    refunded.

    Args:
        day (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
