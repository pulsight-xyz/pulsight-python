from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_trader_tip_stats_response import (
    InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    window: str | Unset = "7d",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{wallet_address}/tips".format(
            wallet_address=quote(str(wallet_address), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
    | None
):
    if response.status_code == 200:
        response_200 = (
            InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse.from_dict(
                response.json()
            )
        )

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
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
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
    window: str | Unset = "7d",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
]:
    """Get Trader Tip Stats

    Args:
        wallet_address (str):
        window (str | Unset):  Default: '7d'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    window: str | Unset = "7d",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
    | None
):
    """Get Trader Tip Stats

    Args:
        wallet_address (str):
        window (str | Unset):  Default: '7d'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
    """

    return sync_detailed(
        wallet_address=wallet_address,
        client=client,
        window=window,
    ).parsed


async def asyncio_detailed(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    window: str | Unset = "7d",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
]:
    """Get Trader Tip Stats

    Args:
        wallet_address (str):
        window (str | Unset):  Default: '7d'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse]
    """

    kwargs = _get_kwargs(
        wallet_address=wallet_address,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wallet_address: str,
    *,
    client: AuthenticatedClient,
    window: str | Unset = "7d",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
    | None
):
    """Get Trader Tip Stats

    Args:
        wallet_address (str):
        window (str | Unset):  Default: '7d'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerTraderTipStatsResponse
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            window=window,
        )
    ).parsed
