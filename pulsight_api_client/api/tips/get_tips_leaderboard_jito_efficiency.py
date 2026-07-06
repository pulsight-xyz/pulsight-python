from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_jito_efficiency_row import (
    PulsightInternalCoreDomainAggregatorJitoEfficiencyRow,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tips/leaderboard/jito-efficiency",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                PulsightInternalCoreDomainAggregatorJitoEfficiencyRow.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

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
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
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
    limit: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
]:
    """Jito-efficiency leaderboard

    Args:
        window (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]]
    """

    kwargs = _get_kwargs(
        window=window,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
    | None
):
    """Jito-efficiency leaderboard

    Args:
        window (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
    """

    return sync_detailed(
        client=client,
        window=window,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
]:
    """Jito-efficiency leaderboard

    Args:
        window (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]]
    """

    kwargs = _get_kwargs(
        window=window,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
    | None
):
    """Jito-efficiency leaderboard

    Args:
        window (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorJitoEfficiencyRow]
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            limit=limit,
        )
    ).parsed
