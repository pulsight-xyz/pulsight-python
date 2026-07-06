from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_trader_export_request import (
    InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
)
from ...models.pulsight_internal_core_domain_trader_trader import (
    PulsightInternalCoreDomainTraderTrader,
)
from ...types import Response


def _get_kwargs(
    *,
    body: InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/traders/export",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderTrader]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PulsightInternalCoreDomainTraderTrader.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 401:
        response_401 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 402:
        response_402 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_402

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
    | list[PulsightInternalCoreDomainTraderTrader]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderTrader]
]:
    """Export Traders

     Exports trader records based on advanced filters.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerTraderExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderTrader]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderTrader]
    | None
):
    """Export Traders

     Exports trader records based on advanced filters.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerTraderExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderTrader]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderTrader]
]:
    """Export Traders

     Exports trader records based on advanced filters.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerTraderExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderTrader]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerTraderExportRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainTraderTrader]
    | None
):
    """Export Traders

     Exports trader records based on advanced filters.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerTraderExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainTraderTrader]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
