from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_api_key_rename_request import (
    InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
)
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/me/api-keys/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | InternalAdaptersPrimaryHttpHandlerErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | InternalAdaptersPrimaryHttpHandlerErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
) -> Response[Any | InternalAdaptersPrimaryHttpHandlerErrorResponse]:
    """Rename API Key

     Updates the display name of one of the caller's api tokens.

    Args:
        id (str):
        body (InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
) -> Any | InternalAdaptersPrimaryHttpHandlerErrorResponse | None:
    """Rename API Key

     Updates the display name of one of the caller's api tokens.

    Args:
        id (str):
        body (InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
) -> Response[Any | InternalAdaptersPrimaryHttpHandlerErrorResponse]:
    """Rename API Key

     Updates the display name of one of the caller's api tokens.

    Args:
        id (str):
        body (InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest,
) -> Any | InternalAdaptersPrimaryHttpHandlerErrorResponse | None:
    """Rename API Key

     Updates the display name of one of the caller's api tokens.

    Args:
        id (str):
        body (InternalAdaptersPrimaryHttpHandlerApiKeyRenameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
