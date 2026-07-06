from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_tokens_row import (
    InternalAdaptersPrimaryHttpHandlerTokensRow,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{wallet_address}/tokens".format(
            wallet_address=quote(str(wallet_address), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InternalAdaptersPrimaryHttpHandlerTokensRow.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
]:
    """List Trader Token Positions

    Args:
        wallet_address (str):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerTokensRow]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
    | None
):
    """List Trader Token Positions

    Args:
        wallet_address (str):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
]:
    """List Trader Token Positions

    Args:
        wallet_address (str):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerTokensRow]]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
    | None
):
    """List Trader Token Positions

    Args:
        wallet_address (str):
        sort (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerTokensRow]
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed
