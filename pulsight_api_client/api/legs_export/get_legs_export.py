from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_legs_export_catalog import (
    PulsightInternalCoreDomainAggregatorLegsExportCatalog,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/legs/export",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorLegsExportCatalog.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 403:
        response_403 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
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
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
]:
    """List the exportable days of DEX legs

     Lists the complete UTC days of DEX legs the export serves, every venue the ledger records (inside
    the ledger's 90-day history), how many parts each day is split into and the column schema. Free.
    Needs an api token with the `data:export` scope on an account the export is granted to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorLegsExportCatalog]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
    | None
):
    """List the exportable days of DEX legs

     Lists the complete UTC days of DEX legs the export serves, every venue the ledger records (inside
    the ledger's 90-day history), how many parts each day is split into and the column schema. Free.
    Needs an api token with the `data:export` scope on an account the export is granted to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorLegsExportCatalog
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
]:
    """List the exportable days of DEX legs

     Lists the complete UTC days of DEX legs the export serves, every venue the ledger records (inside
    the ledger's 90-day history), how many parts each day is split into and the column schema. Free.
    Needs an api token with the `data:export` scope on an account the export is granted to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorLegsExportCatalog]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorLegsExportCatalog
    | None
):
    """List the exportable days of DEX legs

     Lists the complete UTC days of DEX legs the export serves, every venue the ledger records (inside
    the ledger's 90-day history), how many parts each day is split into and the column schema. Free.
    Needs an api token with the `data:export` scope on an account the export is granted to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorLegsExportCatalog
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
