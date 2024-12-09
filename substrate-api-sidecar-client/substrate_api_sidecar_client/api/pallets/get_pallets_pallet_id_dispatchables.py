from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pallet_dispatchables import PalletDispatchables
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pallet_id: str,
    *,
    only_ids: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["onlyIds"] = only_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/pallets/{pallet_id}/dispatchables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PalletDispatchables]]:
    if response.status_code == 200:
        response_200 = PalletDispatchables.from_dict(response.json())

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
) -> Response[Union[Error, PalletDispatchables]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, PalletDispatchables]]:
    """Get a list of dispatchables for a pallet.

     Returns a list of dispatchable item metadata for distpachable items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletDispatchables]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        only_ids=only_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, PalletDispatchables]]:
    """Get a list of dispatchables for a pallet.

     Returns a list of dispatchable item metadata for distpachable items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletDispatchables]
    """

    return sync_detailed(
        pallet_id=pallet_id,
        client=client,
        only_ids=only_ids,
    ).parsed


async def asyncio_detailed(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, PalletDispatchables]]:
    """Get a list of dispatchables for a pallet.

     Returns a list of dispatchable item metadata for distpachable items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletDispatchables]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        only_ids=only_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, PalletDispatchables]]:
    """Get a list of dispatchables for a pallet.

     Returns a list of dispatchable item metadata for distpachable items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletDispatchables]
    """

    return (
        await asyncio_detailed(
            pallet_id=pallet_id,
            client=client,
            only_ids=only_ids,
        )
    ).parsed
