from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_adapters_primary_http_handler_error_response import (
    InternalAdaptersPrimaryHttpHandlerErrorResponse,
)
from ...models.internal_adapters_primary_http_handler_paginated_credit_ledger import (
    InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/me/credits/ledger",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
    | None
):
    if response.status_code == 200:
        response_200 = (
            InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger.from_dict(
                response.json()
            )
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
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
]:
    """Get My Credit Ledger

     Returns one page of the caller's credit ledger entries (grants, consumes, refunds), newest first,
    alongside the total the request matches. `from` and `to` are RFC3339 and bound a half-open [from,
    to) window; either may be omitted to leave that side unbounded, and `total` counts the window rather
    than the whole ledger.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
    | None
):
    """Get My Credit Ledger

     Returns one page of the caller's credit ledger entries (grants, consumes, refunds), newest first,
    alongside the total the request matches. `from` and `to` are RFC3339 and bound a half-open [from,
    to) window; either may be omitted to leave that side unbounded, and `total` counts the window rather
    than the whole ledger.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> Response[
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
]:
    """Get My Credit Ledger

     Returns one page of the caller's credit ledger entries (grants, consumes, refunds), newest first,
    alongside the total the request matches. `from` and `to` are RFC3339 and bound a half-open [from,
    to) window; either may be omitted to leave that side unbounded, and `total` counts the window rather
    than the whole ledger.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
) -> (
    InternalAdaptersPrimaryHttpHandlerErrorResponse
    | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
    | None
):
    """Get My Credit Ledger

     Returns one page of the caller's credit ledger entries (grants, consumes, refunds), newest first,
    alongside the total the request matches. `from` and `to` are RFC3339 and bound a half-open [from,
    to) window; either may be omitted to leave that side unbounded, and `total` counts the window rather
    than the whole ledger.

    Args:
        limit (int | Unset):
        offset (int | Unset):
        from_ (str | Unset):
        to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalAdaptersPrimaryHttpHandlerErrorResponse | InternalAdaptersPrimaryHttpHandlerPaginatedCreditLedger
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            from_=from_,
            to=to,
        )
    ).parsed
