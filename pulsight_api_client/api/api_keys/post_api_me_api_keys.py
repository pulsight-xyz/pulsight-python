from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_ports_input_api_key_create_request import (
    PulsightInternalCorePortsInputAPIKeyCreateRequest,
)
from ...models.pulsight_internal_core_ports_input_created_api_key import (
    PulsightInternalCorePortsInputCreatedAPIKey,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PulsightInternalCorePortsInputAPIKeyCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/me/api-keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCorePortsInputCreatedAPIKey
    | None
):
    if response.status_code == 201:
        response_201 = PulsightInternalCorePortsInputCreatedAPIKey.from_dict(
            response.json()
        )

        return response_201

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

    if response.status_code == 403:
        response_403 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_403

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
    | PulsightInternalCorePortsInputCreatedAPIKey
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
    body: PulsightInternalCorePortsInputAPIKeyCreateRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCorePortsInputCreatedAPIKey
]:
    """Create API Key

     Creates an api token. The plaintext is returned once and never stored — copy it now.

    Args:
        body (PulsightInternalCorePortsInputAPIKeyCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCorePortsInputCreatedAPIKey]
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
    body: PulsightInternalCorePortsInputAPIKeyCreateRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCorePortsInputCreatedAPIKey
    | None
):
    """Create API Key

     Creates an api token. The plaintext is returned once and never stored — copy it now.

    Args:
        body (PulsightInternalCorePortsInputAPIKeyCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCorePortsInputCreatedAPIKey
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PulsightInternalCorePortsInputAPIKeyCreateRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCorePortsInputCreatedAPIKey
]:
    """Create API Key

     Creates an api token. The plaintext is returned once and never stored — copy it now.

    Args:
        body (PulsightInternalCorePortsInputAPIKeyCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCorePortsInputCreatedAPIKey]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PulsightInternalCorePortsInputAPIKeyCreateRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCorePortsInputCreatedAPIKey
    | None
):
    """Create API Key

     Creates an api token. The plaintext is returned once and never stored — copy it now.

    Args:
        body (PulsightInternalCorePortsInputAPIKeyCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCorePortsInputCreatedAPIKey
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
