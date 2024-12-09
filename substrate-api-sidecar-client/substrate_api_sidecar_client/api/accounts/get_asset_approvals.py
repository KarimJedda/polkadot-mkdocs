from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_assets_approval import AccountAssetsApproval
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    at: Union[Unset, str] = UNSET,
    asset_id: str,
    delegate: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params["assetId"] = asset_id

    params["delegate"] = delegate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/asset-approvals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountAssetsApproval, Error]]:
    if response.status_code == 200:
        response_200 = AccountAssetsApproval.from_dict(response.json())

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
) -> Response[Union[AccountAssetsApproval, Error]]:
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
    asset_id: str,
    delegate: str,
) -> Response[Union[AccountAssetsApproval, Error]]:
    """Get an asset approval for an account.

     Returns information about an account's asset approval transaction. It is required to pass in a
    delegate and an assetId as query parameters.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        asset_id (str): An assetId represented as an unsignedInteger.
        delegate (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountAssetsApproval, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        asset_id=asset_id,
        delegate=delegate,
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
    asset_id: str,
    delegate: str,
) -> Optional[Union[AccountAssetsApproval, Error]]:
    """Get an asset approval for an account.

     Returns information about an account's asset approval transaction. It is required to pass in a
    delegate and an assetId as query parameters.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        asset_id (str): An assetId represented as an unsignedInteger.
        delegate (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountAssetsApproval, Error]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        at=at,
        asset_id=asset_id,
        delegate=delegate,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    asset_id: str,
    delegate: str,
) -> Response[Union[AccountAssetsApproval, Error]]:
    """Get an asset approval for an account.

     Returns information about an account's asset approval transaction. It is required to pass in a
    delegate and an assetId as query parameters.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        asset_id (str): An assetId represented as an unsignedInteger.
        delegate (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountAssetsApproval, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        asset_id=asset_id,
        delegate=delegate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    asset_id: str,
    delegate: str,
) -> Optional[Union[AccountAssetsApproval, Error]]:
    """Get an asset approval for an account.

     Returns information about an account's asset approval transaction. It is required to pass in a
    delegate and an assetId as query parameters.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        asset_id (str): An assetId represented as an unsignedInteger.
        delegate (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountAssetsApproval, Error]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            at=at,
            asset_id=asset_id,
            delegate=delegate,
        )
    ).parsed
