from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_traders_wallet_address_pnl_series_window import (
    GetApiTradersWalletAddressPnlSeriesWindow,
)
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_usecases_trader_pnl_series_result import (
    PulsightInternalCoreUsecasesTraderPnlSeriesResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wallet_address: str,
    *,
    window: GetApiTradersWalletAddressPnlSeriesWindow
    | Unset = GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{wallet_address}/pnl-series".format(
            wallet_address=quote(str(wallet_address), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreUsecasesTraderPnlSeriesResult.from_dict(
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
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
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
    window: GetApiTradersWalletAddressPnlSeriesWindow
    | Unset = GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
]:
    """Get Trader Daily PnL Series

     Returns daily realised PnL points (oldest first) for a trader, sourced from the aggregator's
    `trader_daily_pnl_series` SQL function.

    Args:
        wallet_address (str):
        window (GetApiTradersWalletAddressPnlSeriesWindow | Unset):  Default:
            GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderPnlSeriesResult]
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
    window: GetApiTradersWalletAddressPnlSeriesWindow
    | Unset = GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
    | None
):
    """Get Trader Daily PnL Series

     Returns daily realised PnL points (oldest first) for a trader, sourced from the aggregator's
    `trader_daily_pnl_series` SQL function.

    Args:
        wallet_address (str):
        window (GetApiTradersWalletAddressPnlSeriesWindow | Unset):  Default:
            GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderPnlSeriesResult
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
    window: GetApiTradersWalletAddressPnlSeriesWindow
    | Unset = GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
]:
    """Get Trader Daily PnL Series

     Returns daily realised PnL points (oldest first) for a trader, sourced from the aggregator's
    `trader_daily_pnl_series` SQL function.

    Args:
        wallet_address (str):
        window (GetApiTradersWalletAddressPnlSeriesWindow | Unset):  Default:
            GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderPnlSeriesResult]
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
    window: GetApiTradersWalletAddressPnlSeriesWindow
    | Unset = GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderPnlSeriesResult
    | None
):
    """Get Trader Daily PnL Series

     Returns daily realised PnL points (oldest first) for a trader, sourced from the aggregator's
    `trader_daily_pnl_series` SQL function.

    Args:
        wallet_address (str):
        window (GetApiTradersWalletAddressPnlSeriesWindow | Unset):  Default:
            GetApiTradersWalletAddressPnlSeriesWindow.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderPnlSeriesResult
    """

    return (
        await asyncio_detailed(
            wallet_address=wallet_address,
            client=client,
            window=window,
        )
    ).parsed
