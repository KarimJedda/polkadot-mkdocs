from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.extrinsic_index import ExtrinsicIndex
from ...types import UNSET, Response, Unset


def _get_kwargs(
    block_id: str,
    extrinsic_index: str,
    *,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["eventDocs"] = event_docs

    params["extrinsicDocs"] = extrinsic_docs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/blocks/{block_id}/extrinsics/{extrinsic_index}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ExtrinsicIndex]]:
    if response.status_code == 200:
        response_200 = ExtrinsicIndex.from_dict(response.json())

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
) -> Response[Union[Error, ExtrinsicIndex]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    block_id: str,
    extrinsic_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
) -> Response[Union[Error, ExtrinsicIndex]]:
    """Get an extrinsic by its extrinsicIndex and block height or hash. The pair blockId, extrinsicIndex is
    sometimes referred to as a Timepoint.

     Returns a single extrinsic.

    Args:
        block_id (str):
        extrinsic_index (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExtrinsicIndex]]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        extrinsic_index=extrinsic_index,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    block_id: str,
    extrinsic_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
) -> Optional[Union[Error, ExtrinsicIndex]]:
    """Get an extrinsic by its extrinsicIndex and block height or hash. The pair blockId, extrinsicIndex is
    sometimes referred to as a Timepoint.

     Returns a single extrinsic.

    Args:
        block_id (str):
        extrinsic_index (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExtrinsicIndex]
    """

    return sync_detailed(
        block_id=block_id,
        extrinsic_index=extrinsic_index,
        client=client,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
    ).parsed


async def asyncio_detailed(
    block_id: str,
    extrinsic_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
) -> Response[Union[Error, ExtrinsicIndex]]:
    """Get an extrinsic by its extrinsicIndex and block height or hash. The pair blockId, extrinsicIndex is
    sometimes referred to as a Timepoint.

     Returns a single extrinsic.

    Args:
        block_id (str):
        extrinsic_index (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExtrinsicIndex]]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        extrinsic_index=extrinsic_index,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    block_id: str,
    extrinsic_index: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
) -> Optional[Union[Error, ExtrinsicIndex]]:
    """Get an extrinsic by its extrinsicIndex and block height or hash. The pair blockId, extrinsicIndex is
    sometimes referred to as a Timepoint.

     Returns a single extrinsic.

    Args:
        block_id (str):
        extrinsic_index (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExtrinsicIndex]
    """

    return (
        await asyncio_detailed(
            block_id=block_id,
            extrinsic_index=extrinsic_index,
            client=client,
            event_docs=event_docs,
            extrinsic_docs=extrinsic_docs,
        )
    ).parsed
