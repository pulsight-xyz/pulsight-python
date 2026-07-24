from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_webhook_notifier_create_request import (
    InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
)
from ...models.pulsight_internal_core_domain_webhook_notifier import (
    PulsightInternalCoreDomainWebhookNotifier,
)
from ...types import Response


def _get_kwargs(
    *,
    body: InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/webhook-notifiers/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainWebhookNotifier
    | None
):
    if response.status_code == 201:
        response_201 = PulsightInternalCoreDomainWebhookNotifier.from_dict(
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
    | PulsightInternalCoreDomainWebhookNotifier
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
    body: InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainWebhookNotifier
]:
    """Create Webhook Notifier

     Creates a new webhook notifier for the authenticated user.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainWebhookNotifier]
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
    body: InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainWebhookNotifier
    | None
):
    """Create Webhook Notifier

     Creates a new webhook notifier for the authenticated user.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainWebhookNotifier
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainWebhookNotifier
]:
    """Create Webhook Notifier

     Creates a new webhook notifier for the authenticated user.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainWebhookNotifier]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainWebhookNotifier
    | None
):
    """Create Webhook Notifier

     Creates a new webhook notifier for the authenticated user.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerWebhookNotifierCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainWebhookNotifier
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
