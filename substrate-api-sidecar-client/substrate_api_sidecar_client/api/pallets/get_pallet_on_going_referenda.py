from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pallets_on_going_referenda import PalletsOnGoingReferenda
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
        "url": "/pallets/on-going-referenda",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PalletsOnGoingReferenda]:
    if response.status_code == 200:
        response_200 = PalletsOnGoingReferenda.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PalletsOnGoingReferenda]:
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
) -> Response[PalletsOnGoingReferenda]:
    """Get a list of all on-going referenda that have track `root (0)` and `whitelisted (1)`, along with
    their associated information.

     Returns information associated with on-going referenda which includes the referendum's `enactment`,
    `submitted` and `deciding` fields.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PalletsOnGoingReferenda]
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
) -> Optional[PalletsOnGoingReferenda]:
    """Get a list of all on-going referenda that have track `root (0)` and `whitelisted (1)`, along with
    their associated information.

     Returns information associated with on-going referenda which includes the referendum's `enactment`,
    `submitted` and `deciding` fields.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PalletsOnGoingReferenda
    """

    return sync_detailed(
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[PalletsOnGoingReferenda]:
    """Get a list of all on-going referenda that have track `root (0)` and `whitelisted (1)`, along with
    their associated information.

     Returns information associated with on-going referenda which includes the referendum's `enactment`,
    `submitted` and `deciding` fields.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PalletsOnGoingReferenda]
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
) -> Optional[PalletsOnGoingReferenda]:
    """Get a list of all on-going referenda that have track `root (0)` and `whitelisted (1)`, along with
    their associated information.

     Returns information associated with on-going referenda which includes the referendum's `enactment`,
    `submitted` and `deciding` fields.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PalletsOnGoingReferenda
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
        )
    ).parsed
