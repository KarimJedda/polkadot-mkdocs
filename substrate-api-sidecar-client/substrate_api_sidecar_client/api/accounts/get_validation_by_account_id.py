from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_validation import AccountValidation
from ...types import Response


def _get_kwargs(
    address: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{address}/validate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AccountValidation]:
    if response.status_code == 200:
        response_200 = AccountValidation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AccountValidation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AccountValidation]:
    """Validate a given address.

     Returns whether the given address is valid ss58 format, the ss58 prefix if the address has one, the
    network address format, and what the account ID is for this address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountValidation]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AccountValidation]:
    """Validate a given address.

     Returns whether the given address is valid ss58 format, the ss58 prefix if the address has one, the
    network address format, and what the account ID is for this address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountValidation
    """

    return sync_detailed(
        address=address,
        client=client,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AccountValidation]:
    """Validate a given address.

     Returns whether the given address is valid ss58 format, the ss58 prefix if the address has one, the
    network address format, and what the account ID is for this address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountValidation]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AccountValidation]:
    """Validate a given address.

     Returns whether the given address is valid ss58 format, the ss58 prefix if the address has one, the
    network address format, and what the account ID is for this address.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountValidation
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
        )
    ).parsed
