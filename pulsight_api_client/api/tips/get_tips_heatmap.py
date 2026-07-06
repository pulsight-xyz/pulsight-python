from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_heatmap_response import (
    PulsightInternalCoreDomainAggregatorHeatmapResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bucket: str | Unset = UNSET,
    horizon_hours: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["bucket"] = bucket

    params["horizon_hours"] = horizon_hours

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tips/heatmap",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorHeatmapResponse.from_dict(
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
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
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
    bucket: str | Unset = UNSET,
    horizon_hours: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
]:
    """Tip heatmap

    Args:
        bucket (str | Unset):
        horizon_hours (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorHeatmapResponse]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        horizon_hours=horizon_hours,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bucket: str | Unset = UNSET,
    horizon_hours: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
    | None
):
    """Tip heatmap

    Args:
        bucket (str | Unset):
        horizon_hours (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorHeatmapResponse
    """

    return sync_detailed(
        client=client,
        bucket=bucket,
        horizon_hours=horizon_hours,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bucket: str | Unset = UNSET,
    horizon_hours: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
]:
    """Tip heatmap

    Args:
        bucket (str | Unset):
        horizon_hours (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorHeatmapResponse]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        horizon_hours=horizon_hours,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bucket: str | Unset = UNSET,
    horizon_hours: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorHeatmapResponse
    | None
):
    """Tip heatmap

    Args:
        bucket (str | Unset):
        horizon_hours (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorHeatmapResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            bucket=bucket,
            horizon_hours=horizon_hours,
        )
    ).parsed
