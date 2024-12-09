from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pallet_events import PalletEvents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pallet_id: str,
    *,
    only_ids: Union[Unset, bool] = UNSET,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["onlyIds"] = only_ids

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/pallets/{pallet_id}/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PalletEvents]]:
    if response.status_code == 200:
        response_200 = PalletEvents.from_dict(response.json())

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
) -> Response[Union[Error, PalletEvents]]:
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
    at: Union[Unset, str] = UNSET,
) -> Response[Union[Error, PalletEvents]]:
    """Get a list of events for a pallet.

     Returns a list of event item metadata for event items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletEvents]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        only_ids=only_ids,
        at=at,
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
    at: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, PalletEvents]]:
    """Get a list of events for a pallet.

     Returns a list of event item metadata for event items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletEvents]
    """

    return sync_detailed(
        pallet_id=pallet_id,
        client=client,
        only_ids=only_ids,
        at=at,
    ).parsed


async def asyncio_detailed(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
    at: Union[Unset, str] = UNSET,
) -> Response[Union[Error, PalletEvents]]:
    """Get a list of events for a pallet.

     Returns a list of event item metadata for event items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PalletEvents]]
    """

    kwargs = _get_kwargs(
        pallet_id=pallet_id,
        only_ids=only_ids,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pallet_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    only_ids: Union[Unset, bool] = UNSET,
    at: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, PalletEvents]]:
    """Get a list of events for a pallet.

     Returns a list of event item metadata for event items of the specified palletId.

    Args:
        pallet_id (str):
        only_ids (Union[Unset, bool]):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PalletEvents]
    """

    return (
        await asyncio_detailed(
            pallet_id=pallet_id,
            client=client,
            only_ids=only_ids,
            at=at,
        )
    ).parsed
