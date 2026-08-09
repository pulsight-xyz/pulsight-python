from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_copyability_request import (
    InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
)
from ...models.internal_adapters_primary_http_handler_copyability_response import (
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse,
)
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/traders/copyability",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = InternalAdaptersPrimaryHttpHandlerCopyabilityResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = InternalAdaptersPrimaryHttpHandlerErrorResponse.from_dict(
            response.json()
        )

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
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
    body: InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Copyability of a wallet set at simulated latencies

     For each wallet's fills, the price a copier filling N blocks later would have got — an entry/exit
    slippage curve and the share of the wallet's edge that survives. Latency is counted in SLOTS, since
    the stored swap timestamp resolves only to whole seconds. Measures PRICE TRANSFER, not PnL. Supply
    size_lamports to also get the EXECUTION half: the slippage band each fill needed (split signal-buy
    vs follow-on) and what each widening step buys, priced at the target's own exit.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerCopyabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerCopyabilityResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Copyability of a wallet set at simulated latencies

     For each wallet's fills, the price a copier filling N blocks later would have got — an entry/exit
    slippage curve and the share of the wallet's edge that survives. Latency is counted in SLOTS, since
    the stored swap timestamp resolves only to whole seconds. Measures PRICE TRANSFER, not PnL. Supply
    size_lamports to also get the EXECUTION half: the slippage band each fill needed (split signal-buy
    vs follow-on) and what each widening step buys, priced at the target's own exit.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerCopyabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerCopyabilityResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
]:
    """Copyability of a wallet set at simulated latencies

     For each wallet's fills, the price a copier filling N blocks later would have got — an entry/exit
    slippage curve and the share of the wallet's edge that survives. Latency is counted in SLOTS, since
    the stored swap timestamp resolves only to whole seconds. Measures PRICE TRANSFER, not PnL. Supply
    size_lamports to also get the EXECUTION half: the slippage band each fill needed (split signal-buy
    vs follow-on) and what each widening step buys, priced at the target's own exit.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerCopyabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerCopyabilityResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalAdaptersPrimaryHttpHandlerCopyabilityRequest,
) -> (
    InternalAdaptersPrimaryHttpHandlerCopyabilityResponse
    | InternalAdaptersPrimaryHttpHandlerErrorResponse
    | None
):
    """Copyability of a wallet set at simulated latencies

     For each wallet's fills, the price a copier filling N blocks later would have got — an entry/exit
    slippage curve and the share of the wallet's edge that survives. Latency is counted in SLOTS, since
    the stored swap timestamp resolves only to whole seconds. Measures PRICE TRANSFER, not PnL. Supply
    size_lamports to also get the EXECUTION half: the slippage band each fill needed (split signal-buy
    vs follow-on) and what each widening step buys, priced at the target's own exit.

    Args:
        body (InternalAdaptersPrimaryHttpHandlerCopyabilityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerCopyabilityResponse | InternalAdaptersPrimaryHttpHandlerErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
