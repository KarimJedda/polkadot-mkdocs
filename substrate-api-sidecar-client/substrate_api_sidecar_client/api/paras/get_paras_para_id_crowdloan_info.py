from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paras_crowdloan_info import ParasCrowdloanInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    para_id: float,
    *,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/paras/{para_id}/crowdloan-info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ParasCrowdloanInfo]:
    if response.status_code == 200:
        response_200 = ParasCrowdloanInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ParasCrowdloanInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    para_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[ParasCrowdloanInfo]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get crowdloan information for a
    `paraId`.

     Returns crowdloan's `fundInfo` and the set of `leasePeriods` the crowdloan`
    covers.

    Args:
        para_id (float):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasCrowdloanInfo]
    """

    kwargs = _get_kwargs(
        para_id=para_id,
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    para_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[ParasCrowdloanInfo]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get crowdloan information for a
    `paraId`.

     Returns crowdloan's `fundInfo` and the set of `leasePeriods` the crowdloan`
    covers.

    Args:
        para_id (float):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasCrowdloanInfo
    """

    return sync_detailed(
        para_id=para_id,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    para_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[ParasCrowdloanInfo]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get crowdloan information for a
    `paraId`.

     Returns crowdloan's `fundInfo` and the set of `leasePeriods` the crowdloan`
    covers.

    Args:
        para_id (float):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ParasCrowdloanInfo]
    """

    kwargs = _get_kwargs(
        para_id=para_id,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    para_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[ParasCrowdloanInfo]:
    """[DEPRECATION NOTE: PHASED OUT ENDPOINT IN FAVOR OF CORETIME] Get crowdloan information for a
    `paraId`.

     Returns crowdloan's `fundInfo` and the set of `leasePeriods` the crowdloan`
    covers.

    Args:
        para_id (float):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ParasCrowdloanInfo
    """

    return (
        await asyncio_detailed(
            para_id=para_id,
            client=client,
            at=at,
        )
    ).parsed
