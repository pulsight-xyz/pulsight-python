from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_usecases_trader_trader_list_result import (
    PulsightInternalCoreUsecasesTraderTraderListResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: str | Unset = "total_profit_7d",
    direction: str | Unset = "desc",
    favorites_only: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["sort_by"] = sort_by

    params["direction"] = direction

    params["favorites_only"] = favorites_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreUsecasesTraderTraderListResult.from_dict(
            response.json()
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
    | PulsightInternalCoreUsecasesTraderTraderListResult
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
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: str | Unset = "total_profit_7d",
    direction: str | Unset = "desc",
    favorites_only: bool | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
]:
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'total_profit_7d'.
        direction (str | Unset):  Default: 'desc'.
        favorites_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        favorites_only=favorites_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: str | Unset = "total_profit_7d",
    direction: str | Unset = "desc",
    favorites_only: bool | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
    | None
):
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'total_profit_7d'.
        direction (str | Unset):  Default: 'desc'.
        favorites_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        favorites_only=favorites_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: str | Unset = "total_profit_7d",
    direction: str | Unset = "desc",
    favorites_only: bool | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
]:
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'total_profit_7d'.
        direction (str | Unset):  Default: 'desc'.
        favorites_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        favorites_only=favorites_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: str | Unset = "total_profit_7d",
    direction: str | Unset = "desc",
    favorites_only: bool | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
    | None
):
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (str | Unset):  Default: 'total_profit_7d'.
        direction (str | Unset):  Default: 'desc'.
        favorites_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            direction=direction,
            favorites_only=favorites_only,
        )
    ).parsed
