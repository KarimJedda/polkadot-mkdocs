from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_pool_assets_balances import AccountPoolAssetsBalances
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    at: Union[Unset, str] = UNSET,
    assets: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    json_assets: Union[Unset, list[str]] = UNSET
    if not isinstance(assets, Unset):
        json_assets = assets

    params["assets"] = json_assets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/pool-asset-balances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountPoolAssetsBalances, Error]]:
    if response.status_code == 200:
        response_200 = AccountPoolAssetsBalances.from_dict(response.json())

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
) -> Response[Union[AccountPoolAssetsBalances, Error]]:
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
    assets: Union[Unset, list[str]] = UNSET,
) -> Response[Union[AccountPoolAssetsBalances, Error]]:
    """Get an array of pool-asset-balances for an account.

     Returns information about an account's pool-asset-balances. This is specific to the pool assets
    pallet for parachains. If no `assets` query parameter is provided, all pool-asset-balances for the
    given account will be returned.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a positive integer) or hash (as a hex string).
        assets (Union[Unset, list[str]]): A list of assetId numbers represented as strings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountPoolAssetsBalances, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        assets=assets,
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
    assets: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[AccountPoolAssetsBalances, Error]]:
    """Get an array of pool-asset-balances for an account.

     Returns information about an account's pool-asset-balances. This is specific to the pool assets
    pallet for parachains. If no `assets` query parameter is provided, all pool-asset-balances for the
    given account will be returned.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a positive integer) or hash (as a hex string).
        assets (Union[Unset, list[str]]): A list of assetId numbers represented as strings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountPoolAssetsBalances, Error]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        at=at,
        assets=assets,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    assets: Union[Unset, list[str]] = UNSET,
) -> Response[Union[AccountPoolAssetsBalances, Error]]:
    """Get an array of pool-asset-balances for an account.

     Returns information about an account's pool-asset-balances. This is specific to the pool assets
    pallet for parachains. If no `assets` query parameter is provided, all pool-asset-balances for the
    given account will be returned.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a positive integer) or hash (as a hex string).
        assets (Union[Unset, list[str]]): A list of assetId numbers represented as strings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountPoolAssetsBalances, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        assets=assets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    assets: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[AccountPoolAssetsBalances, Error]]:
    """Get an array of pool-asset-balances for an account.

     Returns information about an account's pool-asset-balances. This is specific to the pool assets
    pallet for parachains. If no `assets` query parameter is provided, all pool-asset-balances for the
    given account will be returned.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a positive integer) or hash (as a hex string).
        assets (Union[Unset, list[str]]): A list of assetId numbers represented as strings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountPoolAssetsBalances, Error]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            at=at,
            assets=assets,
        )
    ).parsed
