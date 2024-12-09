from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction import Transaction
from ...models.transaction_fee_estimate import TransactionFeeEstimate
from ...models.transaction_fee_estimate_failure import TransactionFeeEstimateFailure
from ...types import Response


def _get_kwargs(
    *,
    body: Transaction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transaction/fee-estimate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
    if response.status_code == 200:
        response_200 = TransactionFeeEstimate.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = TransactionFeeEstimateFailure.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
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
) -> Response[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
    """Receive a fee estimate for a transaction.

     Send a serialized transaction and receive back a naive fee estimate. Note: `partialFee` does not
    include any tips that you may add to increase a transaction's priority. See the reference on
    `compute_fee`. Replaces `/tx/fee-estimate` from versions < v1.0.0. Substrate Reference: -
    `RuntimeDispatchInfo`:
    https://crates.parity.io/pallet_transaction_payment_rpc_runtime_api/struct.RuntimeDispatchInfo.html
    - `query_info`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.query_info -
    `compute_fee`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.compute_fee

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]
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
) -> Optional[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
    """Receive a fee estimate for a transaction.

     Send a serialized transaction and receive back a naive fee estimate. Note: `partialFee` does not
    include any tips that you may add to increase a transaction's priority. See the reference on
    `compute_fee`. Replaces `/tx/fee-estimate` from versions < v1.0.0. Substrate Reference: -
    `RuntimeDispatchInfo`:
    https://crates.parity.io/pallet_transaction_payment_rpc_runtime_api/struct.RuntimeDispatchInfo.html
    - `query_info`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.query_info -
    `compute_fee`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.compute_fee

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Transaction,
) -> Response[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
    """Receive a fee estimate for a transaction.

     Send a serialized transaction and receive back a naive fee estimate. Note: `partialFee` does not
    include any tips that you may add to increase a transaction's priority. See the reference on
    `compute_fee`. Replaces `/tx/fee-estimate` from versions < v1.0.0. Substrate Reference: -
    `RuntimeDispatchInfo`:
    https://crates.parity.io/pallet_transaction_payment_rpc_runtime_api/struct.RuntimeDispatchInfo.html
    - `query_info`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.query_info -
    `compute_fee`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.compute_fee

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]
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
) -> Optional[Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]]:
    """Receive a fee estimate for a transaction.

     Send a serialized transaction and receive back a naive fee estimate. Note: `partialFee` does not
    include any tips that you may add to increase a transaction's priority. See the reference on
    `compute_fee`. Replaces `/tx/fee-estimate` from versions < v1.0.0. Substrate Reference: -
    `RuntimeDispatchInfo`:
    https://crates.parity.io/pallet_transaction_payment_rpc_runtime_api/struct.RuntimeDispatchInfo.html
    - `query_info`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.query_info -
    `compute_fee`:
    https://crates.parity.io/pallet_transaction_payment/struct.Module.html#method.compute_fee

    Args:
        body (Transaction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TransactionFeeEstimate, TransactionFeeEstimateFailure]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
