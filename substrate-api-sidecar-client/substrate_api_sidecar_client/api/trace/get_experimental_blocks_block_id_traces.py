from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blocks_trace import BlocksTrace
from ...types import Response


def _get_kwargs(
    block_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/experimental/blocks/{block_id}/traces",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BlocksTrace]:
    if response.status_code == 200:
        response_200 = BlocksTrace.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BlocksTrace]:
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
) -> Response[BlocksTrace]:
    """[Experimental - subject to breaking change.] Get traces for the given `blockId`.

     Returns traces (spans and events) of the specified block from
    RPC `state_straceBlock`. Consult the [RPC docs](https://github.com/paritytech/substrate/blob/aba8760
    01651506f85c14baf26e006b36092e1a0/client/rpc-api/src/state/mod.rs#L140) for conceptual info.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocksTrace]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BlocksTrace]:
    """[Experimental - subject to breaking change.] Get traces for the given `blockId`.

     Returns traces (spans and events) of the specified block from
    RPC `state_straceBlock`. Consult the [RPC docs](https://github.com/paritytech/substrate/blob/aba8760
    01651506f85c14baf26e006b36092e1a0/client/rpc-api/src/state/mod.rs#L140) for conceptual info.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocksTrace
    """

    return sync_detailed(
        block_id=block_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BlocksTrace]:
    """[Experimental - subject to breaking change.] Get traces for the given `blockId`.

     Returns traces (spans and events) of the specified block from
    RPC `state_straceBlock`. Consult the [RPC docs](https://github.com/paritytech/substrate/blob/aba8760
    01651506f85c14baf26e006b36092e1a0/client/rpc-api/src/state/mod.rs#L140) for conceptual info.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocksTrace]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BlocksTrace]:
    """[Experimental - subject to breaking change.] Get traces for the given `blockId`.

     Returns traces (spans and events) of the specified block from
    RPC `state_straceBlock`. Consult the [RPC docs](https://github.com/paritytech/substrate/blob/aba8760
    01651506f85c14baf26e006b36092e1a0/client/rpc-api/src/state/mod.rs#L140) for conceptual info.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocksTrace
    """

    return (
        await asyncio_detailed(
            block_id=block_id,
            client=client,
        )
    ).parsed
