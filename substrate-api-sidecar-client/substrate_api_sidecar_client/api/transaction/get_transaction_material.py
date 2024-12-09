from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.transaction_material import TransactionMaterial
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    at: Union[Unset, str] = UNSET,
    no_meta: Union[Unset, bool] = False,
    metadata: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params["noMeta"] = no_meta

    params["metadata"] = metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transaction/material",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, TransactionMaterial]]:
    if response.status_code == 200:
        response_200 = TransactionMaterial.from_dict(response.json())

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
) -> Response[Union[Error, TransactionMaterial]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    no_meta: Union[Unset, bool] = False,
    metadata: Union[Unset, str] = UNSET,
) -> Response[Union[Error, TransactionMaterial]]:
    """Get all the network information needed to construct a transaction offline.

     Returns the material that is universal to constructing any signed transaction offline. Replaces
    `/tx/artifacts` from versions < v1.0.0.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        no_meta (Union[Unset, bool]):  Default: False.
        metadata (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TransactionMaterial]]
    """

    kwargs = _get_kwargs(
        at=at,
        no_meta=no_meta,
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    no_meta: Union[Unset, bool] = False,
    metadata: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, TransactionMaterial]]:
    """Get all the network information needed to construct a transaction offline.

     Returns the material that is universal to constructing any signed transaction offline. Replaces
    `/tx/artifacts` from versions < v1.0.0.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        no_meta (Union[Unset, bool]):  Default: False.
        metadata (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TransactionMaterial]
    """

    return sync_detailed(
        client=client,
        at=at,
        no_meta=no_meta,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    no_meta: Union[Unset, bool] = False,
    metadata: Union[Unset, str] = UNSET,
) -> Response[Union[Error, TransactionMaterial]]:
    """Get all the network information needed to construct a transaction offline.

     Returns the material that is universal to constructing any signed transaction offline. Replaces
    `/tx/artifacts` from versions < v1.0.0.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        no_meta (Union[Unset, bool]):  Default: False.
        metadata (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TransactionMaterial]]
    """

    kwargs = _get_kwargs(
        at=at,
        no_meta=no_meta,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    no_meta: Union[Unset, bool] = False,
    metadata: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, TransactionMaterial]]:
    """Get all the network information needed to construct a transaction offline.

     Returns the material that is universal to constructing any signed transaction offline. Replaces
    `/tx/artifacts` from versions < v1.0.0.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        no_meta (Union[Unset, bool]):  Default: False.
        metadata (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TransactionMaterial]
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
            no_meta=no_meta,
            metadata=metadata,
        )
    ).parsed
