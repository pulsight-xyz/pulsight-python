from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_mint_live_metrics import (
    PulsightInternalCoreDomainAggregatorMintLiveMetrics,
)
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/live".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorMintLiveMetrics.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_404

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
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
]:
    """Get Mint Live Metrics

     Returns the mint's live header figures — latest price, market cap and lifetime distinct traders — on
    the same basis as the corresponding fields of GET /api/mints/{pubkey}, from sources that update with
    ingest rather than on a refresh cadence. Intended for polling: it reads none of the identity row's
    enrichment (authorities, bonding curve, dev holdings, risk cohorts). Fields are independently
    optional — an unpriceable mint reports no price, and a quote-registry mint (WSOL, the USD stables)
    reports no trader count.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintLiveMetrics]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
    | None
):
    """Get Mint Live Metrics

     Returns the mint's live header figures — latest price, market cap and lifetime distinct traders — on
    the same basis as the corresponding fields of GET /api/mints/{pubkey}, from sources that update with
    ingest rather than on a refresh cadence. Intended for polling: it reads none of the identity row's
    enrichment (authorities, bonding curve, dev holdings, risk cohorts). Fields are independently
    optional — an unpriceable mint reports no price, and a quote-registry mint (WSOL, the USD stables)
    reports no trader count.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintLiveMetrics
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
]:
    """Get Mint Live Metrics

     Returns the mint's live header figures — latest price, market cap and lifetime distinct traders — on
    the same basis as the corresponding fields of GET /api/mints/{pubkey}, from sources that update with
    ingest rather than on a refresh cadence. Intended for polling: it reads none of the identity row's
    enrichment (authorities, bonding curve, dev holdings, risk cohorts). Fields are independently
    optional — an unpriceable mint reports no price, and a quote-registry mint (WSOL, the USD stables)
    reports no trader count.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintLiveMetrics]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintLiveMetrics
    | None
):
    """Get Mint Live Metrics

     Returns the mint's live header figures — latest price, market cap and lifetime distinct traders — on
    the same basis as the corresponding fields of GET /api/mints/{pubkey}, from sources that update with
    ingest rather than on a refresh cadence. Intended for polling: it reads none of the identity row's
    enrichment (authorities, bonding curve, dev holdings, risk cohorts). Fields are independently
    optional — an unpriceable mint reports no price, and a quote-registry mint (WSOL, the USD stables)
    reports no trader count.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintLiveMetrics
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
