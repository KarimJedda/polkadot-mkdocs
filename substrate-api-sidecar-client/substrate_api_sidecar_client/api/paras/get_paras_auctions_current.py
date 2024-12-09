from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paras_auctions_current import ParasAuctionsCurrent
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
        "url": "/paras/auctions/current",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ParasAuctionsCurrent]:
    if response.status_code == 200:
        response_200 = ParasAuctionsCurrent.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ParasAuctionsCurrent]:
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
) -> Response[ParasAuctionsCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the status of the current auction.

     Returns an overview of the current auction. There is only one auction
    at a time. If there is no auction most fields will be `null`. If the current
    auction phase is in `vrfDelay` and you are looking to retrieve the latest winning
    bids, it is advised to query one block before `finishEnd` in the `endingPeriod` phase
    for that auction as there technically are no winners during the `vrfDelay` and thus
    the field is `null`.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasAuctionsCurrent]
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
) -> Optional[ParasAuctionsCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the status of the current auction.

     Returns an overview of the current auction. There is only one auction
    at a time. If there is no auction most fields will be `null`. If the current
    auction phase is in `vrfDelay` and you are looking to retrieve the latest winning
    bids, it is advised to query one block before `finishEnd` in the `endingPeriod` phase
    for that auction as there technically are no winners during the `vrfDelay` and thus
    the field is `null`.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasAuctionsCurrent
    """

    return sync_detailed(
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[ParasAuctionsCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the status of the current auction.

     Returns an overview of the current auction. There is only one auction
    at a time. If there is no auction most fields will be `null`. If the current
    auction phase is in `vrfDelay` and you are looking to retrieve the latest winning
    bids, it is advised to query one block before `finishEnd` in the `endingPeriod` phase
    for that auction as there technically are no winners during the `vrfDelay` and thus
    the field is `null`.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasAuctionsCurrent]
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
) -> Optional[ParasAuctionsCurrent]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get the status of the current auction.

     Returns an overview of the current auction. There is only one auction
    at a time. If there is no auction most fields will be `null`. If the current
    auction phase is in `vrfDelay` and you are looking to retrieve the latest winning
    bids, it is advised to query one block before `finishEnd` in the `endingPeriod` phase
    for that auction as there technically are no winners during the `vrfDelay` and thus
    the field is `null`.

    Args:
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasAuctionsCurrent
    """

    return (
        await asyncio_detailed(
            client=client,
            at=at,
        )
    ).parsed
