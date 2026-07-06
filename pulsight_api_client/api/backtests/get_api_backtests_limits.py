from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_backtest_settings_response import (
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse,
)
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/backtests/limits",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = (
            InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 401:
        response_401 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
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
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Get Backtest Limits

     Returns the per-run backtest cost ceiling (max credits per run) so clients can show and pre-check
    it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse]
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
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Get Backtest Limits

     Returns the per-run backtest cost ceiling (max credits per run) so clients can show and pre-check
    it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Get Backtest Limits

     Returns the per-run backtest cost ceiling (max credits per run) so clients can show and pre-check
    it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Get Backtest Limits

     Returns the per-run backtest cost ceiling (max credits per run) so clients can show and pre-check
    it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerBacktestSettingsResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
