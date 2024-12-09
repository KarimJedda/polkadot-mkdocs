from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paras_headers import ParasHeaders
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/paras/head/included-candidates",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ParasHeaders]:
    if response.status_code == 200:
        response_200 = ParasHeaders.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ParasHeaders]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[ParasHeaders]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the heads of the included (backed
    and considered available) parachain candidates at the
    specified block height or at the most recent finalized head otherwise.

     Returns an object with all the parachain id's as keys, and their headers as values.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasHeaders]
    """

    kwargs = _get_kwargs(
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[ParasHeaders]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the heads of the included (backed
    and considered available) parachain candidates at the
    specified block height or at the most recent finalized head otherwise.

     Returns an object with all the parachain id's as keys, and their headers as values.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasHeaders
    """

    return sync_detailed(
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[ParasHeaders]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the heads of the included (backed
    and considered available) parachain candidates at the
    specified block height or at the most recent finalized head otherwise.

     Returns an object with all the parachain id's as keys, and their headers as values.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasHeaders]
    """

    kwargs = _get_kwargs(
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[ParasHeaders]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the heads of the included (backed
    and considered available) parachain candidates at the
    specified block height or at the most recent finalized head otherwise.

     Returns an object with all the parachain id's as keys, and their headers as values.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasHeaders
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
        )
    ).parsed
