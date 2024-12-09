from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeerInfo")


@_attrs_define
class PeerInfo:
    """
    Attributes:
        peer_id (Union[Unset, str]): Peer ID.
        roles (Union[Unset, str]): Roles the peer is running
        protocol_version (Union[Unset, str]): Peer's protocol version.
        best_hash (Union[Unset, str]): Hash of the best block on the peer's canon chain.
        best_number (Union[Unset, str]): Height of the best block on the peer's canon chain.
    """

    peer_id: Union[Unset, str] = UNSET
    roles: Union[Unset, str] = UNSET
    protocol_version: Union[Unset, str] = UNSET
    best_hash: Union[Unset, str] = UNSET
    best_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peer_id = self.peer_id

        roles = self.roles

        protocol_version = self.protocol_version

        best_hash = self.best_hash

        best_number = self.best_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peer_id is not UNSET:
            field_dict["peerId"] = peer_id
        if roles is not UNSET:
            field_dict["roles"] = roles
        if protocol_version is not UNSET:
            field_dict["protocolVersion"] = protocol_version
        if best_hash is not UNSET:
            field_dict["bestHash"] = best_hash
        if best_number is not UNSET:
            field_dict["bestNumber"] = best_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        peer_id = d.pop("peerId", UNSET)

        roles = d.pop("roles", UNSET)

        protocol_version = d.pop("protocolVersion", UNSET)

        best_hash = d.pop("bestHash", UNSET)

        best_number = d.pop("bestNumber", UNSET)

        peer_info = cls(
            peer_id=peer_id,
            roles=roles,
            protocol_version=protocol_version,
            best_hash=best_hash,
            best_number=best_number,
        )

        peer_info.additional_properties = d
        return peer_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
