from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction_pool import TransactionPool
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_fee: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeFee"] = include_fee

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/node/transaction-pool",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TransactionPool]:
    if response.status_code == 200:
        response_200 = TransactionPool.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TransactionPool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_fee: Union[Unset, bool] = False,
) -> Response[TransactionPool]:
    """Get pending extrinsics from the Substrate node.

     Returns the extrinsics that the node knows of that have not been included in a block.

    Args:
        include_fee (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionPool]
    """

    kwargs = _get_kwargs(
        include_fee=include_fee,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_fee: Union[Unset, bool] = False,
) -> Optional[TransactionPool]:
    """Get pending extrinsics from the Substrate node.

     Returns the extrinsics that the node knows of that have not been included in a block.

    Args:
        include_fee (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionPool
    """

    return sync_detailed(
        client=client,
        include_fee=include_fee,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_fee: Union[Unset, bool] = False,
) -> Response[TransactionPool]:
    """Get pending extrinsics from the Substrate node.

     Returns the extrinsics that the node knows of that have not been included in a block.

    Args:
        include_fee (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionPool]
    """

    kwargs = _get_kwargs(
        include_fee=include_fee,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_fee: Union[Unset, bool] = False,
) -> Optional[TransactionPool]:
    """Get pending extrinsics from the Substrate node.

     Returns the extrinsics that the node knows of that have not been included in a block.

    Args:
        include_fee (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionPool
    """

    return (
        await asyncio_detailed(
            client=client,
            include_fee=include_fee,
        )
    ).parsed
