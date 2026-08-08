from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_trader_neighbors_response import (
    InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    rel: str | Unset = UNSET,
    plane: str | Unset = UNSET,
    window: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rel"] = rel

    params["plane"] = plane

    params["window"] = window

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{wallet_address}/neighbours".format(
            wallet_address=quote(str(wallet_address), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse | None:
    if response.status_code == 200:
        response_200 = (
            InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    rel: str | Unset = UNSET,
    plane: str | Unset = UNSET,
    window: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse]:
    """Wallets seen trading just before / after a trader

    Args:
        wallet_address (str):
        rel (str | Unset):
        plane (str | Unset):
        window (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        rel=rel,
        plane=plane,
        window=window,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    rel: str | Unset = UNSET,
    plane: str | Unset = UNSET,
    window: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse | None:
    """Wallets seen trading just before / after a trader

    Args:
        wallet_address (str):
        rel (str | Unset):
        plane (str | Unset):
        window (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        rel=rel,
        plane=plane,
        window=window,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    rel: str | Unset = UNSET,
    plane: str | Unset = UNSET,
    window: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse]:
    """Wallets seen trading just before / after a trader

    Args:
        wallet_address (str):
        rel (str | Unset):
        plane (str | Unset):
        window (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        rel=rel,
        plane=plane,
        window=window,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: AuthenticatedClient | Client,
    rel: str | Unset = UNSET,
    plane: str | Unset = UNSET,
    window: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse | None:
    """Wallets seen trading just before / after a trader

    Args:
        wallet_address (str):
        rel (str | Unset):
        plane (str | Unset):
        window (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerTraderNeighborsResponse
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            rel=rel,
            plane=plane,
            window=window,
            limit=limit,
        )
    ).parsed
