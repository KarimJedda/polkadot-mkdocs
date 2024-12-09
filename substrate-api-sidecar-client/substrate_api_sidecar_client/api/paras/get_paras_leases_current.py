from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paras_leases_current import ParasLeasesCurrent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    at: Union[Unset, str] = UNSET,
    current_lease_holders: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params["currentLeaseHolders"] = current_lease_holders

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/paras/leases/current",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ParasLeasesCurrent]:
    if response.status_code == 200:
        response_200 = ParasLeasesCurrent.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ParasLeasesCurrent]:
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
    current_lease_holders: Union[Unset, bool] = True,
) -> Response[ParasLeasesCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get general information about the
    current lease period.

     Returns an overview of the current lease period, including lease holders.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        current_lease_holders (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasLeasesCurrent]
    """

    kwargs = _get_kwargs(
        at=at,
        current_lease_holders=current_lease_holders,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    current_lease_holders: Union[Unset, bool] = True,
) -> Optional[ParasLeasesCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get general information about the
    current lease period.

     Returns an overview of the current lease period, including lease holders.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        current_lease_holders (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasLeasesCurrent
    """

    return sync_detailed(
        client=client,
        at=at,
        current_lease_holders=current_lease_holders,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    current_lease_holders: Union[Unset, bool] = True,
) -> Response[ParasLeasesCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get general information about the
    current lease period.

     Returns an overview of the current lease period, including lease holders.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        current_lease_holders (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasLeasesCurrent]
    """

    kwargs = _get_kwargs(
        at=at,
        current_lease_holders=current_lease_holders,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
    current_lease_holders: Union[Unset, bool] = True,
) -> Optional[ParasLeasesCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get general information about the
    current lease period.

     Returns an overview of the current lease period, including lease holders.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.
        current_lease_holders (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasLeasesCurrent
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
            current_lease_holders=current_lease_holders,
        )
    ).parsed
