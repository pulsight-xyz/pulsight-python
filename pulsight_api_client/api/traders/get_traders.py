from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_traders_sort_by import GetTradersSortBy
from ...models.get_traders_window import GetTradersWindow
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
    sort_by: GetTradersSortBy | Unset = GetTradersSortBy.REALIZED_PROFIT,
    direction: str | Unset = "desc",
    window: GetTradersWindow | Unset = GetTradersWindow.VALUE_1,
    f: list[str] | Unset = UNSET,
    favorites_only: bool | Unset = UNSET,
    tracked_only: bool | Unset = UNSET,
    extra_windows: str | Unset = UNSET,
    unit: str | Unset = "sol",
    ref: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["direction"] = direction

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    json_f: list[str] | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params["favorites_only"] = favorites_only

    params["tracked_only"] = tracked_only

    params["extra_windows"] = extra_windows

    params["unit"] = unit

    params["ref"] = ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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

    if response.status_code == 503:
        response_503 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_503

    if response.status_code == 504:
        response_504 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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
    sort_by: GetTradersSortBy | Unset = GetTradersSortBy.REALIZED_PROFIT,
    direction: str | Unset = "desc",
    window: GetTradersWindow | Unset = GetTradersWindow.VALUE_1,
    f: list[str] | Unset = UNSET,
    favorites_only: bool | Unset = UNSET,
    tracked_only: bool | Unset = UNSET,
    extra_windows: str | Unset = UNSET,
    unit: str | Unset = "sol",
    ref: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
]:
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting. The page is ranked by
    `sort_by` at `window`; every row carries its 7d and 30d figures, plus the 1d and lifetime families
    the window or `extra_windows` names.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (GetTradersSortBy | Unset):  Default: GetTradersSortBy.REALIZED_PROFIT.
        direction (str | Unset):  Default: 'desc'.
        window (GetTradersWindow | Unset):  Default: GetTradersWindow.VALUE_1.
        f (list[str] | Unset):
        favorites_only (bool | Unset):
        tracked_only (bool | Unset):
        extra_windows (str | Unset):
        unit (str | Unset):  Default: 'sol'.
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        window=window,
        f=f,
        favorites_only=favorites_only,
        tracked_only=tracked_only,
        extra_windows=extra_windows,
        unit=unit,
        ref=ref,
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
    sort_by: GetTradersSortBy | Unset = GetTradersSortBy.REALIZED_PROFIT,
    direction: str | Unset = "desc",
    window: GetTradersWindow | Unset = GetTradersWindow.VALUE_1,
    f: list[str] | Unset = UNSET,
    favorites_only: bool | Unset = UNSET,
    tracked_only: bool | Unset = UNSET,
    extra_windows: str | Unset = UNSET,
    unit: str | Unset = "sol",
    ref: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
    | None
):
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting. The page is ranked by
    `sort_by` at `window`; every row carries its 7d and 30d figures, plus the 1d and lifetime families
    the window or `extra_windows` names.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (GetTradersSortBy | Unset):  Default: GetTradersSortBy.REALIZED_PROFIT.
        direction (str | Unset):  Default: 'desc'.
        window (GetTradersWindow | Unset):  Default: GetTradersWindow.VALUE_1.
        f (list[str] | Unset):
        favorites_only (bool | Unset):
        tracked_only (bool | Unset):
        extra_windows (str | Unset):
        unit (str | Unset):  Default: 'sol'.
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        window=window,
        f=f,
        favorites_only=favorites_only,
        tracked_only=tracked_only,
        extra_windows=extra_windows,
        unit=unit,
        ref=ref,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: GetTradersSortBy | Unset = GetTradersSortBy.REALIZED_PROFIT,
    direction: str | Unset = "desc",
    window: GetTradersWindow | Unset = GetTradersWindow.VALUE_1,
    f: list[str] | Unset = UNSET,
    favorites_only: bool | Unset = UNSET,
    tracked_only: bool | Unset = UNSET,
    extra_windows: str | Unset = UNSET,
    unit: str | Unset = "sol",
    ref: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
]:
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting. The page is ranked by
    `sort_by` at `window`; every row carries its 7d and 30d figures, plus the 1d and lifetime families
    the window or `extra_windows` names.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (GetTradersSortBy | Unset):  Default: GetTradersSortBy.REALIZED_PROFIT.
        direction (str | Unset):  Default: 'desc'.
        window (GetTradersWindow | Unset):  Default: GetTradersWindow.VALUE_1.
        f (list[str] | Unset):
        favorites_only (bool | Unset):
        tracked_only (bool | Unset):
        extra_windows (str | Unset):
        unit (str | Unset):  Default: 'sol'.
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderTraderListResult]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        direction=direction,
        window=window,
        f=f,
        favorites_only=favorites_only,
        tracked_only=tracked_only,
        extra_windows=extra_windows,
        unit=unit,
        ref=ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    sort_by: GetTradersSortBy | Unset = GetTradersSortBy.REALIZED_PROFIT,
    direction: str | Unset = "desc",
    window: GetTradersWindow | Unset = GetTradersWindow.VALUE_1,
    f: list[str] | Unset = UNSET,
    favorites_only: bool | Unset = UNSET,
    tracked_only: bool | Unset = UNSET,
    extra_windows: str | Unset = UNSET,
    unit: str | Unset = "sol",
    ref: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderTraderListResult
    | None
):
    """List Traders

     Retrieves a list of traders supporting advanced filtering and sorting. The page is ranked by
    `sort_by` at `window`; every row carries its 7d and 30d figures, plus the 1d and lifetime families
    the window or `extra_windows` names.

    Args:
        limit (int | Unset):  Default: 20.
        offset (int | Unset):  Default: 0.
        sort_by (GetTradersSortBy | Unset):  Default: GetTradersSortBy.REALIZED_PROFIT.
        direction (str | Unset):  Default: 'desc'.
        window (GetTradersWindow | Unset):  Default: GetTradersWindow.VALUE_1.
        f (list[str] | Unset):
        favorites_only (bool | Unset):
        tracked_only (bool | Unset):
        extra_windows (str | Unset):
        unit (str | Unset):  Default: 'sol'.
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

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
            window=window,
            f=f,
            favorites_only=favorites_only,
            tracked_only=tracked_only,
            extra_windows=extra_windows,
            unit=unit,
            ref=ref,
        )
    ).parsed
