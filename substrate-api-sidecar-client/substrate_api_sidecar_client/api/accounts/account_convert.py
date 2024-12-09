from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_convert import AccountConvert
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    scheme: Union[Unset, str] = "sr25519",
    prefix: Union[Unset, str] = "42",
    public_key: Union[Unset, str] = "True",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["scheme"] = scheme

    params["prefix"] = prefix

    params["publicKey"] = public_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/convert",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountConvert, Error]]:
    if response.status_code == 200:
        response_200 = AccountConvert.from_dict(response.json())

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
) -> Response[Union[AccountConvert, Error]]:
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
    scheme: Union[Unset, str] = "sr25519",
    prefix: Union[Unset, str] = "42",
    public_key: Union[Unset, str] = "True",
) -> Response[Union[AccountConvert, Error]]:
    """Convert a given AccountId to an SS58 address.

     Returns the SS58 prefix, the network address format, the SS58 address, and the AccountId that was
    given as input parameter, the scheme that was used and if it is a public key or not (boolean).

    Args:
        account_id (str):
        scheme (Union[Unset, str]):  Default: 'sr25519'.
        prefix (Union[Unset, str]):  Default: '42'.
        public_key (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountConvert, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        scheme=scheme,
        prefix=prefix,
        public_key=public_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scheme: Union[Unset, str] = "sr25519",
    prefix: Union[Unset, str] = "42",
    public_key: Union[Unset, str] = "True",
) -> Optional[Union[AccountConvert, Error]]:
    """Convert a given AccountId to an SS58 address.

     Returns the SS58 prefix, the network address format, the SS58 address, and the AccountId that was
    given as input parameter, the scheme that was used and if it is a public key or not (boolean).

    Args:
        account_id (str):
        scheme (Union[Unset, str]):  Default: 'sr25519'.
        prefix (Union[Unset, str]):  Default: '42'.
        public_key (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountConvert, Error]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        scheme=scheme,
        prefix=prefix,
        public_key=public_key,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scheme: Union[Unset, str] = "sr25519",
    prefix: Union[Unset, str] = "42",
    public_key: Union[Unset, str] = "True",
) -> Response[Union[AccountConvert, Error]]:
    """Convert a given AccountId to an SS58 address.

     Returns the SS58 prefix, the network address format, the SS58 address, and the AccountId that was
    given as input parameter, the scheme that was used and if it is a public key or not (boolean).

    Args:
        account_id (str):
        scheme (Union[Unset, str]):  Default: 'sr25519'.
        prefix (Union[Unset, str]):  Default: '42'.
        public_key (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountConvert, Error]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        scheme=scheme,
        prefix=prefix,
        public_key=public_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scheme: Union[Unset, str] = "sr25519",
    prefix: Union[Unset, str] = "42",
    public_key: Union[Unset, str] = "True",
) -> Optional[Union[AccountConvert, Error]]:
    """Convert a given AccountId to an SS58 address.

     Returns the SS58 prefix, the network address format, the SS58 address, and the AccountId that was
    given as input parameter, the scheme that was used and if it is a public key or not (boolean).

    Args:
        account_id (str):
        scheme (Union[Unset, str]):  Default: 'sr25519'.
        prefix (Union[Unset, str]):  Default: '42'.
        public_key (Union[Unset, str]):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountConvert, Error]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            scheme=scheme,
            prefix=prefix,
            public_key=public_key,
        )
    ).parsed
