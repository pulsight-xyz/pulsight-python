from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_legs_export_by_day_facts_by_dataset_dataset import (
    GetLegsExportByDayFactsByDatasetDataset,
)
from ...types import Response


def _get_kwargs(
    day: str,
    dataset: GetLegsExportByDayFactsByDatasetDataset,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/legs/export/{day}/facts/{dataset}".format(
            day=quote(str(day), safe=""),
            dataset=quote(str(dataset), safe=""),
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
    dataset: GetLegsExportByDayFactsByDatasetDataset,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download one token facts file of a day

     Streams, as Parquet (zstd), one token facts file (schema `facts_schema` of the catalog) of the UTC
    day, for the mints traded that day on any venue. `minutes`: per mint and minute with trades, buys,
    swaps (transactions counted per trader and side), fees_sol and volume_sol (lamports, a transaction's
    fee and value counted once), new_traders (traders whose first ledger trade of the mint falls in the
    minute), trades and tipped_trades (non-arb buys and sells, and those whose transaction paid a tip).
    `mints`: mint_id, mint (base58), created_ms, first_trade_ms, supply (raw units, 0 = unknown),
    dev_known and dev_first_sell_ms (0 = none). `bundles`: each sealed bundle cohort generation's
    sealed_ms and initial holding (raw units). `insiders`: per insider wallet (32 raw bytes) and minute
    of the day, found_ms (when the wallet became an insider of the mint) and its net token flow (trades
    and transfers). `insider_flows`: the same rows with every trade counted once, a later-corrected
    trade included, each with its wallet's hop (its distance from the mint's creator in the insider
    walk) and first_slot (the slot of the transfer that made it an insider), plus one row with flow 0 at
    the minute of its reach for an insider reached that day with no move in the file. `activity`: per
    mint and minute with trades, swaps, buys, fees_sol and volume_sol (lamports) as the live activity
    figures count them, tip_trades and tipped_trades (non-arb buys and sells whose landing tip is
    recorded, and those that paid one). `activity_base`: per mint, the same six figures over everything
    before the day. Timestamps are unix milliseconds. The catalog's `facts` lists the files a day
    carries, and a new file can join it under the same `facts_schema`. A request refused before
    streaming (400, 403, 429) is not charged, and one the server fails to deliver is refunded.

    Args:
        day (str):
        dataset (GetLegsExportByDayFactsByDatasetDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
        dataset=dataset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    day: str,
    dataset: GetLegsExportByDayFactsByDatasetDataset,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Download one token facts file of a day

     Streams, as Parquet (zstd), one token facts file (schema `facts_schema` of the catalog) of the UTC
    day, for the mints traded that day on any venue. `minutes`: per mint and minute with trades, buys,
    swaps (transactions counted per trader and side), fees_sol and volume_sol (lamports, a transaction's
    fee and value counted once), new_traders (traders whose first ledger trade of the mint falls in the
    minute), trades and tipped_trades (non-arb buys and sells, and those whose transaction paid a tip).
    `mints`: mint_id, mint (base58), created_ms, first_trade_ms, supply (raw units, 0 = unknown),
    dev_known and dev_first_sell_ms (0 = none). `bundles`: each sealed bundle cohort generation's
    sealed_ms and initial holding (raw units). `insiders`: per insider wallet (32 raw bytes) and minute
    of the day, found_ms (when the wallet became an insider of the mint) and its net token flow (trades
    and transfers). `insider_flows`: the same rows with every trade counted once, a later-corrected
    trade included, each with its wallet's hop (its distance from the mint's creator in the insider
    walk) and first_slot (the slot of the transfer that made it an insider), plus one row with flow 0 at
    the minute of its reach for an insider reached that day with no move in the file. `activity`: per
    mint and minute with trades, swaps, buys, fees_sol and volume_sol (lamports) as the live activity
    figures count them, tip_trades and tipped_trades (non-arb buys and sells whose landing tip is
    recorded, and those that paid one). `activity_base`: per mint, the same six figures over everything
    before the day. Timestamps are unix milliseconds. The catalog's `facts` lists the files a day
    carries, and a new file can join it under the same `facts_schema`. A request refused before
    streaming (400, 403, 429) is not charged, and one the server fails to deliver is refunded.

    Args:
        day (str):
        dataset (GetLegsExportByDayFactsByDatasetDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        day=day,
        dataset=dataset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
