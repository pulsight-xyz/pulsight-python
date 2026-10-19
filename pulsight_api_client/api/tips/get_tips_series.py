from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_tip_series import (
    PulsightInternalCoreDomainAggregatorTipSeries,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tips/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorTipSeries
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorTipSeries.from_dict(
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
    | PulsightInternalCoreDomainAggregatorTipSeries
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
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorTipSeries
]:
    """Tip series

     The window's tip figures per bucket (60 s up to 4 h, or a day for the 90-day window; at most 180
    buckets): tipped transactions, tips and priority fees in both currencies, and the median, 90th and
    99th percentile tip. Buckets without a tipped transaction are absent; the last bucket is still
    filling.

    Args:
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorTipSeries]
    """

    kwargs = _get_kwargs(
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorTipSeries
    | None
):
    """Tip series

     The window's tip figures per bucket (60 s up to 4 h, or a day for the 90-day window; at most 180
    buckets): tipped transactions, tips and priority fees in both currencies, and the median, 90th and
    99th percentile tip. Buckets without a tipped transaction are absent; the last bucket is still
    filling.

    Args:
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorTipSeries
    """

    return sync_detailed(
        client=client,
        window=window,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorTipSeries
]:
    """Tip series

     The window's tip figures per bucket (60 s up to 4 h, or a day for the 90-day window; at most 180
    buckets): tipped transactions, tips and priority fees in both currencies, and the median, 90th and
    99th percentile tip. Buckets without a tipped transaction are absent; the last bucket is still
    filling.

    Args:
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorTipSeries]
    """

    kwargs = _get_kwargs(
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorTipSeries
    | None
):
    """Tip series

     The window's tip figures per bucket (60 s up to 4 h, or a day for the 90-day window; at most 180
    buckets): tipped transactions, tips and priority fees in both currencies, and the median, 90th and
    99th percentile tip. Buckets without a tipped transaction are absent; the last bucket is still
    filling.

    Args:
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorTipSeries
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
        )
    ).parsed
