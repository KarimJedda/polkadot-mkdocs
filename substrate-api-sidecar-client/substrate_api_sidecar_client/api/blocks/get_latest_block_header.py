from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_header import BlockHeader
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    finalized: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["finalized"] = finalized

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/blocks/head/header",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BlockHeader, Error]]:
    if response.status_code == 200:
        response_200 = BlockHeader.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BlockHeader, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
) -> Response[Union[BlockHeader, Error]]:
    """Get information about the header of the most recent finalized block.

     Returns the most recently finalized block's header.

    Args:
        finalized (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockHeader, Error]]
    """

    kwargs = _get_kwargs(
        finalized=finalized,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
) -> Optional[Union[BlockHeader, Error]]:
    """Get information about the header of the most recent finalized block.

     Returns the most recently finalized block's header.

    Args:
        finalized (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockHeader, Error]
    """

    return sync_detailed(
        client=client,
        finalized=finalized,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
) -> Response[Union[BlockHeader, Error]]:
    """Get information about the header of the most recent finalized block.

     Returns the most recently finalized block's header.

    Args:
        finalized (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockHeader, Error]]
    """

    kwargs = _get_kwargs(
        finalized=finalized,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
) -> Optional[Union[BlockHeader, Error]]:
    """Get information about the header of the most recent finalized block.

     Returns the most recently finalized block's header.

    Args:
        finalized (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockHeader, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            finalized=finalized,
        )
    ).parsed
