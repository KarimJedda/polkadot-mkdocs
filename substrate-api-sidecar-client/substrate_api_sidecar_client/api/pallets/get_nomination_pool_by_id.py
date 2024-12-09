from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pallets_nomination_pool import PalletsNominationPool
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pool_id: str,
    *,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/pallets/nomination-pools/{pool_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PalletsNominationPool]:
    if response.status_code == 200:
        response_200 = PalletsNominationPool.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PalletsNominationPool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[PalletsNominationPool]:
    """Get information and metadata associated with a nomination pool.

     Returns information associated with a nomination pool which includes the nomination pools'
    `bondedPool`, `rewardPool` and `metadata`.

    Args:
        pool_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PalletsNominationPool]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[PalletsNominationPool]:
    """Get information and metadata associated with a nomination pool.

     Returns information associated with a nomination pool which includes the nomination pools'
    `bondedPool`, `rewardPool` and `metadata`.

    Args:
        pool_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PalletsNominationPool
    """

    return sync_detailed(
        pool_id=pool_id,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[PalletsNominationPool]:
    """Get information and metadata associated with a nomination pool.

     Returns information associated with a nomination pool which includes the nomination pools'
    `bondedPool`, `rewardPool` and `metadata`.

    Args:
        pool_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PalletsNominationPool]
    """

    kwargs = _get_kwargs(
        pool_id=pool_id,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[PalletsNominationPool]:
    """Get information and metadata associated with a nomination pool.

     Returns information associated with a nomination pool which includes the nomination pools'
    `bondedPool`, `rewardPool` and `metadata`.

    Args:
        pool_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PalletsNominationPool
    """

    return (
        await asyncio_detailed(
            pool_id=pool_id,
            client=client,
            at=at,
        )
    ).parsed
