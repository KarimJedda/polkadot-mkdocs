from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_with_decoded_xcm_msgs import BlockWithDecodedXcmMsgs
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    block_id: str,
    *,
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    finalized_key: Union[Unset, bool] = UNSET,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["eventDocs"] = event_docs

    params["extrinsicDocs"] = extrinsic_docs

    params["noFees"] = no_fees

    params["finalizedKey"] = finalized_key

    params["decodedXcmMsgs"] = decoded_xcm_msgs

    params["paraId"] = para_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/blocks/{block_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BlockWithDecodedXcmMsgs, Error]]:
    if response.status_code == 200:
        response_200 = BlockWithDecodedXcmMsgs.from_dict(response.json())

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
) -> Response[Union[BlockWithDecodedXcmMsgs, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    finalized_key: Union[Unset, bool] = UNSET,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Response[Union[BlockWithDecodedXcmMsgs, Error]]:
    """Get a block by its height or hash.

     Returns a single block. BlockId can either be a block hash or a block height. Replaces
    `/block/{number}` from versions < v1.0.0.

    Args:
        block_id (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        finalized_key (Union[Unset, bool]):
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockWithDecodedXcmMsgs, Error]]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        finalized_key=finalized_key,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    finalized_key: Union[Unset, bool] = UNSET,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Optional[Union[BlockWithDecodedXcmMsgs, Error]]:
    """Get a block by its height or hash.

     Returns a single block. BlockId can either be a block hash or a block height. Replaces
    `/block/{number}` from versions < v1.0.0.

    Args:
        block_id (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        finalized_key (Union[Unset, bool]):
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockWithDecodedXcmMsgs, Error]
    """

    return sync_detailed(
        block_id=block_id,
        client=client,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        finalized_key=finalized_key,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    ).parsed


async def asyncio_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    finalized_key: Union[Unset, bool] = UNSET,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Response[Union[BlockWithDecodedXcmMsgs, Error]]:
    """Get a block by its height or hash.

     Returns a single block. BlockId can either be a block hash or a block height. Replaces
    `/block/{number}` from versions < v1.0.0.

    Args:
        block_id (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        finalized_key (Union[Unset, bool]):
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockWithDecodedXcmMsgs, Error]]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        event_docs=event_docs,
        extrinsic_docs=extrinsic_docs,
        no_fees=no_fees,
        finalized_key=finalized_key,
        decoded_xcm_msgs=decoded_xcm_msgs,
        para_id=para_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    event_docs: Union[Unset, bool] = False,
    extrinsic_docs: Union[Unset, bool] = False,
    no_fees: Union[Unset, bool] = False,
    finalized_key: Union[Unset, bool] = UNSET,
    decoded_xcm_msgs: Union[Unset, bool] = False,
    para_id: Union[Unset, str] = UNSET,
) -> Optional[Union[BlockWithDecodedXcmMsgs, Error]]:
    """Get a block by its height or hash.

     Returns a single block. BlockId can either be a block hash or a block height. Replaces
    `/block/{number}` from versions < v1.0.0.

    Args:
        block_id (str):
        event_docs (Union[Unset, bool]):  Default: False.
        extrinsic_docs (Union[Unset, bool]):  Default: False.
        no_fees (Union[Unset, bool]):  Default: False.
        finalized_key (Union[Unset, bool]):
        decoded_xcm_msgs (Union[Unset, bool]):  Default: False.
        para_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockWithDecodedXcmMsgs, Error]
    """

    return (
        await asyncio_detailed(
            block_id=block_id,
            client=client,
            event_docs=event_docs,
            extrinsic_docs=extrinsic_docs,
            no_fees=no_fees,
            finalized_key=finalized_key,
            decoded_xcm_msgs=decoded_xcm_msgs,
            para_id=para_id,
        )
    ).parsed
