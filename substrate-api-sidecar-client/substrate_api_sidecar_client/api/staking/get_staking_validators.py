from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.staking_validators import StakingValidators
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
        "url": "/pallets/staking/validators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, StakingValidators]]:
    if response.status_code == 200:
        response_200 = StakingValidators.from_dict(response.json())

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
) -> Response[Union[Error, StakingValidators]]:
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
) -> Response[Union[Error, StakingValidators]]:
    r"""Get all validators (active/waiting) of a specific chain.

     Returns a list of all validators addresses and their corresponding status which can be either active
    or waiting. It will also return a list of active validators that will not be part of the next era
    for staking. They will be under the key \"validatorsToBeChilled\". It's important to note, that
    addresses can be present in both the \"validators\" key, and \"validatorsToBeChilled\".

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StakingValidators]]
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
) -> Optional[Union[Error, StakingValidators]]:
    r"""Get all validators (active/waiting) of a specific chain.

     Returns a list of all validators addresses and their corresponding status which can be either active
    or waiting. It will also return a list of active validators that will not be part of the next era
    for staking. They will be under the key \"validatorsToBeChilled\". It's important to note, that
    addresses can be present in both the \"validators\" key, and \"validatorsToBeChilled\".

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StakingValidators]
    """

    return sync_detailed(
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[Union[Error, StakingValidators]]:
    r"""Get all validators (active/waiting) of a specific chain.

     Returns a list of all validators addresses and their corresponding status which can be either active
    or waiting. It will also return a list of active validators that will not be part of the next era
    for staking. They will be under the key \"validatorsToBeChilled\". It's important to note, that
    addresses can be present in both the \"validators\" key, and \"validatorsToBeChilled\".

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StakingValidators]]
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
) -> Optional[Union[Error, StakingValidators]]:
    r"""Get all validators (active/waiting) of a specific chain.

     Returns a list of all validators addresses and their corresponding status which can be either active
    or waiting. It will also return a list of active validators that will not be part of the next era
    for staking. They will be under the key \"validatorsToBeChilled\". It's important to note, that
    addresses can be present in both the \"validators\" key, and \"validatorsToBeChilled\".

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StakingValidators]
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
        )
    ).parsed
