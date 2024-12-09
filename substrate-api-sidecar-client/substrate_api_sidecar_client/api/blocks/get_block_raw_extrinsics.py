from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.block_raw import BlockRaw
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    block_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/blocks/{block_id}/extrinsics-raw",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BlockRaw, Error]]:
    if response.status_code == 200:
        response_200 = BlockRaw.from_dict(response.json())

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
) -> Response[Union[BlockRaw, Error]]:
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
) -> Response[Union[BlockRaw, Error]]:
    """Get a blocks header & its extrinsics as hex values.

     Returns a block & its extrinsics as hex values. BlockId can either be a block hash or a block
    height.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockRaw, Error]]
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
) -> Optional[Union[BlockRaw, Error]]:
    """Get a blocks header & its extrinsics as hex values.

     Returns a block & its extrinsics as hex values. BlockId can either be a block hash or a block
    height.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockRaw, Error]
    """

    return sync_detailed(
        block_id=block_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BlockRaw, Error]]:
    """Get a blocks header & its extrinsics as hex values.

     Returns a block & its extrinsics as hex values. BlockId can either be a block hash or a block
    height.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BlockRaw, Error]]
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
) -> Optional[Union[BlockRaw, Error]]:
    """Get a blocks header & its extrinsics as hex values.

     Returns a block & its extrinsics as hex values. BlockId can either be a block hash or a block
    height.

    Args:
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BlockRaw, Error]
    """

    return (
        await asyncio_detailed(
            block_id=block_id,
            client=client,
        )
    ).parsed
