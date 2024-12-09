from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block import Block
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    range_: str,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["range"] = range_

    params["eventDocs"] = event_docs

    params["extrinsicDocs"] = extrinsic_docs

    params["noFees"] = no_fees

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/blocks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list["Block"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_blocks_item_data in _response_200:
            componentsschemas_blocks_item = Block.from_dict(componentsschemas_blocks_item_data)

            response_200.append(componentsschemas_blocks_item)

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
) -> Response[Union[Error, list["Block"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    range_: str,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
) -> Response[Union[Error, list["Block"]]]:
    """Get a range of blocks by their height.

     Given a range query parameter return an array of all the blocks within that range.

    Args:
        range_ (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['Block']]]
    """

    kwargs = _get_kwargs(
        range_=range_,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    range_: str,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
) -> Optional[Union[Error, list["Block"]]]:
    """Get a range of blocks by their height.

     Given a range query parameter return an array of all the blocks within that range.

    Args:
        range_ (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['Block']]
    """

    return sync_detailed(
        client=client,
        range_=range_,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    range_: str,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
) -> Response[Union[Error, list["Block"]]]:
    """Get a range of blocks by their height.

     Given a range query parameter return an array of all the blocks within that range.

    Args:
        range_ (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['Block']]]
    """

    kwargs = _get_kwargs(
        range_=range_,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    range_: str,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
) -> Optional[Union[Error, list["Block"]]]:
    """Get a range of blocks by their height.

     Given a range query parameter return an array of all the blocks within that range.

    Args:
        range_ (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['Block']]
    """

    return (
        await asyncio_detailed(
            client=client,
            range_=range_,
            event_docs=event_docs,
            extrinsic_docs=extrinsic_docs,
            no_fees=no_fees,
        )
    ).parsed
