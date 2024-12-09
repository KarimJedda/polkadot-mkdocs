from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pallet_errors_item import PalletErrorsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pallet_id: str,
    error_item_id: str,
    *,
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params["metadata"] = metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/pallets/{pallet_id}/errors/{error_item_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PalletErrorsItem]]:
    if response.status_code == 200:
        response_200 = PalletErrorsItem.from_dict(response.json())

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
) -> Response[Union[Error, PalletErrorsItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pallet_id: str,
    error_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Response[Union[Error, PalletErrorsItem]]:
    """Get the value of an error item.

     Returns the value stored under the errorItemId.

    Args:
        pallet_id (str):
        error_item_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletErrorsItem]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        error_item_id=error_item_id,
        at=at,
        metadata=metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pallet_id: str,
    error_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Optional[Union[Error, PalletErrorsItem]]:
    """Get the value of an error item.

     Returns the value stored under the errorItemId.

    Args:
        pallet_id (str):
        error_item_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletErrorsItem]
    """

    return sync_detailed(
        pallet_id=pallet_id,
        error_item_id=error_item_id,
        client=client,
        at=at,
        metadata=metadata,
    ).parsed


async def asyncio_detailed(
    pallet_id: str,
    error_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Response[Union[Error, PalletErrorsItem]]:
    """Get the value of an error item.

     Returns the value stored under the errorItemId.

    Args:
        pallet_id (str):
        error_item_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletErrorsItem]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        error_item_id=error_item_id,
        at=at,
        metadata=metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pallet_id: str,
    error_item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    metadata: Union[Unset, bool] = False,
) -> Optional[Union[Error, PalletErrorsItem]]:
    """Get the value of an error item.

     Returns the value stored under the errorItemId.

    Args:
        pallet_id (str):
        error_item_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        metadata (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletErrorsItem]
    """

    return (
        await asyncio_detailed(
            pallet_id=pallet_id,
            error_item_id=error_item_id,
            client=client,
            at=at,
            metadata=metadata,
        )
    ).parsed
