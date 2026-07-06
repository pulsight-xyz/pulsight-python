from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_usecases_trader_daily_profits_result import (
    PulsightInternalCoreUsecasesTraderDailyProfitsResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trader_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    sort_by: str | Unset = "date",
    direction: str | Unset = "desc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["from_date"] = from_date

    params["to_date"] = to_date

    params["sort_by"] = sort_by

    params["direction"] = direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/traders/{trader_id}/daily-profits".format(
            trader_id=quote(str(trader_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreUsecasesTraderDailyProfitsResult.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

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
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    sort_by: str | Unset = "date",
    direction: str | Unset = "desc",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
]:
    """List Trader Daily Profits

     Retrieves aggregated daily profits for a specific trader.

    Args:
        trader_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        from_date (str | Unset):
        to_date (str | Unset):
        sort_by (str | Unset):  Default: 'date'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderDailyProfitsResult]
    """

    kwargs = _get_kwargs(
        trader_id=trader_id,
        limit=limit,
        offset=offset,
        from_date=from_date,
        to_date=to_date,
        sort_by=sort_by,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    sort_by: str | Unset = "date",
    direction: str | Unset = "desc",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
    | None
):
    """List Trader Daily Profits

     Retrieves aggregated daily profits for a specific trader.

    Args:
        trader_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        from_date (str | Unset):
        to_date (str | Unset):
        sort_by (str | Unset):  Default: 'date'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderDailyProfitsResult
    """

    return sync_detailed(
        trader_id=trader_id,
        client=client,
        limit=limit,
        offset=offset,
        from_date=from_date,
        to_date=to_date,
        sort_by=sort_by,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    sort_by: str | Unset = "date",
    direction: str | Unset = "desc",
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
]:
    """List Trader Daily Profits

     Retrieves aggregated daily profits for a specific trader.

    Args:
        trader_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        from_date (str | Unset):
        to_date (str | Unset):
        sort_by (str | Unset):  Default: 'date'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderDailyProfitsResult]
    """

    kwargs = _get_kwargs(
        trader_id=trader_id,
        limit=limit,
        offset=offset,
        from_date=from_date,
        to_date=to_date,
        sort_by=sort_by,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trader_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    sort_by: str | Unset = "date",
    direction: str | Unset = "desc",
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreUsecasesTraderDailyProfitsResult
    | None
):
    """List Trader Daily Profits

     Retrieves aggregated daily profits for a specific trader.

    Args:
        trader_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        from_date (str | Unset):
        to_date (str | Unset):
        sort_by (str | Unset):  Default: 'date'.
        direction (str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreUsecasesTraderDailyProfitsResult
    """

    return (
        await asyncio_detailed(
            trader_id=trader_id,
            client=client,
            limit=limit,
            offset=offset,
            from_date=from_date,
            to_date=to_date,
            sort_by=sort_by,
            direction=direction,
        )
    ).parsed
