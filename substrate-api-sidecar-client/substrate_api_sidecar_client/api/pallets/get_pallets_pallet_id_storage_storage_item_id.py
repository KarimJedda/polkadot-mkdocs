from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pallet_storage_item import PalletStorageItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pallet_id: str,
    storage_item_id: str,
    *,
    keys: Union[Unset, list[str]] = UNSET,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_keys: Union[Unset, list[str]] = UNSET
    if not isinstance(keys, Unset):
        json_keys = keys

    params["keys"] = json_keys

    params["at"] = at

    params["metadata"] = metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/pallets/{pallet_id}/storage/{storage_item_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PalletStorageItem]]:
    if response.status_code == 200:
        response_200 = PalletStorageItem.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, PalletStorageItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pallet_id: str,
    storage_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keys: Union[Unset, list[str]] = UNSET,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Response[Union[Error, PalletStorageItem]]:
    """Get the value of a storage item.

     Returns the value stored under the storageItemId. If it is a map, query param key1 is required. If
    the storage item is double map query params key1 and key2 are required.

    Args:
        pallet_id (str):
        storage_item_id (str):
        keys (Union[Unset, list[str]]): An array of storage keys.
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletStorageItem]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        storage_item_id=storage_item_id,
        keys=keys,
        at=at,
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pallet_id: str,
    storage_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keys: Union[Unset, list[str]] = UNSET,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Optional[Union[Error, PalletStorageItem]]:
    """Get the value of a storage item.

     Returns the value stored under the storageItemId. If it is a map, query param key1 is required. If
    the storage item is double map query params key1 and key2 are required.

    Args:
        pallet_id (str):
        storage_item_id (str):
        keys (Union[Unset, list[str]]): An array of storage keys.
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletStorageItem]
    """

    return sync_detailed(
        pallet_id=pallet_id,
        storage_item_id=storage_item_id,
        client=client,
        keys=keys,
        at=at,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    pallet_id: str,
    storage_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keys: Union[Unset, list[str]] = UNSET,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Response[Union[Error, PalletStorageItem]]:
    """Get the value of a storage item.

     Returns the value stored under the storageItemId. If it is a map, query param key1 is required. If
    the storage item is double map query params key1 and key2 are required.

    Args:
        pallet_id (str):
        storage_item_id (str):
        keys (Union[Unset, list[str]]): An array of storage keys.
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletStorageItem]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        storage_item_id=storage_item_id,
        keys=keys,
        at=at,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pallet_id: str,
    storage_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keys: Union[Unset, list[str]] = UNSET,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Optional[Union[Error, PalletStorageItem]]:
    """Get the value of a storage item.

     Returns the value stored under the storageItemId. If it is a map, query param key1 is required. If
    the storage item is double map query params key1 and key2 are required.

    Args:
        pallet_id (str):
        storage_item_id (str):
        keys (Union[Unset, list[str]]): An array of storage keys.
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletStorageItem]
    """

    return (
        await asyncio_detailed(
            pallet_id=pallet_id,
            storage_item_id=storage_item_id,
            client=client,
            keys=keys,
            at=at,
            metadata=metadata,
        )
    ).parsed
