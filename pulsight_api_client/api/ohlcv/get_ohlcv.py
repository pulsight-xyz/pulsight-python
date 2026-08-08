from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_ohlcv_row import (
    InternalAdaptersPrimaryHttpHandlerOhlcvRow,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    market: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    remove_outliers: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["mint"] = mint

    params["tf"] = tf

    params["pool"] = pool

    params["market"] = market

    params["quote"] = quote

    params["from"] = from_

    params["to"] = to

    params["limit"] = limit

    params["removeOutliers"] = remove_outliers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ohlcv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InternalAdaptersPrimaryHttpHandlerOhlcvRow.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

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
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
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
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    market: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    remove_outliers: bool | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
]:
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        market (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        remove_outliers (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        tf=tf,
        pool=pool,
        market=market,
        quote=quote,
        from_=from_,
        to=to,
        limit=limit,
        remove_outliers=remove_outliers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    market: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    remove_outliers: bool | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
    | None
):
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        market (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        remove_outliers (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
    """

    return sync_detailed(
        client=client,
        mint=mint,
        tf=tf,
        pool=pool,
        market=market,
        quote=quote,
        from_=from_,
        to=to,
        limit=limit,
        remove_outliers=remove_outliers,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    market: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    remove_outliers: bool | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
]:
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        market (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        remove_outliers (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        tf=tf,
        pool=pool,
        market=market,
        quote=quote,
        from_=from_,
        to=to,
        limit=limit,
        remove_outliers=remove_outliers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    market: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    remove_outliers: bool | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
    | None
):
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        market (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        limit (int | Unset):
        remove_outliers (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[InternalAdaptersPrimaryHttpHandlerOhlcvRow]
    """

    return (
        await asyncio_detailed(
            client=client,
            mint=mint,
            tf=tf,
            pool=pool,
            market=market,
            quote=quote,
            from_=from_,
            to=to,
            limit=limit,
            remove_outliers=remove_outliers,
        )
    ).parsed
