from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_cashback_claims_page import (
    PulsightInternalCoreDomainAggregatorCashbackClaimsPage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["kind"] = kind

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{wallet_address}/cashback/claims".format(
            wallet_address=quote(str(wallet_address), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorCashbackClaimsPage.from_dict(
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
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
]:
    """Reward history of a wallet

     One wallet's reward events, newest first, paged: both its claim_cashback executions and the holder-
    reward payouts pushed to it, interleaved in one timestamp order and told apart by `kind`. A claim
    carries the pump program it swept; a payout carries the coin that paid it. Read from the raw ledgers
    (75-day retention): older events have aged out; the program-reported anchors on the rewards panel
    carry the true all-time totals. Amounts are in the event's quote-mint base units (lamports for WSOL
    rows, which is nearly all of them), and `amount_lamports` is zero on a payout whose quote could not
    be priced in SOL — `priced` says which.

    Args:
        wallet_address (str):
        kind (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackClaimsPage]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        kind=kind,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
    | None
):
    """Reward history of a wallet

     One wallet's reward events, newest first, paged: both its claim_cashback executions and the holder-
    reward payouts pushed to it, interleaved in one timestamp order and told apart by `kind`. A claim
    carries the pump program it swept; a payout carries the coin that paid it. Read from the raw ledgers
    (75-day retention): older events have aged out; the program-reported anchors on the rewards panel
    carry the true all-time totals. Amounts are in the event's quote-mint base units (lamports for WSOL
    rows, which is nearly all of them), and `amount_lamports` is zero on a payout whose quote could not
    be priced in SOL — `priced` says which.

    Args:
        wallet_address (str):
        kind (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        kind=kind,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
]:
    """Reward history of a wallet

     One wallet's reward events, newest first, paged: both its claim_cashback executions and the holder-
    reward payouts pushed to it, interleaved in one timestamp order and told apart by `kind`. A claim
    carries the pump program it swept; a payout carries the coin that paid it. Read from the raw ledgers
    (75-day retention): older events have aged out; the program-reported anchors on the rewards panel
    carry the true all-time totals. Amounts are in the event's quote-mint base units (lamports for WSOL
    rows, which is nearly all of them), and `amount_lamports` is zero on a payout whose quote could not
    be priced in SOL — `priced` says which.

    Args:
        wallet_address (str):
        kind (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackClaimsPage]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        kind=kind,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
    | None
):
    """Reward history of a wallet

     One wallet's reward events, newest first, paged: both its claim_cashback executions and the holder-
    reward payouts pushed to it, interleaved in one timestamp order and told apart by `kind`. A claim
    carries the pump program it swept; a payout carries the coin that paid it. Read from the raw ledgers
    (75-day retention): older events have aged out; the program-reported anchors on the rewards panel
    carry the true all-time totals. Amounts are in the event's quote-mint base units (lamports for WSOL
    rows, which is nearly all of them), and `amount_lamports` is zero on a payout whose quote could not
    be priced in SOL — `priced` says which.

    Args:
        wallet_address (str):
        kind (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorCashbackClaimsPage
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            kind=kind,
            limit=limit,
            offset=offset,
        )
    ).parsed
