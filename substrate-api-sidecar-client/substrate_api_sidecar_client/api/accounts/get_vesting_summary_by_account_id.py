from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_vesting_info import AccountVestingInfo
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/vesting-info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountVestingInfo, Error]]:
    if response.status_code == 200:
        response_200 = AccountVestingInfo.from_dict(response.json())

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
) -> Response[Union[AccountVestingInfo, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[Union[AccountVestingInfo, Error]]:
    """Get vesting information for an account.

     Returns the vesting schedule for an account. Replaces `/vesting/{address}` from versions < v1.0.0.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountVestingInfo, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[Union[AccountVestingInfo, Error]]:
    """Get vesting information for an account.

     Returns the vesting schedule for an account. Replaces `/vesting/{address}` from versions < v1.0.0.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountVestingInfo, Error]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[Union[AccountVestingInfo, Error]]:
    """Get vesting information for an account.

     Returns the vesting schedule for an account. Replaces `/vesting/{address}` from versions < v1.0.0.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountVestingInfo, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[Union[AccountVestingInfo, Error]]:
    """Get vesting information for an account.

     Returns the vesting schedule for an account. Replaces `/vesting/{address}` from versions < v1.0.0.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountVestingInfo, Error]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            at=at,
        )
    ).parsed
