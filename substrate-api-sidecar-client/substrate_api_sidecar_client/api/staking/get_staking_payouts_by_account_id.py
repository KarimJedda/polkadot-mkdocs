from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_staking_payouts import AccountStakingPayouts
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    at: Union[Unset, str] = UNSET,
    depth: Union[Unset, str] = "1",
    era: Union[Unset, str] = "`active_era - 1`",
    unclaimed_only: Union[Unset, str] = "True",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params["depth"] = depth

    params["era"] = era

    params["unclaimedOnly"] = unclaimed_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/staking-payouts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountStakingPayouts, Error]]:
    if response.status_code == 200:
        response_200 = AccountStakingPayouts.from_dict(response.json())

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
) -> Response[Union[AccountStakingPayouts, Error]]:
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
    depth: Union[Unset, str] = "1",
    era: Union[Unset, str] = "`active_era - 1`",
    unclaimed_only: Union[Unset, str] = "True",
) -> Response[Union[AccountStakingPayouts, Error]]:
    """Get payout information for a _Stash_ account.

     Returns payout information for the last specified eras. If specifying both the depth and era query
    params, this endpoint will return information for (era - depth) through era. (i.e. if depth=5 and
    era=20 information will be returned for eras 16 through 20). N.B. You cannot query eras less then
    `current_era - HISTORY_DEPTH`. N.B. The `nominator*` fields correspond to the address being queried,
    even if it is a validator's _Stash_ address. This is because a validator is technically nominating
    itself.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        depth (Union[Unset, str]):  Default: '1'.
        era (Union[Unset, str]):  Default: '`active_era - 1`'.
        unclaimed_only (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountStakingPayouts, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        depth=depth,
        era=era,
        unclaimed_only=unclaimed_only,
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
    depth: Union[Unset, str] = "1",
    era: Union[Unset, str] = "`active_era - 1`",
    unclaimed_only: Union[Unset, str] = "True",
) -> Optional[Union[AccountStakingPayouts, Error]]:
    """Get payout information for a _Stash_ account.

     Returns payout information for the last specified eras. If specifying both the depth and era query
    params, this endpoint will return information for (era - depth) through era. (i.e. if depth=5 and
    era=20 information will be returned for eras 16 through 20). N.B. You cannot query eras less then
    `current_era - HISTORY_DEPTH`. N.B. The `nominator*` fields correspond to the address being queried,
    even if it is a validator's _Stash_ address. This is because a validator is technically nominating
    itself.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        depth (Union[Unset, str]):  Default: '1'.
        era (Union[Unset, str]):  Default: '`active_era - 1`'.
        unclaimed_only (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountStakingPayouts, Error]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        at=at,
        depth=depth,
        era=era,
        unclaimed_only=unclaimed_only,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    depth: Union[Unset, str] = "1",
    era: Union[Unset, str] = "`active_era - 1`",
    unclaimed_only: Union[Unset, str] = "True",
) -> Response[Union[AccountStakingPayouts, Error]]:
    """Get payout information for a _Stash_ account.

     Returns payout information for the last specified eras. If specifying both the depth and era query
    params, this endpoint will return information for (era - depth) through era. (i.e. if depth=5 and
    era=20 information will be returned for eras 16 through 20). N.B. You cannot query eras less then
    `current_era - HISTORY_DEPTH`. N.B. The `nominator*` fields correspond to the address being queried,
    even if it is a validator's _Stash_ address. This is because a validator is technically nominating
    itself.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        depth (Union[Unset, str]):  Default: '1'.
        era (Union[Unset, str]):  Default: '`active_era - 1`'.
        unclaimed_only (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountStakingPayouts, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        at=at,
        depth=depth,
        era=era,
        unclaimed_only=unclaimed_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    depth: Union[Unset, str] = "1",
    era: Union[Unset, str] = "`active_era - 1`",
    unclaimed_only: Union[Unset, str] = "True",
) -> Optional[Union[AccountStakingPayouts, Error]]:
    """Get payout information for a _Stash_ account.

     Returns payout information for the last specified eras. If specifying both the depth and era query
    params, this endpoint will return information for (era - depth) through era. (i.e. if depth=5 and
    era=20 information will be returned for eras 16 through 20). N.B. You cannot query eras less then
    `current_era - HISTORY_DEPTH`. N.B. The `nominator*` fields correspond to the address being queried,
    even if it is a validator's _Stash_ address. This is because a validator is technically nominating
    itself.

    Args:
        account_id (str):
        at (Union[Unset, str]): Block height (as a non-negative integer) or hash (as a hex
            string).
        depth (Union[Unset, str]):  Default: '1'.
        era (Union[Unset, str]):  Default: '`active_era - 1`'.
        unclaimed_only (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountStakingPayouts, Error]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            at=at,
            depth=depth,
            era=era,
            unclaimed_only=unclaimed_only,
        )
    ).parsed
