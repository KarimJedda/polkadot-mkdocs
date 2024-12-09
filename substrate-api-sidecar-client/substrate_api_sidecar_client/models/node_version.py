from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeVersion")


@_attrs_define
class NodeVersion:
    """Version information of the node.

    Attributes:
        client_version (Union[Unset, str]): Node's binary version.
        client_impl_name (Union[Unset, str]): Node's implementation name.
        chain (Union[Unset, str]): Node's chain name.
    """

    client_version: Union[Unset, str] = UNSET
    client_impl_name: Union[Unset, str] = UNSET
    chain: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_version = self.client_version

        client_impl_name = self.client_impl_name

        chain = self.chain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_version is not UNSET:
            field_dict["clientVersion"] = client_version
        if client_impl_name is not UNSET:
            field_dict["clientImplName"] = client_impl_name
        if chain is not UNSET:
            field_dict["chain"] = chain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        client_version = d.pop("clientVersion", UNSET)

        client_impl_name = d.pop("clientImplName", UNSET)

        chain = d.pop("chain", UNSET)

        node_version = cls(
            client_version=client_version,
            client_impl_name=client_impl_name,
            chain=chain,
        )

        node_version.additional_properties = d
        return node_version

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
