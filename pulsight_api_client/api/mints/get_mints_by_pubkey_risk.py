from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_risk_report import (
    PulsightInternalCoreDomainAggregatorRiskReport,
)
from ...types import Response


def _get_kwargs(
    pubkey: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/risk".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorRiskReport
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorRiskReport.from_dict(
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
    | PulsightInternalCoreDomainAggregatorRiskReport
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
    | PulsightInternalCoreDomainAggregatorRiskReport
]:
    """Token Risk Report

     Scored token risk assessment: normalised score + named risks, top-10 concentration, dev %,
    mint/freeze authority state, snipers, liquidity, honeypot/copycat. Wallet lists are behind
    /risk/cohorts.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorRiskReport]
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
    | PulsightInternalCoreDomainAggregatorRiskReport
    | None
):
    """Token Risk Report

     Scored token risk assessment: normalised score + named risks, top-10 concentration, dev %,
    mint/freeze authority state, snipers, liquidity, honeypot/copycat. Wallet lists are behind
    /risk/cohorts.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorRiskReport
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
    | PulsightInternalCoreDomainAggregatorRiskReport
]:
    """Token Risk Report

     Scored token risk assessment: normalised score + named risks, top-10 concentration, dev %,
    mint/freeze authority state, snipers, liquidity, honeypot/copycat. Wallet lists are behind
    /risk/cohorts.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorRiskReport]
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
    | PulsightInternalCoreDomainAggregatorRiskReport
    | None
):
    """Token Risk Report

     Scored token risk assessment: normalised score + named risks, top-10 concentration, dev %,
    mint/freeze authority state, snipers, liquidity, honeypot/copycat. Wallet lists are behind
    /risk/cohorts.

    Args:
        pubkey (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorRiskReport
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
        )
    ).parsed
