from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_runtime_metadata_metadata_version_response_200 import GetRuntimeMetadataMetadataVersionResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    metadata_version: str,
    *,
    at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["at"] = at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/runtime/metadata/{metadata_version}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetRuntimeMetadataMetadataVersionResponse200]:
    if response.status_code == 200:
        response_200 = GetRuntimeMetadataMetadataVersionResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetRuntimeMetadataMetadataVersionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    metadata_version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[GetRuntimeMetadataMetadataVersionResponse200]:
    """Get the requested version of runtime metadata in decoded, JSON form.

     Returns the requested version of runtime metadata as a JSON object. Substrate Reference: - FRAME
    Support: https://crates.parity.io/frame_support/metadata/index.html - Knowledge Base:
    https://substrate.dev/docs/en/knowledgebase/runtime/metadata

    Args:
        metadata_version (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRuntimeMetadataMetadataVersionResponse200]
    """

    kwargs = _get_kwargs(
        metadata_version=metadata_version,
        at=at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    metadata_version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[GetRuntimeMetadataMetadataVersionResponse200]:
    """Get the requested version of runtime metadata in decoded, JSON form.

     Returns the requested version of runtime metadata as a JSON object. Substrate Reference: - FRAME
    Support: https://crates.parity.io/frame_support/metadata/index.html - Knowledge Base:
    https://substrate.dev/docs/en/knowledgebase/runtime/metadata

    Args:
        metadata_version (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRuntimeMetadataMetadataVersionResponse200
    """

    return sync_detailed(
        metadata_version=metadata_version,
        client=client,
        at=at,
    ).parsed


async def asyncio_detailed(
    metadata_version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Response[GetRuntimeMetadataMetadataVersionResponse200]:
    """Get the requested version of runtime metadata in decoded, JSON form.

     Returns the requested version of runtime metadata as a JSON object. Substrate Reference: - FRAME
    Support: https://crates.parity.io/frame_support/metadata/index.html - Knowledge Base:
    https://substrate.dev/docs/en/knowledgebase/runtime/metadata

    Args:
        metadata_version (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRuntimeMetadataMetadataVersionResponse200]
    """

    kwargs = _get_kwargs(
        metadata_version=metadata_version,
        at=at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    metadata_version: str,
    *,
    client: Union[AuthenticatedClient, Client],
    at: Union[Unset, str] = UNSET,
) -> Optional[GetRuntimeMetadataMetadataVersionResponse200]:
    """Get the requested version of runtime metadata in decoded, JSON form.

     Returns the requested version of runtime metadata as a JSON object. Substrate Reference: - FRAME
    Support: https://crates.parity.io/frame_support/metadata/index.html - Knowledge Base:
    https://substrate.dev/docs/en/knowledgebase/runtime/metadata

    Args:
        metadata_version (str):
        at (Union[Unset, str]): Block identifier, as the block height or block hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRuntimeMetadataMetadataVersionResponse200
    """

    return (
        await asyncio_detailed(
            metadata_version=metadata_version,
            client=client,
            at=at,
        )
    ).parsed
