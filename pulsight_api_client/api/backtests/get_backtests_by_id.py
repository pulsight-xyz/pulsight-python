from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_usecases_backtest_backtest_record import (
    PulsightInternalCoreUsecasesBacktestBacktestRecord,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/backtests/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreUsecasesBacktestBacktestRecord.from_dict(
            response.json()
        )

        return response_200

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
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
]:
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
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
]:
    """Get Backtest

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesBacktestBacktestRecord]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
    | None
):
    """Get Backtest

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesBacktestBacktestRecord
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
]:
    """Get Backtest

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesBacktestBacktestRecord]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesBacktestBacktestRecord
    | None
):
    """Get Backtest

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesBacktestBacktestRecord
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
