from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_ohlcv_candle import (
    PulsightInternalCoreDomainAggregatorOHLCVCandle,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["mint"] = mint

    params["tf"] = tf

    params["pool"] = pool

    params["quote"] = quote

    params["from"] = from_

    params["to"] = to

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
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                PulsightInternalCoreDomainAggregatorOHLCVCandle.from_dict(
                    response_200_item_data
                )
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
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
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
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
]:
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        tf=tf,
        pool=pool,
        quote=quote,
        from_=from_,
        to=to,
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
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
    | None
):
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
    """

    return sync_detailed(
        client=client,
        mint=mint,
        tf=tf,
        pool=pool,
        quote=quote,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
]:
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]]
    """

    kwargs = _get_kwargs(
        mint=mint,
        tf=tf,
        pool=pool,
        quote=quote,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mint: str,
    tf: str,
    pool: str | Unset = UNSET,
    quote: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
    | None
):
    """List OHLCV Candles

     Returns OHLCV buckets for a mint at the given timeframe within `[from, to)`. Both time params are
    optional; omitting them returns the last ~500 candles.

    Args:
        mint (str):
        tf (str):
        pool (str | Unset):
        quote (str | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | list[PulsightInternalCoreDomainAggregatorOHLCVCandle]
    """

    return (
        await asyncio_detailed(
            client=client,
            mint=mint,
            tf=tf,
            pool=pool,
            quote=quote,
            from_=from_,
            to=to,
        )
    ).parsed
