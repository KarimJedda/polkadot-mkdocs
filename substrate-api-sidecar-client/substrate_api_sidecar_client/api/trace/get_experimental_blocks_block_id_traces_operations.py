from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blocks_trace_operations import BlocksTraceOperations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    block_id: str,
    *,
    actions: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["actions"] = actions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/experimental/blocks/{block_id}/traces/operations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BlocksTraceOperations]:
    if response.status_code == 200:
        response_200 = BlocksTraceOperations.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BlocksTraceOperations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    actions: Union[Unset, bool] = False,
) -> Response[BlocksTraceOperations]:
    r"""[Experimental - subject to breaking change.] Get the operations from the
    specified block.

     Returns the operations from the most recently finalized block. Operations
    represent one side of a balance change. For example if Alice transfers
    100unit to Bob there will be two operations; 1) Alice - 100 2) Bob + 100.

    Given account A and A's balance at block k0 (Ak0), if we sum all the
    operations for A from block k1 through kn against Ak0, we will end up
    with A's balance at block kn (Akn). Thus, operations can be used to audit
    that balances change as expected.

    This is useful for Substrate based chains because the advanced business
    logic can make it difficult to ensure auditable balance reconciliation
    based purely on events. Instead of using events one can use the
    operations given from this endpoint.

    Note - each operation corresponds to a delta of a single field of the
    `system::AccountData` storage item (i.e `free`, `reserved`, `misc_frozen`
    and `fee_frozen`).
    Note - operations are assigned a block execution phase (and extrinsic index
    for those in the apply extrinsic phase) based on an \"action group\". For
    example all the operations for 1 extrinsic will be in the same action group.
    The action groups can optionally be fetched with the `action` query param
    for closer auditing.
    Note - There are no 0 value operations (e.g. a transfer of 0, or a
    transfer to itself)

    To learn more about operation and action group creation please consult
    [this diagram](https://docs.google.com/drawings/d/1vZoJo9jaXlz0LmrdTOgHck9_1LsfuQPRmTr-
    5g1tOis/edit?usp=sharing)

    Args:
        block_id (str):
        actions (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocksTraceOperations]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        actions=actions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    actions: Union[Unset, bool] = False,
) -> Optional[BlocksTraceOperations]:
    r"""[Experimental - subject to breaking change.] Get the operations from the
    specified block.

     Returns the operations from the most recently finalized block. Operations
    represent one side of a balance change. For example if Alice transfers
    100unit to Bob there will be two operations; 1) Alice - 100 2) Bob + 100.

    Given account A and A's balance at block k0 (Ak0), if we sum all the
    operations for A from block k1 through kn against Ak0, we will end up
    with A's balance at block kn (Akn). Thus, operations can be used to audit
    that balances change as expected.

    This is useful for Substrate based chains because the advanced business
    logic can make it difficult to ensure auditable balance reconciliation
    based purely on events. Instead of using events one can use the
    operations given from this endpoint.

    Note - each operation corresponds to a delta of a single field of the
    `system::AccountData` storage item (i.e `free`, `reserved`, `misc_frozen`
    and `fee_frozen`).
    Note - operations are assigned a block execution phase (and extrinsic index
    for those in the apply extrinsic phase) based on an \"action group\". For
    example all the operations for 1 extrinsic will be in the same action group.
    The action groups can optionally be fetched with the `action` query param
    for closer auditing.
    Note - There are no 0 value operations (e.g. a transfer of 0, or a
    transfer to itself)

    To learn more about operation and action group creation please consult
    [this diagram](https://docs.google.com/drawings/d/1vZoJo9jaXlz0LmrdTOgHck9_1LsfuQPRmTr-
    5g1tOis/edit?usp=sharing)

    Args:
        block_id (str):
        actions (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocksTraceOperations
    """

    return sync_detailed(
        block_id=block_id,
        client=client,
        actions=actions,
    ).parsed


async def asyncio_detailed(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    actions: Union[Unset, bool] = False,
) -> Response[BlocksTraceOperations]:
    r"""[Experimental - subject to breaking change.] Get the operations from the
    specified block.

     Returns the operations from the most recently finalized block. Operations
    represent one side of a balance change. For example if Alice transfers
    100unit to Bob there will be two operations; 1) Alice - 100 2) Bob + 100.

    Given account A and A's balance at block k0 (Ak0), if we sum all the
    operations for A from block k1 through kn against Ak0, we will end up
    with A's balance at block kn (Akn). Thus, operations can be used to audit
    that balances change as expected.

    This is useful for Substrate based chains because the advanced business
    logic can make it difficult to ensure auditable balance reconciliation
    based purely on events. Instead of using events one can use the
    operations given from this endpoint.

    Note - each operation corresponds to a delta of a single field of the
    `system::AccountData` storage item (i.e `free`, `reserved`, `misc_frozen`
    and `fee_frozen`).
    Note - operations are assigned a block execution phase (and extrinsic index
    for those in the apply extrinsic phase) based on an \"action group\". For
    example all the operations for 1 extrinsic will be in the same action group.
    The action groups can optionally be fetched with the `action` query param
    for closer auditing.
    Note - There are no 0 value operations (e.g. a transfer of 0, or a
    transfer to itself)

    To learn more about operation and action group creation please consult
    [this diagram](https://docs.google.com/drawings/d/1vZoJo9jaXlz0LmrdTOgHck9_1LsfuQPRmTr-
    5g1tOis/edit?usp=sharing)

    Args:
        block_id (str):
        actions (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlocksTraceOperations]
    """

    kwargs = _get_kwargs(
        block_id=block_id,
        actions=actions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    block_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    actions: Union[Unset, bool] = False,
) -> Optional[BlocksTraceOperations]:
    r"""[Experimental - subject to breaking change.] Get the operations from the
    specified block.

     Returns the operations from the most recently finalized block. Operations
    represent one side of a balance change. For example if Alice transfers
    100unit to Bob there will be two operations; 1) Alice - 100 2) Bob + 100.

    Given account A and A's balance at block k0 (Ak0), if we sum all the
    operations for A from block k1 through kn against Ak0, we will end up
    with A's balance at block kn (Akn). Thus, operations can be used to audit
    that balances change as expected.

    This is useful for Substrate based chains because the advanced business
    logic can make it difficult to ensure auditable balance reconciliation
    based purely on events. Instead of using events one can use the
    operations given from this endpoint.

    Note - each operation corresponds to a delta of a single field of the
    `system::AccountData` storage item (i.e `free`, `reserved`, `misc_frozen`
    and `fee_frozen`).
    Note - operations are assigned a block execution phase (and extrinsic index
    for those in the apply extrinsic phase) based on an \"action group\". For
    example all the operations for 1 extrinsic will be in the same action group.
    The action groups can optionally be fetched with the `action` query param
    for closer auditing.
    Note - There are no 0 value operations (e.g. a transfer of 0, or a
    transfer to itself)

    To learn more about operation and action group creation please consult
    [this diagram](https://docs.google.com/drawings/d/1vZoJo9jaXlz0LmrdTOgHck9_1LsfuQPRmTr-
    5g1tOis/edit?usp=sharing)

    Args:
        block_id (str):
        actions (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlocksTraceOperations
    """

    return (
        await asyncio_detailed(
            block_id=block_id,
            client=client,
            actions=actions,
        )
    ).parsed
