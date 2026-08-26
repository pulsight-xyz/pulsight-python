from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.pulsight_internal_core_domain_aggregator_mint_activity_seed import (
    PulsightInternalCoreDomainAggregatorMintActivitySeed,
)
from ...types import UNSET, Response


def _get_kwargs(
    pubkey: str,
    *,
    from_: int,
    to: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/mints/{pubkey}/activity".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
    | None
):
    if response.status_code == 200:
        response_200 = PulsightInternalCoreDomainAggregatorMintActivitySeed.from_dict(
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
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
]:
    """Mint Activity Seed

     Returns the mint's per-minute swap count + network fees (tx fee + MEV tip, lamports) over [from,
    to), plus the lifetime totals strictly before `from`. Range capped at 25 hours.

    Args:
        pubkey (str):
        from_ (int):
        to (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintActivitySeed]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
    | None
):
    """Mint Activity Seed

     Returns the mint's per-minute swap count + network fees (tx fee + MEV tip, lamports) over [from,
    to), plus the lifetime totals strictly before `from`. Range capped at 25 hours.

    Args:
        pubkey (str):
        from_ (int):
        to (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintActivitySeed
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
]:
    """Mint Activity Seed

     Returns the mint's per-minute swap count + network fees (tx fee + MEV tip, lamports) over [from,
    to), plus the lifetime totals strictly before `from`. Range capped at 25 hours.

    Args:
        pubkey (str):
        from_ (int):
        to (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintActivitySeed]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient,
    from_: int,
    to: int,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | PulsightInternalCoreDomainAggregatorMintActivitySeed
    | None
):
    """Mint Activity Seed

     Returns the mint's per-minute swap count + network fees (tx fee + MEV tip, lamports) over [from,
    to), plus the lifetime totals strictly before `from`. Range capped at 25 hours.

    Args:
        pubkey (str):
        from_ (int):
        to (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | PulsightInternalCoreDomainAggregatorMintActivitySeed
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
