from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction import Transaction
from ...models.transaction_failed_to_parse import TransactionFailedToParse
from ...models.transaction_failed_to_submit import TransactionFailedToSubmit
from ...models.transaction_success import TransactionSuccess
from ...types import Response


def _get_kwargs(
    *,
    body: Transaction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transaction",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    if response.status_code == 200:
        response_200 = TransactionSuccess.from_dict(response.json())

        return response_200
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["TransactionFailedToParse", "TransactionFailedToSubmit"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_transaction_failure_type_0 = TransactionFailedToSubmit.from_dict(data)

                return componentsschemas_transaction_failure_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_transaction_failure_type_1 = TransactionFailedToParse.from_dict(data)

            return componentsschemas_transaction_failure_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Transaction,
) -> Response[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    """Submit a transaction to the node's transaction pool.

     Accepts a valid signed extrinsic. Replaces `/tx` from versions < v1.0.0.

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TransactionSuccess, Union['TransactionFailedToParse', 'TransactionFailedToSubmit']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Transaction,
) -> Optional[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    """Submit a transaction to the node's transaction pool.

     Accepts a valid signed extrinsic. Replaces `/tx` from versions < v1.0.0.

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TransactionSuccess, Union['TransactionFailedToParse', 'TransactionFailedToSubmit']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Transaction,
) -> Response[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    """Submit a transaction to the node's transaction pool.

     Accepts a valid signed extrinsic. Replaces `/tx` from versions < v1.0.0.

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TransactionSuccess, Union['TransactionFailedToParse', 'TransactionFailedToSubmit']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Transaction,
) -> Optional[Union[TransactionSuccess, Union["TransactionFailedToParse", "TransactionFailedToSubmit"]]]:
    """Submit a transaction to the node's transaction pool.

     Accepts a valid signed extrinsic. Replaces `/tx` from versions < v1.0.0.

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TransactionSuccess, Union['TransactionFailedToParse', 'TransactionFailedToSubmit']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
