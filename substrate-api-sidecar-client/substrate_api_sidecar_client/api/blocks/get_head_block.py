from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_with_decoded_xcm_msgs import BlockWithDecodedXcmMsgs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    finalized: Union[Unset, bool] = True,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["finalized"] = finalized

    params["eventDocs"] = event_docs

    params["extrinsicDocs"] = extrinsic_docs

    params["noFees"] = no_fees

    params["decodedXcmMsgs"] = decoded_xcm_msgs

    params["paraId"] = para_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/blocks/head",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BlockWithDecodedXcmMsgs]:
    if response.status_code == 200:
        response_200 = BlockWithDecodedXcmMsgs.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BlockWithDecodedXcmMsgs]:
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
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Response[BlockWithDecodedXcmMsgs]:
    """Get the most recently finalized block.

     Returns the most recently finalized block. Replaces `/block` from versions < v1.0.0.

    Args:
        finalized (Union[Unset, bool]):  Default: True.
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockWithDecodedXcmMsgs]
    """

    kwargs = _get_kwargs(
        finalized=finalized,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Optional[BlockWithDecodedXcmMsgs]:
    """Get the most recently finalized block.

     Returns the most recently finalized block. Replaces `/block` from versions < v1.0.0.

    Args:
        finalized (Union[Unset, bool]):  Default: True.
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockWithDecodedXcmMsgs
    """

    return sync_detailed(
        client=client,
        finalized=finalized,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Response[BlockWithDecodedXcmMsgs]:
    """Get the most recently finalized block.

     Returns the most recently finalized block. Replaces `/block` from versions < v1.0.0.

    Args:
        finalized (Union[Unset, bool]):  Default: True.
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlockWithDecodedXcmMsgs]
    """

    kwargs = _get_kwargs(
        finalized=finalized,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    finalized: Union[Unset, bool] = True,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Optional[BlockWithDecodedXcmMsgs]:
    """Get the most recently finalized block.

     Returns the most recently finalized block. Replaces `/block` from versions < v1.0.0.

    Args:
        finalized (Union[Unset, bool]):  Default: True.
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlockWithDecodedXcmMsgs
    """

    return (
        await asyncio_detailed(
            client=client,
            finalized=finalized,
            event_docs=event_docs,
            extrinsic_docs=extrinsic_docs,
            no_fees=no_fees,
            decoded_xcm_msgs=decoded_xcm_msgs,
            para_id=para_id,
        )
    ).parsed
